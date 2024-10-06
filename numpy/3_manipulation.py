import numpy as np

# Différentes méthode qui permette de manipuler des tables


A = np.zeros((3,2))
B = np.ones((3,2))
print(A)
print(B)

print(np.hstack((A, B))) # Assemble les tables A et B horizontalement
print(np.vstack((A,B))) # Assemble les tables A et B verticalement 

print(np.concatenate((A, B), axis= 0)) # Simple la methode stack, axe 0, 1 ou 2

print(A.reshape((1,6))) # Remanie la forme du tableau 

print(A.ravel()) #Remanie les élements sur 1 seule dimensions 

