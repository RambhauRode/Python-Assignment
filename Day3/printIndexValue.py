#!/usr/bin/env python
# coding: utf-8

# In[62]:


sentence='what we think we become we become programmer'
word='we'
s=sentence.split(" ")
count=0
for we in s:
    if we == word:
        print("Substring at index values: ",int(count))
    count+=1
    
    


# In[ ]:




