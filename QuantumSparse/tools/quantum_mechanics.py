import numpy as np
from QuantumSparse.tools.optimize import jit
from QuantumSparse import operator

#@jit
def expectation_value(Op:operator,Psi:operator)->np.ndarray:
    braket = Psi.dagger() @ Op @ Psi
    return braket.real
    # V  = sparse.csr_matrix(Psi)
    # Vc = V.conjugate(True)
    # return ((Op @ V).multiply(Vc)).toarray().real.sum(axis=0)

# # to be modified
# def expectation_value(Op,Psi):
#     V  = sparse.csr_matrix(Psi)
#     Vc = V.conjugate(True)
#     return ((Op @ V).multiply(Vc)).toarray().real.sum(axis=0)

#@jit
def standard_deviation(Op:operator,Psi:operator,mean:np.ndarray=None)->np.ndarray:
    if mean is None :
        mean = expectation_value(Op,Psi)
    Quad = expectation_value(Op@Op,Psi)
    return np.sqrt( Quad - mean**2)