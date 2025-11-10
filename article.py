article = {"libellé" : "céréales", "prix" : 2, "stock" : 20}

article['catégorie'] = 'blé'

article['prix'] = article['prix'] + 0.10 * article['prix']

valeur = article.pop('stock', None)

valeur = article.pop('inconnu', None)

print(article)
print(valeur)