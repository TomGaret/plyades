from __future__ import division
import numpy as np
from core import State, Epoch, Orbit

iss = State(np.array([8.59072560e+02, -4.13720368e+03,  5.29556871e+03, 7.37289205e+00,   2.08223573e+00,   4.39999794e-01]), t=Epoch(2013, 3, 18, 12, 0), body="Earth", frame="MEE2000")

