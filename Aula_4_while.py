'''
ct = 0 # Valor inicial da variável
soma = 0
print('Digite [-1] para sair')
while True: # Laço de repetição, repete enquanto condição verdadeira
    numero = int(input('Digite um número: ')) # Indentação obrigatória
    if numero == -1:
        break # Sai de uma estrutura de repetição (while)
    ct = ct + 1 # ct += 1 (contador), incremento o ct
    soma = soma + numero  # soma += numero
    # Fim da estrutura de repetição de repetição "while"
print('Quantidade de números:', ct)
print('A soma dos números é: ', soma)
'''

'''ct = 0
soma = 0
print('Digie [-1] para sair')
while True:
    nota = float(input('Digite um número: '))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
    # Fim while
media = soma/ct
print('Quantidade de alunos:', ct)
print('A soma das notas do alunos é:', soma)
print(f"A média da turma é = {media:.2f}")
# string formatada em alternativa a /* print("A média da turma é:", media */
'''
ct = 0
soma = 0
print('Digite [-1] para sair')
while True:
    nota = float(input('Digite um número: '))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
    # Fim while
media = soma/ct
print('Quantidade de alunos:', ct)
print(f"A média da turma de {ct} alunos é {media:.2f}")
# ou, colocar isso em vez do print acima.
# print('A soma das notas do alunos é:', soma, end = " ")
# print(f"e a média da turma é = {media:.2f}")
