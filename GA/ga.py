# -*- coding: utf-8 -*-   

import numpy as np
from config import *

class test(object):

	def __init__(self):

		init_arr = np.random.rand(num)*3-1
		self.all_arr = []
		# every 1 in binary,and means the accuracy
		self.ac = ac
		self.step = 3.0/2**self.ac
		# print('step')
		print(self.step)
		print ('初始种群:'),
		print(init_arr)
		# arr_b = self.iTb(init_arr)
		# print(arr_b)
		# print(self.bTi(arr_b))
		# print(self.func(init_arr))
		# print(max(self.func(init_arr)))

		self.main(init_arr)

	def main(self,init_arr):
		arr = init_arr

		for i in range(evolution_num):

			print("适应性")
			y = self.func(arr)
			print(y)
			print("max:",max(y))

			print("自然选择")
			arr = self.pro(arr,y)
			print('res:'),
			print(arr)
			barr = self.iTb(arr)
			print('res:'),
			print(barr)

			print("杂交")
			barr = self.crossover(barr)
			print('res:'),
			print(barr)

			print("基因突变")
			barr = self.mutation(barr)
			print('res:')
			print (barr)
			arr = np.array(self.bTi(barr))
			self.all_arr.append(arr)
			


	def mutation(self,barr):
		for i in range(num):
			for j in range(2,len(barr[i])):
				if np.random.rand() < bianyi_rate:
					print ("tubian",i,j)
					s = '1' if barr[i][j]=='0' else '0'
					barr[i] = barr[i][:j] + s + barr[i][j+1:]
					# barr[i][j] = '1' if barr[i][j]=='0' else '0'
		return barr

	def crossover(self,arr):
		# arr is binary array
		for x in xrange(0,num,2):
			# print(x)
			if np.random.rand() < jiaohuan_rate:
				# print("jiaohuan~")
				str1 = arr[x][:self.ac/2] + arr[x+1][self.ac/2:]
				str2 = arr[x+1][:self.ac/2] + arr[x][self.ac/2:]

				arr[x] = str1
				arr[x+1] = str2
				# print(str1)
				# print(str2)
		return arr


	def pro(self,arr,y):


		# 负数变正
		y = [i-min(y) for i in y]
		print "y=",
		print(y)
		s = sum(y)
		print "s="+str(s)

		pro_res = []
		tmp = 0
		for i in y:
			pro_res.append(tmp+i)
			tmp = pro_res[-1]
		print "pro_res=",
		print(pro_res)

		rarr = np.random.rand(num)*s
		print "random=",
		print(rarr)
		res = []
		for i in rarr:
			index = self.listinside(pro_res,i)
			res.append(arr[index])
		return res

	def listinside(self,res,i):
		for x in range(num):
			if res[x] > i:
				return x


	def func(self,x):
		return x*np.sin(x*10*np.pi)

	def bTi(self,arr_b):
		return map(self.binaryToint,arr_b)

	def iTb(self,arr_i):
		return map(self.intTobinary,arr_i)

	def binaryToint(self,b):
		return self.step*int(b,base=2)-1
		# return round(self.step*int(b,base=2)-1,6)

	def intTobinary(self,i):
		# return map(bin,map(int,i/self.step))
		b = bin(int((i+1)/self.step))
		if(len(b) < self.ac+2):
			in0 = self.ac+2 - len(b)
			b = b[:2]+'0'*in0+b[2:]
		# if(len(b) > self.ac+2):
		# 	b = b[:24]
		return b



if __name__ == '__main__':
	t = test()
	for i in t.all_arr:
		print(np.ndarray.tolist(i))
	# print(list(t.all_arr))
	# t.main()