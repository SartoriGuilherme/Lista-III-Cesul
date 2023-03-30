qtade = int(input('Informe a quantidade comprada: '))
ValorUnit = float(input('Informe o valor unitário: '))
desconto = float(input('Informe o desconto: '))

ValorComDesconto = qtade * ValorUnit * (1 - desconto/100)

print(f'O total com desconto será R$ {ValorComDesconto:.2f}')

