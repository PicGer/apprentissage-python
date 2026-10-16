# print("Bonjour, je commence ma formation de développeuse IA !")

# import datetime

# #Du problème à l'algorythme

# heure_rendezvous = datetime.datetime datetime(2026, 11, 28, 14, 0)
# heure_actuelle = datetime.datetime.now()

# if heure_actuelle < heure_rendezvous:
#     moyen_de_transport = "voiture"
#     print("choisir un moyen de transport:", moyen_de_transport)
#     print("sepréparer")
#     print("se rendre au garage")
#     print("suivre le trajet")
# else:
#     print("Je suis en retard pour mon rendez-vous !")

# #Les variables en programmation

nom = "Dupond" #String
age = 30 #Integer
prix = 19.99 #Float
est_marié = False #Boolean

print(age)

age = 35

print(age)

# #Calculer des variables

prix_unitaire = 10
quantite = 4

total = prix_unitaire * quantite

print("total_sans_remise:", total)

remise = 0.10
motant_remise = total * remise
total_avec_remise = total - motant_remise

print("montant de la remise:", motant_remise)
print("total_avec_remise:", total_avec_remise)

# #Les opérateurs arythmétiques en pseudo-code

#Utiliser les opérateurs de comparaisons


# Début

#     age_utilisateur <- 17

#     Si age_utilisateur >= 18 Alors
#         Afficher "Accès autorisé"
#     Sinon
#         Afficher "Accès refusé"
#     Fin si
# Fin

# Début

#     age_utilisateur <- "dix"
#     age_utilisateur2 <- "dix"

#     Si age_utilisateur = age_utilisateur2Alors
#         Afficher "Vous avez le même âge"
#     Sinon
#         Afficher "Vous n'avez pas le même âge"
#     Fin si
#Fin

#Les comparaisons dans un système de réservation

chambre_disponible = True
tarif = 150

date_de_reservation = "2026, 10, 06"
date_de_disponibilite = "2026-10-05"

if date_de_reservation in ["2026-10-06", "2026-10-07"]:
    tarif = 150
print("Le tarif est de", tarif, "euros")

# #Les opérateurs logiques

# Si est majeur ET a permis 
# Alors
#     Afficher "Vous pouvez conduire"

# Si est enseignant OU est étudiant
# Alors
#     Afficher "Vous avez droit à une réduction"

# #Résoudre des problèmes avec la logique booléenne #

est_premium = False
montant_commande = 90
habite_etranger = False

commande_suffisante = montant_commande > 100

a_droit_livraison = est_premium or commande_suffisante and not habite_etranger

if a_droit_livraison:
    print("Vous avez droit à la livraison gratuite.")
else:
    print("Vous n'avez pas droit à la livraison gratuite.")


# Manipuler une liste #

taches = ["envoyer un email", "préparer une réunion", "Appeler un client"]
print(taches)
taches.append("Commander les fournitures")
print(taches)
taches.remove("envoyer un email")
print(taches)
taches[0],[1],[1],[0]
print(taches)
if"Appeler un client" in taches:
    print("La tache 'Appeler un client' est présente dans la liste.") 

ventes_mensuelles = [1500, 1800, 1700, 1600, 1750]

# Somme et moyenne
somme_ventes = sum(ventes_mensuelles)
moyenne_ventes = somme_ventes / len(ventes_mensuelles)

# Mois avec la plus grande vente
meilleur_mois = max(ventes_mensuelles)
indice_meilleur_mois = ventes_mensuelles.index(meilleur_mois)

# Mois avec ventes inférieures à la moyenne
mois_faibles = [v for v in ventes_mensuelles if v < moyenne_ventes]

print(f"Total des ventes : {somme_ventes}")
print(f"Moyenne des ventes : {moyenne_ventes:.2f}")
print(f"Mois le plus performant : {indice_meilleur_mois + 1} avec {meilleur_mois} ventes")
print(f"Mois avec ventes sous la moyenne : {mois_faibles}")

# Les dates en programmation #
# Les dates dans un système de réservation #

from datetime import date

debut_sejour = date(2025,7,10)
fin_sejour = date(2025,7,15)

duree =(fin_sejour - debut_sejour).days
print("La durée de séjour est de", duree, "jours")

aujourd_hui = date.today()
fin_disponibilité = date(2025,12,31)

if debut_sejour >= aujourd_hui and fin_sejour <= fin_disponibilité:
    print("Le séjour est disponible")
else:
    print("Le séjour n'est pas disponible")
if debut_sejour.month in [7,8]:
    tarif_nuit = 120
else:
    tarif_nuit = 80
total = tarif_nuit * duree

print("Le tarif total pour le séjour est de", total, "euros")
print("Le tarif par nuit est de", tarif_nuit, "euros")

# Les fonctions en programmation #

def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

def dire_bonjour_prenom(prenom):
        print("Bonjour " + prenom + "!")

dire_bonjour_prenom("Jean")  

def afficher_bienvenue():
    print("Bienvenue !")

def accueil_utilisateur(prenom):
    print("Bienvenue !")

def accueil_utilisateur(prenom):
    afficher_bienvenue()
    dire_bonjour_prenom(prenom)

accueil_utilisateur("Marie")
accueil_utilisateur("Géraldine")

# Utliser des fonctions prédéfinies #

ventes = [100.5, 230.0, 89.99, 145.0, 210.25]
total = sum(ventes)

print("Le total des ventes est de :", total, "€")

# Calculer la moyenne des ventes #

moyenne = sum(ventes) / len(ventes)

plus_grande_vente = max(ventes)
print("La plus grande vente est de :", plus_grande_vente, "€")

plus_petite_vente = min(ventes)
print("La plus grande vente est de :", plus_petite_vente, "€")

# Calculer le total des ventes #

total = round(total, 2)
print("Le total des ventes arrondi est de :",total,"€")