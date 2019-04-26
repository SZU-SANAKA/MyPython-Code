# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:44 2019

@author: Ptero
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft Yahei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

npData = np.loadtxt("data.txt") # 载入所有数据

npCurrent = npData[1:,0]
npGrayscale = npData[0,1:]
npExpData = npData[1:,1:]
#npGrayscale = npGrayscale[1:]

#i = 0
#
#npGrayscaleMatrix = npGrayscale
#while (i < 24):
#    npGrayscaleMatrix = np.vstack((npGrayscaleMatrix, npGrayscale))
#    i = i + 1
    
    
#plt.plot(npGrayscaleMatrix, npExpData,label=str(npCurrent[i]))

plt.subplots(figsize=(12,8))
i = 0
while (i<20):
    plt.plot(npGrayscale, npExpData[i], label=str(npCurrent[i]))
    i = i + 1
    
plt.legend()
plt.title('Current v.s Grayscale')
plt.xlabel('RGB Grayscale')
plt.ylabel('Ec')
plt.xlim([0,255])
plt.ylim([0,50])
plt.grid()
plt.show()
