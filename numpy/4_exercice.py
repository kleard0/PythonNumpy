import numpy as np

def initialisation(m,n):
    A = np.random.randn(m,n)
    B = np.ones((m,1))
    AB = np.concatenate((A,B), axis=1)
    return AB
    
print(initialisation(3, 4))
 