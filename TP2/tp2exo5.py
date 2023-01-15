nombre = int(input("Entrez un nombre entier:"))
if nombre == 0:
    print("Le nombre et zéro (et il est pair)")
else:
    if nombre > 0:
        posi_nega = "positif"
    else:
        posi_nega = "négatif"

    if (nombre%2) == 0:
        pair_impair = "pair"
    else:
        pair_impair = "impair"

    print("Le nombre est {} et {}".format(posi_nega,pair_impair))