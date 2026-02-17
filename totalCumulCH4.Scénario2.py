import matplotlib.pyplot as plt
import numpy as np

scenarios = ['Témoin\n', '10% TS', '20% TS', '30% TS', '50% TS', '100% TS']
valeurs = [0.04, 0.03, 0.04, 0.04, 0.05, 0.08]
couleurs = ['green'] * 6 

plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 12}) 

# Bar Chart
bars = plt.bar(scenarios, valeurs, color=couleurs, edgecolor='black', alpha=0.8)

plt.ylabel('Production méthane cumulée (m³ / kg VS)', fontsize=14, fontweight='bold')


# Ajout des valeurs
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.002, round(yval, 2), 
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.ylim(0, 0.1) 

plt.tight_layout()
plt.show()