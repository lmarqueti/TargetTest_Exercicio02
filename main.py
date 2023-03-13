'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e
retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''
# Input do usuário
num = int(input("Digite um número: "))

# variáveis que vão armazenar os dois primeiros números
num1 = 0
num2 = 1

# Verifica se o número pertence ou não à sequência
pertence = False

# Verifica se o número é igual a um dos dois primeiros números
if num == num1 or num == num2:
    pertence = True

# Verifica se ele é um dos próximos números da sequência
else:
    while num2 < num:
        proximo = num1 + num2
        if proximo == num:
            pertence = True
            break
        else:
            num1 = num2
            num2 = proximo

# Print resultado
if pertence:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")

