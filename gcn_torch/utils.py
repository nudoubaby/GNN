import numpy as np
import pickle as pkl
import scipy.sparse as sp

def sample_mask(idx, l):
    """create mask"""
    mask = np.zeros(l)
    mask[idx] = 1
    return np.array(mask, dtype=np.bool)

def load_data(dataset_str):
    """
    loads input data from gcn_troch/data directory
    :param dataset_str:
    :return:
    """
    names = ['x', 'y', 'tx', 'ty', 'allx', 'ally', 'graph']


