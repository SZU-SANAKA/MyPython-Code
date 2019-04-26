# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 22:32:44 2019

@author: Ptero
"""

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft Yahei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

npData = np.loadtxt("data2.txt") # 载入所有数据

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

#plt.subplots(figsize=(12,8))
#i = 0
#while (i<20):
#    plt.plot(npGrayscale, npExpData[i], label=str(npCurrent[i]))
#    i = i + 1
#    
#plt.legend()
#plt.title('Current v.s Grayscale')
#plt.xlabel('RGB Grayscale')
#plt.ylabel('Ec')
#plt.xlim([0,255])
#plt.ylim([0,50])
#plt.grid()
#plt.show()

#fig, ax = plt.subplots(1, 1, figsize=(12, 6),
#                         subplot_kw={'xticks': [], 'yticks': []})

# 创建X轴序列数据
npX = np.linspace(0,len(npGrayscale),len(npGrayscale),endpoint = False)
npY = np.linspace(0,len(npCurrent),len(npCurrent),endpoint = False)
npX = npX[::2]
npY = npY[::2]

lstXTickLabel = []
for each in npX:
    lstXTickLabel.append(str(int(npGrayscale[int(each)])))
    
lstYTickLabel = []
for each in npY:
    lstYTickLabel.append(str(int(npCurrent[int(each)])))

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
X, Y = np.meshgrid(npGrayscale, npCurrent)
surf = ax.plot_surface(X, Y, npExpData, linewidth=0, antialiased=False, cmap="viridis")
ax.set_xlabel("灰度")
ax.set_ylabel("光机电流强度系数")
ax.set_zlabel("光能量密度（mJ/cm^2）")
#ax.set_xticks(npX)
#ax.set_yticks(npY)
#ax.set_xticklabels(lstXTickLabel)
#ax.set_yticklabels(lstYTickLabel)
#fig.colorbar(im, ax=ax)
#fig.text(0.75,0.9,"光能量密度\n(mJ/cm^2)")
plt.show()

#plt.savefig('光机电流和灰度的关系.png')
