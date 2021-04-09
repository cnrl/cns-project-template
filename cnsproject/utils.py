"""
Module for utility functions.

Note: You are going to need to implement DoG and Gabor filters. A possible opt
ion would be to write them in this file but it is not a must and you can define\
a separate module/package for them.
"""
import torch
import numpy as np


def step_function(time: int, step_size: int, scale: int):
    I = torch.zeros(time, 1)
    I[5*scale:, 0] = step_size
    return I


def two_way_step_function(time: int, step_size: int, scale: int):
    I = torch.zeros(time, 1)
    I[5*scale:10*scale, 0] = step_size
    return I


def random_step_function(time: int, step_size: int, scale: int):
    I = np.zeros([time, 1])
    n = np.random.randint(time-20, size=10)
    n = np.sort(np.unique(n))
    for i in n:
        I[i:i+20, 0] = np.random.randint(step_size)
    I = torch.from_numpy(I)
    return I
