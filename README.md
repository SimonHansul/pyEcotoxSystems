# A Python wrapper for EcotoxSystems.jl

This package makes implementations from [EcotoxSystems.jl](https://github.com/SimonHansul/EcotoxSystems.jl) available in Python. 


## Quickstart 

Install from github

```bash
pip install git+https://github.com/simonhansul/pyecotoxsystems.git
```

then import in Python

```Python 
import pyecotoxsystems as ets
```

Doing this for the first time triggers the installation of Julia dependencies, which takes a few minutes. These should be one-time costs, however.

```Python
import matplotlib.pyplot as plt
p = ets.defaultparams
sim = ets.ODE_simulator(p) # run the default simulation
plt.plot(sim.t, sim.S) # plot growth trajectory
plt.show()

p.glb.t_max = 56. # adjust simulated timespan
p.glb.dX_in = 25_000 # adjust food input rate
sim = ets.IBM_simulator(p) # run the default IBM simulation
plt.plot(sim.glb.t, sim.glb.N) # plot population trajectory
plt.show()
```






