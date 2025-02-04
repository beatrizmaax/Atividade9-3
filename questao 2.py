def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contagem = sum(1 for letra in frase if letra in vogais)
    return contagem
frase = input("Digite uma frase: ")
total_vogais = contar_vogais(frase)
print(f"A frase contém {total_vogais} vogais.")