duplicata = float(input('Informe o preço da duplicata: '))
diasDeAtraso = int(input('Informe o número de dias de atraso: '))

ValorComMulta = duplicata + diasDeAtraso * 0.05 + 5

print(f'O preço da duplicata com multa é{ValorComMulta:.2f}')