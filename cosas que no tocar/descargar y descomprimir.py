import os
import requests
import zipfile

# URL del archivo ZIP que deseas descargar
url_archivo_zip = "https://mediafilez.forgecdn.net/files/5289/530/Server-Files-0.2.58.zip"
# Ruta de destino para guardar el archivo ZIP
ruta_destino = "/workspaces/ATM9/Minecraft-server-20240515T000717Z-001.zip"

# Descargar el archivo ZIP
response = requests.get(url_archivo_zip)
with open(ruta_destino, "wb") as archivo_zip:
    archivo_zip.write(response.content)

# Descomprimir el archivo ZIP en la misma ubicación
with zipfile.ZipFile(ruta_destino, "r") as zip_ref:
    zip_ref.extractall("/workspaces/ATM9")

print("Archivo ZIP descargado y descomprimido con éxito.")