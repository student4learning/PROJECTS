# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:51:53 2020

@author: Acer
"""


import pandas as pd
import numpy as np
import datetime

#Tshirt email
DE_Tshirt = pd.read_csv('C:/Users/Acer/Downloads/DEtshirt_1307.csv')
DE_Tshirt = pd.DataFrame(DE_Tshirt, columns =['Sendout','Selection:','Accepted','Confirmed Openers','Clickers','Unsubscribes'
                                             ])
DE_Tshirt['Send_Date'] = pd.to_datetime(DE_Tshirt['Sendout'], format='%d-%m-%Y %H:%M:%S')
DE_Tshirt['Send_Date'] = DE_Tshirt['Send_Date'].dt.strftime('%Y-%m-%d')
DE_Tshirt = DE_Tshirt.groupby(['Selection:']).sum().reset_index()
DE_Tshirt_week1 = DE_Tshirt[DE_Tshirt['Send_Date'] < '2020-06-30' ]
DE_Tshirt_week2 = DE_Tshirt[DE_Tshirt['Send_Date'] >= '2020-06-30']
DE_Tshirt_week1 = DE_Tshirt_week1.groupby(['Selection:']).sum().reset_index()
DE_Tshirt_week2 = DE_Tshirt_week2.groupby(['Selection:']).sum().reset_index()

#metric calc
DE_Tshirt_week1['CTR'] = DE_Tshirt_week1['Clickers']/DE_Tshirt_week1['Accepted']
DE_Tshirt_week1['OR'] = DE_Tshirt_week1['Confirmed Openers']/DE_Tshirt_week1['Accepted']
DE_Tshirt_week1['CTOR'] =  DE_Tshirt_week1['Clickers']/DE_Tshirt_week1['Confirmed Openers']

DE_Tshirt_week2['CTR'] = DE_Tshirt_week2['Clickers']/DE_Tshirt_week2['Accepted']
DE_Tshirt_week2['OR'] = DE_Tshirt_week2['Confirmed Openers']/DE_Tshirt_week2['Accepted']
DE_Tshirt_week2['CTOR'] =  DE_Tshirt_week2['Clickers']/DE_Tshirt_week2['Confirmed Openers']


#Organic flow
DE_org_all_1 = pd.read_csv('C:/Users/Acer/Downloads/export-message-overview (19).csv')
DE_org_all_2 = pd.read_csv('C:/Users/Acer/Downloads/export-message-overview (18).csv')

DE_org_DF = DE_org_all_1.append(DE_org_all_2)
DE_org_DF = pd.DataFrame(DE_org_DF, columns =['Sendout','Selection:','Accepted','Confirmed Openers','Clickers','Unsubscribes'
                                             ])
DE_org_DF['Send_Date'] = pd.to_datetime(DE_org_DF['Sendout'],errors='coerce')
DE_org_DF['Send_Date'] = DE_org_DF['Send_Date'].dt.strftime('%d/%m/%Y')

DE_org_DF['campaign_type'] = '0'

DE_org_DF = DE_org_DF[DE_org_DF['Selection:'].str.contains('Pampers DE WS Organic_Recurring_v6')]
DE_org_DF['Selection:'] = DE_org_DF['Selection:'].astype(str).apply(lambda x: x.replace('75445',''))

DE_org_DF['campaign_type'] = np.where(DE_org_DF['Selection:'].str.contains('34|32'), 'profile' ,DE_org_DF['campaign_type'])

DE_org_DF['campaign_type'] = np.where(DE_org_DF['Selection:'].str.contains('36|7'), 'rewards' ,DE_org_DF['campaign_type'])

DE_org_DF['campaign_type'] = np.where(DE_org_DF['Selection:'].str.contains('38|15'), 'content' ,DE_org_DF['campaign_type'])

DE_rewards = DE_org_DF[DE_org_DF['campaign_type'].str.contains('rewards')]
DE_rewards = DE_rewards.groupby(['campaign_type']).sum().reset_index()


DE_org_DF_week1 = DE_org_DF[DE_org_DF['Send_Date'] < '2020-06-30' ]
DE_org_DF_week2 = DE_org_DF[DE_org_DF['Send_Date'] >= '2020-06-30']

DE_org_DF_week1 = DE_org_DF_week1.groupby(['campaign_type']).sum().reset_index()
DE_org_DF_week2 = DE_org_DF_week2.groupby(['campaign_type']).sum().reset_index()


#metrics calc
DE_org_DF_week1['CTR'] = DE_org_DF_week1['Clickers']/DE_org_DF_week1['Accepted']
DE_org_DF_week1['OR'] = DE_org_DF_week1['Confirmed Openers']/DE_org_DF_week1['Accepted']
DE_org_DF_week1['CTOR'] =  DE_org_DF_week1['Clickers']/DE_org_DF_week1['Confirmed Openers']

DE_org_DF_week2['CTR'] = DE_org_DF_week2['Clickers']/DE_org_DF_week2['Accepted']
DE_org_DF_week2['OR'] = DE_org_DF_week2['Confirmed Openers']/DE_org_DF_week2['Accepted']
DE_org_DF_week2['CTOR'] =  DE_org_DF_week2['Clickers']/DE_org_DF_week2['Confirmed Openers']


"""BDU data sources and handling

DE_op_cl=pd.read_csv('C:/Users/Acer/Downloads/DE_org_OPCLK.csv')
DE_deliv=pd.read_csv('C:/Users/Acer/Downloads/DE_org_DELIV.csv')

DE_op_cl_app = pd.read_csv('C:/Users/Acer/Downloads/DE_org_OPCLK.csv')
DE_deliv_app = pd.read_csv('C:/Users/Acer/Downloads/DE_org_DELIV.csv')

DE_wh_all = pd.merge(DE_op_cl,
                 DE_deliv[['cmpgn_id', 'delivered']],
                 on='cmpgn_id', 
                 how='left')

DE_app_all = pd.merge(DE_op_cl_app,
                 DE_deliv_app[['cmpgn_id', 'delivered']],
                 on='cmpgn_id', 
                 how='left')

#DE_wh_all = DE_wh_all.groupby(['email_sent_date']).sum().reset_index()
DE_app_all['campaign_type'] = '0'

DE_app_all = DE_app_all[DE_app_all['cmpgn_segment_name'].str.contains('Pampers DE WS Organic_Recurring_v6')]
DE_app_all['cmpgn_segment_name'] = DE_app_all['cmpgn_segment_name'].astype(str).apply(lambda x: x.replace('75445',''))

DE_app_all['campaign_type'] = np.where(DE_app_all['cmpgn_segment_name'].str.contains('34|32'), 'profile' ,DE_app_all['campaign_type'])

DE_app_all['campaign_type'] = np.where(DE_app_all['cmpgn_segment_name'].str.contains('36|54|7'), 'rewards' ,DE_app_all['campaign_type'])

DE_app_all['campaign_type'] = np.where(DE_app_all['cmpgn_segment_name'].str.contains('38|15'), 'content' ,DE_app_all['campaign_type'])

DE_app_all = DE_app_all.groupby(['campaign_type']).sum().reset_index()

#metrics2
DE_wh_all['CTR'] = DE_wh_all['clicked'] / DE_wh_all['delivered'].astype(int)
DE_wh_all['OR'] = DE_wh_all['opened'] / DE_wh_all['delivered'].astype(int)
DE_wh_all['CTOR'] = DE_wh_all['clicked'] / DE_wh_all['opened']

#DE_app_all = DE_app_all.groupby(['email_sent_date']).sum().reset_index()

DE_app_all = DE_app_all.dropna()
DE_app_all['CTR'] = DE_app_all['clicked'] / DE_app_all['delivered'].astype(int)
DE_app_all['OR'] = DE_app_all['opened'] / DE_app_all['delivered'].astype(int)
DE_app_all['CTOR'] = DE_app_all['clicked'] / DE_app_all['opened']

DE_wh_all = pd.DataFrame(DE_tshirt, columns =['Name:','Subject ','delivered','Opens','Clicks','Unsubscribes', 
                                            'CTR','OR','CTOR'])

"""