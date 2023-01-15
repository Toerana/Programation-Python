note1= input("Veuillez entrer la note du module 1 et le coefficient correspondant : ")
note2= input("Veuillez entrer la note du module 2 et le coefficient correspondant : ")
note3= input("Veuillez entrer la note du module 3 et le coefficient correspondant : ")
note4= input("Veuillez entrer la note du module 4 et le coefficient correspondant : ")
note5= input("Veuillez entrer la note du module 5 et le coefficient correspondant : ")

S1 = note1.split()
S2 = note2.split()
S3 = note3.split()
S4 = note4.split()
S5 = note5.split()

S1_note_coef = (float(S1[0])*float(S1[1]))
S1_coef = (float(S1[1]))
S2_note_coef = (float(S2[0])*float(S2[1]))
S2_coef = (float(S2[1]))
S3_note_coef = (float(S3[0])*float(S3[1]))
S3_coef = (float(S3[1]))
S4_note_coef = (float(S4[0])*float(S4[1]))
S4_coef = (float(S4[1]))
S5_note_coef = (float(S5[0])*float(S5[1]))
S5_coef = (float(S5[1]))

nominateur = S1_note_coef+S2_note_coef+S3_note_coef+S4_note_coef+S5_note_coef
denominateur = S1_coef+S2_coef+S3_coef+S4_coef+S5_coef

moyenne = nominateur/denominateur

if moyenne > 10 and (float(S1[0])) >=8 and (float(S2[0])) >=8 and (float(S3[0])) and (float(S4[0]))>= 8 and (float(S5[0])) >=8:
    print("moyenne générale = ",round(moyenne,2))
    print("Admis")
else:
    print("moyenne générale = ",round(moyenne,2))
    print("Non Admis")

