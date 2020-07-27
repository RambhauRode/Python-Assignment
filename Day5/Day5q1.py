#!/usr/bin/env python
# coding: utf-8

# In[11]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
print("list1: ",list1)
print("list2: ",list2)

s1=len(list1)
s2=len(list2)

res=[]
i,j=0,0
while i<s1 and j<s2:
    if list1[i]<list2[j]:
        res.append(list1[i])
        i+=1
    else:
        res.append(list2[j])
        j += 1
        
res=res+list1[i:]+list2[j:]
print("Sorted Merged List",res)


# In[ ]:




