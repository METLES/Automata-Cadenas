import streamlit as st
import re

#titulo
st.title("Expresiones regulares en Python")
#header o cabecera
st.markdown("### :star: Hecho por Metles :star:")
st.markdown(">Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.")

# Ingresar la cadena de caracteres
st.markdown("### ***Ingresa la cadena a evaluar***")
cadena = st.text_input("")

col1 , col2 = st.columns(2)
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

if (st.button("Evaluar")):
    with col1:
        st.markdown("## ***Palabras y su tipo***")
        for palabra in palabras:
            if re.match(digito, palabra):
                st.markdown(f" **{palabra}** ***-> Número entero***")
                contadores["numeros_enteros"] += 1
            elif re.match(minusculas, palabra):
                st.markdown(f" **{palabra}** ***-> Palabra en minúsculas***")
                contadores["palabras_minusculas"] += 1
            elif re.match(mayusculas, palabra):
                st.markdown(f" **{palabra}** ***-> Palabra en mayúsculas***")
                contadores["palabras_mayusculas"] += 1
            elif re.match(identificador, palabra):
                st.markdown(f" **{palabra}** ***-> Identificador***")
                contadores["identificadores"] += 1
            elif re.match(simbolo, palabra):
                st.markdown(f" **{palabra}** ***-> Símbolo***")
                contadores["simbolos"] += 1
            else:
                st.markdown(f"**'{palabra}'** -> ***No clasificado***")

    # Mostrar el resumen de contadores
    with col2:
        st.markdown("## ***Resumen***")
        for categoria, cantidad in contadores.items():
            st.write(f"{categoria.replace('_', ' ').capitalize()}: {cantidad}")
