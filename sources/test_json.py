import json
import base64
import os
import pytest


OUTPUT_DIR = "../JSON_OUTPUT"



#On vérifie la présence de chaque données nécessaires dans le fichier JSON ainsi que leur type

# TC3 – ID correct
def test_tc3_id_valid():
    all_errors= []
    for file_name in os.listdir(OUTPUT_DIR):
        with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
            data = json.load(f)
            if "id" not in data or not isinstance(data["id"], int):
                all_errors.append(f"{file_name} : id manquant ou mauvais type")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))

# TC4 – Encodage Base64
def test_tc4_content_base64():
    all_errors= []
    for file_name in os.listdir(OUTPUT_DIR):
        with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
            data= json.load(f)
#On vérifie que la valeur de content est bien encodé en Base64
#               le décodage Base64 réussit sans erreur
#               Le résultat est bien une chaîne de caractère str
#               On réencode la chaîne décodée pour vérifier que ce n'est pas un faux positif
 
            if "content" in data:
                try:
                    decoded = base64.b64decode(data["content"], validate=True)
                    if base64.b64encode(decoded).decode() != data["content"]:
                        all_errors.append(f"{file_name} : encodage Base64 incorrect")
                except Exception:
                    all_errors.append(f"{file_name} : Mauvais encodage. Dois être en Base64")
            else:
                all_errors.append(f"{file_name} : content manquant")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))



# TC5 – Direction correcte
def test_tc5_direction_valid():
    all_errors = []
    for file_name in os.listdir(OUTPUT_DIR):
        with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
            data = json.load(f)
            if "direction" not in data or data["direction"] not in ["originating", "destinating"]:
                all_errors.append(f"{file_name} : direction manquante ou mauvais type")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))

# TC6 – Timestamp correct
def test_tc6_timestamp_valid():
    all_errors = []
    for file_name in os.listdir(OUTPUT_DIR):
        with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
            data = json.load(f)
            if "timestamp" not in data or not isinstance(data["timestamp"], int):
                all_errors.append(f"{file_name} : timestamp manquant ou mauvais type")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))

# TC7 – Contact correct
def test_tc7_contact_valid():
    all_errors = []
    for file_name in os.listdir(OUTPUT_DIR):
        with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
            data = json.load(f)
            if "contact" not in data or not isinstance(data["contact"], str) or not data["contact"].strip():
                all_errors.append(f"{file_name} : contact manquant ou mauvais type")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))


# TC11 – Fichier JSON bien formé
def test_tc11_json_valid_format():
    all_errors = []
    for file_name in os.listdir("../JSON_MAL_FORME"):
        if not file_name.endswith(".json"):
            continue # Si ce n'est pas un .json on skip
        try:
            with open(os.path.join(OUTPUT_DIR, file_name), "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError: # Erreur de parsing levée
            all_errors.append(f"{file_name} : JSON malformé")
    if all_errors:
        pytest.fail("\n" + "\n".join(all_errors))


#Pour éviter de lancer les tests si le fichier est importé quelque part.
if __name__ == "__main__":
    pytest.main()