import random
from dataclasses import dataclass
from math import pi



#exercice 1


class StringFoo:
    def __init__(self, message):
        self.message = message

   def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())

str_foo = StringFoo("bjr")
str_foo.print_string()



#exercice 2


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.largeur * self.longueur

    def afficher_infos(self):
        print("Largeur :", self.largeur)
        print("Longueur :", self.longueur)
        print("Aire :", self.aire)


rectangle1 = Rectangle(10, 20)
rectangle1.calcul_aire()
rectangle1.afficher_infos()



#exercice 3


from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcule_aire(self):
        return pi * self.rayon * self.rayon

    def calcule_circonference(self):
        return 2 * pi * self.rayon


cercle = Cercle(5)
aire = cercle.calcule_aire()
circonference = cercle.calcule_circonference()

print(f'Aire du cercle : {aire}')
print(f'Circonférence du cercle : {circonference}')



# Exercice 5


@dataclass
class Caracteristique:
   dexterite: int = random.randint(1, 20)
   constitution: int = random.randint(1, 20)
   sagesse: int = random.randint(1, 20)
   charisme: int = random.randint(1, 20)
   force: int = random.randint(1, 20)
   intelligence: int = random.randint(1, 20)



# Exercice 4 et 6 enemble avec la partie de exercice 5


class hero:
   def __init__(self, goyo):
       self.nom_du_héros = goyo
       self.nombre_point_de_vie = random.randint(25, 500) + random.randint(25, 500)
       self.force_attaque = random.randint(55, 100)
       self.force_défensive = random.randint(70, 200)
   def recevoir_des_dommages(self, dmg):
       self.nombre_point_de_vie = dmg - self.force_défensive
   def faire_une_attaque(self):
       self.force_attaque = self.force_attaque + random.randint(1, 6)
   def est_vivant(self):
       return self.nombre_point_de_vie <= 0
h = hero("goyo")
h.recevoir_des_dommages(100)








































