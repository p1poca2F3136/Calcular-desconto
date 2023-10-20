preco = float(input("Qual é o preço do produto? R$"))

desconto = float(input('Qual é a porcentagem de desconto? %'))

novo_preco = preco - (preco * desconto / 100)

print("O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}".format(preco, desconto, novo_preco))

#20/10/2023