# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:49:33 2019

@author: Ptero
"""

import pandas as pd
import numpy as np

fname = "HD.xlsx"
dfSheet = pd.read_excel(fname, sheet_name="Sheet1",header = None)
dfData = dfSheet.iloc[88:113,3:22] # 提取试验数据
npData = dfData.values # 提取Excel数据，转换成numpy类型数组
npCurrent = dfSheet.iloc[88:113,2].values # 提取Excel电流值数据
npGrayscale = dfSheet.iloc[87,3:22].values # 提取Excel灰度数据
npCurrent = np.reshape(npCurrent,(1,len(npCurrent)))
npGrayscale = np.reshape(npGrayscale,(1,len(npGrayscale)))
npGrayscale_zeropadding = np.hstack(([[0]],npGrayscale)) # 在数据最前方补零，保证数据维度可以正确合并

npOutput = np.hstack((npCurrent.T,npData)) # 将数据和电流值合并，电流值是第一列
npOutput = np.vstack((npGrayscale_zeropadding,npOutput)) # 将数据和灰度值合并，合并后，灰度值是第一行
np.savetxt("data.txt",npOutput, delimiter = "\t", fmt = "%0.3f", header="Grayscale v.s. Current intensity")
