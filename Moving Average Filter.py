#!/usr/bin/env python
# coding: utf-8

# In[10]:


# BAGINDA (130-)
# IoT IF-41
# Assignment 1 - Moving Average Filter

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# menggunakan dataset 15
data = pd.read_csv("15.csv")
df = pd.DataFrame(data)

# menggunakan kolom D "z acceleration"
df1 = df.iloc[:,3].rolling(window=200).mean()
df2 = df.iloc[:,3].rolling(window=500).mean()
df3 = df.iloc[:,3].rolling(window=1000).mean()

plt.figure()

plt.plot(df1,label='window 200', color='orange')
plt.plot(df2,label='window 500', color='blue')
plt.plot(df3,label='window 1000', color='green')
plt.legend(loc=1)
plt.show()


# In[11]:


# sumber: https://towardsdatascience.com/implementing-moving-averages-in-python-1ad28e636f9d

