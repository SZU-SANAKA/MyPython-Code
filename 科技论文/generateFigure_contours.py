# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:44 2019

@author: Ptero
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

npData = np.loadtxt("data2.txt") # 载入所有数据

npCurrent = npData[1:,0]
npGrayscale = npData[0,1:]
npExpData = npData[1:,1:]


# 创建X轴序列数据
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

fig = plt.figure()
ax = fig.gca()

# 绘制等高线图
X, Y = np.meshgrid(npGrayscale, npCurrent)
C0 = ax.contourf(X, Y, npExpData, 20, alpha=.68, cmap=plt.cm.hot)
C = ax.contour(X, Y, npExpData, 8, colors='black', linewidths=0.5)

ax.set_xlabel("灰度")
ax.set_ylabel("光机电流强度系数")
ax.clabel(C, inline=True, fontsize=10)

fig.colorbar(C0, ax=ax) # 显示颜色表

#plt.show()

#plt.savefig('光机电流和灰度的关系-等高线-黑白.png')
plt.savefig('光机电流和灰度的关系-等高线-彩色.png')
