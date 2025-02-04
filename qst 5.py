def converter_reais_para_dolares(valor_reais, cotacao_dolar):
    valor_dolares = valor_reais / cotacao_dolar
    return valor_dolares
valor_reais = float(input("Digite o valor em reais: R$ "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_convertido = converter_reais_para_dolares(valor_reais, cotacao_dolar)
print(f"Com R$ {valor_reais:.2f}, você pode comprar US$ {valor_convertido:.2f}.")