import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter # <--- NOUVEL IMPORT POUR LISSER

# ==========================================
# 1. CONFIGURATION
# ==========================================
scenarios = {
    "0% ": "dynamic_out_test6.csv",
    "10%": "dynamic_out_test7.csv",
    "25%": "dynamic_out_test8.csv",
    "50%": "dynamic_out_test9.csv",
}

colors = ['black', '#1f77b4', '#00bfff', '#2ca02c', '#ff7f0e', '#d62728']

plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 12})

print("--- Génération de la courbe Méthane LISSÉE ---")

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

        # --- RECUPERATION DONNEES ---
        if 'V_ch4_cumul' in df.columns:
            methane = df.loc[mask, 'V_ch4_cumul'].values # .values pour s'assurer que c'est un array numpy
        elif 'q_ch4' in df.columns:
            methane = np.cumsum(df.loc[mask, 'q_ch4']) * (1/96)
            methane = methane.values
        else:
            continue

        # --- ETAPE DE LISSAGE ---
        try:
            methane_smooth = savgol_filter(methane, window_length=51, polyorder=3)
        except:
            # Si le tableau est trop petit pour le filtre, on garde l'original
            methane_smooth = methane

        # Tracé de la courbe lissée
        plt.plot(time_slice, methane_smooth, label=nom, color=colors[i], linewidth=2.5)

    except Exception as e:
        print(f"⚠️ Problème avec {nom} : {e}")

# ==========================================
# 3. TITRES ET AXES
# ==========================================

plt.xlabel('Temps (Jours)', fontsize=14, fontweight='bold')
plt.ylabel('Production cumulée de méthane (m³/kg VS)', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, 10)

# Légende
plt.legend(fontsize=12, loc='upper left', framealpha=0.9, fancybox=True, shadow=True)

plt.tight_layout()
plt.show()