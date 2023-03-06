num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro: "))


operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

if operacao not in ['+', '-', '*', '/']:
    print("Operação inválida!")
else:
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2

   
print("O resultado da operação é" , operacao)