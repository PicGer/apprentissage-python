print("Bonjour, je commence ma formation de développeuse IA !")

import datetime
import re
import unittest

 # Du problème à l'algorythme #

heure_rendezvous = datetime.datetime(2026, 11, 28, 14, 0)
heure_actuelle = datetime.datetime.now()

if heure_actuelle < heure_rendezvous:
     moyen_de_transport = "voiture"
     print("choisir un moyen de transport:", moyen_de_transport)
     print("se préparer")
     print("se rendre au garage")
     print("suivre le trajet")
else:
     print("Je suis en retard pour mon rendez-vous !")

 # Les variables en programmation #

nom = "Dupond" #String
age = 30 #Integer
prix = 19.99 #Float
est_marié = False #Boolean

print(age)

age = 35

print(age)

 # Calculer des variables #

prix_unitaire = 10
quantite = 4

total = prix_unitaire * quantite

print("total_sans_remise:", total)

remise = 0.10
motant_remise = total * remise
total_avec_remise = total - motant_remise

print("montant de la remise:", motant_remise)
print("total_avec_remise:", total_avec_remise)

 # Les opérateurs arythmétiques en pseudo-code #

 # Utiliser les opérateurs de comparaisons en pseudo-code #

#Début

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

#     Si age_utilisateur = age_utilisateur2 Alors
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

 # Les opérateurs logiques en pseudo-code #

# Si est majeur ET a permis 
# Alors
#     Afficher "Vous pouvez conduire"

# Si est enseignant OU est étudiant
# Alors
#     Afficher "Vous avez droit à une réduction"

 # Résoudre des problèmes avec la logique booléenne #

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
    afficher_bienvenue()
    dire_bonjour_prenom(prenom)

accueil_utilisateur("Marie")
accueil_utilisateur("Géraldine")

# Calculer l'âge : Définir la fonction puis appeler la fonction #

def calculer_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    age= current_year - birth_day
    if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
        age-= 1
    return age

age = calculer_age(1990, 5, 17, 2026, 10, 18)
print(age)

# Conception de fonction efficace #
# Définition de la fonction #

nom = "Géraldine"

def calculer_total(produits):
    return sum(produits)

def afficher_message_bienvenue(nom):
    print("Bienvenue ", nom)

def verifier_reduction(total):
    if total > 100:
        print("Vous avez le droit à une réduction de 10% !")
          
def generer_recu(nom, produits):
    total= calculer_total(produits)
    afficher_message_bienvenue(nom)
    verifier_reduction(total)
    print("Total à payer :", total)

 # Appeler la fonction #

generer_recu(nom, [45, 60, 20])

 # Système de facturation #
 # Vérifier infos clients #

def valider_client(client):
    return "nom" in client and "adresse" in client

 # Calculer le sous-total des articles #

def calculer_sous_total(articles):
    total = 0
    for article in articles:
        total += article["prix"] * article["quantite"]
    return total
    
# Appliquer les taxes TVA #

def appliquer_taxes(sous_total, taux_TVA=20):
    return round(sous_total * (1 + taux_TVA / 100), 2)

# Générer la facture finale #

def generer_facture(client, articles):
    if not valider_client(client):
        return "Erreur : informations clients invalides"

    sous_total = calculer_sous_total(articles)
    total_ttc = appliquer_taxes(sous_total)

    facture = f"Facture pour {client['nom']}\n"
    facture += f"Adresse : {client['adresse']}\n\n"

    facture += "Articles :\n"
    for article in articles:
        facture += f"- {article['nom']} x{article['quantite']} : {article['prix']}€\n"

    facture += f"\nSous-total : {sous_total}€\n"
    facture += f"Total (TTC) : {total_ttc}€\n"

    return facture

articles = [
    {"nom": "Pain", "prix": 1.20, "quantite": 2},
    {"nom": "Croissant", "prix": 1.10, "quantite": 3},
]

client = {"nom": "Jean Dupont", "adresse": "10 rue de Paris, 75000 Paris"}
print(generer_facture(client, articles))

 # Effectuer un test unitaire automatisé #

 # import unittest #

class TestFonctions(unittest.TestCase):

    def test_appliquer_taxes(self):
        self.assertEqual(appliquer_taxes(100), 120)  # Test avec taux par défaut
        self.assertEqual(appliquer_taxes(200, 10), 220)  # Test avec un autre taux
        self.assertEqual(appliquer_taxes(0), 0)  # Cas limite : montant nul
        self.assertAlmostEqual(appliquer_taxes(99.99), 119.99, places=2)  # Test de précision

# Exécuter les tests

if __name__ == "__main__":
    unittest.main()

# Vérifier si un email est valide #

 # import re #

def valider_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

 # Tests #

print(valider_email("contact@entreprise.com"))  # ✅ True
print(valider_email("invalide@@exemple.com"))   # ❌ False

 # Vérifier si un numéro de téléphone est valide #

def formater_telephone(numero):
    # Reformate un numéro de téléphone français en affichage standard #
    numero = numero.replace(" ", "").replace("-", "")
    if len(numero) == 10 and numero.isdigit():
        return f"{numero[:2]} {numero[2:4]} {numero[4:6]} {numero[6:8]} {numero[8:]}"
    return "Numéro invalide"

 # Tests #

print(formater_telephone("0612345678"))  # ✅ "06 12 34 56 78"
print(formater_telephone("01-23-45-67-89"))  # ✅ "01 23 45 67 89"
print(formater_telephone("12345"))  # ❌ "Numéro invalide"