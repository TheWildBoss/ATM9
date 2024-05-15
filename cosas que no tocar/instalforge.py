import os
import requests
import zipfile

# Descarga el instalador de Forge
def descargar_forge(url_descarga, directorio_destino):
  """
  Descarga el instalador de Forge desde la URL especificada y lo guarda en el directorio indicado.

  Args:
    url_descarga: La URL del archivo instalador de Forge.
    directorio_destino: La ruta completa del directorio donde se guardará el instalador.
  """
  nombre_archivo = os.path.basename(url_descarga)  # Extrae el nombre del archivo de la URL

  # Crea el directorio si no existe
  if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

  # Descarga el archivo
  respuesta = requests.get(url_descarga, stream=True)
  if respuesta.status_code == 200:
    with open(os.path.join(directorio_destino, nombre_archivo), 'wb') as f:
      for chunk in respuesta.iter_content(chunk_size=1024):
        f.write(chunk)
  else:
    raise Exception(f"Error al descargar el instalador de Forge: {respuesta.status_code}")

# Ejecuta el instalador de Forge
def ejecutar_forge(instalador, directorio_destino):
  """
  Ejecuta el instalador de Forge y configura el servidor en el directorio indicado.

  Args:
    instalador: La ruta completa del archivo instalador de Forge.
    directorio_destino: La ruta completa del directorio donde se instalará el servidor.
  """
  # Ejecuta el instalador con argumentos para instalar en el directorio especificado
  os.system(f"java -jar {instalador} --installServer {directorio_destino}")

# Descarga e instala Forge
def instalar_forge(url_descarga, directorio_destino):
  """
  Descarga e instala Forge desde la URL especificada en el directorio indicado.

  Args:
    url_descarga: La URL del archivo instalador de Forge.
    directorio_destino: La ruta completa del directorio donde se instalará el servidor.
  """
  descargar_forge(url_descarga, directorio_destino)
  instalador = os.path.join(directorio_destino, os.path.basename(url_descarga))
  ejecutar_forge(instalador, directorio_destino)

# Ejemplo de uso
url_descarga = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.2-43.2.20/forge-1.19.2-43.2.20-installer.jar"  # URL del instalador
directorio_destino = "/workspaces/ATM9/servidor_minecraft"  # Directorio de instalación

instalar_forge(url_descarga, directorio_destino)

print("Forge instalado correctamente en", directorio_destino)
