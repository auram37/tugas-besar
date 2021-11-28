# menambah file
import pandas as pd
import numpy as np

df = pd.read_csv("./documents/movies.csv")

df

# nama kolom data
df.columns


# In[5]:

# jumlah baris dan kolom data
df.shape

# cek banyak missing data
df.isnull().sum()

# jumlah missing data
df.isnull().sum().sum()

# cek persenan data yang missing
for cols in df.columns:
    missing_data = np.mean(df[cols].isnull())*100
    print('{} = {}%'.format(cols, missing_data))

# menghapus data yang missing
df_drop = df.dropna()

# hasil data setelah dilakukan pengghapusan
df_drop

# jumlah baris dan kolom data setelah penghapusan
df_drop.shape

# jumlah data yang missing setelah penghapusan
df_drop.isnull().sum()


# cek jumlah data yang duplikat
df.duplicated().sum()

# cek tipe data
df_drop.dtypes


# mengganti tipe data
df['budget'] = df_drop['budget'].astype('int64')
df['gross'] = df_drop['gross'].astype('int64')
df['votes'] = df_drop['votes'].astype('int64')



