print("Entrer x")
x = int(input())
print("Entrer y")
y = int(input())
print("Avant permutation:\n x:{} \n y:{}".format(x,y))
x = x*y
y = x/y
x = x/y

print("Après permutation:\n x:{} \n y:{}".format(x,y))