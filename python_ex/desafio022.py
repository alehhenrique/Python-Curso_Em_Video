nome_completo=str(input('Qual seu nome completo? '))
print('Seu nome todo maiúsculo: {}'.format(nome_completo.upper()))
print('Seu nome todo minúsculo: {}'.format(nome_completo.lower()))
print(len(nome_completo.strip().replace(" ", '')))
print(len(nome_completo.split()[0]))
