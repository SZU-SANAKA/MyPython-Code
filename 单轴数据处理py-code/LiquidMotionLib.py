# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:11:20 2019

@author: Li Yang Shenzhen University
"""

import numpy as np
from scipy.signal import butter, lfilter, freqz

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    #normal_cutoff = cutoff / nyq
    b, a = butter(order, cutoff[0] / nyq, btype='low', analog=False)
    return b, a

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    #normal_cutoff = cutoff / nyq
    b, a = butter(order, cutoff[0] / nyq, btype='high', analog=False)
    return b, a

def butter_bandpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    #normal_cutoff = cutoff / nyq
    b, a = butter(order, [cutoff[0] / nyq, cutoff[1] / nyq], btype='bandpass', analog=False)
    return b, a

def butter_bandstop(cutoff, fs, order=5):
    nyq = 0.5 * fs
    #normal_cutoff = cutoff / nyq
    b, a = butter(order, [cutoff[0] / nyq, cutoff[1] / nyq], btype='bandstop', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_bandpass_filter(data, cutoff, fs, order=5):
    b, a = butter_bandpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_bandstop_filter(data, cutoff, fs, order=5):
    b, a = butter_bandstop(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
