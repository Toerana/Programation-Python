import datetime
print("Entrer votre Age")
age = int(input())
naissance = datetime.date.today().year - age
print("Votre année de naissance est : ",naissance)