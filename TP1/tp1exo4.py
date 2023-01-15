jour = 1
print("minute passé du mois")
minute_du_mois = int(input())
heure = minute_du_mois//3600
jour = jour + heure//24
heure = heure%24
minute = minute_du_mois - (jour-1)*(3600*24) - heure*3600
print("nous somme le {} il est {}:{} ".format(jour,heure,minute))
