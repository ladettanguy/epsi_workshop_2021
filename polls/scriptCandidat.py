from models import Candidat, Block
import json

c1 = Candidat(id_candidat=1, nom="Melanchon", prenom="Jean-Luc", parti="a france insoumise", description="Travailler moins pour gagner plus (ou pas)")
c2 = Candidat(id_candidat=2, nom="Asselineau", prenom="Francois", parti="Union populaire républicaine", description="C'est pas faux")
c3 = Candidat(id_candidat=3, nom="Le Pen", prenom="Marine", parti="Rassemblement nationnal", description="Liberté liberté chérie")
c4 = Candidat(id_candidat=4, nom="Poisson", prenom="Jean-Frédéric", parti="La voix du peuple", description="L'humilité, c'est pas quand il ya des infiltrations")
c5 = Candidat(id_candidat=1, nom="Dupont-Aignan", prenom="Nicolas", parti="Debout la france", description="Arthour, pas changer assiette pour fromage")
c6 = Candidat(id_candidat=1, nom="Arthaud", prenom="Nathalie", parti="Lutte ouvriere", description="Vous avez parlé de votre amitié avec une truite")
c7 = Candidat(id_candidat=1, nom="Roussel ", prenom="Fabien", parti="Parti communiste français", description="Je crois qu’il faut que vous arrêtiez d’essayer de dire des trucs ")
c8 = Candidat(id_candidat=1, nom="Poutou", prenom="Philippe", parti="Parti anti-capitaliste", description="Au bûcher ")
c9 = Candidat(id_candidat=1, nom="Bertrand", prenom="Xavier", parti="Les républicains", description="Elle est où la poulette ?")
c1.save()
c2.save()
c3.save()
c4.save()
c5.save()
c6.save()
c7.save()
c8.save()
c9.save()

b=Block(hashPrecedent="000",actuel="1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0")
b.save()