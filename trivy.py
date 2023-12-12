import subprocess   # Para la ejecución de comandos Bash
from shlex import quote    # Sanitizar la entrada
from re import compile   # Caracteres permitidos como entrada
import argparse     # Manejo de argumentos

img = "ubuntu:latest"   # Imagen a escanear

# Ejecutar un comando en Bash
#resultado = subprocess.run("trivy --format json --quiet image " + img, shell=True, capture_output=True, text=True)


# Imprimir el resultado
#print(resultado.stdout)

def sanitize(input):
    # Escapar caracteres especiales
    input_sanitized = quote(input)
    
    # Validar el formato con regex (ejemplo)
    input_valid = compile(r'^[a-zA-Z0-9.:]*$')  # Acepta letras, números, punto y/o dos puntos.
    if not input_valid.match(input):
        raise ValueError("Entrada no válida. Debe contener solo letras, números, punto y/o dos puntos.")
    
    return input_sanitized

def comand(img):
    result = subprocess.run("trivy --format json --quiet image " + img , shell=True, capture_output=True, text=True)
    if result.stdout == "":
        print ("imagen no encontrada.")
    else:
        with open('result.json', 'w') as file:
            file.write(result.stdout)

def scan(img):
    try:
        sanitize(img)
        # print("Entrada valida.")
        # Ejecutar comando
        comand(img)
        
    except ValueError as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Escanea imágenes docker y retorna un archivo json con los resultados.')
    
    # Definir la bandera '--image' que tome un argumento
    parser.add_argument('--image', type=str, help='Nombre de la imagen a escanear.')
    
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    else:
        # Acceder al valor de la bandera '--image'
        if args.image:
            print(f'El valor de --image es: {args.image}')
            scan(args.image)

if __name__ == '__main__':
    main()

