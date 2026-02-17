import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. CONFIGURATION
# ==========================================
scenarios = {
    "0% ": "dynamic_out_test6.csv",
    "10%": "dynamic_out_test7.csv",
    "25%": "dynamic_out_test8.csv",
    "50%": "dynamic_out_test9.csv",
}

# Couleurs pour les scénarios
colors = ['black', '#1f77b4', '#00bfff', '#2ca02c', '#ff7f0e', '#d62728']

# Colonnes à sommer pour obtenir les AGV totaux
cols_agv = ['S_va', 'S_bu', 'S_pro', 'S_ac']

plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 12}) 

print("--- Génération de la courbe AGV Totaux (Somme S_va, S_bu, S_pro, S_ac) ---")

# ==========================================
# 2. TRAITEMENT ET TRACÉ
# ==========================================
for i, (nom, fichier) in enumerate(scenarios.items()):
    try:
        # Lecture du fichier (séparateur point-virgule)
        df = pd.read_csv(fichier, sep=';') 
        
        # Gestion de l'axe temps
        if 'time' in df.columns:
            time = df['time'].values
        else:
            time = np.arange(len(df)) * (1/96)
            
        mask = time <= 10
        time_slice = time[mask]
        
        if len(time_slice) == 0: continue

        # CALCUL : Somme des 4 paramètres AGV
        # On vérifie si les colonnes existent pour éviter les erreurs
        available_cols = [c for c in cols_agv if c in df.columns]
        agv_total = df.loc[mask, available_cols].sum(axis=1)

        # Tracé de la courbe globale pour le scénario
        plt.plot(time_slice, agv_total, label=nom, color=colors[i], linewidth=2.5)

    except Exception as e:
        print(f"⚠️ Problème avec {nom} : {e}")

# ==========================================
# 3. MISE EN FORME
# ==========================================
plt.xlabel('Temps (Jours)', fontsize=14, fontweight='bold')
plt.ylabel(r'Concentration en AGV totaux ($kg\ \text{DCO} / m^3$)', fontsize=14, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 10)

plt.legend(fontsize=12, loc='upper right', framealpha=0.9, fancybox=True, shadow=True)
plt.tight_layout()

# Sauvegarde du nouveau graphique
plt.savefig('agv_totaux_somme.png')
plt.show()