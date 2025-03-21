# Générateur de fichiers JSON depuis une base SQLite

## Description

Ce projet a pour objectif de tester un **composant logiciel** qui lit une base de données SQLite représentant des messages d’une messagerie, et génère en sortie un fichier `.json` par message. Chaque fichier JSON doit respecter un format précis.
Ne disposant pas du code à tester, je me suis focalisé sur l'implémentation des tests visant les notamment les fichiers de sorties (les fichiers JSON), que j'ai simulé. 

---

### Champs obligatoires dans un message :
| Champ      | Type     | Description                                 |
|------------|----------|---------------------------------------------|
| `id`       | Integer  | Identifiant unique du message               |
| `timestamp`| Integer  | Horodatage UNIX du message                  |
| `direction`| String   | "originating" ou "destinating"              |
| `content`  | String   | Contenu encodé en Base64                    |
| `contact`  | String   | Nom du contact associé                      |

---

## Tests

Les tests sont écrits avec `pytest` et couvrent les cas suivants :
- Vérification de la présence et du type des champs (`id`, `timestamp`, `direction`, etc.)
- Validité du format Base64 pour `content`
- Conformité des valeurs (`direction`, chaînes non vides)
- JSON bien formé (pas de JSON malformé)
- Fichiers générés en bonne quantité

Lancement des tests :
```bash
pytest -v
```

Pour enregistrer les résultats dans un fichier log :
```bash
pytest -v > ../logs/tests_output.log 2>&1
```

---

## Organisation

```
.
├── JSON_OUTPUT/           # Répertoire contenant les fichiers JSON de test
├── tests/
│   ├── test_json.py   # Tests unitaires par cas de test
│   └── json_generation.py               # Générateur de fichiers JSON de test
├── logs/                 # Logs d'exécution des tests
├── protocole_test_json.md # Présente les protocoles de test
└── README.md             # Présentation du projet
```

---

## Pré-requis

- Python 3.x
- Modules : `pytest`, `base64`, `json`, `os`

