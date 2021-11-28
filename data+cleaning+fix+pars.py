
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

df = pd.read_csv("./documents/movies.csv")


# In[3]:

df


# In[4]:

# nama kolom data
df.columns


# In[5]:

# jumlah baris dan kolom data
df.shape


# In[6]:

# cek banyak missing data
df.isnull().sum()


# In[7]:

# jumlah missing data
df.isnull().sum().sum()


# In[49]:

# menghapus data yang missing
df_drop = df.dropna()


# In[50]:

# hasil data setelah dilakukan pengghapusan
df_drop


# In[51]:

# jumlah baris dan kolom data setelah penghapusan
df_drop.shape


# In[12]:

# jumlah data yang missing setelah penghapusan
df_drop.isnull().sum()


# In[12]:

# cek jumlah data yang duplikat
df.duplicated().sum()


# In[54]:

# cek tipe data
df_drop.dtypes


# In[53]:

# mengganti tipe data
df['budget'] = df_drop['budget'].astype('int64')
df['gross'] = df_drop['gross'].astype('int64')
df['votes'] = df_drop['votes'].astype('int64')


# In[61]:

# cek persenan data yang missing
for cols in df.columns:
    missing_data = np.mean(df[cols].isnull())*100
    print('{} = {}%'.format(cols, missing_data))


# In[ ]:



