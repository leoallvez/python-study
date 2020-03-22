
def calcular_preco(codigo, qtd):
    if codigo == 100:
        return 1.20 * qtd
    elif codigo == 101:
        return 1.30 * qtd
    elif codigo == 102:
        return 1.50 * qtd
    elif codigo == 103:
        return 1.20 * qtd
    elif codigo == 104:
        return 1.70 * qtd
    elif codigo == 105:
        return 2.20 * qtd
    elif codigo == 106:
        return 1.00 * qtd


print(f"valor total: R${calcular_preco(106, 10)}")

