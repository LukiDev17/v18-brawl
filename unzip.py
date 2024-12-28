import zipfile
import os

# Pfad zur ZIP-Datei und zum Zielverzeichnis
zip_path = 'v18 brawl.zip'
extract_path = 'v18_brawl_unzipped'

# Erstellen des Zielverzeichnisses, falls es nicht existiert
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Entpacken der ZIP-Datei
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f'Dateien wurden erfolgreich nach {extract_path} entpackt.')
