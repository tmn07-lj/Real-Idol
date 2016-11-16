# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time
def func(x):
	return x*np.sin(x*10*np.pi)


class pic(object):
	"""docstring for pic"""
	def __init__(self):
		
		x = np.linspace(-1, 2, 1000)
		y = func(x)
		# z = np.cos(x**2)

		plt.figure(figsize=(10,6))
		plt.plot(x,y,color="red",linewidth=2)

		# plt.plot(0.22,func(0.22),'o',color="blue")

		# plt.plot(x,z,"b--",label="$cos(x^2)$")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.title("x*sin(10*pi*x)")
		plt.ylim(-2.5,2.5)
		plt.legend()
		plt.show()
		self.p = plt
		pass
	def draw(self,x):
		self.p.plot(x,func(x),'o',color="blue")
		self.p.show()
		pass

p = pic()
time.sleep(2)
p.draw(1)
# x = np.linspace(-1, 2, 1000)
# y = x*np.sin(x*10*np.pi)
# # z = np.cos(x**2)

# plt.figure(figsize=(10,6))
# plt.plot(x,y,color="red",linewidth=2)

# plt.plot(0.22,func(0.22),'o',color="blue")

# # plt.plot(x,z,"b--",label="$cos(x^2)$")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("x*sin(10*pi*x)")
# plt.ylim(-2.5,2.5)
# plt.legend()
# plt.show()