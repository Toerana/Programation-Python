BASE = (4)
fromage = 800
eau = 2
ail = 2
pain = 400
nbConvive = int(input("Nombre de convives :"))
fromage = fromage * nbConvive /BASE
eau = eau * nbConvive /BASE
ail = ail * nbConvive /BASE
pain = pain * nbConvive /BASE
print("Pour faire une fondue fribourgoise pour ",nbConvive," il vous faut:")
print("- ",fromage,"gr de fromage")
print("- ",eau,"dl d'eau")
print("- ",ail,"gousse(s) d'ail")
print("- ",pain,"gr de pain")