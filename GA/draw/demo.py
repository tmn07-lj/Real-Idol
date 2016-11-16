# -*- coding: utf-8 -*-   
  
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
start = [1, 0.18, 0.63, 0.29, 0.03, 0.24, 0.86, 0.07, 0.58, 0] 
metric =[[0.03, 0.86, 0.65, 0.34, 0.34, 0.02, 0.22, 0.74, 0.66, 0.65], 
     [0.43, 0.18, 0.63, 0.29, 0.03, 0.24, 0.86, 0.07, 0.58, 0.55], 
     [0.66, 0.75, 0.01, 0.94, 0.72, 0.77, 0.20, 0.66, 0.81, 0.52] 
    ] 
fig = plt.figure() 
window = fig.add_subplot(111) 
line, = window.plot(start) 
#如果是参数是list,则默认每次取list中的一个元素,
#即metric[0],metric[1],...
def update(data): 
  line.set_ydata(data) 
  return line, 
x = np.linspace(-1, 2, 1000)
y = x*np.sin(x*10*np.pi)
# z = np.cos(x**2)

# plt.figure(figsize=(10,6))
plt.plot(x,y,color="red",linewidth=2)
ani = animation.FuncAnimation(fig, update, metric, interval=2*1000) 
plt.show() 