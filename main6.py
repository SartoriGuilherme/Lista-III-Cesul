qtade = int(input('Informe a quantidade comprada: '))
ValorUnit = float(input('Informe o valor unitário: '))
desconto = float(input('Informe o desconto: '))

totalSemDesconto = qtade * ValorUnit
ValorDesconto = totalSemDesconto * desconto/100
ValorComDesconto = totalSemDesconto - ValorDesconto

print(f'O total sem desconto será R$ {totalSemDesconto:.2f}')
print(f'O total do desconto será R$ {ValorDesconto:.2f}')
print(f'O total com desconto será R$ {ValorComDesconto:.2f}')
