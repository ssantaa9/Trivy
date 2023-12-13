import subprocess   # Para la ejecución de comandos Bash

# Ejecutar el comando de Trivy y guardar los resultados
def scan_images(images):
    # Recorrer la lista de imágenes
    for img in images:
        # Ejecutar el comando de Trivy
        result = subprocess.run("trivy --format json --quiet image " + img , shell=True, capture_output=True, text=True)
        # Guardar el resultado del escaneo en un archivo
        with open(img+'_scan_result.json', 'w') as file:
            file.write(result.stdout)

def main():
    # Comando para listar el ID de las imagenes
    images = subprocess.run("docker images -q", shell=True, capture_output=True, text=True)
    images = images.stdout.strip().split('\n')  # Poner las imágenes en una lista
    scan_images(images) # Escanear las imágenes

# Ejecución de script local
if __name__ == '__main__':
    main()
