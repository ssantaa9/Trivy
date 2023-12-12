import subprocess   # Para la ejecución de comandos Bash
from shlex import quote    # Sanitizar entradas
from re import compile   # Caracteres permitidos como entrada
import argparse     # Manejo de argumentos

# Función para sanitizar los argumentos y caracteres permitidos
def sanitize(input):
    input_sanitized = quote(input)  # Escapar caracteres especiales
    input_valid = compile(r'^[a-zA-Z0-9.:]*$')  # Acepta letras, números, punto y/o dos puntos.
    # Verificar que la entrada solo contenga los caracteres permitidos
    if not input_valid.match(input):
        raise ValueError("Entrada no válida. Debe contener solo letras, números, punto y/o dos puntos.")
    
    return input_sanitized

# Ejecutar el comando de Trivy y guardar resultado
def scan_image(img):
    # Ejecutar el comando de Trivy
    result = subprocess.run("trivy --format json --quiet image " + img , shell=True, capture_output=True, text=True)
    # Si no hay salida, es porque la imagen no existe en los repositorios de docker
    if result.stdout == "":
        print ("imagen no encontrada.")
    else:
        # Guardar el resultado del escaneo en un archivo
        with open('image_result.json', 'w') as file:
            file.write(result.stdout)

# Sanitizar y escanear
def scan(img):
    try:
        sanitize(img)   # Sanitizar el argumento y verificar caracteres permitidos
        scan_image(img) # Escanear una imagen
        
    except ValueError as e:
        print(e)

def main():
    # Definir el parser para agregar argumentos con su respectiva descripción
    parser = argparse.ArgumentParser(description='Escanea imágenes docker y retorna un archivo json con los resultados.')
    
    # Definir la bandera '--image' que tome un argumento
    parser.add_argument('--image', type=str, help='Nombre de la imagen a escanear.')
    
    # Guardar los argumentos
    args = parser.parse_args()

    # Verificar que se haya introducido argumentos
    if not any(vars(args).values()):
        parser.print_help() # Si no se ingresaron argumentos, imprimir el menú help
    else:
        # Acceder al valor de la bandera '--image'
        if args.image:
            scan(args.image)    # Sanitizar y escanear

# Ejecución de script local
if __name__ == '__main__':
    main()
