# DOCUMENT 2 — ÉTUDES DE CAS (USE CASES)
### BCG · Round 0 · Olivier Ratier · 21 octobre · 100% français

> **Comment t'entraîner avec ce document.**
> 1. Lis seulement l'énoncé. Mets un chrono. Prends **90 secondes** pour écrire ta structure, à voix haute si possible.
> 2. Déroule le cas **à l'oral** comme si Olivier était en face. Enregistre-toi.
> 3. Compare ensuite avec la réponse modèle. L'objectif n'est pas de réciter la mienne, c'est de vérifier que ta **structure** tient et que tu n'as rien oublié de gros.
> 4. Refais le même cas 2 jours plus tard sans relire.

---

## RAPPEL MÉTHODE — LES 5 PREMIÈRES ÉTAPES (à faire sur CHAQUE cas)

Cette séquence doit devenir un réflexe. Elle t'évite le blanc après l'énoncé et montre une tête bien structurée.

1. **Reformule la question** (en version courte, pas mot pour mot). Si des chiffres sont donnés, répète-les — et transforme-les en pourcentage quand c'est possible.
2. **Vérifie l'objectif.** « L'objectif principal, c'est X. Y a-t-il d'autres objectifs que je devrais garder en tête ? »
3. **Pose 2-3 questions de clarification** (seulement si utile pour structurer).
4. **Labellise le cas + pose ta structure MECE.** Prends 60-90 s de silence pour écrire. Puis tourne tes notes vers l'interlocuteur et déroule : d'abord les grands titres (les « buckets »), ensuite le détail.
5. **Énonce une hypothèse.** « Mon hypothèse de départ, c'est que… — c'est ce que je vais chercher à prouver ou à infirmer. »

**Et pour conclure (recommandation) :** la réponse d'abord → le pourquoi → le comment → les risques (priorisés par impact × probabilité) → les prochaines étapes (court terme / long terme). 30 à 90 secondes, linéaire et net.

> **Spécial profil tech/ERP :** Olivier n'attend PAS de toi un calcul de part de marché façon MBA. Il va probablement te donner un cas **ERP / transformation / IA** — ton terrain. Ta valeur ajoutée : relier la **techno** à l'**operating model** et à la **valeur business**. Montre que tu penses stratégie *et* exécution.

---

## CAS 1 — STRATÉGIE ERP : « Faut-il migrer vers S/4HANA ? » ⭐ (le plus probable)

**Énoncé (ce qu'Olivier pourrait dire) :**
> « Notre client est un groupe industriel européen, plusieurs milliards d'euros de chiffre d'affaires, présent dans 20 pays. Il tourne aujourd'hui sur un vieil ERP SAP ECC, très customisé, qui arrive en fin de support. Le DSI veut migrer vers S/4HANA. Le PDG, lui, n'est pas convaincu : il voit une facture énorme et un risque de programme qui dérape. Il nous demande : est-ce qu'on y va, et si oui, comment ? »

### Ta reformulation + objectif
> « Si je résume : un groupe industriel multi-pays, sur un SAP ECC fortement customisé en fin de support, se demande s'il doit migrer vers S/4HANA, et si oui selon quelle approche. L'objectif principal, c'est de prendre une décision go / no-go éclairée et de cadrer le "comment". Est-ce qu'il y a un autre objectif implicite — par exemple une contrainte de date liée à la fin de support, ou une ambition de transformation au-delà de la simple migration technique ? »

*(Olivier répondra sûrement : la fin de support SAP ECC est un facteur de temps réel, et oui, le PDG veut que ça serve à quelque chose, pas juste "iso-fonctionnel".)*

### Hypothèse
> « Mon hypothèse : la migration vaut le coup, mais à condition de ne pas la traiter comme un projet IT iso-périmètre. La valeur ne vient pas de HANA en soi, elle vient de la standardisation des processus et des capacités data/IA qu'on débloque. Je vais chercher à valider ça. »

### Structure MECE — 4 buckets
Je labellise : **cas de décision d'investissement / transformation.** Je l'analyse en quatre blocs.

**1. Le "pourquoi" — la rationale stratégique**
- Qu'est-ce qui pousse vraiment ? Fin de support (risque/coût du maintien), dette technique du custom, ou ambition de transformation (data, IA, agilité) ?
- Quelle est la cible : juste rester sous support, ou devenir "data-driven" ?
- *WCS — c'est quoi le succès dans la tête du PDG ?* (réduire le coût de maintenance ? accélérer les clôtures ? débloquer l'IA ? réduire les délais supply chain ?)

**2. Le "quoi" — l'état des lieux et l'ampleur**
- Reconstruire l'état *réel* : combien de custom, combien de modules, combien d'interfaces, combien d'utilisateurs, quelle qualité de données ?
- Le custom est le nerf de la guerre : chaque développement spécifique = coût de migration + dette future. Combien peut-on ramener au standard ?
- Qualité et gouvernance des données (migrer des données sales dans un système neuf = reproduire le problème en pire).

**3. Le "comment" — les options d'approche** (c'est là que tu brilles)
- **Brownfield** (conversion technique du système existant) : plus rapide, moins cher, mais on embarque la dette.
- **Greenfield** (reconstruction sur un cœur standard propre) : plus cher/long, mais on nettoie et on standardise — on capte la vraie valeur.
- **Hybride / "selective"** : on repart propre là où ça compte (finance, supply chain), on convertit le reste.
- Mon arbitrage : fonction du ratio custom et de l'ambition. Fort custom + ambition de transformation → plutôt greenfield sélectif.

**4. La valeur et le risque — le business case**
- *Valeur :* réduction du coût de maintenance, clôtures plus rapides, moins de spécifique, et surtout la plateforme pour l'analytics et l'**IA agentique** (automatiser achats, rapprochements, planification).
- *Coûts :* licences, intégrateur, data migration, change management, double run.
- *Risques (priorisés) :* dérive du programme (le #1 — c'est la peur du PDG), résistance au changement, qualité de données, interruption d'activité au cutover.

### Recommandation (réponse d'abord)
> « Oui, le client doit migrer — mais pas comme une migration technique. **Il doit en faire une transformation de l'operating model avec un cœur standard.**
>
> *Pourquoi :* la fin de support rend le statu quo plus risqué que le mouvement, et surtout un simple "lift & shift" dépenserait beaucoup pour ne capter aucune des vraies valeurs — data et IA.
>
> *Comment :* une approche greenfield sélective — on repart sur un cœur standard propre sur la finance et la supply chain, on réduit drastiquement le custom, et on séquence par vagues géographiques pour limiter le risque.
>
> *Les risques, dans l'ordre :* d'abord la dérive du programme — on la maîtrise par une gouvernance forte, un cœur standard pré-validé et des go-lives par vagues plutôt qu'un big bang. Ensuite le change management, qu'on démarre dès le jour un. Enfin la qualité des données, qu'on traite en amont, pas au cutover.
>
> *Prochaines étapes :* un diagnostic de 6 à 8 semaines pour chiffrer le ratio de custom réductible et bâtir le business case par vague. C'est là qu'on peut vous aider. »

> **Ton edge personnel à placer :** « C'est exactement le type de programme où j'ai vu des transformations déraper — et presque toujours pour la même raison : on migre le custom au lieu de revenir au standard. »

---

## CAS 2 — TURNAROUND : « Un programme de transformation qui déraille » ⭐

**Énoncé :**
> « Un distributeur paneuropéen a lancé il y a 18 mois un grand programme de transformation ERP. On est à 12 mois du go-live prévu, le budget est déjà dépassé de 40%, deux dates de go-live ont été ratées, et le comité de direction songe à tout arrêter. On nous appelle. Que faites-vous ? »

### Reformulation + objectif
> « Donc : un programme ERP paneuropéen, 18 mois de lancé, +40% de budget, deux go-live manqués, et un Comex au bord de l'arrêt. L'objectif : diagnostiquer pourquoi ça déraille et décider s'il faut continuer, redresser, ou arrêter — et dans tous les cas, limiter la casse. Est-ce que le vrai objectif du Comex, c'est de livrer coûte que coûte, ou de reprendre le contrôle et savoir la vérité ? »

### Hypothèse
> « Mon hypothèse : le problème n'est quasi jamais purement technique. C'est de la gouvernance, du périmètre qui enfle, et un désalignement entre les attentes métier et ce qui se construit. Je vais vérifier ça avant de parler solution. »

### Structure MECE — "Diagnostic → Décision → Redressement"

**1. Diagnostic — pourquoi ça déraille** (E le plus large d'abord)
- *Gouvernance :* qui décide ? Y a-t-il un vrai sponsor exécutif ? Les décisions sont-elles prises ou repoussées ?
- *Périmètre :* est-ce qu'il a enflé (scope creep) ? Combien de custom ajouté en route ?
- *Alignement métier / solution :* ce qui se construit correspond-il au besoin réel ? Les utilisateurs ont-ils été embarqués ?
- *Delivery :* qualité de l'intégrateur, de l'équipe, de la donnée. Le planning était-il réaliste au départ ?

**2. Décision — continuer, redresser, arrêter**
- Analyse coût-bénéfice *forward-looking* : le coût pour finir vs la valeur restante vs le coût d'arrêt. On ne raisonne pas sur l'argent déjà dépensé (sunk cost).
- Trois scénarios chiffrés à présenter au Comex.

**3. Redressement — le plan si on continue**
- Reconstruire l'image fidèle de l'état réel (pas l'état déclaré par l'équipe en place).
- Re-cadrer le périmètre : geler le custom, revenir au cœur standard partout où c'est possible.
- Re-séquencer : passer d'un big bang à des go-live par vagues, pour obtenir des victoires rapides et restaurer la confiance.
- Gouvernance : un sponsor exécutif unique, des décisions hebdomadaires, une communication transparente.

### Recommandation
> « Avant de décider d'arrêter, je refais le diagnostic de l'état réel en 2-3 semaines — parce que le Comex décide aujourd'hui sur des perceptions, pas sur des faits. Mon hypothèse, c'est qu'on peut redresser sans tout jeter.
>
> *Comment :* on gèle le périmètre et le custom, on revient au standard, on repasse d'un big bang à des vagues avec une première victoire rapide sous 90 jours, et on met un sponsor exécutif unique avec des décisions prises chaque semaine.
>
> *Risques :* que le +40% de budget cache un problème plus profond de qualité de delivery — d'où le diagnostic d'abord. Et la fatigue des équipes.
>
> *Next steps :* diagnostic express, puis trois scénarios chiffrés — continuer / redresser / arrêter — pour une décision du Comex en connaissance de cause. »

> **Ton edge :** « C'est précisément ce que je fais : reprendre des programmes en difficulté en cours de route. Et à chaque fois, le vrai problème n'est pas là où on le croit — il est dans l'écart entre l'état déclaré et l'état réel. »

---

## CAS 3 — BUSINESS CASE IA : « Faut-il déployer de l'IA agentique dans l'ERP ? » ⭐

**Énoncé :**
> « Le directeur financier d'un groupe de biens de consommation a entendu parler d'"agents IA" partout. Il nous demande : est-ce que je devrais investir dans de l'IA agentique dans mon ERP, sur quoi en priorité, et comment je sais que ça rapporte ? »

### Reformulation + objectif
> « L'objectif : aider le DAF à décider s'il investit dans l'IA agentique dans l'ERP, à prioriser les cas d'usage, et à mesurer le retour. Est-ce que le but, c'est réduire des coûts, accélérer des processus, ou se positionner stratégiquement sur l'IA ? »

### Hypothèse
> « Mon hypothèse : oui, mais la valeur ne vient pas de "faire de l'IA" — elle vient de cibler quelques processus transactionnels à fort volume et forte répétitivité, où un agent remplace du travail manuel à faible valeur. On commence petit, on prouve, on étend. »

### Structure MECE — "Où → Quelle valeur → Comment → Risques"

**1. Où appliquer — la grille de priorisation**
- Critères : volume de transactions × part de manuel × niveau de règles (plus c'est répétitif et basé sur des règles, plus l'agent est efficace) × risque/criticité (commencer là où l'erreur n'est pas catastrophique).
- Candidats naturels dans l'ERP : traitement des commandes d'achat, rapprochement de factures (3-way match), relances clients, ordonnancement de production, nettoyage/enrichissement de données.

**2. Quelle valeur — le business case**
- Gains : réduction de l'effort manuel (ETP redéployés), accélération des cycles (ex : clôture, cash), réduction d'erreurs, meilleure donnée.
- Référence crédible : sur des processus ciblés, on observe des réductions d'effort manuel de l'ordre de 60-70%.
- Coûts : build des agents, intégration ERP, gouvernance IA, conduite du changement.

**3. Comment — l'approche de déploiement**
- Partir d'UN cas d'usage pilote (fort irritant, faible risque), le livrer vite, mesurer, puis industrialiser.
- Combiner les briques : process mining pour *trouver* où est le gaspillage, RPA + GenAI/LLM pour *exécuter*, agents pour *décider dans un cadre*.
- Gouvernance : human-in-the-loop au début, garde-fous, traçabilité des décisions de l'agent.

**4. Risques**
- Hallucination / décision erronée d'un agent sur un processus critique → human-in-the-loop + périmètre maîtrisé.
- Données de mauvaise qualité → l'agent amplifie le problème.
- Adoption : les équipes doivent faire confiance à l'agent.

### Recommandation
> « Oui, investir — mais par la preuve, pas par la hype. On démarre sur un seul processus à fort volume et faibles enjeux, typiquement le rapprochement de factures, on vise une réduction d'effort manuel de l'ordre de 60-70%, on mesure, et on en fait la vitrine qui finance la suite.
>
> *Comment :* process mining pour cibler, puis un agent avec human-in-the-loop, étendu par vagues.
> *Risques :* qualité de données et confiance — traités dès le pilote.
> *Next steps :* un pilote de 8-12 semaines sur un processus, avec des indicateurs de valeur définis à l'avance. »

> **Ton edge :** « C'est exactement la méthode avec laquelle j'ai piloté nos premiers pilotes IA — partir d'un irritant précis, prouver vite, puis étendre. Et c'est là qu'on a atteint les 70% de réduction d'effort manuel. »

---

## CAS 4 — RÉDUCTION DE COÛTS / EFFICACITÉ OPÉRATIONNELLE

**Énoncé :**
> « Une entreprise manufacturière doit réduire ses coûts opérationnels de 15% en deux ans, sans dégrader le service client. Par où commencez-vous ? »

### Reformulation + objectif
> « Objectif : -15% de coûts opérationnels en 2 ans, contrainte forte = ne pas dégrader le service client. Est-ce qu'il y a une cible prioritaire (production, achats, structure) ou on balaie tout ? »

### Hypothèse
> « Mon hypothèse : la plus grosse poche de valeur n'est pas dans la coupe brutale, mais dans l'automatisation des processus transactionnels et la standardisation — ça réduit le coût sans toucher au service client. »

### Structure — framework coûts (labor / production / finance) + MECE
D'abord cadrer : décomposer la base de coûts (quelles sont les 3 plus grosses poches ? trends sur 3 ans ? benchmark vs concurrents ?). Puis attaquer par leviers :

**1. Main d'œuvre / processus**
- Automatiser les tâches transactionnelles répétitives (achats, factures, saisie) via RPA + IA → gros gisement, sans toucher au client.
- Cross-training, réduction des heures sup.

**2. Production**
- Investir dans la techno pour la productivité, réduire les stocks (JIT), consolider, lignes flexibles.
- Renégocier et consolider les fournisseurs.

**3. Finance / structure**
- Vendre les actifs non essentiels, renégocier la dette, optimiser le working capital (faire payer les clients plus tôt).

**Garde-fou service client :** on classe chaque levier par impact-coût × risque-client, et on ne touche pas aux leviers qui dégradent l'expérience. L'automatisation est idéale car elle réduit le coût *et* fiabilise le service.

### Recommandation
> « Je priorise l'automatisation des processus transactionnels et la standardisation : c'est le levier qui donne le plus de points de pourcentage sans toucher au service client. Je complète par la supply chain (stocks, fournisseurs) et la finance (actifs non essentiels, BFR).
> *Risque :* couper trop vite au mauvais endroit et casser le service — d'où la grille impact × risque-client.
> *Next steps :* un diagnostic des 3 plus grosses poches de coûts + un quick win d'automatisation sous 90 jours pour financer la suite. »

---

## CAS 5 — MARKET SIZING / ESTIMATION (le cas "math" possible)

> Olivier peut glisser une estimation pour tester ta logique. **La règle : structure d'abord, calcul ensuite, à voix haute, et on raisonne en ordres de grandeur.** Le chiffre final importe moins que le chemin.

**Énoncé type :**
> « Estimez le nombre de transactions de commandes d'achat traitées par an par une entreprise industrielle de 10 000 employés. »

### Méthode (annonce ta roadmap avant de calculer)
> « Je vais estimer ça en trois temps : d'abord combien de personnes passent des commandes, puis combien de commandes chacune génère, puis j'agrège. »

- Sur 10 000 employés, supposons ~10% ont un rôle qui déclenche des achats (prod, maintenance, services généraux, R&D) → **~1 000 personnes acheteuses**.
- Hypothèse : chaque personne génère en moyenne ~2 commandes par semaine → ~100 par an → **~100 000 commandes/an** côté opérationnel.
- J'ajoute les achats récurrents automatiques (réappro matières, contrats) : disons +50% → **~150 000 PO/an**, ordre de grandeur.

> « Donc de l'ordre de 100 000 à 150 000 commandes par an. Et ce chiffre est intéressant stratégiquement : à ce volume, automatiser le traitement des commandes par un agent IA, même partiellement, représente des milliers d'heures économisées — c'est typiquement là qu'un business case IA devient évident. »

**Astuce :** termine toujours une estimation en **reliant le chiffre à une implication business**. Ça te distingue d'un candidat qui s'arrête au nombre.

---

## CAS 6 — "BRAINSTORM" / QUESTION OUVERTE (très fréquent en Round 0 court)

> En 30 min, Olivier n'a pas toujours le temps d'un cas complet. Il peut poser une question ouverte pour voir ta structure en live.

**Exemples et comment répondre :**

**« Quels sont, selon vous, les 3 principales raisons pour lesquelles les transformations ERP échouent ? »**
> « Je les classe en trois familles. **Un, la gouvernance :** pas de vrai sponsor exécutif, décisions repoussées. **Deux, le périmètre :** on garde trop de spécifique au lieu de revenir au standard, et le scope enfle. **Trois, l'humain :** le change management traité en fin de projet alors qu'il devrait démarrer au jour un. Si je devais n'en garder qu'une : l'écart entre l'état déclaré du projet et son état réel — c'est la racine de presque tout le reste. »

**« Comment l'IA agentique va-t-elle changer l'ERP dans les 5 ans ? »**
> « On passe d'un ERP qui *enregistre* le travail à un ERP qui *fait* le travail. Aujourd'hui, un humain lit, décide, saisit. Demain, un agent exécute les tâches transactionnelles à règles — commandes, rapprochements, réappro — et l'humain se concentre sur l'exception et la décision. Trois conséquences : moins de travail manuel, des cycles plus courts, et une bascule du rôle de l'humain vers la supervision. Le gagnant ne sera pas celui qui a le meilleur modèle, mais celui qui a les meilleures données et les bons garde-fous. »

**Structure réflexe pour TOUTE question ouverte :** « Je vois ça en 3 axes… » puis 3 buckets MECE, puis une phrase de synthèse qui tranche. Ne jamais lister en vrac.

---

## CHECKLIST DE FIN DE CAS (à te répéter)

- [ ] J'ai reformulé et vérifié l'objectif ?
- [ ] J'ai posé une structure MECE *avant* de plonger dans le détail ?
- [ ] J'ai énoncé une hypothèse ?
- [ ] J'ai regardé l'externe (économie/marché) avant l'interne ?
- [ ] J'ai conclu par : **réponse → pourquoi → comment → risques priorisés → next steps** ?
- [ ] J'ai relié au moins une fois le cas à mon vécu ERP/IA réel (mon edge) ?
- [ ] J'ai raisonné en ordres de grandeur et relié les chiffres au business ?
