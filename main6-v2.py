qtade = int(input('Informe a quantidade comprada: '))
ValorUnit = float(input('Informe o valor unitário: '))
desconto = float(input('Informe o desconto: '))

totalSemDesconto = qtade * ValorUnit
ValorComDesconto = totalSemDesconto - (totalSemDesconto * desconto/100)

print(f'O total sem desconto será R$ {totalSemDesconto:.2f}')
print(f'O total com desconto será R$ {ValorComDesconto:.2f}')

