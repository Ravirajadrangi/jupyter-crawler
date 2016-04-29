
# coding: utf-8

# In[1]:

from google_utils import getKeywordCount
from wordCount import wordCount
import operator

from pymongo import MongoClient
con = MongoClient('127.0.0.1', 27017)
db = con.article_connections
wordCountCache = db.wcCache
wordCountCache.ensure_index("word")


# In[2]:

import math
def getCachedKeywordCount(word):
    cachedWord = wordCountCache.find_one({"word":word})
    if cachedWord:
        return cachedWord["count"]
    count = getKeywordCount(word)
    wordCountCache.insert({"word":word, "count":count})
    return count

def calidf(counts):
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


# In[3]:

articles = db.englishpod
print articles.count()
articles.find_one()


# In[4]:

import re, operator
from wordCount import wordCount
file = open('articles.in', 'r')
p = re.compile(r'(^.*\([A-Z][0-9]+\))', re.M)
articlesIn = re.split(p, file.read())
for i in range(len(articlesIn)):
    title = articlesIn[2*i+1]
    content = articlesIn[2*i+2]
    if articles.find_one({'title':title}):
        print title + ' exists!'
        continue
    print '=== Processing ' + title
    counts = wordCount(content)
    keyidfs = calidf(counts)
    sorted_tuple = sorted(keyidfs.items(), key=operator.itemgetter(1))
    articles.insert_one({'title':title, 'content':content, 'keyidfs':sorted_tuple[0:10]})
    print '=== End processing ' + title


# In[ ]:



