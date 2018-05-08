# stat-mech-final
Code for running simulation programs. The simulation programs themselves are not included and can be found for free at http://homepage.tudelft.nl/v9k6y/imsst/.


The file names refer to problem numbers in the textbook at the above link. We ran all of these scripts in the 'Run' sub-directory of the LJ-MC directory. All python files follow a similar structure and were separated for simplicity/simultaneous work on different problems.


To run all of the files, the usage is the same (no arguments) but we reiterate for simplicity. In some simulations, certain generated plots may pop up which you can save at your leisure.


(51-a.py) Conducts simulations over a variety of lengths of sides of the boxes (decreasing density). Parses the log files to retrieve the fraction of moves accepted during the simulation. Plots the trend of density versus fraction of moves accepted during the simulation.
Usage: python 51-a.py


(51-b.py) Conducts simulations over a variety of lengths of sides of the boxes (increasing density). Parses the log files to retrieve the simulated average pressure. Then fits the simulated pressure to a 3rd order polynomial. Finally plots the resulting 3rd order polynomial model alongside simulated pressure points.
Usage: python 51-b.py


(51-c.py) Conducts simulations over a variety of numbers of particles, while holding the density constant. Parses the log files to retrieve the simulated average energy and heat capacity. Plots the energy and heat capacity versus the number of particles in the simulation in attempt to show they are roughly constant. 
Usage: python 51-c.py

Conducts simulations at the Boyle temperature for num_trials trials, each for 5000 steps. Retrieves the simulated pressures from the log file and fits them to an order'th order polynomial. Graphs the coefficients used to fit the pressure to show trends in the coefficients.
Usage: python 52.py

(calc_boyle.py) Estimates the second virial coefficient using an n-point trapezoidal sum. It searches for a zero crossing of the coefficient over a range of temperatures specified in the 'T' variable. If it finds a zero crossing, it prints the temperature at which the zero crossing occurs (Boyle Temperature). If it doesn't, it graphs the virial coefficients as a function of temperature for debugging purposes.
Usage: python calc_boyle.py

(53.py) Runs a simulation at $T^*$ = .65, $\rho$ = 0.3 for 1e6 iterations, saving the resulting trajectory as Traject_base.xyz. It then runs several shorter simulations (500 steps each) at increasing temperature. Saves the trajectory files as Traject_(temperature).xyz so that all trajectory files can be viewed later in VMD. 
Usage: python 53.py