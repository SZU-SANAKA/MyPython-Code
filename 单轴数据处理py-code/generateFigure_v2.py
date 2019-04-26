# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:44 2019

@author: Ptero
"""

import numpy as np
import matplotlib.pyplot as plt
import LiquidMotionLib as lml # Liquid Motion 专用函数库

plt.rcParams['font.sans-serif']=['Microsoft Yahei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

npData = np.loadtxt("data\\打印2.txt").T # 载入所有数据
ch1 = npData[0]
ch2 = npData[1]
ch3 = npData[2]
ch4 = npData[3]

fs = 285
nStart = 0
nSpan = 50000
nEnd = nStart + nSpan
t_factor = 1/fs





t = np.linspace(nStart, nEnd, nSpan, endpoint= False, dtype=int)
x = ch1[nStart:nEnd]
x2 = lml.butter_lowpass_filter(x, [100], fs, order=2)

fig, ax = plt.subplots(2, 1, figsize=(8, 6))
t = t*t_factor
ax[0].plot(t, x)
ax[1].plot(t, x2)
#ax[0].set_ylim([1.2,1.4])
#ax[0].set_xlim([37,38])
#ax[1].set_ylim([1.2,1.4])
#ax[1].set_xlim([37,38])




#npCurrent = npData[1:,0]
#npGrayscale = npData[0,1:]
#npExpData = npData[1:,1:]
##npGrayscale = npGrayscale[1:]
#
##i = 0
##
##npGrayscaleMatrix = npGrayscale
##while (i < 24):
##    npGrayscaleMatrix = np.vstack((npGrayscaleMatrix, npGrayscale))
##    i = i + 1
#    
#    
##plt.plot(npGrayscaleMatrix, npExpData,label=str(npCurrent[i]))
#
##plt.subplots(figsize=(12,8))
##i = 0
##while (i<20):
##    plt.plot(npGrayscale, npExpData[i], label=str(npCurrent[i]))
##    i = i + 1
##    
##plt.legend()
##plt.title('Current v.s Grayscale')
##plt.xlabel('RGB Grayscale')
##plt.ylabel('Ec')
##plt.xlim([0,255])
##plt.ylim([0,50])
##plt.grid()
##plt.show()
#
##fig, ax = plt.subplots(1, 1, figsize=(12, 6),
##                         subplot_kw={'xticks': [], 'yticks': []})
#
## 创建X轴序列数据
#npX = np.linspace(0,len(npGrayscale),len(npGrayscale),endpoint = False)
#npY = np.linspace(0,len(npCurrent),len(npCurrent),endpoint = False)
#npX = npX[::2]
#npY = npY[::2]
#
#lstXTickLabel = []
#for each in npX:
#    lstXTickLabel.append(str(int(npGrayscale[int(each)])))
#    
#lstYTickLabel = []
#for each in npY:
#    lstYTickLabel.append(str(int(npCurrent[int(each)])))
#
#fig, ax = plt.subplots(1, 1, figsize=(8, 6))
#im = ax.imshow(npExpData, cmap='viridis')
#ax.set_xlabel("灰度")
#ax.set_ylabel("光机电流强度系数")
#ax.set_xticks(npX)
#ax.set_yticks(npY)
#ax.set_xticklabels(lstXTickLabel)
#ax.set_yticklabels(lstYTickLabel)
#fig.colorbar(im, ax=ax)
#fig.text(0.75,0.9,"光能量密度\n(mJ/cm^2)")
#plt.show()
#
#plt.savefig('光机电流和灰度的关系.png')
