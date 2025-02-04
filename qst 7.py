def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()
cpf = input("Digite o CPF (apenas números): ")
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
