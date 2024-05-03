#Há uma forma de se formatar strings utilizando f-strings
variavel = 'Emerson'
print(f'{variavel}')
print(f'{variavel: >10}') #Permite que todo o espaço mostrado da string seja de até 10 espaços. > indica que caso a string nao preencha
print(f'{variavel: <10}') #todo o espaço, a string será preenchida à direita. < preenchida a esquerda. ^ a variavel ficará ao centro
print(f'{variavel: ^10}') #e o preenchimento será dividido entre esquerda e direita.