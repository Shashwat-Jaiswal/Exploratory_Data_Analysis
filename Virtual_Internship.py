#!/usr/bin/env python
# coding: utf-8

# # Name-Shashwat Jaiswal
# 
# 
# # Graduate Rotational Internship Program :- The Sparks Foundation
# 
# # Task 4: Exploratory Data Analysis- Terrorism
# 
# 
# #### EDA on Dataset ("GLOBAL TERRORISM") :-- https://bit.ly/2TK5Xn5
# 
# #### 1. As a security/defence analyst, tried to find out the hot zone of Terrorism.
# #### 2. Mentioned what all the security issues and insights that can be derived by the EDA. 

# ### Importing the libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Loading the Dataset

# In[8]:


data = pd.read_csv("C:/Users/user/.jupyter/global_terrorism.csv",encoding='ISO-8859-1',low_memory=False)
print("Data is loaded")


# In[9]:


df = data
df


# In[15]:


## TOTAL NO OF ROWS AND COLUMNS
df.shape


# In[24]:


## some basic statistical details 
df.describe()


# In[96]:


## COLUMNS IN THE DATA SET
df.columns.values
## WE ANALYZE THAT MANY COLUMNS CAN BE REMOVED OR RENAMED


# In[98]:


## TOTAL NO OF ROWS ANS COLUMNS
df.shape


# In[95]:


## Summary of the dataframe
df.info()


# ### Cleaning the Data 

# In[78]:


## RENAMING THE COLUMNS ,IN MORE READABLE FORM
data.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'State','city':'City','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','targsubtype1_txt':'Targetsubtype','target1':'Target','weaptype1_txt':'Weapon','nkill':'kill','nwound':'Wound','gname':'Group','motive':'Motive','region_txt':'Region'},inplace=True)


# In[39]:


## TAKING THE USEFUL COLUMNS 
new_data = data[['Year','Month','Day','Country','State','City','Attacktype','Targettype','Targetsubtype','Target','Weapon','kill','Wound','Group','Motive','Region']]


# In[40]:


new_data.head().T


# In[41]:


## THE COLUMN IS UPDATED 
new_data.shape


# In[44]:


## CHECKING FOR THE MISSING VALUES
new_data.isnull().sum()


# In[45]:


#filling the columns those having missing values
nd=new_data
nd['City'] = nd['City'].fillna(0)
nd['State'] =nd['State'].fillna(0)
nd['Targetsubtype'] =nd['Targetsubtype'].fillna(0)
nd['Target'] =nd['Target'].fillna(0)
nd['Weapon'] =nd['Weapon'].fillna(0)
nd['kill'] =nd['kill'].fillna(0)
nd['Wound'] =nd['Wound'].fillna(0)
nd['Group'] =nd['Group'].fillna(0)
nd['Motive'] =nd['Motive'].fillna(0)
nd.isnull().sum()


# In[48]:


print("Country with maximum no of attacks:\n",nd['Country'].value_counts().head(10))
## LOOK!,We analyzed Iraq has max Attacks.


# In[55]:


plt.figure(figsize = (10,5))
sns.barplot(df['Country'].value_counts()[:15].index,df['Country'].value_counts()[:15])
plt.title('Top Countries Effected',fontsize=14,weight="bold")
plt.xlabel('Countries',fontsize=12,weight="bold")
plt.ylabel('Count',fontsize=12,weight="bold")
plt.xticks(rotation=60)
sns.despine()
plt.show()
## VISUALIZING MOST EFFECTED COUNTRIES


# In[61]:


plt.figure(figsize = (10,5))
sns.barplot(df['State'].value_counts()[:15].index,df['State'].value_counts()[:15])
plt.title('Top States Effected',fontsize=14,weight="bold")
plt.xlabel('State',fontsize=12,weight="bold")
plt.ylabel('Count',fontsize=12,weight="bold")
plt.xticks(rotation=75)
sns.despine()
plt.show()
## VISUALIZING MOST EFFECTED STATES


# In[69]:


pd.crosstab(nd.Year,nd.Region).plot(kind='area',figsize=(10,5))
plt.title("Terrorist Activities by Region in Each year",fontsize=14,weight="bold")
plt.ylabel('Number of attacks',fontsize=12,weight="bold")
plt.xlabel('year',fontsize=12,weight="bold")
sns.despine()
plt.grid()
plt.show()
## Area plot


# In[68]:


plt.subplots(figsize=(10,5))
sns.countplot('Year',data = new_data)
plt.xticks(rotation=90)
plt.title('No. of terrorist activities each year',fontsize=14,weight="bold")
sns.despine()
plt.show()


# In[71]:


plt.subplots(figsize=(15,5))
sns.countplot(x=nd['Attacktype'],order = nd['Attacktype'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('Method',)
plt.title('Types of Attack',fontsize=14,weight="bold")
sns.despine()
plt.show()


# ### Finding out the terrorist organizations that carried out the operations in different country.

# In[83]:


plt.subplots(figsize=(10,8))
sns.barplot(y=nd['Group'].value_counts()[1:12].index,x=nd['Group'].value_counts()[1:12].values)
plt.title('Most Active Terrorist Organizations',fontsize=14,weight='bold')
plt.show()


# ### Analyzing attacks with reference to month
# 

# In[86]:


plt.figure(figsize=(10,10))
df['Month'].value_counts().plot(kind='pie',autopct="%.1f%%")
plt.show()
## MOST ATTACKS WE SEE ARE HAPPENING IN MAY & THE LEAST IN NOVEMBER.


# ##### MOST LIKELY TARGETS

# In[87]:


TOP_10_TARGET = df['Target'].value_counts()[:10]
print(TOP_10_TARGET)
## BELOW WE CAN SEE THAT MOST OF THE TARGETS WHERE THE "CIVILIANS".


# # RESULT :-
# 
# ##### <1>. Mostly the targets were the Citizens.
# ##### <2>. Terrorist activities are more in Middle East and South  Africa.
# ##### <3>. Iraq has suffered the maximum no. of terror attacks.
# ##### <4>. Andora has suffered the minimum no of terror attacks.
# ##### <5>. Attacks has increased in 2010 in Middle east and South africa.
# ##### <6>. Top 5 countries with most attacks: Iraq,  Pakistan,Afghanistan,India,Columbia.
# ##### <7>. Top 5 cities with most attacks: Baghdad ,Karachi,Lima , Mosul, Belfast.
# ##### <8>.Total no. of attacks from 1970 has increased drastically till 2017.
# ##### <9>. Muslims are effected most by these attacks.
# ##### <10>. Terrorist attacks in Middle East and North America had fatal            consequences.
# 

# #                  ----THANKYOU----

# In[ ]:




