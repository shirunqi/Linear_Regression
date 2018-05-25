#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_author_ = 'shirunqi'

import numpy as np
import matplotlib.pyplot as plt
def linear_plot():
	data = [[5.06, 5.79], [4.92, 6.61], [4.67, 5.48], [4.54, 6.11], [4.26, 6.39],[4.07, 4.81], [4.01, 4.16], [4.01, 5.55], [3.66, 5.05], [3.43, 4.34],[3.12, 3.24], [3.02, 4.80], [2.87, 4.01], [2.64, 3.17], [2.48, 1.61],[2.48, 2.62], [2.02, 2.50], [1.95, 3.59], [1.79, 1.49], [1.54, 2.10], ]
	
	x = [p[0] for p in data] # 从data中提取横、纵坐标
	y = [q[1] for q in data]
	
	n = len(x)               # 计算线性回归方程系数
	a1 = a2 = a3 = a4 = 0
	a11 = a12 = a21 = a22 = a31 = a32 = 0
	w = b = 0
	for i in range(0,n):
		a1 += x[i] * y[i]
		a2 += x[i]
		a3 += y[i]
		a4 += x[i] * x[i]
	a11 = n * a1
	a12 = a2 * a3
	a21 = n * a4
	a22 = a2 * a2
	a31 = a4 * a3
	a32 = a2 * a1
	b = (a31 - a32) / (a21 - a22)
	w = (a11 - a12) / (a21 - a22)
	b = round(b,2)
	w = round(w,2)
	 
	fig = plt.figure()             # 绘图
	plt.scatter(x,y,color='blue')  # 绘制散点图
	x1 = np.linspace(0,6,100)
	y1 = w * x1 + b
	plt.plot(x1,y1,color = 'red')  # 绘制拟合直线
	plt.show()
	
	return w, b, fig

w,b,fig = linear_plot()
print(w,b)