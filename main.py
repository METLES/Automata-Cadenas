import re

# Ingresar la cadena de caracteres
cadena = input("Ingresa la cadena a evaluar: ")

# Dividir la cadena en palabras usando espacios como separadores
palabras = cadena.split()

# Estructura de las expresiones regulares en python
# [] - Especifican que caracteres especificos debera tener la REGEX
# ^  - Especifica que la palabra debera comenzar con lo solicitado dentro de los corchetes
# $  - Especifica que la palabra debera terminar con la REGEX dentro del corchete

# Definición del Alfabeto
digito = r"^\d+$"  # Número entero (solo dígitos)
minusculas = r"^[a-z]+$"  # Palabras en minúsculas
mayusculas = r"[A-Z]+$"  # Palabras en mayúsculas
identificador = r"^[a-zA-Z_]\w*$"  # Identificador (nombre de variable)
simbolo = r"^[\$\%\&\*\+\-\=/]+$"  # Símbolos especiales

# Contadores para cada caso del alfabeto
contadores = {
    "numeros_enteros": 0,
    "palabras_minusculas": 0,
    "palabras_mayusculas": 0,
    "identificadores": 0,
    "simbolos": 0
}

# Ciclo para evaluar cada palabra
for palabra in palabras:
    if re.match(digito, palabra):
        print(f"'{palabra}' -> Número entero")
        contadores["numeros_enteros"] += 1
    elif re.match(minusculas, palabra):
        print(f"'{palabra}' -> Palabra en minúsculas")
        contadores["palabras_minusculas"] += 1
    elif re.match(mayusculas, palabra):
        print(f"'{palabra}' -> Palabra en mayúsculas")
        contadores["palabras_mayusculas"] += 1
    elif re.match(identificador, palabra):
        print(f"'{palabra}' -> Identificador")
        contadores["identificadores"] += 1
    elif re.match(simbolo, palabra):
        print(f"'{palabra}' -> Símbolo")
        contadores["simbolos"] += 1
    else:
        print(f"'{palabra}' -> No clasificado")

# Mostrar el resumen de contadores
print("\n--- Resumen ---")
for categoria, cantidad in contadores.items():
    print(f"{categoria.replace('_', ' ').capitalize()}: {cantidad}")
