def contar_nomes_com_a(nomes):
    return sum(1 for nome in nomes if nome.lower().startswith('a'))
nomes = []
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)
qtd_nomes_com_a = contar_nomes_com_a(nomes)
print(f"Quantidade de nomes que começam com a letra 'A': {qtd_nomes_com_a}")