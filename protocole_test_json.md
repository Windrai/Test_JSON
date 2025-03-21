
# Protocole de test – Générateur de fichiers JSON depuis une base SQLite

## Objectif

Valider le bon fonctionnement d’un composant logiciel qui lit une base SQLite représentant des messages d’une messagerie et génère un fichier JSON par message, dans un répertoire de sortie, au format spécifié.

---

## Contexte

- **Entrée** : Fichier `.sqlite` contenant une table de messages.
- **Sortie** : Un fichier `.json` par message, généré dans un répertoire.

- `content` est encodé en Base64.
- `direction` est soit `"originating"` soit `"destinating"`.

---

## Pré-requis

- Base de données SQLite de test contenant des messages types (Je n'en ai pas)
- Répertoire pour les fichiers de sortie (Ici JSON_OUTPUT)
- Outil d’exécution du composant (Je ne l'ai pas)
- Outil de lecture JSON 

---

## Cas de test

| ID     | Titre                         | Description                                                                 | Résultat attendu                                                     |
|--------|-------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| TC1   | Génération simple             | Vérifier qu’un fichier JSON est généré à partir d’un message simple        | Le fichier JSON est généré avec les champs corrects                 |
| TC2   | Tous les messages traités     | Vérifier que les N messages de la base sont traités                        | N fichiers `.json` sont générés                                     |
| TC3   | ID correct                    | Vérifier que le champ `id` est présent et que c'est un int                 | Le champ ID est bien un int                                         |
| TC4   | Encodage Base64               | Vérifier que le champ `content` est présent et est bien encodé en Base64   | Le champ `content` du JSON est bien encodé en base64                |
| TC5   | Direction correcte            | Vérifier que le message dans `direction` est présent et bien 'originating' ou 'destinating'| Le champ 'direction' est bien l'une des deux valeurs|
| TC6   | Timestamp correct             | Vérifier que `timestamp` est bien un entier (et non une string par exemple)| Le champ `timestamp` est un entier valide dans le JSON              |
| TC7   | Contact correct               | Vérifier que le champ `contact` n'est pas vide et est bien un string       | Erreur gérée proprement ou fichier non généré                       |
| TC8   | Base de données vide          | Vérifier le comportement avec une base SQLite sans messages                | Aucun fichier JSON généré, aucune erreur déclenchée                 |
| TC9   | Fichier SQLite manquant       | Vérifier le comportement si la base SQLite est absente                     | Une erreur est retournée                                            |
| TC10  | Répertoire de sortie inexistant | Vérifier si le répertoire de sortie est créé automatiquement             | Le répertoire est créé ou une erreur est retournée                  |
| TC11  | Fichier JSON bien formé       | Vérifier que tous les fichiers .json sont bien formés                      | Tous les fichiers sont valides au format JSON                       |


## Remarques : 

J'ai implémenté les cas test TC3 à 7 et TC11 dans `sources/test_json.py`
---

## Critères de validation

- Tous les champs requis sont présents et conformes
- Le contenu texte est encodé correctement en Base64
- Les erreurs sont gérées proprement sans faire crasher le composant
- Le nombre de fichiers .json générés correspond exactement au nombre de messages valides
- Chaque fichier est un JSON bien formé

---

## Annexes (optionnelles)

- Jeux de données SQLite de test (`bdd_test.sqlite`)
- Scripts de validation (ex: script Python pour valider les fichiers JSON)
- Rapport de test (résultats, erreurs rencontrées, logs)

---

## Exemple de données en base

| id | timestamp   | direction   | content          | contact |
|----|-------------|-------------|------------------|---------|
| 1  | 1710873600  | originating | Bonjour, ça va?  | Bertrand|
| 2  | 1710877200  | destinating | Oui, et toi?     | Cloé    |

Fichier attendu pour le premier message :

```json
{
  "id": 1,
  "timestamp": 1710873600,
  "direction": "originating",
  "content": "SGVsbG8gd29ybGQh",
  "contact": "Bertrand"
}
```
