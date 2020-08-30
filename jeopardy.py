#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[99]:


pd.set_option('display.max_colwidth', -1)
jeopardy = pd.read_csv('jeopardy.csv')
jeopardy.head()


# In[100]:


jeopardy=jeopardy.rename(columns={
    "Show Number":"number",
    " Air Date": "date",
    " Round" :"round",
    " Category":"category",
    " Value": "value",
    " Question":"question",
    " Answer":"answer"})
print(jeopardy.columns)


# In[63]:


def keywords_questions(data, words):
    filters = lambda x :all(word.lower() in x.lower() for word in words)
    return data.loc[data['question'].apply(filters)]


# In[56]:


keywords_questions(jeopardy,["King","England"])


# In[104]:


jeopardy["values"]=jeopardy["value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)
print(jeopardy["values"])


# In[105]:


filtered=keywords_questions(jeopardy, ["King"])
print(filtered["values"].mean())


# In[106]:


def get_answer_count(data):
    return data["answer"].value_counts()
print(get_answer_count(filtered))


# In[107]:


def time_filter(data, year_two_digits):
    data['date'].apply(lambda x: x[0:2]=year_two_digits)
    return data


# In[108]:


time_filter(keywords_questions(jeopardy, ["Computer"]),'19')


# In[ ]:




