primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
maior_valor = 0

if primeiro_valor > segundo_valor:
    maior_valor = primeiro_valor
    print('Maior valor: {}'.format(maior_valor))
elif segundo_valor > primeiro_valor:
    maior_valor = segundo_valor
    print('Maior valor: {}'.format(maior_valor))
else:
    print('Os valores são iguais')