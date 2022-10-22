print('Olá, prof! Meu nome é Mia, e eu vim te ajudar a organizar e analisar as notas dos seus alunos!')
num_alunos = int(input('Primeiro, preciso saber: Quantos alunos têm na sala? '))
lista_alunos = {}
    #if num_alunos not in int:
    #    print('Por favor, digite sua resposta utilizando apenas algarismos.')
    #    num_alunos = int(input('Primeiro, preciso saber: Quantos alunos têm na sala? '))
    #else:
print('Ótimo! Agora, pode digitar as notas de cada aluno.')
for i in range(num_alunos):
    nome = str(input('Nome do aluno: '))
    notas = float(input(f'Nota do aluno: '))
    lista_alunos[nome] = notas

for aluno, nota in lista_alunos.items():
    media = sum(lista_alunos.values())/len(lista_alunos)
    print(f'{aluno} tirou {nota}')
print(f'A média das notas é {media}')
    #lista_alunos.sort()
    #quantidade_notas = len(lista_alunos)
     #if quantidade_notas % 2 == 0:
        #mediana1 = lista_alunos[quantidade_notas // 2]
        #mediana2 = lista_alunos[quantidade_notas // 2 - 1]
        #mediana = (mediana1 + mediana2) / 2
    #else:
        #mediana = lista_alunos[quantidade_notas // 2]
    #print(mediana)





