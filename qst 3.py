def calcular_media_ponderada(nota1, peso1, nota2, peso2):
    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    return media
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
media_final = calcular_media_ponderada(nota1, peso1, nota2, peso2)
print(f"A média ponderada das notas é: {media_final:.2f}")
