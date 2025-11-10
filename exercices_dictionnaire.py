# Exercice 1 : 

# etu = {"prenom" : "Jean", "nom" : "Dupont" , "promo": "BTS2_2025", "moyenne" : 15}

# print(f"{etu["nom"].upper()} {etu["prenom"][0].upper()}{etu["prenom"][1:]} - Promo : {etu["promo"][0].upper()}{etu["promo"][1:]} - Moyenne : {etu["moyenne"]}")

# age = int(input("Donnez un age : "))

# etu.update({"age" : age})

# print(etu)


# Exercice 2 : 

article = {"libellé" : "céréales", "prix" : 2, "stock" : 20}

article['catégorie'] = 'blé'

article['prix'] = article['prix'] + 0.10 * article['prix']

valeur = article.pop('stock', None)

valeur = article.pop('inconnu', None)

print(article)
print(valeur)