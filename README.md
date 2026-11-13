# mcnp-primer-to-openmc
A repository of examples from the MCNP Primer (Section III of LA-UR-26-23119) built in OpenMC. 

Examples: 
01
02
03
04
05
06
07
08
09
10
11
12 (fixed error)
13

14  (look into how mcnp does vol calcs)
15  (rotation matrix does not use degrees)
16x (why was openmc able to accept a sympy object? it broke the xml) 
    (up vector is not aligned; behaves strangely)
    (despite best efforts, could not get Z->X' tilt correct for case 1)
    (need to figure out case 2?)
    
17 plot_settings.pkl is problematic? also, unit management for tallies? 
   use surfacefilter + flux score. openmc-plotter labels as particle-cm/source. but it is actually particle/source. 
   source def complete
18 (missing source definitions)
   source def and tally complete
   FilterMeta? 
19 add source
20 confirm hard irreproducible due to lack of tessellation in openmc
21 complete; need to dblcheck that universe 3 elements are set correctly
   possibly change how universes are centered within a lattice grid? (or provide
   option for it)
	Why don't volume calcs return the volume file name?
