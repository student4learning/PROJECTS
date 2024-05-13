# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:24:49 2020

@author: Acer
"""
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime

ws = pd.read_csv('C:/Users/Acer/Downloads/WS delivery 2020-08-20.csv')
we_column_names = list(ws.columns.values) 
#DataFrame manipulation
#sum campaign name
#sum date

def DF_CHANGE (DF):
    temp = DF.copy()
    #fix date column to get month and year
    temp['year_month'] = pd.to_datetime(temp['year_month'])
    temp = temp[temp['cmpgn_name'].str.contains('[Oo]rganic|[Oo]rg|WS|Welcome|W_|RTTM|_ES')]
    temp = temp.groupby(['year_month', 'cmpgn_name'])['unique_delivered','openers','clickers'].sum().reset_index()
    temp = temp.groupby(['year_month'])['unique_delivered','openers','clickers'].sum().reset_index()
    temp['day'] = temp['year_month'].dt.day
    temp['month'] = temp['year_month'].dt.month
    temp['month_name'] = temp['year_month'].dt.strftime("%B")
    temp['year'] = temp['year_month'].dt.year
    temp = temp.drop(columns={'year_month'})
    temp['date_numb'] = temp['year'].astype(str) + '_' + temp['month'].astype(str) 
    temp['date_str'] = temp['year'].astype(str) + '_' + temp['month_name'].astype(str) 
    temp = temp.groupby(['date_numb', 'date_str'])['unique_delivered','openers','clickers'].sum().reset_index()
    
    #calculate metrics for each month
    temp['OPR_perc'] = round((temp['openers']/temp['unique_delivered'])*100,2)
    temp['CTR_perc'] = round((temp['clickers']/temp['unique_delivered'])*100,2)
    temp['CTOR_perc'] = round((temp['clickers']/temp['openers'])*100,2)
   
    return temp

def plot_KPI(DF_plot):
    temp = DF_plot.copy()

    #calculate kpi for current month vs last month
    CTR_C = round(temp['CTR_perc'].tolist()[-1],2)
    CTOR_C = round(temp['CTOR_perc'].tolist()[-1],2)
    OPR_C = round(temp['OPR_perc'].tolist()[-1],2)
    CTR_C_L= temp['CTR_perc'].tolist()[-1] - temp['CTR_perc'].tolist()[-2]
    CTR_C_L = round(CTR_C_L, 2)
    print(CTR_C_L)
    CTOR_C_L = temp['CTOR_perc'].tolist()[-1] - temp['CTOR_perc'].tolist()[-2]
    CTOR_C_L = round(CTOR_C_L, 2)
    print(CTOR_C_L)
    OPR_C_L = temp['OPR_perc'].tolist()[-1] - temp['OPR_perc'].tolist()[-2]
    OPR_C_L = round(OPR_C_L,2)
    print(OPR_C_L)
    
    #create report    
    scat_plot_x = temp['date_str']
    x_kpi_coord=[2,2,6,6,2]
    y_kpi_coord_OPR=[0.5,temp['OPR_perc'].iloc[-1],temp['OPR_perc'].iloc[-1],0.5,0.5]
    y_kpi_coord_CTR=[0.5,temp['CTR_perc'].iloc[-1],temp['CTR_perc'].iloc[-1],0.5,0.5]
    y_kpi_coord_CTOR=[0.5,temp['CTOR_perc'].iloc[-1],temp['CTOR_perc'].iloc[-1],0.5,0.5]


    fig = make_subplots(
    rows=4, cols=4,
    shared_xaxes=True,
    shared_yaxes=True,
    vertical_spacing=0.04,
    specs=[[{"colspan": 3},{},{},{}],
           [{"colspan": 3},{},{},{}],
           [{"colspan": 3},{},{},{}],
           [{"colspan": 3},{},{},{}]],
                            print_grid=True)
#OPR graph
    fig.append_trace(go.Scatter(
        x=scat_plot_x,
        y=temp['OPR_perc'],
        fill = 'tozeroy',
        fillcolor='lightgoldenrodyellow',
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
    x=[temp['date_str'].iloc[-2]],
    y=[20.0],
    text=['Open Rate %',
          ],
          mode="text",
          textfont=dict(family="sans serif",size=24,color="LightSeaGreen")
        ),row = 1, col = 1)
#CTR graph     
    fig.append_trace(go.Scatter(
        x=scat_plot_x,
        y= temp['CTR_perc'],
        fill='tozeroy',
        fillcolor='LightSkyBlue',
     ), row=2, col=1)
    fig.add_trace(go.Scatter(
    x=[temp['date_str'].iloc[-2]],
    y=[2.0],
    text=['CRT %',
          ],
          mode="text",
          textfont=dict(family="sans serif",size=24,color="LightSeaGreen")
        ),row = 2, col = 1)
#CTOR graph
    fig.append_trace(go.Scatter(
        x=scat_plot_x,
        y=temp['CTOR_perc'],
        fill='tozeroy',
        fillcolor='lightsteelblue',
        ), row=3, col=1)
    fig.add_trace(go.Scatter(
    x=[temp['date_str'].iloc[-2]],
    y=[4.0],
    text=['Click to Open Rate %',
          ],
          mode="text",
          textfont=dict(family="sans serif",size=24,color="LightSeaGreen")
        ),row = 3, col = 1)
#Delivered graph
    fig.append_trace(go.Scatter(
        x=scat_plot_x,
        y=temp['delivered'],
        fill='tozeroy',
        fillcolor="dimgrey"
    ), row=4, col=1)
    fig.add_trace(go.Scatter(
    x=[temp['date_str'].iloc[-2]],
    y=[400000.0],
    text=['Delivered %',
          ],
          mode="text",
          textfont=dict(family="sans serif",size=24,color="LightSeaGreen")
        ),row = 4, col = 1)
#KPI side metrics(OPR, CTR, CTOR)
    fig.append_trace(
        go.Scatter(
            x = x_kpi_coord,
            y = y_kpi_coord_OPR, 
            fill="toself",
            fillcolor="lightgoldenrodyellow")
        ,row=1, col =4)
    fig.add_trace(go.Scatter(
            x=[4, 5],
            y=[2, 1.0],
            text=[#str(OPR_C_L) +'%',
            str(OPR_C) +'%',
            "vs last month"],
            mode="text",
            textfont=dict(family="sans serif",size=18,color="LightSeaGreen")
        ),row=1, col = 4)    
    fig.append_trace(
        go.Scatter(
           x = x_kpi_coord,
           y = y_kpi_coord_CTR,
            fill="toself",
            fillcolor="LightSkyBlue")
        , row=2, col =4)
    fig.add_trace(go.Scatter(
    x=[4, 5],
    y=[2,1.0],
    text=[#str(CTR_C_L) + '%',
          str(CTR_C) + '%',
          "vs last month"],
          mode="text",
          textfont=dict(family="sans serif",size=18,color="LightSeaGreen")
        ),row = 2, col = 4)
    fig.append_trace(
        go.Scatter(
            x = x_kpi_coord,
            y = y_kpi_coord_CTOR, 
            fill="toself",
            fillcolor="lightsteelblue")
        , row=3, col =4)
    fig.add_trace(go.Scatter(
    x=[4, 5],
    y=[2, 1.0],
    text=[#str(CTOR_C_L) + '%',
          str(CTOR_C) + '%',
          "vs last month"],
          mode="text",
          textfont=dict(family="sans serif",size=18,color="LightSeaGreen")
        ), row=3, col = 4)
    
        
    """fig.add_trace(go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ]), row =1, col = 2)"""

    fig.update_layout(showlegend=False)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    plot(fig)
    
    return temp
    return fig
    return CTR_C_L
    return CTOR_C_L
    return OPR_C_L

bb=pd.DataFrame(DF_CHANGE(ws))
cc=pd.DataFrame(plot_KPI(bb))

#NEXT STEPS: ADD TEXT TO BOTTOM LEFT OF LINE GRAPHS, REMOVE X AND Y AXIS ON THE BOXES, REMOVE BACKGOUND, ADD COLOUR AND LETTER TEMPLATE


def customization():
    colors_array = ['#00A9A4', '#F8B017', '#80D4D2', '#006562', '#F5911B', '#FCD88B']

    layout_custom = go.layout.Template(
        layout=go.Layout(titlefont=dict(size=24, color=colors_array[0]),
                        legend=dict(orientation='h',y=1.1)))
    
    return colors_array, layout_custom
    
    
ws['date'] = [x.split(None, 1)[0] for x in ws['year_month']]

