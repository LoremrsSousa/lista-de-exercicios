# Preços dos ovos
preco_pequeno = 7.80
preco_medio = 12.90
preco_grande = 23.95

# Preços dos recheios
preco_chocolate_preto = 9.67
preco_chocolate_branco = 4.50
preco_chocolate_ao_leite = 9.32

# Preços dos adicionais
preco_kitkat = 4.67
preco_mms = 5.43

# Taxas de entrega e presente
taxa_entrega = 5.00
taxa_presente = 2.50

# Taxas de pagamento
taxa_cartao = 3.30
taxa_dinheiro_pix = 0.10


print("Bem-vindo(a) à loja de ovos de Páscoa da Dona Maria!")
print("Tamanhos disponíveis:")
print("1 - Pequeno (R$7.80)")
print("2 - Médio (R$12.90)")
print("3 - Grande (R$23.95)")
tamanho = int(input("Escolha o tamanho do ovo: "))

print("Recheios disponíveis:")
print("1 - Chocolate preto (R$9.67)")
print("2 - Chocolate branco (R$4.50)")
print("3 - Chocolate ao leite (R$9.32)")
recheio_1 = int(input("Escolha o primeiro tipo de recheio: "))
recheio_2 = int(input("Escolha o segundo tipo de recheio (ou 0 se não quiser): "))

print("Adicionais disponíveis:")
print("1 - KitKat (R$4.67)")
print("2 - MM'S (R$5.43)")
adicionais = []
while True:
    opcao = input("Escolha um adicional (ou 0 para sair): ")
    if opcao == "0":
        break
    elif opcao == "1":
        adicionais.append("KitKat")
    elif opcao == "2":
        adicionais.append("MM'S")
    else:
        print("Opção inválida")
       
def calcular_preco(self):
        preco_base = 0
        if self.tamanho == 'pequeno':
            preco_base += 7.80
        elif self.tamanho == 'medio':
            preco_base += 12.90
        elif self.tamanho == 'grande':
            preco_base += 23.95
        
        if self.sabor == 'chocolate_preto':
            preco_base += 9.67
        elif self.sabor == 'chocolate_branco':
            preco_base += 4.50
        elif self.sabor == 'chocolate_ao_leite':
            preco_base += 9.32
        
        if self.recheio1:
            preco_base += 0.5 * preco_base
        if self.recheio2:
            preco_base += 0.5 * preco_base
        
        for adicional in self.adicionais:
            if adicional == 'kitkat':
                preco_base += 4.67
            elif adicional == 'mms':
                preco_base += 5.43
        
        if self.presente:
            preco_base += 2.50
        if self.entrega:
            preco_base += 5.00
        
        preco_total = preco_base * self.quantidade
        
        if self.pagamento == 'cartao':
            preco_total += 3.30
        elif self.pagamento == 'dinheiro' or self.pagamento == 'pix':
            preco_total -= 0.1 * preco_total
        
        return preco_total
