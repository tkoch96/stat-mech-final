# Calls the Monte Carlo Fluids Simulator a bunch of times
import os
import numpy as np
import matplotlib.pyplot as plt

def run_sims():
	density = .3
	l_side = np.cbrt(256/density)
	with open('Input','w') as f:
		text = "Ncycle   Ninit   Npart   Linit   Temp\n \
		1000000      10      256    .true.  .65\nDeltax   Box \n \
		.2  %.5f"%(l_side)
		f.write(text)
	os.system("..\Source\mc.exe >> 53.txt")
	os.system("cp Traject.xyz Traject_base.xyz")
	os.system("cp Coordnew Coordnew_base")

	temps = np.linspace(.9,1.1,20)
	for temp in temps:
		with open('Input','w') as f:
			text = "Ncycle   Ninit   Npart   Linit   Temp\n \
			500      10      256    .false.  %.4f\nDeltax   Box \n \
			.2  %.5f"%(temp, l_side)
			f.write(text)
		os.system("cp Coordnew_base Coordold")
		os.system("..\Source\mc.exe >> 53.txt")
		os.system("cp Traject.xyz Traject_%.4f.xyz"%temp)


def main():
	run_sims()

if __name__ == "__main__":
	main()
