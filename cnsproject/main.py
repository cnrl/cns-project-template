from network.neural_populations import LIFPopulation
from plotting.plotting import plot_result
from utils import step_function, two_way_step_function, random_step_function
from network.monitors import Monitor


import torch
import numpy as np

t = 15
dt = 100

I = step_function(t, dt, 5)


n = LIFPopulation((1,),True,False,10,1,False,False,10,10)
n.dt = 1
monitor = Monitor(n, state_variables=["s", "v"])


for i in range(len(I)):
    n.forward(i, I)
    monitor.record()

s = monitor.get("s")
v = monitor.get("v")
s = s.numpy()

spike_mom = np.array([0])
spike_freq = np.array([0])
spike_mom = np.append(spike_mom, s.nonzero()[0])
spike_freq = np.append(spike_freq, np.cumsum(1/s.nonzero()[0]))

plot_result(I, v, n.threshold)

