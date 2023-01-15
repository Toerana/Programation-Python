a=int(input("Entrez la premiere  valeur : "))
b=int(input("Entrez la deuxieme  valeur : "))
c=int(input("Entrez la troisieme valeur : "))

print("Les valeurs entrees sont : a = ",a,", b = ",b," et c = ",c)
print("Permutation: a ==> b, b ==> c, c ==> a")
temp = c
c = b
b = a
a = temp

print("Les valeurs permutees sont : a = ",a,", b = ",b," et c = ",c)