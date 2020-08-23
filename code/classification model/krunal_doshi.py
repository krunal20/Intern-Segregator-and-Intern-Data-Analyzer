#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
import warnings
from sklearn.exceptions import DataConversionWarning
from sklearn.exceptions import ConvergenceWarning
df = pd.read_csv(sys.argv[1], header=0)

df.fillna(value = 'None', inplace = True)


# In[39]:


df.columns


# In[55]:


def score(df):
    df['resumelink'] = np.where(df['Link to updated Resume (Google/ One Drive link preferred)'] == 'None', 0, 1)
    df['linkedinlink'] = np.where(df['link to Linkedin profile'] == 'None', 0, 1)
    xdf = df.drop(labels = ['First Name', 'Emergency Contact Number', 'University Name', 'Last Name', 'City', 'State', 'Zip Code', 'DOB [DD/MM/YYYY]', 'Email Address', 'Contact Number', 'Link to updated Resume (Google/ One Drive link preferred)', 'link to Linkedin profile', 'How Did You Hear About This Internship?', 'Label'], axis = 1)
    xdf = pd.get_dummies(data = xdf, drop_first = True)
    ydf = pd.get_dummies(data = df['Label'], drop_first = True)
    from sklearn.neighbors import KNeighborsClassifier
    from math import sqrt
    n = int(sqrt(xdf.Age.count()*75/100))
    if n%2 == 0:
        n = n-1
    clf = KNeighborsClassifier(n_neighbors = n)
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import f1_score
    #scores = cross_validate(clf, xdf, ydf, scoring=['accuracy', 'f1'], cv = 20)
    xtrain, xtest, ytrain, ytest = train_test_split(xdf, ydf.ineligible)
    clf.fit(xtrain,ytrain)
    ypred = clf.predict(xtest)
    results = f1_score(ypred,ytest)
    return results


# In[56]:


print(score(df))

