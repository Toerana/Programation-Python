nom_prenom1= input('Enter prénom et nom n°1 :')
nom_prenom2= input('Enter prénom et nom n°2 :')

liste_nom_prenom1 = []
liste_nom_prenom1 = nom_prenom1.split()
liste_nom_prenom2 = []
liste_nom_prenom2 = nom_prenom2.split()


if liste_nom_prenom1[1] < liste_nom_prenom2[1]:
    print(liste_nom_prenom1[0].capitalize(),liste_nom_prenom1[1].upper())
    print(liste_nom_prenom2[0].capitalize(),liste_nom_prenom2[1].upper())
elif liste_nom_prenom2[1] < liste_nom_prenom1[1]:
    print(liste_nom_prenom2[0].capitalize(),liste_nom_prenom2[1].upper())
    print(liste_nom_prenom1[0].capitalize(),liste_nom_prenom1[1].upper())
elif liste_nom_prenom1[0] < liste_nom_prenom2[0]:
    print(liste_nom_prenom1[0].capitalize(),liste_nom_prenom1[1].upper())
    print(liste_nom_prenom2[0].capitalize(),liste_nom_prenom2[1].upper())
elif liste_nom_prenom2[0] < liste_nom_prenom1[0]:
    print(liste_nom_prenom2[0].capitalize(),liste_nom_prenom2[1].upper())
    print(liste_nom_prenom1[0].capitalize(),liste_nom_prenom1[1].upper())
