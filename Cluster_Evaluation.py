#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from sklearn.feature_extraction.text import TfidfVectorizer
import math

dir_cluster="/Users/prochetasen/Downloads/Results2/"

clusters=os.listdir(dir_cluster)

def computeSim(doc1,doc2):
    sim=0
    len1=0
    len2=0
    for i in range(len(doc1[0])):
        sim=sim+doc1[0][i]*doc2[0][i]
        len1=len1+doc1[0][i]*doc1[0][i]
        len2=len2+doc2[0][i]*doc2[0][i]
        
  
    return sim/(math.sqrt(len1)*math.sqrt(len2))



def cluster_eval(docs):
    sim=0
    docLen=docs.shape[0]
    k=0
    for i in range(0,docLen-1):
        for j in range(i+1, docLen):
            z=computeSim(X[i,].toarray(),X[j,].toarray())
            sim=sim+z
           
                 
    return sim/(docLen*((docLen-1)/2))

def computeIntrasim(cluster1,cluster2):
    
    k=len(cluster1)
    for i in range(len(cluster2)):
        cluster1.append(cluster2[i])
   
    x1 = vectorizer.fit_transform(cluster1)
    
    sim=0
    x1Len=x1.shape[0]
    for i in range(k):
        for j in range(k,x1Len):
            sim=sim+computeSim(x1[i,].toarray(),x1[j,].toarray())
            
    
    return sim/((x1Len-k)*k)





corpus=[]


vectorizer = TfidfVectorizer()

totalSim=0
count=0
cluster_docs=[]
for cluster in clusters:
    print("Cluster number ",cluster)
    docs=[]
    files=os.listdir(dir_cluster+cluster)
    for file in files:
        text=""
        with open("/Users/prochetasen/Downloads/Results2/"+cluster+"/"+file,"r") as f1:
            for line in f1:
                  text=text+line
        docs.append(text)
    X = vectorizer.fit_transform(docs)
    #print(vectorizer.get_feature_names())
    #print(X)
    
    sim=cluster_eval(X)
    totalSim=totalSim+sim
    count=count+1
    cluster_docs.append(docs)
    #if count==1:
        #break
    

intra_sim=0    
for i in range(len(cluster_docs)-1):
    for j in range(i+1, len(cluster_docs)):
        intra_sim=intra_sim+computeIntrasim(cluster_docs[i],cluster_docs[j])
        #break
    #break
      
        


    
c=len(cluster_docs)*(len(cluster_docs)-1)/2 


print("Avg similarity within clusters ",totalSim/len(clusters))
print("Avg similarity Between clusters ",intra_sim/c)
    #break


# In[ ]:





# In[ ]:




