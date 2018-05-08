import numpy as np
import matplotlib.pyplot as plt
import math

r_cut = 2.5
n = 1000
sigma = 1.0
epsilon = 1.0
T = np.linspace(3,3.3,1000)

def lj(r):
	return 4 * epsilon * (np.power(sigma/r,12) - np.power(sigma/r,6))

def func(x,beta):
	#integrand
	return np.power(x,2) * (1 - np.exp(-beta * lj(x)))


B_2 = []
for t in T: #for each temperature, estimate the integral
	s = 0 #first term is zero
	beta = 1.0 / t
	for i,r in enumerate(np.linspace(0,r_cut,n+1)):
		if i == 0:
			#first term is 0
			continue
		s += func(r_cut * i / n,beta)

	s -= .5 * func(r_cut,beta) #overcounted in the for loop
	s *= r_cut / n
	B_2.append(2 * math.pi * s) #estimate of B_2 at this temperature
for i,el in enumerate(B_2): #look where the coefficients change sign
	if el > 0:
		print(T[i]) #this is the boyle temperature
		exit(0)
plt.plot(B_2)
plt.show()