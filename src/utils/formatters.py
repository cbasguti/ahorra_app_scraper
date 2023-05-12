import re

def formatPriceExito(string):
    # Eliminar todos los caracteres que no sean números ni puntos
    numeros = re.sub(r'[^0-9.]', '', string)

    # Remover los puntos de miles
    numeros = numeros.replace('.', '')

    # Convertir a entero
    entero = int(numeros)

    return entero   

def formatPriceEuro(cadena):
    # Eliminar el símbolo de moneda y el espacio en blanco
    cadena = cadena.replace("$", "").replace(" ", "")
    # Verificar si la cadena contiene una coma decimal
    if "," in cadena:
        # Eliminar los separadores de miles
        cadena = cadena.replace(".", "").replace(",", ".")
    # Convertir la cadena a un número entero
    numero = int(float(cadena))
    # Retornar el número formateado como una cadena
    return str(numero)