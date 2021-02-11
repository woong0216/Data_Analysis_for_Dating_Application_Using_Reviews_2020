# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:44:31 2020

Co-occurrence

@author: jaewoong Han
"""


import pandas as pd
import numpy as np

doc = pd.read_excel("./data/글램+위피 후 긍정 TF-IDF 가중치.xlsx")
doc=doc.sort_values(by='documents',ascending=True)
doc=doc.reset_index(drop=True)

doc.rename(columns = {'Weighted value' : 'Weighted_value'}, inplace = True)
doc= doc[doc.Weighted_value >=0.35]

sentences_greater_2 = len(doc['sentences']) >= 2
value_greater_point3 = doc['Weighted_value'] >= 0.5

doc = doc[sentences_greater_2 & value_greater_point3]

sentences_greater_2 = len(doc['sentences']) >= 2
value_greater_point3 = doc['Weighted_value'] >= 0.3

doc = doc[sentences_greater_2 & value_greater_point3]

doc2=doc.pivot(index='documents',columns='sentences',values='Weighted_value')

df_pivoted1=doc2
df_pivoted2 = df_pivoted1.copy()
df_pivoted2.columns = df_pivoted2.columns.values
df_pivoted2.reset_index(level=0, inplace=True)
df = df_pivoted2.fillna(0)


data1=np.dot(df.transpose(),df)
data2=pd.DataFrame(data1)

data2.to_excel("글램+위피 후 긍정 행렬 최종.xlsx")