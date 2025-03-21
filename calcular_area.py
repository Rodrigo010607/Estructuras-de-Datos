def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.

    Args:
        largo (float): La longitud del rectángulo.
        ancho (float): El ancho del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    if largo <= 0 or ancho <= 0:
        raise ValueError("El largo y el ancho deben ser valores positivos.")
    return largo * ancho


# Llamada para probar el método
if __name__ == "__main__":
    try:
        largo = 5.0
        ancho = 3.0
        area = calcular_area_rectangulo(largo, ancho)
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area}")
    except ValueError as e:
        print(e)