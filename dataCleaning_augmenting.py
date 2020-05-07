# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:57:30 2020

@author: abhi0
"""

import pandas as pd
import numpy as np

df_beside=pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/IdiomBeside-2.csv")
dfIdioms=list(df_beside['A hot potato'])
notNullIdx_1=np.where(df_beside[df_beside.columns[1]].isnull()==False)

for i in (notNullIdx_1[0][:]):
    print(i)

df_meanings=['']*len(dfIdioms)

temp=notNullIdx_1[0][:]

df_meanings[temp[0]]=df_beside[df_beside.columns[1]][notNullIdx_1[0][0]]

numCol=5 #number of columns not taking the first into consideration
notNullIdx=[]

for i in range(1,6):
    notNullIdx.append(np.where(df_beside[df_beside.columns[i]].isnull()==False))
    temp=notNullIdx[i-1]
    for k in range(len(temp[0])):
        df_meanings[temp[0][k]]=df_beside[df_beside.columns[i]][temp[0][k]]  
        
meanFrame=[]
IdiomFrame=[]
meanFrame=pd.DataFrame(df_meanings)        
IdiomFrame=pd.DataFrame(dfIdioms)

result_1=pd.concat([IdiomFrame,meanFrame],axis=1)
###############################################################################
        
#For the other csv files: 
df_below=\
pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/IdiomBelow_1.csv")   

meanList=[]
idiomList=[]
for i in range(1,len(df_below),2):
    temp=df_below['Idiom'][i]
    startIdx=temp.find(' ')
    meanList.append(temp[startIdx+1:])
    idiomList.append(df_below['Idiom'][i-1])
 
meanFrame=pd.DataFrame(meanList)
IdiomFrame=pd.DataFrame(idiomList)

result_2=pd.concat([IdiomFrame,meanFrame],axis=1)

############################################################################$
#For the otehr below csv file: 

df_below2=\
pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/IdiomBelow_2.csv")       
         
tempList=list(df_below2[df_below2.columns[0]][1:])

meanList=[]
idiomList=[]

for i in range(1,len(tempList),2):
    temp=tempList[i-1]
    meanList.append(temp)
    idiomList.append(tempList[i])
    
meanFrame=pd.DataFrame(meanList)
IdiomFrame=pd.DataFrame(idiomList)

result_3=pd.concat([IdiomFrame,meanFrame],axis=1)    
    
############################################################################## 
###  
df_beside=\
pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/IdiomBeside.csv")
 
meanList=[]
idiomList=[]

idiomList=list(df_beside[df_beside.columns[0]])
meanList=list(df_beside[df_beside.columns[1]])   

meanFrame=pd.DataFrame(meanList)
IdiomFrame=pd.DataFrame(idiomList) 

result_4=pd.concat([IdiomFrame,meanFrame],axis=1)

##############################################################################

df3=\
pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/IdiomBelow_3.csv")
temp=[]  
idiomList=[]
meanList=[] 

import re
 
for i in range(len(df3)):
    tempPrime=df3['Idioms and meaning'][i] 
    if '–' not in tempPrime:
        continue
    else:
        temp=re.split('\s\–\s',tempPrime)
        idiomList.append(temp[0])
        meanList.append(temp[1])
        
meanFrame=pd.DataFrame(meanList)
IdiomFrame=pd.DataFrame(idiomList) 

result_5=pd.concat([IdiomFrame,meanFrame],axis=1)  

##############################################################################
df4=\
pd.read_csv("C:/Users/abhi0/OneDrive/Documents/Idioms_meaning_collection/Idiom_Below4.csv")

temp=[]
idiomList=[]
meanList=[]

for i in range(len(df4)):
    
    tempPrime=df4[df4.columns[0]][i]
    
    if ':' not in tempPrime:
        continue
    else:
        temp=df4[df4.columns[0]][i].split(':')
        idiomList.append(temp[0])
        meanList.append(temp[1])
        
meanFrame=pd.DataFrame(meanList)
IdiomFrame=pd.DataFrame(idiomList) 

result_6=pd.concat([IdiomFrame,meanFrame],axis=1)  

result_6.isnull().sum()
result_6.isna().sum()
        
########################### #Merging the data-frames: ########################

finalResult=pd.concat([result_1,result_2,\
                       result_3,result_4,result_5,result_6],axis=0,ignore_index=True)
    
#Adding header:
finalResult.columns=['Idiom','Meaning']  

finalResult.dropna(inplace=True)  
finalResult.reset_index(drop=True,inplace=True)    

##looking for special characters in a the meaning
##might contain another meaning,can be moved to another list
#looking for headings
string_check= re.compile('[@_#$%^&()<>/\|;}{~:0-9]')
tempIdx=[]
tempStr=[]
    
for i in range(len(finalResult['Meaning'])):
    
    if(len(finalResult['Meaning'][i])==0):
        continue
    else:
        if(string_check.search(finalResult['Meaning'][i]) == None):
            continue
        else: 
            tempStr.append(finalResult['Meaning'][i])
            tempIdx.append(i)
            if finalResult['Meaning'][i].isupper()==True:
                finalResult.drop(i,inplace=True)  
                
   
    
#Removing some unnecessary rows: 
Idx=[]            
Idx=np.where(finalResult['Meaning']=='Meaning')     
for i in range(len(Idx)):
    finalResult.drop(Idx[i],inplace=True)   

##Move the double-meanings of the idioms or duplicate


    
      
    
    