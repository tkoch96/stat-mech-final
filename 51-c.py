# Calls the Monte Carlo Fluids Simulator a bunch of times
import os
import numpy as np
import matplotlib.pyplot as plt

def run_sims():
	n_particles = range(50,256)
	density = .1
	for n_particle in n_particles:
		l_side = np.cbrt(n_particle / density)
		with open('Input','w') as f:
			text = "Ncycle   Ninit   Npart   Linit   Temp\n \
			10000      10      %d    .true.  2.0\nDeltax   Box \n \
			1.0      %.3f"%(n_particle, l_side)
			f.write(text)
		#os.system("..\Source\mc.exe >> 51-c.txt")
	energies,heat_caps = parse_outputs()
	
	# plot results
	plt.subplot(2,1,1)
	plt.plot(n_particles, np.divide(energies,n_particles))
	plt.ylabel("E/N")
	plt.title("Average Energy per Particle")
	plt.subplot(2,1,2)
	plt.plot(n_particles, np.divide(heat_caps, n_particles))
	plt.xlabel('Number of Particles (N)')
	plt.ylabel("C_v/N")
	plt.title("Heat Capacity per Particle")

	plt.show()

def parse_outputs():
	#retrieve all the fractions of moves accepted from the simulation log file
	energies = [] 
	heat_caps = []
	with open('51-c.txt') as f:
		for row in f:
			#check for energy
			if '<E>' in row:
				tmp = row.split(' ')
				if 'E-' in tmp[-1]:
					#formatting case 1 - number is last element (minus the newline)
					print(tmp[-1][0:-2])
					energies.append(float(tmp[-1][0:-1]))
				else:
					#formatting case 2
					#find numeric element of tmp
					for el in tmp:
						try:
							float(el)
							energies.append(float(el))
							break
						except ValueError:
							continue
			#check for heat capacity
			if 'Cv' in row:		
				tmp = row.split(' ')
				if 'E-' in tmp[-1]:
					#formatting case 1 - number is last element (minus the newline)
					print(tmp[-1][0:-2])
					heat_caps.append(float(tmp[-1][0:-1]))
				else:
					#formatting case 2
					#find numeric element of tmp
					for el in tmp:
						try:
							float(el)
							heat_caps.append(float(el))
							break
						except ValueError:
							continue
	return [energies, heat_caps]

def main():
	run_sims()

if __name__ == "__main__":
	main()
