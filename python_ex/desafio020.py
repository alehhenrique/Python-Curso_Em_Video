import random
qntd_alunos=int(input('Quantidade de alunos: '))
nomes =[]
for alunos in range(0, qntd_alunos):
    nome=input('Qual o nome do aluno? ')
    nomes.append(nome)
print(random.shuffle(nomes))
