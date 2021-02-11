# -*- coding: utf-8 -*-
"""
Created on Web Nov 11 18:24:12 2020

Divide by Period

@author: jaewoong Han
"""

# package
import re
from konlpy.tag import Hannanum
from pprint import pprint
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

# load file
data_glam = pd.read_excel("./data/글램.xlsx")
data_dang = pd.read_excel("./data/당연시.xlsx")
data_sim = pd.read_excel("./data/심쿵.xlsx")
data_amanda = pd.read_excel("./data/아만다.xlsx")
data_wipi = pd.read_excel("./data/위피.xlsx")
data_noon = pd.read_excel("./data/정오의데이트.xlsx")

## 글램+위피 up/ 나머지down
data_up = pd.concat([data_sim, data_wipi])
data_down = pd.concat([data_glam, data_dang,data_amanda,data_noon])

# data 기간 별 수정
data_up['DATE']=data_up['DATE'].str.replace('년','')
data_up['DATE']=data_up['DATE'].str.replace('월','')
data_up['DATE']=data_up['DATE'].str.replace('일','')
data_up['DATE']=data_up['DATE'].str.replace(" ",'')
data_down['DATE']=data_down['DATE'].str.replace('년','')
data_down['DATE']=data_down['DATE'].str.replace('월','')
data_down['DATE']=data_down['DATE'].str.replace('일','')
data_down['DATE']=data_down['DATE'].str.replace(" ",'')
data_up['DATE']=pd.to_numeric(data_up['DATE'])
data_down['DATE']=pd.to_numeric(data_down['DATE'])

data_up_1 = data_up['DATE'] <= 20181231
data_up_2 = data_up['DATE'] >= 20190101
data_up_1 = data_up[data_up_1]
data_up_2 = data_up[data_up_2]

data_down_1 = data_down['DATE'] <= 20181231
data_down_2 = data_down['DATE'] >= 20190101
data_down_1 = data_down[data_down_1]
data_down_2 = data_down[data_down_2]

# 기간별 저장
data_up_1.to_excel('글램+위피 전.xlsx')
data_up_2.to_excel('글램+위피 후.xlsx')
data_down_1.to_excel('심쿵+당연시+아만다+정오 전.xlsx')
data_down_2.to_excel('심쿵+당연시+아만다+정오 후.xlsx')


