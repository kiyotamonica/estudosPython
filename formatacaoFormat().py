# Basicamente, para se usar o format(), é preciso chamar o método, passar os argumentos
# e utilizar o par de chaves no local desejado
# para delimitar casas decimais é só utilizar o :.(casas decimais)f dentro das chaves

a = 'Olá,'
b = 'Mundo'
c = ':)'

stringFormatada = '{} {} {}'.format(a,b,c)
print(stringFormatada)

# Pode ser feito mais diretamente também:
print('{} {} {}'.format(a,b,c))