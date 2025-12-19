# coding: utf8

import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# =========================
# Chargement correct du CSV
# =========================
contenu = pd.read_csv(
    "./data/resultats-elections-presidentielles-2022-1er-tour.csv",
    encoding="utf-8",   # ou "latin-1" si utf-8 échoue
    sep=",",
    quotechar='"'
)

# Vérification des colonnes
print("Colonnes détectées :")
print(contenu.columns.tolist())
print(contenu.head())

# =========================
# Colonnes principales (exactes selon CSV)
# =========================
col_departement = "Libellé du département"
col_inscrits = "Inscrits"
col_abstentions = "Abstentions"
col_votants = "Votants"
col_blancs = "Blancs"
col_nuls = "Nuls"
col_exprimes = "Exprimés"


# =========================
# Question 5
# =========================
print(contenu)


# =========================
# Question 6
# =========================
nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)
print("Nombre de lignes :", nb_lignes)
print("Nombre de colonnes :", nb_colonnes)

# =========================
# Question 7
# =========================
print("\nTypes des colonnes :")
for col in contenu.columns:
    print(col, ":", contenu[col].dtype)

# =========================
# Question 8
# =========================
print("\nPremières lignes du tableau :")
print(contenu.head())

# =========================
# Question 9 : colonne Inscrits
# =========================
print("\nColonne Inscrits :")
print(contenu[col_inscrits])

# =========================
# Question 11 : graphiques en barres
# =========================
os.makedirs("images/barres", exist_ok=True)

for i in range(len(contenu)):
    departement = contenu.loc[i, col_departement]
    inscrits = contenu.loc[i, col_inscrits]
    votants = contenu.loc[i, col_votants]

    nom_fichier = re.sub(r"[\\/:*?\"<>|]", "-", str(departement))

    plt.figure()
    plt.bar(["Inscrits", "Votants"], [inscrits, votants])
    plt.title(departement)
    plt.savefig(f"images/barres/{nom_fichier}.png")
    plt.close()

# =========================
# Question 12 : graphiques circulaires
# =========================
os.makedirs("images/circulaires", exist_ok=True)

for i in range(len(contenu)):
    departement = contenu.loc[i, col_departement]

    valeurs = [
        contenu.loc[i, col_blancs],
        contenu.loc[i, col_nuls],
        contenu.loc[i, col_exprimes],
        contenu.loc[i, col_abstentions]
    ]

    labels = ["Blancs", "Nuls", "Exprimés", "Abstention"]

    nom_fichier = re.sub(r"[\\/:*?\"<>|]", "-", str(departement))

    plt.figure()
    plt.pie(valeurs, labels=labels, autopct="%1.1f%%")
    plt.title(departement)
    plt.savefig(f"images/circulaires/{nom_fichier}.png")
    plt.close()

# =========================
# Question 13 : histogramme des inscrits
# =========================
plt.figure()
plt.hist(contenu[col_inscrits], bins=10, density=True)
plt.title("Distribution des inscrits")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Densité")
plt.show()
