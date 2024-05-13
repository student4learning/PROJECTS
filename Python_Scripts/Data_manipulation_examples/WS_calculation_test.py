# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:19:10 2020

@author: Acer
"""


#########Welcome Series
WS_all = pd.read_csv('C:/Users/Acer/Downloads/WS delivery 2020-06-01.csv')
WS_all_DF_colname = list(WS_all.columns.values) 
WS_all['year_month'] = pd.to_datetime(WS_all['year_month'],errors='coerce')
WS_all['year_month'] = WS_all['year_month'].dt.strftime('%Y/%m')
WS_all = WS_all.groupby(['market', 'campaign_type','year_month']).sum().reset_index()

#Divide campaings in Organic, App reg, Co-reg and not defined
WS_Organ = WS_all[WS_all['campaign_type'].str.contains('Organic')]
WS_Organ = WS_Organ.groupby(['market','year_month']).sum().reset_index()
WS_Organ['CTR'] = (WS_Organ['clickers']/WS_Organ['unique_delivered'])*100
WS_Organ_CTR = WS_Organ['clickers'].sum()/WS_Organ['unique_delivered'].sum()
WS_Organ['OR'] = (WS_Organ['openers']/WS_Organ['unique_delivered'])*100
WS_Organ_OR = WS_Organ['openers'].sum()/WS_Organ['unique_delivered'].sum()
print(round(WS_Organ_CTR,2))
print(round(WS_Organ_OR,2))



WS_Appreg = WS_all[WS_all['campaign_type'].str.contains('AppReg')]
WS_Appreg = WS_Appreg.groupby(['market','year_month']).sum().reset_index()
WS_Appreg['CTR'] = (WS_Appreg['clickers']/WS_Appreg['unique_delivered'])*100
WS_Appreg_CTR = WS_Appreg['clickers'].sum()/WS_Appreg['unique_delivered'].sum()
WS_Appreg['OR'] = (WS_Appreg['openers']/WS_Appreg['unique_delivered'])*100
WS_Appreg_OR = WS_Appreg['openers'].sum()/WS_Appreg['unique_delivered'].sum()
print(round(WS_Organ_CTR,2))
print(round(WS_Organ_OR,2))

WS_Coreg = WS_all[WS_all['campaign_type'].str.contains('CoReg')]
WS_Coreg = WS_Coreg.groupby(['market','year_month']).sum().reset_index()
WS_Coreg['CTR'] = (WS_Coreg['clickers']/WS_Coreg['unique_delivered'])*100
WS_Coreg_CTR = WS_Coreg['clickers'].sum()/WS_Coreg['unique_delivered'].sum()
WS_Coreg['OR'] = (WS_Coreg['openers']/WS_Coreg['unique_delivered'])*100
WS_Coreg_OR= WS_Coreg['openers'].sum()/WS_Coreg['unique_delivered'].sum()
print(round(WS_Organ_CTR,2))
print(round(WS_Organ_OR,2))

WS_undef_campaigns = WS_all[WS_all['campaign_type'].str.contains('Not defined')]
WS_undef_campaigns = WS_undef_campaigns.groupby(['market','year_month']).sum().reset_index()
WS_undef_campaigns['CTR'] = (WS_undef_campaigns['clickers']/WS_undef_campaigns['unique_delivered'])*100
WS_undef_campaigns_CTR = WS_undef_campaigns['clickers'].sum()/WS_undef_campaigns['unique_delivered'].sum()
WS_undef_campaigns['OR'] = (WS_undef_campaigns['openers']/WS_undef_campaigns['unique_delivered'])*100
WS_undef_campaigns_OR= WS_undef_campaigns['openers'].sum()/WS_undef_campaigns['unique_delivered'].sum()
print(round(WS_Organ_CTR,2))
print(round(WS_Organ_OR,2))

#Matching the data for unidentified campaigns (put this before the Welcome series campaign split once done)
WS_campaigns = pd.read_excel('C:/Users/Acer/Documents/Profissional/Saatchi/resources/4.P&G/PAMPERS/welcome_series_campaing_map.xlsx')
WS_undef_campaigns = WS_all[WS_all['campaign_type'].str.contains('Not defined')]
WS_undef_campaigns=WS_undef_campaigns.drop(columns=['campaign_type'])

WS_match_all = pd.merge(WS_undef_campaigns,WS_campaigns[['cmpgn_name', 'campaign_type']],on='cmpgn_name', how='left')
