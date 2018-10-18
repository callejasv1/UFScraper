
# coding: utf-8

# ### UF Scraper
# #### Objetivo: Hacer un robot que descargue automáticamente los valores de la UF

# In[36]:


import requests
import bs4 
import re
import pandas as pd
import numpy as np


# Traemos la página del **Banco Central** que contiene la URL  (https://si3.bcentral.cl/bdemovil/BDE/Series/MOV_SC_PR11)

# In[37]:


res = requests.get('https://si3.bcentral.cl/bdemovil/BDE/Series/MOV_SC_PR11')


# Parseamos el texto desde la página, utilizando la biblioteca **BeautifulSoup4**

# In[16]:


res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"lxml")


# Utilizando la biblioteca **Re** , encontramos la variable razorArrayDatos que contiene las fechas y valores de la UF

# In[17]:


pattern = re.compile("var razorArrayDatos = \[(.*?)\];")
array =pattern.findall(soup.text)


# Transformamos los datos en DataFrame

# In[38]:


str = ''.join(array)

list= str.split('","')

df = pd.DataFrame(list)


# Limpiamos la data de *comillas y corchetes*

# In[ ]:


df2= df[0].str.split(',', expand=True)

df2 = df2.replace('"','')

df2[0] = df2[0].map(lambda x: x.lstrip('["'))
df2[1] = df2[1].map(lambda x: x.rstrip(']"'))


# Transformamos la fecha (desde milisegundos a fecha)

# In[22]:


df2[0] = pd.to_datetime(df2[0], unit='ms')


# Nombramos las columnas

# In[34]:


df2.columns = ['Fecha','UF']


# In[40]:


df2.head()

