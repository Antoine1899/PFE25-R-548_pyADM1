Sujet : Optimisation de la production de biogaz à partir de matières issues de toilettes sèches. Simulations via le modèle ADM1 en situation de co-digestion (à partir d'une unité de méthanisation agricole classique) pour évaluer l'impact de ces apports.

PyADM1 est donc un script Python implémentant le modèle de digestion anaérobie (Anaerobic Digestion Model number 1) établi par l'IWA et qui est actuellement un standard de référence dans le monde scientifique.
Nous nous basons sur ce modèle afin de tester les recherches faites dans le cadre de notre projet.

Pour utiliser les scripts Python, il faudra installer un logiciel utilisant Python v3 et les bibliothèques suivantes : Numpy, Scipy, Pandas, Matplotlib et Copy.

Veuillez télécharger l'intégralité des fichiers contenant les codes sources Python et les jeux de données pour faire des tests unitaires. Veuillez également trouver les résultats de ces tests parmi les fichiers.
Ensuite, pour faire une simulation, veuillez suivre ces instructions :
- Ouvrir “PyADM1.py” sur Spyder. 
- Charger le fichier d’entrée voulu dans le script et changer le nom du fichier de sortie en conséquence.
- Lancer la simulation : les graphiques vont s’afficher.
- Utiliser les autres scripts pour obtenir un graphique en particulier où les courbes des différents résultats sont superposées.

Workflow : 
- Branche “main” : branche principale correspondant à la version validée avec toutes les dernières versions des fichiers. 
- Branche “travail” : expérimentations concernant la prise en main du dossier et le calibrage nécessaire pour simuler la méthanisation d’un intrant agricole classique.
- Branche “travail.2” : expérimentations concernant l’apport de toilettes sèches.
- Branche “travail.3” : expérimentations concernant l’ajout de l’urine dans la composition des toilettes sèches.

Origine du travail sr lequel nous nous sommes appuyé pour l'adapter à notre projet : 
@article {Sadrimajd2021.03.03.433746,
	author = {Sadrimajd, Peyman and Mannion, Patrick and Howley, Enda and Lens, Piet N. L.},
	title = {PyADM1: a Python implementation of Anaerobic Digestion Model No. 1},
	elocation-id = {2021.03.03.433746},
	year = {2021},
	doi = {10.1101/2021.03.03.433746},
	URL = {https://www.biorxiv.org/content/early/2021/03/04/2021.03.03.433746},
	eprint = {https://www.biorxiv.org/content/early/2021/03/04/2021.03.03.433746.full.pdf},
	journal = {bioRxiv}
}

Auteurs du travail : Antoine TRAN, Valentin PASQUINI, Eva GOUJON, Yann JEZEQUIEL, Mor NDIAYE, Brian YOUMBI DIESSE.
Année : 2026
