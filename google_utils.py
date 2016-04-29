
# coding: utf-8

# In[10]:


import httplib
import re

engineUrl = 'www.google.com'
searchPath = '/search?q='

def search(searchStr, regex):
    match = re.search(regex, searchStr)
    # If-statement after search() tests if it succeeded
    if match:                      
        return match
    else:
        print 'did not find'

def getKeywordCount(keyword):
    connection = httplib.HTTPSConnection(engineUrl)
    connection.request('GET', searchPath + keyword)
    response = connection.getresponse()
    resultStr = response.read()
    connection.close()

    prefix = 'About '
    suffix = ' results'
    regex = '([0-9,]+)'

    countStr = search(resultStr, prefix+regex+suffix).group(1).replace(",", "")
    return int(countStr)


# In[ ]:



