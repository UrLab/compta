# Comptabilité de l'Urlab

<https://urlab.be>  
  
## Instructions pour le ou la responsable des comptes de l'Urlab

Chaque année une réunion doit être faite avec la présidence et la trésorerie du cerkinfo, c.f. le repo [PVREUS](https://github.com/urlab/PVREUS).  
  
Pour chaque entrée ou sortie, il faut indiquer dans un fichier au format [csv](https://www.rfc-editor.org/rfc/rfc4180) la Date, la Nature (courses, cotisation, matériel, etc.), la Quantité (-12.65, 22.34, etc.) et le numéro du ticket en question si applicable.  
  
Pour chaque Quadri, il faut produire un bilan du quadri contenant :
- Combien il y avait au début du quadri
- Combien il y a à la fin du quadri
- Dans quoi est parti l'argent dépensé
- D'où vient l'argent récolté
  
L'idée de structure de ce repo est donc la suivante :
- Toutes les transactions d'un mois sont condensées dans un fichier csv nommé au format \<numéro du mois\>\<nom du mois\> (09septembre.csv, etc.)
- Tous les fichiers csv d'une année sont placés dans un dossier nommé par l'année (2025/, 2026/, etc.)
- Tous les bilans sont placés dans le dossier bilans/
- Tous les tickets du quadri courant sont placés dans le dossier Tickets/, au format .jpg
- A la fin de chaque quadri une backup des tickets doit être faite et placée dans le NAS du hs
  
De cette manière, en utilisant le dernier bilan pluss les transaction qui ont eu lieu on peut vérifier la véracité des comptes. A noter que les backups de tickets ont tout intérêt à être dupliquées, en envoyer une au cerkinfo est une bonne idée.

