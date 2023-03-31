ct = 0 # Contador
soma = 0
# ou ct = soma = 0
print('Digite [0] para sair')
while True:           # While valor != 0:
    valor = int(input('Digite um número: '))
    if valor == 0:    # Valor igual (==) a 0 é a condição de saída
        break         # O break força a saída da estrutura de repetição (while)
    resto = valor % 2 # O operador % pega o resto da divisão
    if resto == 0:    # Se o resto é zero o valor é par
        soma = soma + valor # soma += valor #incrementa a soma de valores
        ct = ct + 1    # ct+= 1 # incrementa a contagem de notas
    # Fim da estrutura de repetição "while"
if ct != 0:
    media = soma/ct
    print("A média de todos os pares é:", media)
else:
    print('Não foi digitado um número par.')
