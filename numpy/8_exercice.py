import numpy as np

from scipy import misc #permet d'accèder à des images par défaut
import matplotlib.pyplot as plt # bibliothèque de visualisation graphique 

face = misc.face(gray= True) #charge une image intégré dans scipy
plt.imshow(face, cmap=plt.cm.gray) # affiche l'image contenu dans face grace à matplotlib (sous forme de donnée
print(type(face))
print(face.shape)
plt.show() #affiche reelement l'image

# Exercice 

new_image  = (face[96:570, 128:896])
plt.imshow(new_image) # affiche l'image contenu dans face grace à matplotlib (sous forme de donnée
print(type(new_image))
print(new_image.shape)
plt.show() 


