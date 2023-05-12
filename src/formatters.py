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
    cadena = cadena.split(',')[0]
    # Retornar el número formateado como una cadena
    cadena = cadena.replace('.', '')

    entero = int(cadena)

    return entero