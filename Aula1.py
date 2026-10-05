""""
num = int(input("Digite sua idade:"))
print("Eu tenho", num, "anos")
"""
"""""
x=int(input("Digite o primeiro valor:"))
y=int(input("Digite o segundo valor:"))

print ("A soma de", x, "+", y, "é", x+y)
print ("A subtração de", x, "-", y, "é", x-y)
print ("A multiplicação de", x, "*", y, "é", x*y)
print ("A divisão de", x, "/", y, "é", x/y)
"""
""""
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Voce já pode dirigir")

else:
    print("Voce não pode dirigir")
"""

# comparando qual o maior número entre doi números inseridos e exibir na tela
""""
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 >= num2:
    print("O maior número é", num1)

else:
    print ("O maior número é", num2)

"""
"""
idade = int(input("Digite sua idade: "))
if idade >=20:
    if idade <=60:
        print("Idade entre 20 e 60 anos")
    else:
        print("A idade não está entre 20 e 60")

else:
    print("A idade não está entre 20 e 60")
"""

# elif é indicado para comparação de vários condições do if
"""
semana = int(input("Digite um numero qualquer: "))

if semana == 1:
    print("Domingo")
elif semana == 2:
    print("Segunda")
elif semana == 3:
    print("Terça")
elif semana == 4:
    print("Quarta")
elif semana == 5:
    print("Quinta")
elif semana == 6:
    print("Sexta")
elif semana == 7:
    print("Sábado")

else:
    print("Número inválido")
    """
"""
n = 10
cont = 0

while cont < n:
    print(cont)
    cont = cont + 1
"""

# Confirguração do range, primeiro parÂmetro é a inicialização, o segundo o final (até onde ele vai) e o terceiro o intervalo da execução.
"""
n = 10
cont = 0

for cont in range(n):
    print(cont)
"""

"""
for i in range(2, 16, 2):
    print(i)

"""

"""
for i in range(20, -1, -2):
    print(i)
"""
# Condições and e or, quando todas as condições forem verdadeiras usar o and e uma delas esjam satisfastórias usar o or.
"""""
idade = 70
if idade >= 20 and idade <= 60:
    print("idade de 20 a 60 anos")

else:
    print("idade não está entre 20 e 60 anos")
"""

"""

idade = 18
if idade >= 20 or idade <= 60:
    print("idade maior que 20 anos")

else:
    print("idade não está entre 20 e 60 anos")
"""

"""
import math


x = math.cos(3)
print(x)

z = math.tan(2)
print(z)


print (math.pow(2, 2))

print (math.sqrt(4))
"""
""""
import random
"""

""""
for i in range(10): #percorrer 10 vezes, trabalhando valores de 1 a 6 randômicos.
    x = random.randrange(1, 7)
    print (x)
    """

""""
for i in range(10):
    x = random.randrange(1, 7, 2)
    print (x)
    """
""""
for i in range(10):
    x = random.randint(1, 7) #randint para aparecer o número 7 também
    print (x)
    """
"""cesta = ["Banana", "Maça", "Laranja", ["Uva", "Pera"]]

# for i in range(3):
print(cesta[3][0])

print(len(cesta))
"""
