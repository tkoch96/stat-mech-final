# Calls the Monte Carlo Fluids Simulator a bunch of times
import os
import numpy as np
import matplotlib.pyplot as plt

def run_sims():
	temp = 3.10720720721
	N = 64
	l_sides = np.linspace(8,12,50)
	num_trials = 70
	for _ in range(num_trials):
		for l_side in l_sides:
			with open('Input','w') as f:
				text = "Ncycle   Ninit   Npart   Linit   Temp\n \
				5000      10      %d    .true.  %.6f\nDeltax   Box \n \
				2      %.3f"%(N,temp,l_side)
				f.write(text)
			#os.system("..\Source\mc.exe >> 52.txt")
	densities = N / np.power(l_sides,3)
	pressures = parse_outputs()
	order = 3 #order of polynomial
	b2 = 0
	total_coeff = np.zeros(shape=(num_trials,order+1))
	b2s = []
	for i in range(num_trials):
		coeff = np.polyfit(densities, \
			pressures[i*50:(i+1) * 50], order)
		total_coeff[i] = coeff
	#plot results
	for i in range(order+1):
		plt.plot(range(num_trials),total_coeff[:,i],label="x^%d coeff."%(order-i))

	plt.legend()
	plt.xlabel("Trial Number")
	plt.ylabel("Coefficient Value")
	plt.title("Poly. Coefficients used to Fit Pressure")
	plt.show()
def parse_outputs():
	#retrieve all the fractions of moves accepted from the simulation log file
	pressures = [] 
	with open('52.txt') as f:
		for row in f:
			#if 'Virial' in row and 'Sim' not in row and 'Initial' not in row:
			if '<P>' in row:
				tmp = row.split(' ')
				if 'E-' in tmp[-1]:
					#formatting case 1 - number is last element (minus the newline)
					pressures.append(float(tmp[-1][0:-1]))
				else:
					#formatting case 2
					#find numeric element of tmp
					for el in tmp:
						try:
							float(el)
							pressures.append(float(el))
							break
						except ValueError:
							continue
	return pressures

def main():
	run_sims()

if __name__ == "__main__":
	main()
