import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. CONFIGURATION
# ==========================================
scenarios = {
    "0% ": "dynamic_out_témoin.csv",
    "10%": "dynamic_out_test1.csv",
    "20%": "dynamic_out_test2.csv",
    "30%": "dynamic_out_test3.csv",
    "50%": "dynamic_out_test4.csv",
    "100%": "dynamic_out_test5.csv"
}

# COULEURS BIEN DISTINCTES
colors = ['black', '#1f77b4', '#00bfff', '#2ca02c', '#ff7f0e', '#d62728']

plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 12}) 

print("--- Génération de la courbe Ammoniac ---")

# ==========================================
# 2. TRAITEMENT
# ==========================================
for i, (nom, fichier) in enumerate(scenarios.items()):
    try:
        df = pd.read_csv(fichier, sep=';') 
        
        # Gestion du temps
        if 'time' in df.columns:
            time = df['time'].values
        else:
            time = np.arange(len(df)) * (1/96)
            
        mask = time <= 10
        time_slice = time[mask]
        
        if len(time_slice) == 0: continue

        # --- RÉCUPÉRATION AMMONIAQUE (S_nh3) ---
        # Vérifie si ta colonne s'appelle "S_nh3", "Snh3" ou "S_IN"
        if 'S_nh3' in df.columns:
            nh3 = df.loc[mask, 'S_nh3']
        elif 'Snh3' in df.columns:
            nh3 = df.loc[mask, 'Snh3']
        else:
            # Fallback si le nom est différent
            print(f"⚠️ Colonne Ammoniac introuvable dans {nom}")
            continue

        # Tracé
        plt.plot(time_slice, nh3, label=nom, color=colors[i], linewidth=2.5)

    except Exception as e:
        print(f"⚠️ Problème avec {nom} : {e}")

# ==========================================
# 3. LE TITRE ET LES AXES
# ==========================================

# Titre (Optionnel, décommente si besoin)
# plt.title('Concentration en Ammoniaque ($S_{nh3}$)', fontsize=16, fontweight='bold')

# Axe X
plt.xlabel('Temps (Jours)', fontsize=14, fontweight='bold')

# Axe Y - CORRECTION DU GRAS (On utilise le ³ unicode)
# L'unité standard ADM1 est kmole N / m³
plt.ylabel('Concentration en ammoniac (kmol / m³)', fontsize=14, fontweight='bold')

# Grille et Limites
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 10)

# Si tes valeurs sont très faibles (car pas d'urine), tu peux décommenter
# la ligne ci-dessous pour zoomer l'axe Y (ajuste la valeur max)
# plt.ylim(0, 0.05) 

# Légende
plt.legend(fontsize=12, loc='upper right', framealpha=0.9, fancybox=True, shadow=True)

plt.tight_layout()
plt.show()