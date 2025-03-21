import json
import base64
import os

OUTPUT_DIR = "../JSON_OUTPUT"

#Le but est de générer des fichiers JSON que le programme devrait fournir en sortie
def create_json_output() : 
    #On check si le dossier de sortie existe, sinon on le créer
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

#Création d'un exemple de dictionnaire python
    messages=[
        #On teste avec un message valide avec direction = originating
        {
            "id": 1,
            "timestamp": 1710873600,
            "direction": "originating",
            #Conversion de la chaîne en binaire puis en Base64 puis en chaîne de caractères pour JSON
            "content": base64.b64encode("Bonjour, vous allez bien?".encode()).decode(),
            "contact": "Bertrand"
        },
        #On teste avec un message valide avec direction = destinating
        {
            "id" :2,
            "timestamp": 1710877200,
            "direction": "destinating",
            "content": base64.b64encode("Très bien, merci!".encode()).decode(),
            "contact": "Cloé"
        },
        #On teste sans direction
        {
            "id" :3,
            "timestamp": 1710877200,
            "content": base64.b64encode("Je n\' pas de direction".encode()).decode(),
            "contact": "Gérard"
        },
        #On teste sans contact
        {
            "id" :4,
            "timestamp": 1710877200,
            "direction": "originating",
            "content": base64.b64encode("Je n\' pas de contact".encode()).decode(),
        },
        #On teste sans timestamp
        {
            "id" :5,
            "direction": "originating",
            "content": base64.b64encode("Je n\' pas de timestamp".encode()).decode(),
            "contact": "Théo"
        },
        #On teste dans content
        {
            "id" :6,
            "timestamp": 1710877200,
            "direction": "originating",
            "contact": "Pascal"
        },
        #On teste sans id 
        {
            "timestamp": 1710877200,
            "direction": "originating",
            "content": base64.b64encode("Je n\' pas de timestamp".encode()).decode(),
            "contact": "Pascal"
        },
        #On teste un mauvais encodage
        {   
            "id": 8,
            "timestamp": 1710873600,
            "direction": "originating",
            "content": base64.b85encode("Bonjour, vous allez bien?".encode()).decode(),
            "contact": "Grégoire"
        },
        #On teste les erreurs de type
        {
            "id": "bad_type",
            "timestamp": "blabla_timestamp",
            "direction": 1,
            #Conversion de la chaîne en binaire puis en Base64 puis en chaîne de caractères pour JSON
            "content": base64.b64encode("Bonjour, vous allez bien?".encode()).decode(),
            "contact": 4
        }
    ]

    for msg in messages:
        #Sous le linux
        if "id" in msg :
            json_path = f"{OUTPUT_DIR}/" + f"message_{msg['id']}.json"
        else : 
            json_path = f"{OUTPUT_DIR}/" + f"message_sans_id.json"
        with open(json_path, "w", encoding="utf-8") as json_file:
            #Conversion du dictionnaire msg en Chaîne JSON
            json.dump(msg, json_file, indent=4)

#On créer les fichier json
create_json_output()
print("Les fichiers JSON ont été générés.")