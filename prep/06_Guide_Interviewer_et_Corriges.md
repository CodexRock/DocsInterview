# 06 - Guide du partenaire et corrigés

## Ne pas donner ce document au candidat avant le cas

Tous les cas sont fictifs et originaux. Les éléments biographiques du cas C9 doivent venir de l'expérience réelle du candidat. Les chiffres des autres cas sont des données d'exercice, pas des benchmarks.

## Comment conduire un cas en quinze minutes

Lis l'énoncé, puis laisse le candidat clarifier et prendre une pause de structure. Donne les données lorsqu'il pose une question pertinente ; s'il cherche longtemps une information indisponible, dis-le et oriente-le vers une donnée utile. Une information décisive doit finir par être fournie, sinon le cas devient un jeu de devinettes.

Ne corrige pas immédiatement une petite erreur. Demande d'abord « Cet ordre de grandeur vous paraît-il cohérent ? ». En cas de blocage de plus d'une minute : un indice ciblé. Note l'indice donné pour le débrief. Une interruption teste la synthèse ; elle ne doit pas créer une mise en scène hostile.

**Repères de temps :** énoncé et clarification, 2 minutes ; structure et choix du test, 2 ; analyse et calculs, 6 ; complication, 3 ; recommandation, 1 ; marge, 1. Pour un cas de douze minutes, réduire l'analyse et utiliser une seule complication.

Évalue séparément la structure, les chiffres, le jugement et l'échange. Les propositions alternatives sont recevables si elles respectent les données et les contraintes.

---

## C1 - Factures : capacité libérée et cash

### Informations à donner progressivement

**À la clarification.** Le DAF veut un payback cash inférieur ou égal à vingt-quatre mois **depuis la mise en service**. Le build dure trois mois, avant cette mise en service. Les 1,5 M€ sont traités comme une sortie initiale ; on ignore impôts et actualisation dans le calcul principal. La capacité productive retenue pour l'exercice est de 1 600 heures par ETP et par an.

**Quand le candidat demande le potentiel.** 30% des factures sont des exceptions. Elles consomment 50% du temps humain. Sur le reste, l'automatisation économiserait 80% du temps ; sur les exceptions, 50%, revue humaine incluse. Ce sont des hypothèses à valider, pas des performances déjà garanties.

**Quand il aborde la capture.** Le DAF peut supprimer ou éviter des coûts équivalents à **10 ETP**, pas 26. Le reste de la capacité serait redéployé, sans économie supplémentaire démontrée à ce stade.

**Sur les autres bénéfices.** 100 M€ d'achats annuels sont éligibles à un escompte de 2%. Le taux de capture de l'escompte passerait de 20% à 60%. Pour l'exercice, le coût additionnel de financement du paiement plus tôt est supposé nul. En situation réelle, ce coût doit être calculé et soustrait de l'escompte supplémentaire.

**Sur le calendrier.** Première année après mise en service : 50% des bénéfices cash récurrents de régime stabilisé ; coût de run annuel complet de 0,4 M€. Dès l'année 2 : 100% des bénéfices et du run. Pas de nouvelle dépense initiale.

### Calculs attendus

40 × 60 k€ = **2,4 M€ de coût d'équipe par an**. 180 000 factures en exception ; 420 000 standard. La moitié du temps correspond à 20 ETP dans chaque catégorie. La part des transactions n'est pas la part du temps.

Standard : 20 × 80% = **16 ETP** ; exceptions : 20 × 50% = **10 ETP** ; total : **26 ETP de capacité**, soit 65%. À 1 600 h/ETP : 41 600 h/an. Valeur théorique au coût complet : **1,56 M€**, distincte du cash réalisable.

Cash sur le travail : 10 × 60 k€ = **0,6 M€/an**. Escompte : 100 × 2% × (60%-20%) = **0,8 M€/an**. Bénéfice brut cash : **1,4 M€/an**. Net du run : **1 M€/an** à régime stabilisé.

Année 1 : 0,5 × 1,4 - 0,4 = **0,3 M€**. Après deux ans : 0,3 + 1 = **1,3 M€**, inférieur à 1,5. Solde au début de l'année 3 : 0,2 M€ ; à flux uniforme de 1 M€/an : 0,2 an = 2,4 mois. **Payback : 26,4 mois depuis la mise en service ; 29,4 mois depuis le début du build.** Le modèle suppose des flux uniformes dans la troisième année.

Sur trois ans : -1,5 + 0,3 + 1 + 1 = **+0,8 M€** de cash cumulé. ROI cash simple sur trois ans : 0,8 / 1,5 = **53,3%**, sans actualisation. Cela ne signifie pas que le critère des vingt-quatre mois est satisfait.

### Recommandation orale possible

> « Je ne financerais pas le déploiement complet dans ces conditions, car il ne respecte pas votre seuil de vingt-quatre mois. Le payback est d'environ vingt-six mois après mise en service : seuls dix ETP donnent une économie, même si vingt-six ETP de capacité sont libérés. Le projet reste positif sur trois ans, mais dépend fortement de l'escompte. Je proposerais de négocier le coût initial et de valider les hypothèses sur un pilote borné avant de vous représenter un dossier d'investissement. »

### Relances et variantes

**« Quel coût initial permet de tenir vingt-quatre mois ? »** Au maximum **1,3 M€** avec les autres hypothèses inchangées, hors coût additionnel d'un pilote. Réduction requise de 0,2 M€, soit **13,3%**. Ou gains supplémentaires réellement encaissables de 0,2 M€ sur ces deux premières années.

**« Si tous les 26 ETP devenaient une économie ? »** Bénéfices bruts : 1,56 + 0,8 = 2,36 ; net stabilisé : 1,96. Année 1 : 1,18 - 0,4 = 0,78. Reste 0,72 ; 0,72 / 1,96 = 0,3673 an. Payback : **environ 16,4 mois** après mise en service. Ce scénario explique comment une hypothèse de capture change fortement la réponse.

**« Et sans escompte ? »** Net stabilisé : 0,6 - 0,4 = 0,2 ; année 1 : 0,3 - 0,4 = -0,1. Payback avec ramp-up : **9 ans**, si les hypothèses restaient valables aussi longtemps ; cela rendrait nécessaire une révision complète du dossier.

**« Pourquoi un agent ? »** Vérifier si les rapprochements à règles sont déjà couverts nativement ; un workflow ou des règles déterministes peuvent suffire. Un modèle peut aider sur documents et exceptions. Aucun paiement autonome n'est requis pour obtenir les gains annoncés.

**Signal excellent.** Le candidat distingue capacité, économie et cash, intègre le ramp-up, puis refuse de confondre un ROI positif avec le respect du délai.

---

## C2 - Comparer trois trajectoires ERP

### Données à fournir après la structure

Le coût initial est payé au début. Les flux d'exploitation sont **déjà nets des coûts de fonctionnement supplémentaires**, mais **hors investissement et hors cash ponctuel de stock**. Même horizon de trois ans depuis la décision ; euros non actualisés, hors impôts. Les chiffres sont des estimations du dossier, à valider.

| Option | Investissement initial M€ | Flux an 1 M€ | Flux an 2 M€ | Flux an 3 M€ | Libération ponctuelle de stock |
|---|---|---|---|---|---|
| A Conversion de l'existant | 18 | 1 | 7 | 9 | 3 M€ en an 2 |
| B Refonte complète | 30 | 0 | 12 | 18 | 8 M€ en an 2 |
| C Transformation par périmètres | 20 | 4 | 10 | 12 | 5 M€ en an 1 |

À la question sur le risque : la production connaît un pic commercial en novembre. C suppose des périmètres découplables ; les dépendances intersites et la consolidation doivent encore être confirmées. A dispose d'un scénario de bascule testé ; B exige de nombreuses décisions métier nouvelles.

### Calculs

Cash cumulé trois ans : A = -18 + 1 + 7 + 9 + 3 = **2 M€** ; B = -30 + 0 + 12 + 18 + 8 = **8 M€** ; C = -20 + 4 + 10 + 12 + 5 = **11 M€**.

B dépasse l'enveloppe de 22 M€. C et A passent ce filtre. C crée 9 M€ de plus qu'A sur la période, selon les hypothèses.

C : cumul fin an 1 = -20 + 4 + 5 = **-11** ; fin an 2 = **-1** ; payback = 2 + 1/12 an = **25 mois** environ. A : fin an 2 = -18 + 1 + 7 + 3 = **-7** ; payback = 2 + 7/9 = **33,3 mois**. Ne pas attribuer les 5 M€ de stock à chaque année.

### Recommandation possible

> « Je privilégie C : elle respecte l'enveloppe et apporte onze millions de cash net cumulé sur trois ans, contre deux pour A. Mais cet avantage dépend d'un découplage réellement possible des périmètres. Je vérifierais les flux intersites, les données communes et la consolidation avant d'engager la trajectoire ; je protégerais aussi le pic de novembre. Si la coexistence n'est pas maîtrisable, A redevient une option crédible. »

### Complications

**Flux récurrents de C inférieurs de 30%, stock inchangé.** -20 + 2,8 + 7 + 8,4 + 5 = **3,2 M€**, encore au-dessus d'A nominal à 2 M€, mais avec faible marge. On compare ici C dégradé à A nominal pour un test rapide ; une décision complète mettrait les scénarios de risque sur une base cohérente.

**« C est-il du greenfield ou du selective data transition SAP ? »** Le tableau ne permet pas de le dire. Une trajectoire par périmètres est un séquencement ; une méthode de conversion, de nouvelle implémentation ou de transition sélective est un autre choix, à examiner techniquement.

**« Il faut une seule recommandation. »** C avec condition de faisabilité nommée et date de validation. Une condition vérifiable n'est pas une absence de décision.

**Signal excellent.** Budget comme filtre, flux comparables, BFR ponctuel, risque de coexistence et fenêtre de bascule.

---

## C3 - Programme en difficulté et coûts irrécupérables

### Données

Les 60 M€ sont dépensés sans récupération possible et identiques dans les trois scénarios. Pour simplifier, les bénéfices ci-dessous sont les **flux cash nets d'exploitation cumulés sur la même période de trois ans à compter d'aujourd'hui**, après prise en compte des délais propres aux options. Les coûts restants sont additionnels ; pas de double comptage.

| Option | Dépenses futures M€ | Bénéfices futurs cumulés M€ |
|---|---|---|
| Achever le périmètre initial | 40 | 54 |
| Réduire le périmètre | 24 | 45 |
| Arrêter | 5 de fermeture | 0 |

Le périmètre réduit conserve la vente, l'approvisionnement et la comptabilité nécessaires à l'exploitation. Certaines fonctions analytiques avancées sont reportées. Sa faisabilité métier et ses dépendances doivent être confirmées.

Après l'arbitrage économique : le programme n'a validé que **15 des 20 parcours critiques**, et les cinq restants n'ont pas de contournement accepté. Une semaine de report coûte 0,3 M€, non comprise dans le tableau.

### Raisonnement attendu

Achever : 54 - 40 = **14 M€** ; réduire : 45 - 24 = **21 M€** ; arrêter : **-5 M€**. Réduire offre 7 M€ de valeur incrémentale de plus qu'achever selon les données. Les 60 M€ n'influencent pas le classement futur, mais restent importants pour rendre compte du programme et apprendre de ses dérives.

Le classement économique ne valide pas un démarrage vendredi. Avec cinq flux critiques non couverts et sans contournement accepté, recommander un **no-go dans l'état actuel**, puis un délai borné fondé sur les corrections, tests et responsabilités. 15/20 = **75%**, pas une sécurité suffisante par principe.

### Recommandation possible

> « Je recommande de reconfigurer le programme autour du périmètre réduit : il crée vingt et un millions de valeur future, contre quatorze pour le périmètre complet. Le montant déjà dépensé ne justifie pas de poursuivre la mauvaise option. En revanche, je ne recommande pas le démarrage vendredi : cinq parcours critiques restent sans solution. Il faut sécuriser ces flux et faire valider le go/no-go par les responsables métier et le sponsor. »

**Relance : « Le report coûte cher. »** Quantifier le délai envisagé et les conséquences des flux non couverts. Ne pas convertir une exigence opérationnelle minimale en simple pari financier. Un coût de report de 0,3 M€/semaine est une donnée à comparer, pas une raison suffisante pour accepter une incapacité à exploiter.

**Relance : « Pourquoi pas un pilote dans une usine ? »** Un pilote n'est défendable que si les parcours critiques nécessaires à ce site sont validés et les dépendances contenues. Réduire la taille ne répare pas un défaut bloquant.

**Signal excellent.** Séparer « vaut-il mieux continuer ? », « quel périmètre ? » et « est-on prêt à démarrer ? ».

---

## C4 - Fusion : capter les synergies dans le bon ordre

### Données

Les 150 M€ sont une **cible annuelle du groupe à fin an 3**, pas 150 M€ cumulés ni une promesse entièrement dépendante des systèmes. Le chantier systèmes analysé ici peut soutenir au maximum **28 M€ de gains annuels** :

- 13 M€ accessibles avec données fournisseurs/articles harmonisées et action achats, sans ERP unique ;
- 9 M€ supplémentaires demandant des processus communs et des interfaces fiables, sans nécessité démontrée d'un système unique ;
- 6 M€ supplémentaires nécessitant ici une convergence ERP complète selon le diagnostic fourni.

Ces trois blocs ne se chevauchent pas. Les autres 122 M€ de la cible nécessitent des chantiers distincts.

Deux options initiales, coûts payés au début, bénéfices nets de run et hors impôts :

| Option | Coût M€ | Gains an 1 M€ | Gains an 2 M€ | Gains an 3 M€ |
|---|---|---|---|---|
| D Données et achats communs | 12 | 13 | 13 | 13 |
| E Migration immédiate complète | 45 | 0 | 18 | 28 |

Pour simplifier, D peut produire les 13 M€ dès l'année 1. Le tableau ne chiffre pas encore une option D suivie d'une convergence ni le chantier des 9 M€.

### Analyse

D : -12 + 39 = **27 M€ nets cumulés** ; E : -45 + 0 + 18 + 28 = **1 M€**. E produit plus de gains annuels en an 3 mais moins de cash cumulé sur les trois premières années. C'est une comparaison de trajectoires, pas la preuve qu'il ne faudra jamais converger.

28/150 = **18,7%** de la cible annuelle ; 13/28 = **46,4%** des gains de ce chantier accessibles via données/achats. Ne pas appliquer 28/150 au coût ou au nombre de systèmes.

### Recommandation possible

> « J'engagerais d'abord le chantier données et achats, qui crée vingt-sept millions de cash net sur trois ans. Mais il ne suffit pas à tenir l'objectif : avec les cent vingt-deux millions des autres chantiers, il manque encore quinze millions annuels à fin an 3. Je cadrerais donc immédiatement une trajectoire pour les neuf millions liés aux processus et les six millions liés à la convergence, avec cette échéance. Si elle n'est pas réalisable, le DG devra arbitrer la migration immédiate ou réviser son engagement ; les données actuelles ne permettent pas de financer honnêtement une trajectoire complète séquencée. »

**Relance : « S/4HANA est récent : pourquoi hésiter ? »** Maturité et taille ne prouvent pas la couverture métier de B, ni la capacité de A à absorber B. Tester couverture, volumes, contrôles, données, interfaces, coûts et modèle opérationnel.

**Relance : « Et les bénéfices de D+E ? »** Ils ne s'ajoutent pas aveuglément : les 13 M€ sont inclus dans les 28 M€. Chiffrer un scénario séquencé avec coûts et délais propres, puis comparer sur un horizon assez long.

**Signal excellent.** Distinguer cible annuelle, cumul cash et dépendance réelle des bénéfices aux systèmes ; expliciter que D seul atteint 135 M€ annuels au total et ne satisfait pas la cible de 150 M€.

---

## C5 - Service après go-live : mesurer les causes et l'écart restant

### Données

OTIF mesuré sur **100 000 commandes** dans chaque période comparable, même définition et mêmes règles de promesse. Avant : 96 000 conformes ; après : 84 000. La baisse représente **12 points de pourcentage**, soit 12 000 échecs supplémentaires. La baisse relative du taux est 12/96 = **12,5%**.

Un diagnostic attribue ces 12 000 échecs supplémentaires à trois causes **sans recouvrement** : 5 000 problèmes de référentiel ; 4 000 retards d'intégration ; 3 000 paramètres de planification inadaptés. Les 4 000 échecs qui existaient déjà avant restent inchangés.

Leviers réalisables dans la période étudiée : corriger 80% des échecs data ; 75% des échecs interfaces ; 80% des échecs paramètres. Les taux sont des hypothèses validées pour l'exercice, pas des garanties universelles.

### Calculs

4 000 + 3 000 + 2 400 = **9 400 commandes récupérées**. Nouveau conforme : 84 000 + 9 400 = **93 400**, soit **93,4%**. Cible 94% : il manque **600 commandes**. Le plan ne suffit donc pas encore. Il faut améliorer les leviers ou traiter 600 échecs résiduels, avec preuve de faisabilité.

### Recommandation possible

> « Je ne changerais pas d'outil sur ce seul constat. Les trois causes identifiées expliquent la dégradation et appellent un plan ciblé sur données, interfaces et paramètres. Les leviers chiffrés ramènent le service à 93,4%, encore sous votre cible de 94%. Je sécuriserais un responsable par cause, un contrôle quotidien des commandes à risque et une action supplémentaire portant sur au moins six cents commandes. »

**Relance : « Donnez-moi l'action supplémentaire. »** Examiner les résiduels : références à fort volume, incidents d'intégration récurrents, paramètres sur familles critiques. Un mode dégradé temporaire peut protéger le service si sa charge et ses erreurs sont contrôlées. Ne pas prétendre qu'une action non mesurée apporte exactement les 600.

**Relance : « Pourquoi ne pas utiliser un agent ? »** Si la cause est une interface en retard ou un paramètre faux, réparer la cause est prioritaire. Un assistant peut aider à identifier les dossiers, sans remplacer la correction ni décider seul des priorités clients.

**Signal excellent.** Dénominateur, points de pourcentage, absence de double comptage et mesure de l'objectif restant.

---

## C6 - Rentabilité : le mix et les coûts fixes

### Tableau à donner après la structure

Prix et coûts variables en euros par unité ; volumes en milliers d'unités. Pas d'autre ligne de revenu ou de coût dans l'exercice.

| Produit | Volume N-1 (k) | Volume N (k) | Prix unitaire | Coût variable unitaire |
|---|---|---|---|---|
| A | 80 | 100 | 100 | 60 |
| B | 20 | 10 | 200 | 100 |

Coûts fixes : 2 M€ en N-1 ; 2,4 M€ en N. Le marché est stable. La baisse de B vient d'une perte d'un canal de distribution ; le sujet n'est pas un dysfonctionnement ERP.

### Diagnostic

N-1 : revenus = 8 + 4 = **12 M€** ; variables = 4,8 + 2 = **6,8 M€** ; contribution = **5,2 M€** ; résultat = **3,2 M€**, marge 26,7%.

N : revenus = 10 + 2 = **12 M€** ; variables = 6 + 1 = **7 M€** ; contribution = **5 M€** ; résultat = **2,6 M€**, marge 21,7%.

Volume total : 100 000 à 110 000 = **+10%**, mais mix moins favorable : +20 000 A × 40 = **+0,8 M€** ; -10 000 B × 100 = **-1 M€** ; soit **-0,2 M€** de contribution. Coûts fixes : **-0,4 M€**. Baisse totale : **-0,6 M€**, soit **-18,75%** du résultat initial.

### Complication prix

Option : augmenter le prix A de 5%, de 100 à 105. Une étude fournie estime une baisse de volume A de 4%, de 100 000 à 96 000. Coût variable A toujours 60 ; B et coûts fixes inchangés.

Contribution A = 96 000 × (105-60) = **4,32 M€**, contre 4 M€ actuellement. Résultat global : 4,32 + 1 - 2,4 = **2,92 M€**. Gain : **0,32 M€**, insuffisant pour retrouver 3,2 ; écart résiduel **0,28 M€**.

Seuil de volume A conservant la contribution actuelle : 4 M€ / 45 = **88 889 unités**, soit baisse maximale d'environ **11,1%**, si tous les autres facteurs restent constants.

### Recommandation possible

> « La baisse vient de deux facteurs : deux cent mille euros de mix défavorable et quatre cent mille de coûts fixes supplémentaires. La hausse de prix proposée améliore le résultat de trois cent vingt mille euros, mais laisse deux cent quatre-vingt mille à récupérer. Je testerais sa solidité commerciale et je prioriserais en parallèle la récupération du canal B et les coûts fixes évitables. »

**Relance : « L'IA administrative économiserait 50 k€ : priorité ? »** Elle ne résout qu'une petite part de l'écart et exige son propre coût et délai. Ne pas la prioriser par affinité professionnelle.

**Relance : « Combien de B pour combler les 280 k€ ? »** 280 000 / 100 = **2 800 unités supplémentaires**, si capacité et coûts fixes inchangés, et sans cannibalisation. Il faut vérifier l'accès au canal et la demande.

**Signal excellent.** Expliquer comment des volumes en hausse coexistent avec un CA stable et un résultat en baisse.

---

## C7 - Build ou buy : le temps change l'économie

### Données

Même bénéfice cash brut à maturité : **1 M€/an**, immédiatement complet après mise en service. Pas de bénéfice avant. Horizon exactement trois ans **depuis aujourd'hui**. Dépense initiale payée aujourd'hui. Run seulement après mise en service ; flux uniformes ; pas d'impôts ni actualisation.

| Option | Investissement M€ | Run annuel M€ | Mise en service |
|---|---|---|---|
| Construire | 1,20 | 0,20 | Fin du mois 12 |
| Acheter | 0,25 | 0,45 | Fin du mois 3 |

Les deux couvrent aujourd'hui les critères fonctionnels et de sécurité minimaux. Les conditions de réversibilité du fournisseur doivent encore être confirmées ; elles ne sont pas déclarées bloquantes.

### Calculs

Construire : 2 années de bénéfices et run. Cash net = -1,2 + 2 × (1-0,2) = **0,4 M€**. Coût complet trois ans : 1,2 + 2 × 0,2 = **1,6 M€**.

Acheter : 2,75 années. Cash net = -0,25 + 2,75 × (1-0,45) = **1,2625 M€**. Coût complet : 0,25 + 2,75 × 0,45 = **1,4875 M€**. Avantage cash buy : **0,8625 M€** sur l'horizon.

Payback depuis aujourd'hui, sans ramp-up : build = 1 an + 1,2/0,8 = **2,5 ans** ; buy = 0,25 an + 0,25/0,55 = **0,7045 an**, soit **8,45 mois**. Ne pas appliquer ces délais à C1, dont le ramp-up est différent.

### Recommandation possible

> « Sur trois ans, j'achèterais : l'option génère environ 1,26 million de cash net contre 0,4 pour la construction, principalement grâce à la mise en service plus rapide. Je sécuriserais avant signature la réversibilité, les droits sur les données et les engagements de service. Je ne construirais que si un besoin différenciant ou une contrainte indispensable invalidait réellement l'offre du marché. »

**Relance : « Le build coûte moins cher chaque année. »** Vrai sur le run ; pas sur la période totale étudiée. À horizon plus long, refaire la comparaison avec remplacement, maintenance et évolution des coûts. Ne pas extrapoler une perpétuité sans obsolescence.

**Relance : « Que demander au fournisseur ? »** Démonstration sur cas client représentatifs ; comportement en exception ; intégration ; données exportables ; suivi des performances et incidents ; coût à volume accru ; conditions de sortie.

**Signal excellent.** Début et fin de période explicites ; avantage de la rapidité sans ignorer la dépendance.

---

## C8 - Marché, segment accessible et seuil de rentabilité

### Hypothèses à fournir après l'équation proposée

Il s'agit d'un marché fictif. 2 000 grandes entreprises, 70% équipables, 1 200 factures/mois chacune ; 8 000 entreprises moyennes, 50% équipables, 300 factures/mois. Douze mois/an. Prix : 0,20 €/facture éligible effectivement traitée. On suppose le même usage annuel moyen et aucune autre source de revenu.

À la relance sur l'accès : 60% du volume éligible est compatible avec l'offre actuelle et commercialement accessible. La cible réaliste est 15% de ce volume compatible. Coût variable : 0,05 €/facture ; fixes : 0,8 M€/an ; aucun coût de lancement dans cette question annuelle.

### Calculs

Grandes : 2 000 × 70% × 1 200 × 12 = **20,16 M de factures/an**. Moyennes : 8 000 × 50% × 300 × 12 = **14,4 M**. Total éligible = **34,56 M**. Marché théorique à prix donné : 34,56 × 0,20 = **6,912 M€/an**. C'est un TAM déjà limité par les critères d'équipement explicités.

Accessible : 34,56 × 60% = **20,736 M de factures**, soit SAM = **4,1472 M€**. Cible captée : 20,736 × 15% = **3,1104 M de factures**, soit revenu = **0,62208 M€**.

Contribution par facture : 0,20 - 0,05 = **0,15 €**. Contribution cible : 3,1104 × 0,15 = **0,46656 M€**. Résultat annuel : 0,46656 - 0,8 = **-0,33344 M€**.

Seuil : 800 000 / 0,15 = **5,333 M de factures**, soit 5,333/20,736 = **25,7% du volume accessible**. Le chiffre de 15% ne couvre pas les coûts fixes.

### Recommandation possible

> « À quinze pour cent de son segment accessible, l'offre perd environ trois cent trente-trois mille euros par an. Elle doit atteindre environ vingt-six pour cent du volume accessible pour couvrir les seuls coûts fixes, avec ces prix et coûts variables. Je ne validerais pas le lancement sur cette hypothèse ; je testerais une réduction des coûts fixes, un prix supérieur justifié par la valeur, ou un accès commercial plus large. »

**Relance : « Quelle précision annoncer ? »** 6,9 M€ de TAM ; 4,1 M€ de SAM ; 0,62 M€ de CA cible ; -0,33 M€ de résultat. Garder les calculs détaillés au brouillon, communiquer l'ordre de grandeur utile.

**Relance : « Si le volume des clients moyens est surestimé ? »** Recalculer le segment et la rentabilité ; ne pas défendre une hypothèse pour protéger la conclusion. Identifier la sensibilité principale : adoption, volume, prix et accès.

**Signal excellent.** Formule avant chiffres ; bon dénominateur de part de marché ; contribution, pas CA, pour le seuil.

---

## C9 - Quand le CV devient le cas

### Conduite

Demander au candidat un pilote **réel** : processus, statut, rôle, résultat mesuré. Limiter cette partie à deux minutes. Poser ensuite un contrefactuel : effectif stable et volume stable. Puis réduire encore l'horizon à un an.

### Ce qu'une bonne réponse distingue

Les heures libérées peuvent créer une capacité utile sans réduire les dépenses. La valeur pourrait venir d'heures supplémentaires ou de sous-traitance évitées, d'erreurs réduites, d'un service amélioré ou d'une croissance future absorbée. Chacun doit avoir sa propre preuve ; si aucun effet valorisable n'est établi, l'économie cash peut être nulle.

Ne pas accepter « les ETP seront redéployés, donc le gain financier est certain ». Demander quelle activité reçoit la capacité, quel résultat est attendu et quel responsable en répond.

### Réponse hypothétique possible

> « Avec un volume et un effectif stables, je retire les économies salariales du business case cash. Je cherche alors si le temps libéré évite d'autres dépenses, diminue des erreurs coûteuses ou améliore un résultat métier mesurable. Si aucun de ces effets n'est démontré sur l'horizon retenu, je ne présenterais pas la productivité comme une économie. Le pilote peut rester utile pour apprendre, mais son financement doit être justifié comme tel. »

**Relance : « Alternative à l'IA ? »** Corriger la donnée, simplifier une étape, utiliser le standard ERP, des règles ou une automatisation classique ; comparer le coût complet et le taux d'exception.

**Relance : « Critère d'arrêt ? »** Avant de commencer : seuil de performance et de qualité, effort humain résiduel, coût total, délai de preuve et responsable de décision. Une erreur grave sur une action critique peut imposer une suspension sans attendre le calcul économique.

**Signal excellent.** Le candidat change son raisonnement sous l'hypothèse, sans changer rétroactivement les faits de son expérience.

---

## C10 - Sélection de solution en quatre semaines

### Informations à donner

Périmètre : finance, achats, stocks et ventes dans trois pays. Le délai de quatre semaines porte sur la **recommandation**, pas sur l'implémentation. L'activité exige une traçabilité de lots fiable et la gestion des flux intersites. Les candidats fournisseurs peuvent réaliser une démonstration sur un jeu de données anonyme représentatif.

Après le plan de travail : une solution B affiche un TCO estimé inférieur de 15% à A, mais échoue sur la traçabilité et propose une extension non chiffrée et non démontrée. A satisfait le flux critique ; son TCO doit encore être confirmé. C n'a pas fourni de référence comparable.

### Bonne démarche

Semaine 1 : aligner les objectifs et critères ; observer quelques flux critiques ; inventorier systèmes, données et contraintes ; distinguer exigences indispensables et préférences.

Semaine 2 : shortlist et dossier commun ; demander TCO comparable, capacités, références et démonstrations sur les mêmes scénarios. Les travaux peuvent se chevaucher, avec un propriétaire par volet.

Semaine 3 : tester les flux critiques, les exceptions et l'intégration ; confronter le résultat aux utilisateurs ; vérifier la trajectoire de données, les ressources et les dépendances.

Semaine 4 : comparer les options, scénarios économiques et risques ; recommander ; expliciter les inconnues ; définir les conditions de contractualisation et la phase de cadrage suivante.

Les critères éliminatoires précèdent la pondération : une solution qui ne couvre pas un besoin indispensable n'est pas sauvée par un score moyen. Une extension peut rendre B viable si sa faisabilité, son coût et sa maintenabilité sont établis.

### Recommandation possible

> « Je retiendrais A comme option de référence à ce stade, sous réserve de confirmer le TCO et les conditions de déploiement. L'écart de prix de B ne compense pas un besoin indispensable encore non couvert. Je donnerais à B une fenêtre courte pour démontrer et chiffrer son extension, et je ne recommanderais pas C sans référence ou preuve comparable. La décision finale doit reposer sur les mêmes scénarios métier et le même périmètre de coûts. »

**Signal excellent.** Séparer prix affiché, coût complet, preuve fonctionnelle et plan d'implémentation. Un nom d'éditeur ne remplace aucune de ces preuves.

---

## Débrief commun - dix minutes après chaque cas

1. Faire reformuler la décision finale sans notes.
2. Reprendre le premier moment où l'analyse s'est dispersée.
3. Vérifier un calcul décisif et son effet sur la décision.
4. Demander l'information qui aurait pu renverser la recommandation.
5. Choisir un seul passage à refaire immédiatement.

Le corrigé contient des conclusions défendables avec les données. D'autres choix sont recevables s'ils explicitent une contrainte ou une hypothèse supplémentaire acceptée par le partenaire. Ajouter des bénéfices imaginaires pour sauver une option ne constitue pas une autre bonne solution.
