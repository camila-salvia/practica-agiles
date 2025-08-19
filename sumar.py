def sumar(numeros: str) -> int: ## define la funcion
    if numeros == "": ## si es vacio, retorna 0
        return 0
    partes = numeros.split(",") ## separa los numeros en cada coma
    return sum(int(x) for x in partes) ## convierte cada parte a entero y suma
