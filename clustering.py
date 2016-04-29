
# coding: utf-8

# In[2]:

from pymongo import MongoClient
con = MongoClient('127.0.0.1', 27017)
db = con.article_connections
articles = db.englishpod


# In[ ]:

import operator
def cosdist(a, b):
    aidfs = sorted(a['keyidfs'],operator.itemgetter(0)) 
    bidfs = sorted(b['keyidfs'],operator.itemgetter(0))
    ai = bi = 0;
    while ai<=len(aidfs) and bi<=len(bidfs):
        ka = aidfs[ai][0]
        kb = bidfs[bi][0]
        if(ka>kb):
            

