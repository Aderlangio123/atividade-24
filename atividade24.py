# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

soma = 0
contagem = 0

while True:
    numero = float(input("Digite um número (-1 para sair): "))
    
    if numero == -1:
        break
    
    soma = soma + numero
    contagem = contagem + 1

if contagem > 0:
    media = soma / contagem
    print(f"A média dos números digitados é: {media}")
