import numpy as np
def NS(Qobs, Qsim):
    return 1 - np.sum((Qobs-Qsim)**2) / (np.sum((Qobs-Qobs.mean())**2))

def bias(Qobs, Qsim):
    return np.sum(Qsim - Qobs) / np.sum(Qobs) * 100
