import matplotlib.pyplot as plt
import numpy as np

scenarios = ['0%\n', '10%', '25%', '50%']
valeurs = [0.11 , 0.1 , 0.09, 0.07]
couleurs = ['green'] * 4

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
plt.ylim(0, 0.15) 

plt.tight_layout()
plt.show()