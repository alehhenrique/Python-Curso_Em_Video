dias=int(input('Quantos dias o veículo foi usado? '))
km=float(input('Quantos km foram rodadas no veículo? '))
print('O valor final do aluguel com base que são R$ 60,00 por dia usado e R$ 00.15 por km rodado, o valor do aluguel é {:.2f} reais'.format((dias*60)+(km*0.15)))
