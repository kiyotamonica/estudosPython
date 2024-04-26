# Basicamente, ao colocar um 'f' antes da string, isso permite com que possamos utilizar variáveis dentro da string.
# Para formatar casas decimais, é só utilizar :.(numero de casas)f 

nome = 'Noah'
altura = 0.78
peso = 11
imc = peso / (altura ** 2)
print(f'{nome} tem {altura:.2f}m de altura.')
print('IMC - sem a formatação f-string:', imc)
print(f'IMC - com a formatação f-string: {imc:.2f}')

# A f-string pode ser usada fora do print também:
linha_1 = f'O {nome} tem {altura} de altura, e pesa {peso} kilos !'
print(linha_1)
