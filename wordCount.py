
# coding: utf-8

# In[ ]:


import operator
import re

def wordCount(art):
    wcMap={}
    for w in art.split():
        word = normalize(w)
        if not wcMap.get(word):
            wcMap[word]=0
        wcMap[word]+=1
    return wcMap

def normalize(word):
    rst = word.lower()
    rst = re.sub(r"[^a-z0-9]+", "", rst)
    return rst


# In[ ]:



