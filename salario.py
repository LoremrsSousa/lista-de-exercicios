nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500:
    aumento = salario * 0.1
else:
    aumento = salario * 0.05

novo_salario = salario + aumento
diferenca = novo_salario - salario

print(f"O novo salário de {nome} é R$ {novo_salario:.2f}, um aumento de R$ {diferenca:.2f} em relação ao salário anterior.")