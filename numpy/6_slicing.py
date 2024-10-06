import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(A[:,0]) # Affiche tout les élements de la 1ère colonne 

print(A[0]) # Affiche tout les élements de la 1ère ligne (axe par défaut)

print(A[0:2, 0:2]) # Affiche les 2 premiers élements des 2 premières colonnes 

B = (A[0:2, 0:2]) # Possibilité de récupérer cette section de A et la mettre dans un nv tableau
 
#A[0:2, 0:2] = 10 # On peut selectionner une section de A et lui donner une valeur
print('####')
print(A[:, -2:])

B = np.zeros((4,4))
print(B)

(B[1:3, 1:3]) = 1
print(B)

C = np.zeros((5,5)) # avec un pas 
C[::2, ::2] = 1
print(C)