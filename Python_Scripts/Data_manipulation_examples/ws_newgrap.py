# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:08:29 2020

@author: Acer
"""


import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot

bb=pd.DataFrame(DF_CHANGE(ws))

#calculate kpi for current month vs last month
CTR_C = round(bb['CTR_perc'].tolist()[-1],2)
CTOR_C = round(bb['CTOR_perc'].tolist()[-1],2)
OPR_C = round(bb['OPR_perc'].tolist()[-1],2)
CTR_C_L= bb['CTR_perc'].tolist()[-1] - bb['CTR_perc'].tolist()[-2]
CTR_C_L = round(CTR_C_L, 2)
print(CTR_C_L)
CTOR_C_L = bb['CTOR_perc'].tolist()[-1] - bb['CTOR_perc'].tolist()[-2]
CTOR_C_L = round(CTOR_C_L, 2)
print(CTOR_C_L)
OPR_C_L = bb['OPR_perc'].tolist()[-1] - bb['OPR_perc'].tolist()[-2]
OPR_C_L = round(OPR_C_L,2)
print(OPR_C_L)
    
#create report    
scat_plot_x = bb['date_str']
x_kpi_coord, y_kpi_coord=[2,2,6,6,2],[0.5,2.5,2.5,0.5,0.5]

#create scat plot for each graph with the layout already integrated inside of it