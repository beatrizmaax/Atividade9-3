def analisar_pares_impares(numeros):
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares
    return pares, impares
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
qtd_pares, qtd_impares = analisar_pares_impares(numeros)
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
