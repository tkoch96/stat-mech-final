# Calls the Monte Carlo Fluids Simulator a bunch of times
import os
import numpy as np
import matplotlib.pyplot as plt

def run_sims():
	l_sides = range(5,35)
	for i,l_side in enumerate(l_sides):
		with open('Input','w') as f:
			text = "Ncycle   Ninit   Npart   Linit   Temp\n \
			10000      10      256    .true.  2.0\nDeltax   Box \n \
			1.0      %d"%(l_side)
			f.write(text)
		os.system("..\Source\mc.exe >> 51-a.txt")
		os.system("cp radial radial%d"%i)

	fracs = parse_outputs() #fraction of moves accepted
	fracs = np.array(fracs)

	print(fracs)
	print(l_sides)
	# plot results
	plt.plot(l_sides,fracs)
	plt.xlabel("Length of Box")
	plt.ylabel("Fraction of Moves Accepted")
	plt.title("Fraction of Moves Accepted vs. Density of Container")
	plt.show()

def parse_outputs():
	#retrieve all the fractions of moves accepted from the simulation log file
	fracs = [] 
	with open('51-a.txt') as f:
		for row in f:
			if 'Frac' in row:
				tmp = row.split(' ')
				if 'E-' in tmp[-1]:
					#formatting case 1 - number is last element (minus the newline)
					fracs.append(float(tmp[-1][0:-1]))
				else:
					#formatting case 2
					#find numeric element of tmp
					for el in tmp:
						try:
							float(el)
							fracs.append(float(el))
							break
						except ValueError:
							continue
	return fracs

def main():
	run_sims()

if __name__ == "__main__":
	main()
