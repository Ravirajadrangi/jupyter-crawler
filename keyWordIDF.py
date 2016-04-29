
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
con = MongoClient('127.0.0.1', 27017)
db = con.article_connections
articlesDb = db.englishpod
wordCountCache = db.wcCache
wordCountCache.ensure_index("word")


# In[ ]:

import re
file = open('articles.in', 'r')
p = re.compile(r'(^.*\([A-Z][0-9]+\))', re.M)
articles = p.split(file.read())
file.close()


# In[3]:

from idf import calidf
from wordCount import wordCount
import operator

for i in range(len(articles)/2):
    title = articles[2*i+1]
    content = articles[2*i+2]
    if articlesDb.find_one({'title':title}):
        print 'article title: ' + title + ' exists'
        continue
    print '=== Start Processing ==='
    print 'title: ' + title
    print 'content: ' + content
    article = {"title":title, "content":content}
    
    counts = wordCount(articles[2*i+2])
    idfs = calidf(counts)
    sorted_tuple = sorted(idfs.items(), key=operator.itemgetter(1), reverse=True)
    article['keyidfs']=sorted_tuple[0:10]
    
    articlesDb.insert_one(article)
    print '=== End Processing ==='


# a = articlesDb.find_one({'title':'123'})
# print a

# In[3]:

wordCountCache.count()


# In[ ]:



