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
print('Quantidade de números digitados:', ct)
print('A soma dos números digitados é: ', soma)
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
# Um aluno realizou respectivamente uma prova. Digite a notas dos respectivos alunos.
ct = 0
soma = 0
print('Digite [-1] para sair')
while True:
    nota = float(input('Digite a nota: '))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
    # Fim while
media = soma/ct
print('Quantidade de alunos:', ct)
print(f'A média da turma de {ct} alunos é {media:.2f}')
# ou, colocar isso em vez do print acima.
# print('A soma das notas do alunos é:', soma, end = " ")
# print(f"e a média da turma é = {media:.2f}")
--
(editar e arrumar erro)
ct_masc = 0
ct_fem = 0
variavel_maior = -99999999
variavel_menor = 999999
print('Digite [0] para sair')
while True:
    altura = float(input('Digite a altura: '))
    if altura == 0: # testa condição saída
        break
    genero = input('Digite [m] para Masculino ou [f] para Feminino: ') # Lê gênero, quando for digitar uma letra, ele já assume que é str, mas posso por str ou deixar em branco.
    if genero == 'm': # Pra comparar eu uso as aspas, por isso m está entre aspas. lê: se gênero é masculino
        ct_masc = ct_masc + 1 # ct_mas += 1
    else:
        ct_fem = ct_fem + 1
    if altura > maior:
        maior = altura # atualiza a maior altura
    if altura < menor:  # não pode usar else
        menor = altura  # Fim da estrutura de rep. while
print('Maior altura no grupo:', maior) # print(f'Maior altura no grupo: {maior:.2f}')
print('Menor altura no grupo:', menor) # print('Menor altura: {:.2f}' .format(menor))
print('Quantidade de homens:', ct_masc)
print('Quantidade de mulheres:', ct_fem)
