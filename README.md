# Comptabilité de l'Urlab

<https://urlab.be>  
  
## Instructions pour le ou la responsable des comptes de l'Urlab

Chaque année une réunion doit être faite avec la présidence et la trésorerie du cerkinfo, c.f. le repo [PVREUS](https://github.com/urlab/PVREUS).  
  
Pour chaque entrée ou sortie, il faut indiquer dans un fichier au format [csv](https://www.rfc-editor.org/rfc/rfc4180) la Date, la Nature (courses, outils, etc.), la Quantité (-12.65, 22.34, etc.), le Compte que ça concerne (Caisse, Coffre, Banque, etc), la Catégorie (Bar, Materiel, etc.) et le numéro du ticket en question si applicable, sinon le chiffre -1.  
  
Pour chaque Quadri, il faut produire un bilan du quadri contenant :
- Combien il y avait au début du quadri
- Combien il y a à la fin du quadri
- Dans quoi est parti l'argent dépensé
- D'où vient l'argent récolté
  
L'idée de structure de ce repo est donc la suivante :
- Toutes les transactions d'un mois sont condensées dans un fichier csv nommé au format \<numéro du mois\>\<nom du mois\> (09septembre.csv, etc.)
- Tous les fichiers csv d'une année sont placés dans un dossier nommé par l'année (2025/, 2026/, etc.)
- Tous les bilans sont placés dans le dossier bilans/
- Tous les décomptes de caisse, coffre ou banque sont placés dans le dossier comptages/
- Tous les tickets du quadri courant sont placés dans le dossier Tickets/, au format .jpg
- A la fin de chaque quadri une backup des tickets doit être faite et placée dans le NAS du hs
  
De cette manière, en utilisant le dernier bilan pluss les transaction qui ont eu lieu on peut vérifier la véracité des comptes. A noter que les backups de tickets ont tout intérêt à être dupliquées, en envoyer une au cerkinfo est une bonne idée. En fin de quadri les tickets doivent être stockés dans une enveloppe dans le hs ou le ci.  
La distribution entre le cash dans la caisse du hs, dans le coffre du hs et dans le compte en banque est à la discrétion et à la responsabilité du ou de la responsable des comptes du hs (ça DOIT être écrit dans les bilans), les transferts doivent être indiqués dans les comptes en utilisant deux lignes.  

Exemple de transfert:  
\<date\>,transfert,-75,Caisse,-1
\<date\>,transfert,75,Banque,-1

Ceci permet de très facilement filtrer et extraire toutes les transactions de la caisse par exemple. Il faut noter dans les bilans la distribution de l'argent entre les différents comptes.  
Remarque : Il est conseill? de garder le plus possible les ?crits en ASCII.  

