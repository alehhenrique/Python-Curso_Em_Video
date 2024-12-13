l=float(input('Qual a largura da parede? '))
a=float(input('Qual a altura da parede? '))
area=l*a
print('A parede tem {} de largura e {} de altura, com isso, sua área é de {} m²'.format(l, a, area))
tinta=area/2
print('Será necessário {} litros de tinta para cobrir toda a área da parede'.format(tinta))
