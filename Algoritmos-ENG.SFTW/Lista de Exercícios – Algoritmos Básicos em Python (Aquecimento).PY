""" """ 
# Lista de Exercícios – Algoritmos Básicos em Python (Aquecimento) 

# 1. Escreva um programa que mostre 'Olá, Mundo!' na tela. 

print("Olá, mundo!")

# 2. Leia um número inteiro e mostre seu sucessor e antecessor. 

numero = int(input(("Digite o numero int:")))
print(f"O sucessor: {numero} é {numero + 1} e o antecessor é: {numero - 1}")

# 3. Leia dois números e mostre a soma entre eles. 

numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o numero 2:"))
print(f"a soma entre eles é: {numero1 + numero2}")

# 4. Faça um programa que calcule a média de três notas. 

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
media = (nota1 + nota2 + nota3) / 3
print(f"A medias das 3 notas são: {media}")

# 5. Converta metros para centímetros. 

metros = float(input("Digite a metragem:"))
centimetros = metros * 100
print(f"{metros} A metragem é igual a: {centimetros} cm")
# 6. Leia um número e mostre sua tabuada. 

numero = int(input("Digite o numero para mostrar a tabuada:"))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7. Converta graus Celsius para Fahrenheit. 

grau_celsius = float(input("Digite os graus Celsius::"))
grau_fahrenheit = (grau_celsius * 9/5) +32
print(f"{grau_celsius}ºC é igual a {grau_fahrenheit}ºF")

# 8. Calcule a área de um retângulo. 
retangulo_base = float(input("Digite a base do retângulo:"))
retangulo_altura = float(input("Digite a altura do retângulo:"))
area_retangulo = retangulo_base * retangulo_altura
print(f"A área do retângulo é: {area_retangulo} cm²")

# 9. Leia um número e verifique se é par ou ímpar. 

numero_Qualquer = int(input("Digite um numero, ele é par ou impar?"))
if numero_Qualquer % 2 == 0:
    print(f"O numero {numero_Qualquer} é par.")
else:
    print(f"O numero {numero_Qualquer} é impar.")

# 10. Leia um número e verifique se é positivo, negativo ou zero. 
numero_Qualquer = int(input("Digite um numero, ele é positivo, negativo ou zero?"))
if numero_Qualquer > 0:
    print(f"O numero {numero_Qualquer} é positivo.")
elif numero_Qualquer < 0:
    print(f"O numero {numero_Qualquer} é negativo.")
else:
    print(f"O numero {numero_Qualquer} é zero.")


# 11. Faça um programa que calcule o IMC. 
QuilosMortais = float(input("Digite seu peso em kg:"))
AlturaMortais = float(input("Digite sua altura em metros:"))
imc = QuilosMortais / (AlturaMortais ** 2)
print(f"Seu IMC é: {imc:.2f}")

# 12. Leia três números e mostre o maior deles. 
numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
numero3 = float(input("Digite o terceiro numero:"))

if numero1 > numero2 and numero1 > numero3:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O maior número é: {numero2}")
else:
    print(f"O maior número é: {numero3}")

# 13. Verifique se um número é múltiplo de 3. 
numero = int(input("Digite um numero para verificar se é múltiplo de 3:"))
if numero % 3 == 0:
    print(f"O numero {numero} é múltiplo de 3.")

# 14. Calcule o fatorial de um número. 

numero = int(input("Digite um numero para calcular o fatorial:"))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i  
print(f"O fatorial de {numero} é: {fatorial}")


# 15. Gere os 10 primeiros números da sequência de Fibonacci. 
n1, n2 = 0, 1
print("Sequência de Fibonacci:")

# 16. Conte de 1 a 100 usando um laço de repetição. 
for i in range(1, 101):
    print(i)    

# 17. Some todos os números de 1 até N. 
n = int(input("Digite o valor de N:"))
soma = 0
for i in range(1, n + 1):
    soma += i
print(f"A soma dos números de 1 até {n} é: {soma}")

# 18. Leia números até que o usuário digite 0 e mostre a soma. 

soma = 0
while True:
    numero = int(input("Digite um numero (0 para parar):"))
    if numero == 0:
        break
    soma += numero 
print(f"A soma dos números digitados é: {soma}")

# 19. Conte quantos números pares existem entre 1 e 50. 
contador_pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        contador_pares += 1
print(f"Existem {contador_pares} números pares entre 1 e 50.")


# 20. Inverta um número inteiro (ex: 123 -> 321). 
numero = int(input("Digite um numero inteiro para inverter:"))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = (numero_invertido * 10) + digito
    numero //= 10
print(f"O número invertido é: {numero_invertido}")

# 21. Verifique se uma palavra é um palíndromo. 

palavra = input("Digite uma palavra para verificar se é um palíndromo:")
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:    print(f"A palavra '{palavra}' não é um palíndromo.")

# 22. Conte o número de vogais em uma string. 
string = input("Digite uma string para contar as vogais:")
contador_vogais = 0
for char in string:
    if char.lower() in 'aeiou':
        contador_vogais += 1
print(f"A string '{string}' contém {contador_vogais} vogais.")

# 23. Substitua espaços por hífens em uma frase. 
frase = input("Digite uma frase para substituir os espaços por hífens:")
frase_modificada = frase.replace(" ", "-")
print(f"A frase modificada é: {frase_modificada}")


# 24. Leia uma lista de números e mostre o maior e o menor. 
numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
maior = max(numeros)
menor = min(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# 25. Ordene uma lista de números. 
numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
numeros_ordenados = sorted(numeros)
print(f"A lista ordenada é: {numeros_ordenados}")



# 26. Remova elementos duplicados de uma lista. 
numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
numeros_unicos = list(set(numeros))
print(f"A lista sem elementos duplicados é: {numeros_unicos}")


# 27. Some todos os elementos de uma lista. 
numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
soma = sum(numeros)
print(f"A soma dos elementos da lista é: {soma}")


# 28. Conte quantas vezes um número aparece em uma lista. 
numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
numero_para_contar = float(input("Digite um número para contar quantas vezes aparece na lista:"))
contador = numeros.count(numero_para_contar)
print(f"O número {numero_para_contar} aparece {contador} vezes na lista.")



# 29. Crie um dicionário com nome e idade e exiba os dados. 
fulano = {}
fulano['nome'] = input("Digite o nome da pessoa:")
fulano['idade'] = int(input("Digite a idade da pessoa:"))
print(f"Nome: {fulano['nome']}, Idade: {fulano['idade']}")

# 30. Atualize um valor dentro de um dicionário. 

dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
print("Dicionário original:", dicionario)

# 31. Crie uma função que receba dois números e retorne a soma.
def soma(a, b):
    return a + b
num1 = float(input("Digite o primeiro numero para somar:"))
num2 = float(input("Digite o segundo numero para somar:"))
resultado = soma(num1, num2)
print(f"A soma de {num1} e {num2} é: {resultado}")



# 32. Crie uma função que verifique se um número é primo. 
def oi_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
num = int(input("Digite um numero para verificar se é primo:"))
if oi_primo(num):
    print(f"O numero {num} é primo.")
else:    print(f"O numero {num} não é primo.")



# 33. Use uma função para calcular a área de um círculo. 

def area_circulo(raio):
    import math
    return math.pi * (raio ** 2) 
raio = float(input("Digite o raio do círculo para calcular a área:"))
area = area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area:.2f}")


# 34. Crie uma função recursiva para calcular o fatorial. 
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
numero = int(input("Digite um numero para calcular o fatorial usando recursão:"))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")


# 35. Gere uma lista com os quadrados dos números de 1 a 10.
lista_quadrados = [x**2 for x in range(1, 11)]
print(f"A lista dos quadrados dos números de 1 a 10 é: {lista_quadrados}")


# 36. Utilize list comprehension para filtrar números pares. 

numeros = input("Digite uma lista de números separados por espaço:").split()
numeros = [float(num) for num in numeros]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(f"A lista dos números pares é: {numeros_pares}")


# 37. Leia um arquivo texto e conte o número de linhas. 

texto_arquivo = input("Digite o nome do arquivo para contar as linhas:")

try:
    with open(texto_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        print(f"O número de linhas no arquivo é: {len(linhas)}")
except FileNotFoundError:
    print("Arquivo não encontrado.")

# 38. Escreva dados em um arquivo texto. 

dados = input("Digite os dados para escrever no arquivo:")
texto_arquivo = input("Digite o nome do arquivo para salvar os dados:")

try:
    with open(texto_arquivo, 'w') as arquivo:
        arquivo.write(dados)
    print(f"Dados escritos com sucesso no arquivo {texto_arquivo}")
except Exception as e:
    print(f"Erro ao escrever no arquivo: {e}")

# 39. Crie um menu interativo simples usando while. 
while True:
    print("\nMenu:")
    print("1. opção 1")
    print("2. opção 2")
    print("3. Sair")
    
    escolha = input("Digite sua escolha (1, 2 ou 3):")
    
    if escolha == '1':
        print("Você escolheu a Opção 1.")
    elif escolha == '2':
        print("Você escolheu a Opção 2.")
    elif escolha == '3':
        print("Saindo do menu. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")


# 40. Trate erro de divisão por zero. Dica: Pesquise o uso do try/except.
try:
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
