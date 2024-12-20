from math import hypot
oposto=float(input('Digite o comprimento do cateto oposto: '))
adjacente=float(input('Digite o comprimento do cateto adjacente?: '))
print('O valor da hipotenusa é {:.2f}'.format(hypot(oposto, adjacente)))