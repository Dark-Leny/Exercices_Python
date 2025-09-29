# nom = (str(input("Entrez votre nom : ")))
# prenom = (str(input("Entrez votre prénom : ")))
# genre= (str(input("Veuillez préciser votre genre (H/F): ")))

# titre = ""
# if (genre == "H"):
#     titre = "Monsieur"
# else:
#     titre = "Madame"

# print ("Bonjour ",titre, " ", nom[0:1].upper() + nom[1:].lower(), " ", prenom[0:1].upper() + prenom[1:].lower())






# salaire_annuelle_brut=float(input("Saisir le salaire anuelle brut :"))
# salaire_mensuelle_net=(0.70*salaire_annuelle_brut)/12

# print(f"{salaire_mensuelle_net:.2f}")






# note1 = float(input("Saississez la première note : "))
# note2 = float(input("Saississez la deuxième note : "))
# note3 = float(input("Saississez la troisième note : "))

# moyenne = (note1 + note2 + note3) / 3

# if moyenne >=10 :
# print("admis")
# else :
# print("refusé(e)")

# print(f"{moyenne:.2f}")



# montant_ht = float(input("Montant HT (€) : "))

# match montant_ht:
#     case montant_ht if montant_ht >= 20000:
#         print("Votre montant est élevé")
#     case montant_ht if montant_ht >= 10000:
#         print("Votre montant est moyen")
#     case _:
#         print("Votre montant est faible")