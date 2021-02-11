# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:44:31 2020

TF-IDF

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

doc = pd.read_excel("./data/글램+위피 전.xlsx")
doc=doc.reset_index(drop=True)
doc=doc.dropna(axis=0) # 결측치있는 행 제거
data_date=doc['DATE'] # 리뷰 날짜
data_content=doc['REVIEW'] # 리뷰 콘텐츠

# pre-processing
def review_preprocessing(data):
    # Hannanum package
    pos_tagger = Hannanum()

    # 뉴스를 tokenizing한 후, 명사만 추출
    pos_nouns = pos_tagger.nouns(data)
    
    return ' '.join(pos_nouns)

content_noun=[]
for i in data_content:
    content_noun.append(review_preprocessing(i))
    
    
# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

# ============================================
# -- Get TFIDF
# ============================================
vectorizer = TfidfVectorizer()
sp_matrix = vectorizer.fit_transform(content_noun)

word2id = defaultdict(lambda : 0)
for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx
documents=[]
sentences=[]
values=[]
for i, sent in enumerate(content_noun):
    for token in sent.split():
        documents.append(i)
        sentences.append(token)
        values.append(sp_matrix[i, word2id[token]])
    
#     print('====== document[%d] ======' % i)
#     print( [ (token, sp_matrix[i, word2id[token]]) for token in sent.split() ] )   

res_dict = []
for i in range(len(values)):
    res_dict.append({
        'documents' : documents[i],
        'sentences' : sentences[i],
        'values' : values[i]
    })
    
res_df = pd.DataFrame(res_dict)
res_df.head(20)

res_df.to_excel('글램+위피 전 TF-IDF.xlsx')