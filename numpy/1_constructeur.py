import numpy as np

table1 = np.array([1, 2, 3])
print(table1.ndim) # Affiche le nombre de dimension
print(table1.shape) # Affiche la forme
print(table1.size) # Nombre d'élement du tableau 

table2 = np.zeros((3,2)) # Creer un tableau rempli de zero sur 3 lignes et 2 colonnes
print(table2)
print(type(table2.shape)) # Affiche la classe 

table3 = np.full((5,5), 7)
print(table3)

table4 = np.random.seed(0) # initialisele random avec une seed, permet de reproduire une séq aléatoire 
table4 = np.random.randn(3,4)
print(table4)

table4 = np.eye(5) # Crée une matrice identité 
print(table4)

# Constructeur utile pour la création de graph matplotlib 

table5 = np.linspace(0, 10, 20) # Crée une matrice composé de 20 valeurs allant de 0 à 10
print(table5)

table6 = np.arange(1,10,  2) # Crée un tableau allant de n0 à n-1 avec un pas de 2
print(table6)

