def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    # Usamos la función anterior para asegurar el resultado correcto
    mayor_de_dos = max_of_two(x, y)
    return max_of_two(mayor_de_dos, z)
