import subprocess   #Para la ejecución de comandos Bash

img = "ubuntu:latest"   # Imagen a escanera

# Ejecutar un comando en Bash
resultado = subprocess.run("trivy --format json --quiet image " + img, shell=True, capture_output=True, text=True)

# Imprimir el resultado
print("Código de salida:", resultado.returncode)
print("Salida estándar:")
print(resultado.stdout)