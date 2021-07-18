#!/usr/bin/env python
# coding: utf-8

# In[27]:


# BAGINDA (130-)
# IoT IF-41
# Assignment 1 - Low Pass Filter

import numpy as np
from scipy.signal import butter, lfilter, freqz, filtfilt
import scipy.signal as signal
import pandas as pd
import plotly.graph_objects as go


# In[28]:


dataset = pd.read_csv("14.csv")
df = pd.DataFrame(dataset)

# kebutuhan filtering
t = np.arange(1,1000,5)
T = 5.0         # sample period
fs = 30.0       # sample rate, Hz
cutoff = 2      # frekuensi cutoff dari filter, dalam Hz, sedikit lebih tinggi dari aslinya, 1.2 Hz
nyq = 0.5 * fs  # frekuensi nyquist
order = 2       
n = int(T * fs) # total hasil percobaan


data = df.iloc[:,1]
def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    # mendapatkan koefisien dari filter 
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    y = signal.filtfilt(b, a, data)
    return y


# In[29]:


# Filter data, tampilkan sinyal sebelum dan sesudah filtering.
y = butter_lowpass_filter(data, cutoff, fs, order)
fig = go.Figure()
fig.add_trace(go.Scatter(
            y = data,
            line =  dict(shape =  'spline' ),
            name = 'sinyal dengan noise'
            ))
fig.add_trace(go.Scatter(
            y = y,
            line =  dict(shape =  'spline' ),
            name = 'sinyal hasil filter'
            ))
fig.show()


# In[30]:


# sumber: https://medium.com/analytics-vidhya/how-to-filter-noise-with-a-low-pass-filter-python-885223e5e9b7

