
def numero_maior(n1, n2):
    if n1 > n2:
        return f"número maior é {n1}"
    else:
        return f"número maior é {n2}"


print(numero_maior(10, 20))
print(numero_maior(5, 1))
print(numero_maior(100, 1_000))
print(numero_maior(10, 80))
