def sumar(numeros: str) -> int:
    if numeros == "":
        return 0
    partes = numeros.split(",")
    return sum(int(x) for x in partes)
