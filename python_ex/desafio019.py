import random
qntd_alunos=int(input('Quantidade de alunos: '))
nomes=[]
for alunos in range(0, qntd_alunos):
    nome=(input('Digite o nome do aluno: '))
    nomes.append(nome)
print('O aluno sorteado é {}'.format(random.choice(nomes)))