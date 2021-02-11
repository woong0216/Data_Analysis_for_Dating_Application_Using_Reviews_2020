# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:44:31 2020

Weight value

@author: jaewoong Han
"""


doc = pd.read_excel("./data/글램+위피 전 TF-IDF.xlsx")
doc2=pd.read_excel("./data/글램+위피 전.xlsx")
del doc['Unnamed: 0']
del doc2['Unnamed: 0']

doc2['documents']=doc2.index
doc3=pd.merge(doc,doc2, on='documents')
doc3['Weight STAR']=doc3['STAR']-2
doc3['Weighted value']=doc3['values']*doc3['Weight STAR']

doc3.to_excel('글램+위피 전 긍정_부정.xlsx')



