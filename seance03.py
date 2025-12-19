# coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# LECTURE DES DONNÉES
# =========================

contenu = pd.read_csv("./data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8")

# =========================
# Question 5
# Sélection des colonnes quantitatives
# =========================

colonnes_quantitatives = [col for col in contenu.columns if contenu[col].dtype in ["int64", "float64"]]

# =========================
# Calcul des paramètres statistiques
# =========================

moyennes = []
medianes = []
modes = []
ecarts_types = []
ecarts_absolus = []
etendues = []

for col in colonnes_quantitatives:
    serie = contenu[col]
    moyennes.append(round(serie.mean(), 2))
    medianes.append(round(serie.median(), 2))
    modes.append(round(serie.mode().iloc[0], 2))
    ecarts_types.append(round(serie.std(), 2))
    ecarts_absolus.append(round(np.abs(serie - serie.mean()).mean(), 2))
    etendues.append(round(serie.max() - serie.min(), 2))

# =========================
# Affichage
# =========================

print("Colonnes quantitatives :", colonnes_quantitatives)
print("Moyennes :", moyennes)
print("Médianes :", medianes)
print("Modes :", modes)
print("Écarts-types :", ecarts_types)
print("Écarts absolus :", ecarts_absolus)
print("Étendues :", etendues)

# =========================
# Distance interquartile et interdécile
# =========================

distances_interquartiles = []
distances_interdeciles = []

for col in colonnes_quantitatives:
    serie = contenu[col]
    distances_interquartiles.append(round(serie.quantile(0.75) - serie.quantile(0.25), 2))
    distances_interdeciles.append(round(serie.quantile(0.9) - serie.quantile(0.1), 2))

print("Distances interquartiles :", distances_interquartiles)
print("Distances interdéciles :", distances_interdeciles)

# =========================
# Boîtes à moustaches
# =========================

os.makedirs("img", exist_ok=True)

for col in colonnes_quantitatives:
    plt.figure()
    plt.boxplot(contenu[col])
    plt.title(col)
    plt.savefig(f"img/boxplot_{col}.png")
    plt.close()

# =========================
# Lecture du fichier island-index.csv
# =========================

islands = pd.read_csv("./data/island-index.csv", encoding="utf-8")

# Nettoyage des noms de colonnes pour éviter les espaces invisibles
islands.columns = islands.columns.str.strip()

# Vérifier le nom exact de la colonne Surface
print("Colonnes du fichier islands :", islands.columns)

# Adapter selon le nom exact, par exemple 'Surface (km2)'
surface_col = [col for col in islands.columns if "Surface" in col][0]
surfaces = islands[surface_col]

# =========================
# Catégorisation des surfaces
# =========================

categories = {
    "]0,10]": 0,
    "]10,25]": 0,
    "]25,50]": 0,
    "]50,100]": 0,
    "]100,2500]": 0,
    "]2500,5000]": 0,
    "]5000,10000]": 0,
    "]10000,+∞[": 0
}

for s in surfaces:
    if s <= 10:
        categories["]0,10]"] += 1
    elif s <= 25:
        categories["]10,25]"] += 1
    elif s <= 50:
        categories["]25,50]"] += 1
    elif s <= 100:
        categories["]50,100]"] += 1
    elif s <= 2500:
        categories["]100,2500]"] += 1
    elif s <= 5000:
        categories["]2500,5000]"] += 1
    elif s <= 10000:
        categories["]5000,10000]"] += 1
    else:
        categories["]10000,+∞["] += 1

print("Catégorisation des surfaces des îles :")
for cat, nb in categories.items():
    print(cat, ":", nb)

# =========================
# Export des résultats
# =========================

resultats = pd.DataFrame({
    "Variable": colonnes_quantitatives,
    "Moyenne": moyennes,
    "Médiane": medianes,
    "Mode": modes,
    "Écart-type": ecarts_types,
    "Écart absolu": ecarts_absolus,
    "Étendue": etendues,
    "Distance interquartile": distances_interquartiles,
    "Distance interdécile": distances_interdeciles
})

resultats.to_csv("parametres_statistiques.csv", index=False)
resultats.to_excel("parametres_statistiques.xlsx", index=False)
