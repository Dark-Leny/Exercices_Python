# Exercice 1 : 

# L1 = [3,-2,7,0,-5,7,2]

# longueur = len(L1)
# minimum = min(L1)
# maximum = max(L1)

# print(f"La longueur de la liste est égale à {longueur}")
# print(f"Le minimum de la liste est égale à {minimum}")
# print(f"Le maximum de la liste est égale à {maximum}")

# somme = 0

# for i in L1 :
#     if i >= 0:
#         print(i)
#         somme += i
# print(f"La somme des entiers positifs est égale à {somme}")

# print("Liste triée : ",sorted(L1))
# print(f"Liste originale : {L1}")

# L1.sort(reverse = True)

# print(f"Liste décroissante : {L1}")


# Exercice 2 : 

# def unique_preserve(L):
    
#     result=[]
#     for x in L:
        
#         if x not in result:
            
#             result.append(x)
        
#     return result 

# L= unique_preserve([3,3,1,2,1,4])
# print(L)
# L.pop(2)
# print(L)

# Exercice 3 : 

# def interleave(A, B):
#     result = []
#     for a, b in zip(A,B) :
#         result.append(a)
#         result.append(b)
#     return result

# A = [1, 3, 5]
# B = [2, 4, 6]

# liste_fusionnee = interleave(A,B) 
# print(liste_fusionnee)

# Exercice 4 : 

# notes = [12,9,14,7,18,10]

# print(f"-> Liste d'origine inchangée :{notes}") 
# print(f"-> Liste triée croissante :{sorted(notes)}")

# print(f"-> Liste notes {notes}") 

# print(f"-> Liste triée décroissante :{sorted(notes, reverse=True)}")

# print(f"-> Liste notes {notes}") 

# La différence entre sorted et sort est que sorted renvoie une nouvelle liste triée tandis que sort trie la liste d'origine en place.

# Exercice 5 : 

# produits = ["RAM","SSD","CPU","GPU"]
# produits.insert(1,"HDD")
# print(produits)
# produits.insert(0,"PSU")
# print(produits)
# produits.extend(["Boitier","Ventirad"])
# print(produits)

# Exercice 6 : 

# files = ["log.txt", "temp.tmp", "readme.md", "temp.tmp", "main.py"]

# files.pop(1)

# files.remove("temp.tmp")

# print(files)

# pop supprime un élément à un index donné et remove supprime la première occurrence d'une valeur donnée.

# Exercice 7 : 

# panier = ["banane", ["pomme", "poire", "kiwi"], True, [10, 20, 30]]

# deuxieme_fruit = panier[1][1]
# print(f"Le deuxième fruit est : {deuxieme_fruit}")

# troisieme_entier = panier[3][2]
# print(f"Le troisième entier est : {troisieme_entier}")

# Exercice 8 : 

