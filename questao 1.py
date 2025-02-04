def calcular_desconto(preco, percentual):
    desconto = (preco * percentual) / 100
    preco_final = preco - desconto
    return preco_final
preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite a porcentagem de desconto: "))
preco_com_desconto = calcular_desconto(preco, percentual)
print(f"O preço final com desconto é: R$ {preco_com_desconto:.2f}")
