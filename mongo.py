
# coding: utf-8

# In[1]:


from pymongo import MongoClient
con = MongoClient('127.0.0.1', 27017)
db = con.article_connections
articles = db.articles
wordCountCache = db.wcCache
wordCountCache.ensure_index("word")


# In[4]:

article = articles.find_one()
print article


# In[5]:

from google_utils import getKeywordCount
from wordCount import wordCount
import operator


# In[6]:

counts = wordCount(article["content"])
import math
def getCachedKeywordCount(word):
    cachedWord = wordCountCache.find_one({"word":word})
    if cachedWord:
        return cachedWord["count"]
    count = getKeywordCount(word)
    wordCountCache.insert({"word":word, "count":count})
    return count

def calidf(counts)
    rst={}
    totalArticleCount=getCachedKeywordCount("a");
    total = 0
    for word, count in counts.iteritems():
        print 'checking word: ' + word
        total += count
        if len(word) == 0:
            continue
        wordArtCount=getCachedKeywordCount(word)
        tfidf = math.log(float(totalArticleCount)/(wordArtCount+1)) *count
        rst[word] = tfidf

    for word, count in rst.iteritems():
        rst[word] = float(count)/total
    return rst


# In[14]:

sorted_tuple = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
print sorted_tuple

