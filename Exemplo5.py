def calcular_media_alunos(alunos):
    soma_notas = 0
    qtd_alunos = len(alunos)

    for aluno in alunos:
        nome = aluno["nome"]
        nota = aluno["nota"]
        soma_notas += nota
        print(f"Nome:{nome}, Nota: {nota}")

    media = soma_notas/qtd_alunos
    return media #fim da função

alunos = [
    {"nome": "Alice", "nota": 8},
    {"nome": "Bob", "nota": 7},
    {"nome": "Carol", "nota": 9},
    {"nome": "David", "nota": 6}
]

    #Chamando a função para clacular a média das notas da turma
media_notas = calcular_media_alunos(alunos)
print(f"Média da turma: {media_notas}")
