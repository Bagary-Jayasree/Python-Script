#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


User_details = pd.read_csv('UserDetails.csv')
cooking_sessions = pd.read_csv('CookingSessions.csv')
order_details = pd.read_csv('OrderDetails.csv')


# In[5]:


print(User_details.isnull().sum())


# In[8]:


print(cooking_sessions.isnull().sum())


# In[11]:


print(order_details.isnull().sum())


# In[13]:


User_details.fillna(method= 'ffill', inplace=True)
cooking_sessions.dropna(inplace=True)


# In[14]:


merged_data = pd.merge(User_details, cooking_sessions, on = 'User ID', how ='inner')
merged_data = pd.merge(merged_data, order_details, on = 'User ID', how = 'inner')


# In[15]:


merged_data


# In[20]:


merged_data.columns


# In[22]:


popular_dishes = merged_data['Dish Name_y'].value_counts()
print("Popular Dishes:\n", popular_dishes)


# In[24]:


cooking_vs_orders = merged_data.groupby('User ID')[['Session ID_x','Order ID']].sum()
print("Cooking Sessions vs Orders:\n", cooking_vs_orders)


# In[26]:


age_analysis = merged_data.groupby('Age')['Order ID'].sum()
print("Age vs Order ID:\n", age_analysis)


# In[29]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[31]:


plt.figure(figsize=(10,6))
sns.barplot(x=popular_dishes.index, y=popular_dishes.values)
plt.xticks(rotation=45)
plt.title("Popular Dishes")
plt.show()


# In[34]:


plt.figure(figsize=(10,6))
sns.lineplot(x=age_analysis.index, y=age_analysis.values)
plt.title("Age vs Order Count")
plt.show()


# In[37]:


merged_data.to_csv('MainData.csv', index=False)


# In[ ]:




