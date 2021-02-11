# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:44:31 2020

Weight value + TF-IDF

@author: jaewoong Han
"""

doc = pd.read_excel("./data/글램+위피 후 부정.xlsx")
doc=doc.reset_index(drop=True)

doc=doc.dropna(axis=0) # 결측치있는 행 제거
data_date=doc['DATE'] # 리뷰 날짜
data_content=doc['REVIEW'] # 리뷰 콘텐츠

# 전처리
# 정규식을 이용한 제거
pattern='[|ㄱ-ㅎ|ㅏ-ㅣ]+'
pattern2='[-=.#/:$}]'
repl =''
email_par=[]
for i in doc['REVIEW']:
    text = re.compile(pattern).sub('',i)
    text = re.sub(pattern2,'',text)
    if text =='':
        continue
    else:
        email_par.append(text)
        
# 이모지, 이모티콘 제거
def rmEmoji_ascii(inputString):
    return inputString.encode('euc-kr', 'ignore').decode('euc-kr')
emoji=[]
for a in email_par:
    text = rmEmoji_ascii(a)
    if text =='':
        continue
    else:
        emoji.append(text)
emoji_=[]
for a in emoji:
    b=a.replace('.', '').replace(',','').replace("'","").replace('·', '').replace('=','').replace('\n','')
    emoji_.append(b)

# kkam 이용        
from konlpy.tag import Kkma
kkma = Kkma()

def spacing_kkma(wrongSentence):
    tagged = kkma.pos(wrongSentence)
    corrected = ""
    for i in tagged:
        if i[1][0] in "JEXSO":
            corrected += i[0]
        else:
            corrected += " "+i[0]
    if corrected[0] == " ":
        corrected = corrected[1:]
    return corrected

abc=[]
for sentence in emoji_:
    try:
        text = spacing_kkma(sentence)
        abc.append(text)
    except Exception:
        print("에러")           
        
from konlpy.tag import Okt
okt = Okt()

def spacing_okt(wrongSentence):
    tagged = okt.pos(wrongSentence)
    corrected = ""
    for i in tagged:
        if i[1] in ('Josa', 'PreEomi', 'Eomi', 'Suffix', 'Punctuation'):
            corrected += i[0]
        else:
            corrected += " "+i[0]
    if corrected[0] == " ":
        corrected = corrected[1:]
    return corrected

abcd=[]
for sentence in abc:
    text = spacing_okt(sentence)
    abcd.append(text)
    
email_par_b=[]
for i in abcd:
    text = re.compile(pattern).sub('',i)
    email_par_b.append(text)
    
text_a=[]
for i in email_par_b:
    a=i.split()
    text=[]
    for b in a:
        if b=='어어' or len(b)<=1:
            continue
        else:
            text.append(b)
    text=" ".join(text)    
    text_a.append(text)

def review_preprocessing(data):
    # Hannanum package
    pos_tagger = Hannanum()

    # 리뷰를 tokenizing한 후, 명사만 추출
    pos_nouns = pos_tagger.nouns(data)
    
    return ' '.join(pos_nouns)

content_noun=[]
for i in text_a:
    if len(review_preprocessing(i))<=1:
        continue
    else:
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

res_df.to_excel('./data/글램+위피 후 부정 TF-IDF.xlsx')
       
        
        
        
        
        
        
        
        
        
        
        
        
        




