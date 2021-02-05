import torch as th
import numpy as np

def uniform(shape, scale = 0.5, name=None):
    """uniform initiator"""
    initial = th.empty(shape)
    return th.nn.uniform_(initial, a=-scale, b=scale)

def glorot():
    """Glorot & Bengio (AISTATS 2010) init."""
    pass
    return

def zeros(shape):
    initial = th.zeros(shape, dtype=th.float32)
    return initial

def ones(shape):
    initial = th.ones(shape, dtype=th.float32)
    return initial
