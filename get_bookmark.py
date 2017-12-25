import json
import os
import pandas as pd
import nltk
from nltk import FreqDist
from collections import Counter
import itertools
from pprint import pprint
from nltk.corpus import stopwords
import re

with open(os.path.expanduser('~/.config/google-chrome/Default/Bookmarks'), 'r') as f:
    bookmark_data = json.load(f)

df=bookmark_data["roots"]["bookmark_bar"]["children"]

name_lst=[]
url_lst=[]
for i in range(len(df)):
    try:
        url_lst.append(df[i]["url"])
        name_lst.append(df[i]["name"])
    except:
        pass
df = pd.DataFrame({"name": name_lst, "url": url_lst})

kelimeler=[]
for i in range(len(df)):
    z=nltk.word_tokenize(df["name"][i])
    kelimeler.append(z)

print(kelimeler)

kelimeler=list(itertools.chain(*kelimeler))

stopwords_list = stopwords.words('english')
filtered_words = [word for word in kelimeler if word not in stopwords_list]  ## gereksiz bağlaçlar silindi
valsLower = [item.lower() for item in filtered_words]

clean_list=[]
for i,item in enumerate(valsLower):
    if len(valsLower[i])>2:
        clean_list.append(valsLower[i])

z=Counter(clean_list)

pprint(z)