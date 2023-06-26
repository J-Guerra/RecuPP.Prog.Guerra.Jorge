def reemplazarCaracteres(cadena,caracter,cambio):
    contador = 0
    lista = list(cadena)

    for indice in range(len(lista)):
        if lista[indice] == caracter:
            lista[indice] = cambio
            contador += 1

    cadena = "".join(lista)
    return (cadena, contador)

print(reemplazarCaracteres("Los diputados", "o", "e"))