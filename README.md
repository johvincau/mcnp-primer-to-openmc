# mcnp-primer-to-openmc
A repository of examples from the MCNP Primer (Section III of LA-UR-26-23119) built in OpenMC. 

Examples:
01 d

02 d 

03 d 

04 d

05 d

06 d

07 d

08 d

09 d

10 d

11 d

12 d (fixed error)

13 d


14 d(look into how mcnp does vol calcs)

15 d(rotation matrix does not use degrees)

16xd(why was openmc able to accept a sympy object? it broke the xml) 
    (up vector is not aligned; behaves strangely)
    (despite best efforts, could not get Z->X' tilt correct for case 1)
    (need to figure out case 2?)
    
17 d plot_settings.pkl is problematic? also, unit management for tallies? 
   use surfacefilter + flux score. openmc-plotter labels as particle-cm/source. but it is actually particle/source. source def complete
   
18 d  source def and tally complete
   
19 d added source

20 d confirm hard irreproducible due to lack of auto-tessellation in openmc

21 d complete; need to dblcheck that universe 3 elements are set correctly
   possibly change how universes are centered within a lattice grid? (or provide
   option for it)
	Why don't volume calcs return the volume file name?
	
22 source left unfinished; geom definition complete

23 
24 

25 left undone

26 

27x no point detectors in openmc. would just need a normal cell for heating

28 
