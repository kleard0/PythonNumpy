import numpy as np

A = np.random.randint(0, 10, [5,5]) # tableau avec des valeurs 0-10 et en dimension 5 par 5
print(A<5)
A[A<5] = 10
print(A)