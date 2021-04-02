"""
Module for utility functions.

TODO.

Use this module to implement any required utility function.

Note: You are going to need to implement DoG and Gabor filters. A possible opt
ion would be to write them in this file but it is not a must and you can define\
a separate module/package for them.
"""
import torch
import numpy

def step_function(t: int, dt:int, x: int):
    I = torch.zeros(t*dt, 1)
    I[5*dt:, 0] = x
    return I


def two_way_step_function(t: int, dt:int, x: int):
    I = torch.zeros(t*dt, 1)
    I[5*dt:10*dt, 0] = x
    return I

def random_step_function(t: int, dt:int, x: int):
    I = np.zeros(dt*t)
    n = np.random.randint(dt*t-1, size=10)
    n = np.append(n,[n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10])
    n = np.append(n,[n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10])
    n = np.sort(np.unique(n))
    I[n] = np.random.randint(10, size=len(n))
    I = torch.from_numpy(I)
    return I
