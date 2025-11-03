# Exercice 1 : 

# class Lampe():
    
#     def __init__(self, allumee):
#         self.allumee = allumee
    
#     def allumer(self):
#         self.allumee = True

#     def eteindre (self):
#         self.allumee = False
    
#     def etat (self):
#         if self.allumee:
#             print("la lampe est allumer")
#         else:
#             print("la lampe est éteinte")


# #utilisation
# lampe1 = Lampe(False)
# print(lampe1.etat())
# lampe1.allumer()
# print(lampe1.etat())
# lampe1.eteindre()
# print(lampe1.etat())


# Exercice 2 : 

# class CompteBancaire():

#     def __init__(self,solde=0):
        
#         def deposer(self,montant):
#             self.solde += montant

#         def retirer(self,montant):
#             if montant > self.solde:
#                 ValueError("Le montant est supérieur au solde du compte")
#             else:
#                 self.solde -= montant

# compte = CompteBancaire(100)

# compte.deposer(50)
# print(compte.solde)

# compte.retirer(50)
# print(compte.solde)

# #compte.retirer(500)