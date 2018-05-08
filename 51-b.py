# Calls the Monte Carlo Fluids Simulator a bunch of times
import os
import numpy as np
import matplotlib.pyplot as plt

def run_sims():
	l_sides = np.linspace(np.power(9,3),np.power(6.3496,3))
	l_sides = np.cbrt(l_sides)
	for l_side in l_sides:
		delta_x = l_side / 25 #for help making the frac accepted about .5 (ad-hoc)
		with open('Input','w') as f:
			text = "Ncycle   Ninit   Npart   Linit   Temp\n \
			10000      10      256    .true.  2.0\nDeltax   Box \n \
			%.3f      %.3f"%(delta_x,l_side)
			f.write(text)
		#os.system("..\Source\mc.exe >> 51-b.txt")
	densities = 256 / np.power(l_sides,3)
	pressures = parse_outputs() #extract pressures from log files
	print(densities)
	print(pressures)
	order = 3 #order of polynomial
	coeff = np.polyfit(densities,pressures,order)
	print(coeff)
	p = np.poly1d(coeff)

	# plot results
	plt.plot(densities, pressures, '.', label="Simulated Data") 
	plt.plot(densities, p(densities), '-', label=("%d'rd Order Polynomial Fit"%order))
	plt.legend()
	plt.xlabel("Density")
	plt.ylabel("Pressure")
	plt.title("Fitting Pressure as a Function of Density")
	plt.show()

def parse_outputs():
	#retrieve all the pressures from the log file
	pressures = [] 
	with open('51-b.txt') as f:
		for row in f:
			if '<P>' in row:
				tmp = row.split(' ')
				if 'E-' in tmp[-1]:
					#formatting case 1 - number is last element (minus the newline)
					print(tmp[-1][0:-2])
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
