#!/usr/bin/env python
# coding: utf-8

# # Live Project
# 

# ### Importing Libraries

# In[45]:

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp1 = PdfPages('visualization-output.pdf')


# In[21]:


file=pd.read_csv(sys.argv[1], header = 0)


# In[22]:


file.fillna('None', inplace = True)


# ### Number of students applied for the different technologies
# 

# In[23]:


plt.figure(figsize=(15,10))
file['Areas of interest'].value_counts().plot(kind = 'pie',autopct='%1.1f%%', label='')
plt.legend(bbox_to_anchor=(1.2,0.9), loc="upper left")
title = plt.title('Number of students applied for the different technologies')
title.set_ha("left")
pp1.savefig(dpi=300,bbox_inches="tight")
plt.close()


# ### The number of students applied for Data Science who knew 'Python' and who didn’t.

# In[24]:


a = file['First Name'][(file['Programming Language Known other than Java (one major)'] == 'Python') & (file['Areas of interest'] == 'Data Science ')].count()
b = file['First Name'][file['Areas of interest'] == 'Data Science '].count() - a
df = pd.DataFrame([['did not know python', b], ['knew python', a]], columns = ['python', 'students'])


# In[25]:



fig2=sns.barplot(y="python", x="students", data=df).get_figure()
title3 = plt.title('The number of students applied for Data Science who knew Python and who didn’t')
pp1.savefig(fig2,dpi=300,bbox_inches="tight")
plt.close()


# ### The different ways students learned about this program

# In[26]:



plt.figure(figsize=(15,7))
file['How Did You Hear About This Internship?'].value_counts().plot(kind = 'pie',autopct='%1.1f%%', label='')
plt.legend(bbox_to_anchor=(1.2,0.9), loc="upper left")
title = plt.title('The different ways students learned about this program')
title.set_ha("left")
pp1.savefig(dpi=300,bbox_inches="tight")
plt.close()


# ### Students who are in the fourth year and have a CGPA greater than 8.0.

# In[27]:


df = pd.DataFrame(columns = ['cgpa', 'number of students'])
df1 = file[file['CGPA/ percentage'] > 8.0]
for i in df1['CGPA/ percentage'].unique():
    df = df.append(pd.DataFrame([[i, df1['First Name'][df1['CGPA/ percentage'] == i].count()]] ,columns = ['cgpa', 'number of students']))


# In[28]:



title2 = plt.title('Students who are in the fourth year and have a CGPA greater than 8.0.')
fig=sns.scatterplot(y="number of students", x="cgpa", data=df).get_figure()
pp1.savefig(fig,dpi=300,bbox_inches="tight")
plt.close()


# ### Students who applied for Digital Marketing with verbal and written communication score greater than 8.

# In[29]:


df = pd.DataFrame(columns = ['verbal score', 'written score', 'number of students'])
df1 = file[(file['Rate your written communication skills [1-10]'] > 8) & (file['Rate your verbal communication skills [1-10]'] > 8)]
for i in [9,10]:
    for j in [9,10]:
        df = df.append(pd.DataFrame([[i, j, df1['First Name'][(df1['Rate your verbal communication skills [1-10]'] == i) & (df1['Rate your written communication skills [1-10]'] == i)].count()]] ,columns = ['verbal score', 'written score', 'number of students']))


# In[30]:



fig3=sns.catplot(x="verbal score", y="number of students", hue="written score", data=df, height=6, kind="bar", palette="muted")
title4 = plt.title('Students who applied for Digital Marketing with verbal and written communication score greater than 8.')
pp1.savefig(fig3.fig,dpi=300,bbox_inches="tight")
plt.close()


# ### Year-wise classification of students.

# In[31]:


df = pd.DataFrame(columns = ['year', 'students'])
for i in ['First-year', 'Second-year', 'Third-year', 'Fourth-year']:
    df = df.append(pd.DataFrame([[i, file['First Name'][file['Which-year are you studying in?'] == i].count()]], columns = ['year', 'students']))


# In[32]:



title2 = plt.title('Year Wise Classification of students')
fig=sns.barplot(y="year", x="students", data=df).get_figure()
pp1.savefig(fig,dpi=300,bbox_inches="tight")
plt.close()


# ### Major wise Classification of Students

# In[33]:


df = pd.DataFrame(columns = ['Major', 'students'])
for i in file['Major/Area of Study'].unique():
    df = df.append(pd.DataFrame([[i, file['First Name'][file['Major/Area of Study'] == i].count()]], columns = ['Major', 'students']))


# In[34]:



title2 = plt.title('Area of Study Wise Classification of students')
fig=sns.barplot(y="Major", x="students", data=df).get_figure()
pp1.savefig(fig,dpi=300,bbox_inches="tight")
plt.close()

# ### City wise Classification of students

# In[35]:


df = pd.DataFrame(columns = ['city', 'students'])
for i in file['City'].unique():
    df = df.append(pd.DataFrame([[i, file['First Name'][file['City'] == i].count()]], columns = ['city', 'students']))


# In[36]:



title2 = plt.title('City Wise Classification of students')
fig=sns.barplot(y="city", x="students", data=df).get_figure()
pp1.savefig(fig,dpi=300,bbox_inches="tight")
plt.close()

# ### College wise Classification of Students

# In[37]:


df = pd.DataFrame(columns = ['college', 'students'])
for i in file['College name'].unique():
    df = df.append(pd.DataFrame([[i, file['First Name'][file['College name'] == i].count()]], columns = ['college', 'students']))


# In[38]:



title2 = plt.title('College Wise Classification of students')
fig=sns.barplot(y="college", x="students", data=df).get_figure()
pp1.savefig(fig,dpi=300,bbox_inches="tight")
plt.close()

# ### Plot the relationship between the CGPA and the target variable.

# In[39]:



fig2=sns.barplot(y="CGPA/ percentage", x="Label", data=file).get_figure()
title3 = plt.title('Relationship between the CGPA and the target variable.')
pp1.savefig(fig2,dpi=300,bbox_inches="tight")
plt.close()


# ### Plot the relationship between the Area of Interest and the target variable.

# In[40]:


df = pd.DataFrame(columns = ['Major', 'label', 'students'])
for i in file['Major/Area of Study'].unique():
    for j in file['Label'].unique():
        df = df.append(pd.DataFrame([[i, j, file['First Name'][(file['Major/Area of Study'] == i) & (file['Label'] == j)].count()]], columns = ['Major', 'label', 'students']))


# In[41]:



fig3=sns.catplot(x="Major", y="students", hue="label", data=df, height=6, kind="bar", palette="muted")
fig3.set_xticklabels(rotation = '45', ha='right')
title4 = plt.title('Relationship between the Area of Interest and the target variable.')
pp1.savefig(fig3.fig,dpi=300,bbox_inches="tight")
plt.close()

# ### Plot the relationship between the year of study, major, and the target variable

# In[42]:


df = pd.DataFrame(columns = ['Areas of interest', 'year', 'label', 'students'])
for i in file['Areas of interest'].unique():
    for j in ['First-year', 'Second-year', 'Third-year', 'Fourth-year']:
        for k in file['Label'].unique():
            df = df.append(pd.DataFrame([[i, j, k, file['First Name'][(file['Areas of interest'] == i) & (file['Which-year are you studying in?'] == j) & (file['Label'] == k)].count()]], columns = ['Areas of interest', 'year', 'label', 'students']))


# In[43]:



fig3=sns.catplot(x="Areas of interest", y="students", hue="label", col="year", data=df, height=6, kind="bar", palette="muted")
fig3.set_xticklabels(rotation = '45', ha='right')
title4 = plt.title('Relationship between the Area of Interest and the target variable.')
pp1.savefig(fig3.fig,dpi=300,bbox_inches="tight")
plt.close()

# In[44]:


pp1.close()

