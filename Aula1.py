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


"""
lista = []
num = int(input("Digite um valor: "))

while num != -1:
    lista.append(num)  # append vai adicionar o numero na lista*
    num = int(input("Digite um valor: "))

elemento = int(input("Qual o valor a ser procurado: "))

cont = 0

for i in range(len(lista)):  # len percorre em todos os itens da lista
    if lista[i] == elemento:
        cont += 1

print("O elemento %i aparece %i vezes na sequencia." % (elemento, cont))
"""


"""
# Inserido 4 notas de 6 alunos, e calculado a o número de médias maior que 6 usando o vetor.
alunos = 6
medias = []

for i in range(1, alunos + 1):  # começará com 1 aluno e vai até 8 com o +1.
    notas = 0
    for j in range(1, 5):
        notas += float(input("Digite a nota %i de 4 notas do aluno %i de %i: " %
                       (j, i, alunos)))
    notas /= 4
    medias.append(notas)

num = 0

for media in medias:  # a variável media é o resultado da média de cada aluno.
    if media >= 6:
        num += 1

print("O número de alunos com media maior que 6 é", num)
"""

"""
# Exibindo números de elementos de uma lista sem repetição.

n = int(input("Digite o numero de elementos da lista: "))

lista = []
aux = []

for i in range(n):
    elemento = int(input("Digite o elemnto %i de %i: " % (i + 1, n)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux:
    aparicoes = lista.count(ele)
    for i in range(aparicoes-1): # -1 remove a aparições do número repetido.
        lista.remove(ele)

print(lista)
"""

"""
# Síntaxe de funções


def soma(*lista):  # múltiplos parâmetros
    soma_num = 0
    print(lista)

    for num in lista:
        soma_num += num
    return soma_num


a = (1, 2, 3, 4)
# O operador * desempacota os valores de a na função, sendo assim mantém a variavel e ainda imprime o resultado.
print(soma(*a))
"""

"""
#Sistema bancário: criar conta ou fechar programa.

contas[]
depositos[]

def main():
    opcao = bool(
        int(input("Deseja acessar ou criar uma conta(1) senão fechar o programa (0)")))
    while opcao:
        criarConta()
        acessarSaldo()
        opcao = bool(
            int(input("Deseja acessar ou criar uma conta(1) senão fechar o programa (0)")))

def criarConta ():
    global contas,depositos,saldo
    num_conta = int(input("Digite o número da conta:"))

    while num_conta in contas:
        print ("Conta já existente, DIgite novamente.")
        num_conta = int(input("Digite o número da conta:"))

    contas.append(num_conta)
    deposito = float(input("Digite o valor do primeiro deposito:"))
    while deposito <= 0:
        print("Valor do deposito inválido")
        deposito = float(input("Digite o valor do primeiro deposito:"))
    depositos.append(deposito)
    saldo += deposito

def acessarSaldo():
    global saldo
    opcao = bool(
        int(input("Deseja acessar o saldo do banco (1 - Sim / 0 - Não: ")))
    if opcao:
        print("Osaldo da conta é R$", saldo)

main()

"""


"""
# função que produza a sma dos primeiros n números de uma lista com tamanho m


def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista: "))

    for i in range(m):
        ele = float(input("Digite o elemento %i de %i: " % (i+1, m)))
        lista.append(ele)

    return lista


def main():
    l1 = criaLista()

    n = int(input("Digite o número de elementos que se deseja somar: "))

    soma = 0
    for i in range(1, len(l1)+1):  # contagem da lista começar por 1 em vez de 0
        if i > n:
            break
        soma += l1[i-1]  # atinge a posição correta da lista

    print("A soma é", soma)


main()
"""


"""
tamanho_max = 26


def recebeModo():

 #Função que pergunta se o usuário quer criptografar ou decriptografar e garante que uma entrada válida foi recebida

    while True:
        modo = input("Você deseja criptograr ou decriptografar? \n").lower()
        if modo in 'criptografar c decriptografar d'.split():
            return modo
        else:
            print("Entre 'criptografar' ou 'c' ou 'decriptografar' ou 'd'.")


def recebeChave():

    #Função que pede o valor da chave para o usuário e devolve a chave caso o valor desta esteja adequado

    global tamanho_max
    chave = 0

    while True:
        chave = int(input('Entre com o número da chave (1-%s)' %
                    (tamanho_max)))
        if 1 <= chave <= tamanho_max:
            return chave


def geraMsgTraduzida(modo, mensagem, chave):

    #Traduz a mensagem do usuário de modo conveniente

    if modo[0] == 'd':
        chave *= -1
    traduzido = ''
    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduzido += chr(num)
        else:
            traduzido += simbolo

    return traduzido


def main():

    #Função principal do programa

    modo = recebeModo()
    mensagem = input("Entre com sua mensagem \n")
    chave = recebeChave()
    print("Seu texto traduzido é: ")
    print(geraMsgTraduzida(modo, mensagem, chave))


main()
"""
