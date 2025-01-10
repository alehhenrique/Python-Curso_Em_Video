import random 
qntd_alunos=int(input('Quantidade de alunos: '))
nomes=[]
for alunos in range(0, qntd_alunos):
    nome=str(input('Digite o nome do aluno: '))
    nomes.append(nome)
random.shuffle(nomes)
print('A ordem dos trabalhos será: {}'.format(nomes))
