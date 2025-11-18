Evandro Marcos

 teste
n = input("Digite seu nome: ")
print(f"Olá! {n}")

1ª lista de  Exercício. s.

   Exercício. 1 

  resposta: Um algoritmo é um passo a passo que orienta o computador sobre o que fazer, Ele é essencial no desenvolvimento de software, pois faz o programa funcionar de forma correta e eficiente.   type: ignore

  Exercício.  2

print("hello programming world")

  Exercício.  3 

n1=float(input("digite o primeiro numero: "))
n2=float(input("digite o segundo numero: "))
media= (n1+n2) / 2
print (media)

  Exercício.  4 

num_int= 4
num_real= 4.67
is_true= True
letter= 'L'

print("integer", num_int)
print("real", num_real)
print("boolean", is_true)
print("character", letter)

  Exercício.  5

num1=float(input("digite um numero: "))
num2=float(input("digite um numero: "))

soma= num1+num2
sub= num1-num2
mult= num1*num2
div=num1/num2
if  num2 !=0 :
    print ("Divisão", div)
else:
   print ("não é possivel dividir por zero")
print("Soma", soma)
print("Subtração", sub)
print("multiplicação", mult)

  Exercício.  6

pi= 3.14159
raio= float(input("digite o raio do circulo"))
area= pi*raio**2
print("A area do circulo é:", area)

  Exercício.  7 

pv1=float(input("digite a nota da primeira prova: "))
pv2=float(input("diigite a nota da segunda prova: "))
mediaf= (pv1+pv2)/2
print ("a media das suas provas é:", mediaf)

  Exercício.  8

h= int(input("digite as horas de viagem(somente horas, digite os minutos abaixo): "))
min= int(input("digite os minutos de viagem: "))
velo_media=float(input("digite a velocidade media em km/h: "))

temp= h + min /60
dist= temp * velo_media
cons= dist/12
print("voce percorreu", dist, "km")
print("durante o percurso o consumo foi de", cons, "litros de combustível")

  Exercício.  9

nb=int(input("digite um numero: "))
if nb >0 :
    print ("O numero: ", nb, "é positivo")
elif nb == 0:
    print("esse é o numero zero:", nb)
else:   
    print("Esse numero: ", nb, "é negativo")


  Exercício.  10

nt1=float(input("digite sua primeira nota: "))
nt2=float(input("digite a sua segunda nota: "))
mediaN= (nt1+nt2)/2
if mediaN <=5.9:
    print("voce foi reprovado com media: ", mediaN)
else:
    print("voce foi aprovado com media:", mediaN, "Parabens!!")

  Exercício.  11

a=float(input("digite um numero: "))
b=float(input("digite um numero: "))
c=float(input("digite um numero: "))
if a> b and a> c:
    print("O maior desses numeros é: ", a)
elif b> a and b> c :
    print("O maior desses numeros é: ", b)
elif c> a and c> b:
    print("O maior desses numeros é: ", c)
else:
    print("Os numeros são iguais")

  Exercício.  12

sal= int(input("digite o seu salario e descubra o seu aumento: "))
sal15= sal* (15/100)
ns1= sal+sal15
sal10= sal*(10/100)
ns2= sal+sal10
if sal<=1500:
    print("seu aumento foi de: ", sal15, "e seu salrio atual é: ", ns1)
else:
    print("seu aumento foi de: ", sal10, "seu salario atual é: ", ns2)

  Exercício.  13

L= 1
while L <= 10:
    print(L)
    L += 1

  Exercício.  14

soma1= 0
for E in range(10):
    nume=float(input(f"digite o {E + 1} numero: " ))
    soma1 += nume
media1= soma1/10
print("a media desses numeros é: ", media1)

  Exercício.  15

numtab= int(input("Digite um número para ver sua tabuada : "))

print(f"Tabuada do {numtab}:")

for B in range(1, 11):
    print(f"{numtab} x {B} = {numtab * B}")

 E Exercício.  16
NumRev=[]
for d in range (5):
    numm= float(input(f"digite os numeros dejados {d+1}: "))
    NumRev.append(numm)
print("essa é a ordem inversa dos numeros")
for numm in reversed(NumRev):
    print (numm)

 E Exercício.  17

soma=0
for t in range(5):
    notas=float(input(f"digite a nota do aluno {t+1}: "))
    soma+= notas
MedGrupo= soma /5
print("A media desses cinco alunos é: ", MedGrupo)

 E Exercício.  18

pp=float(input("escreva um numero: "))
if pp % 2==0:
    print("esse numero é par: ", pp)
elif pp==0:
    print("esse é o numero zero", pp)
else:
    print("esse numero ", pp, "é impar")

 E Exercício.  19

ç=float(input("escreva o primeiro numero: "))
çl=float(input("escolha o segundo numero: "))
if ç<çl:
    print("o maior desses numeros é o: ", çl)
elif ç == çl:
    print("os numeros inseridos são iguais")
else:
    print("o maior desses numeros é o: ", ç)
 
 E Exercício.  20

p= int(input("digite o numero desejado: "))
if p <= 1:
  print("O numero ", p, "nao é primo")
else:
    primo = True
    for i in range(2, p):
        if p % i == 0:
            primo = False
            break
            print("o numero", p,"nao é primo")
          
if primo: print("o numero", p, "é primo")
else: print("o numero nao é primo")

2ª Lista de  Exercício. .

  Exercício.  1

 Resposta:O algoritmo começa pedindo que o usuário digite dois números.
 Em seguida, ele compara os dois valores.
 Se o primeiro número for maior que o segundo, o programa mostra que o primeiro é o maior.
 Caso contrário, mostra que o segundo é o maior.
 Por fim, o programa termina.
    ┌────────────┐
    │   Início   │
    └──────┬─────┘
           │
    ┌──────▼─────┐
    │ Ler A, B   │
    └──────┬─────┘
           │
    ┌──────▼───────────────┐
    │ A > B ?              │
    └──────┬──────┬────────┘
           │Sim    │Não
    ┌──────▼─┐   ┌─▼───────┐
    │ Mostrar│   │ Mostrar │
    │ "A"    │   │ "B"     │
    └──────┬─┘   └──┬──────┘
           │        │
           └────┬───┘
                │
          ┌─────▼────┐
          │   Fim    │
          └──────────┘

 css 
     Início
     Leia A, B
     Se A > B então
         Escreva("O maior é A")
     Senão
         Escreva("O maior é B")
     FimSe
 Fim


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))


if a > b:
    print("O maior é:", a)
else:
    print("O maior é:", b)

  Exercício.  2

  Cálculo da fatura de energia elétrica

consumo = float(input("Digite o consumo em kWh: "))

if consumo <= 100:
    tarifa = 0.50
elif consumo <= 200:
    tarifa = 0.70
else:
    tarifa = 0.90

valor_consumo = consumo * tarifa
imposto = valor_consumo * 0.15
total = valor_consumo + imposto

print(f"Consumo: {consumo} kWh")
print(f"Tarifa aplicada: R$ {tarifa:.2f}")
print(f"Valor do consumo: R$ {valor_consumo:.2f}")
print(f"Imposto (15%): R$ {imposto:.2f}")
print(f"Valor total da fatura: R$ {total:.2f}")

Exercício.  3

 Ler a quantidade total de clientes que estão na fila.

 2-Enquanto ainda houver clientes na fila, repita os passos seguintes:
 2.1. Chamar o próximo cliente para atendimento.
 2.2. Realizar o atendimento do cliente.
 2.3. Registrar que o atendimento foi concluído.
 2.4. Reduzir em um o número de clientes que restam na fila.
 2.5. Informar quantos clientes ainda aguardam atendimento.

 3-Quando não houver mais clientes na fila, informar que todos foram atendidos.

  Exercício.  4

peso=float(input("digite seu peso em kilogramas:"))
altura=float(input("digite sua altura em metros"))
imc=peso/altura**2

if imc <= 18.5: print("voce esta abaixo do peso e seu imc é", imc)
elif imc <= 24.9: print("voce esta no peso ideal e seu imc é:", imc)
elif imc <= 29.9: print("voce esta com sobrepeso e seu imc é", imc)
elif imc <= 34.9: print("voce esta com obesidade grau 1 e seu imc é", imc)
elif imc <= 39.9: print("voce esta com obesidade grau 2 e seu imc é", imc)
elif imc >= 40: print("voce esta com obesidade grau 3 e seu imc é", imc)

   Exercício.  5

horasSal = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora (R$): "))

salario_bruto = horasSal * valor_hora
inss = salario_bruto * 0.11
ir = salario_bruto * 0.15
salario_liquido = salario_bruto - (inss + ir)

print("\n===== informaçoes de pagamento =====")
print(f"Horas trabalhadas: {horasSal}")
print(f"Valor da hora: R$ {valor_hora:.2f}")
print("--------------------------------------")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (11%): R$ {inss:.2f}")
print(f"Desconto IR (15%):   R$ {ir:.2f}")
print("--------------------------------------")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
print("=======================================")

   Exercício.  6

z=float(input("digite um numero e descubra a raiz: "))
x= z/2
tole= 0.0001
dif= 1
while dif>tole:
    xn=0.5 * (x + z / x)
    dif= abs(xn-x)
    x=xn

print(f"a raiz quadrada de:", z,"é de aproximadamente", x)

   Exercício.  7

valor = float(input("Digite o valor do produto (R$): "))

print("\nFormas de pagamento:")
print("1 - À vista")
print("2 - Cartão")
print("3 - Parcelado")
pagamento = int(input("Escolha a forma de pagamento (1/2/3): "))

if valor <= 100:
    desconto = 0.05
elif valor <= 500:
    desconto = 0.10
else:
    desconto = 0.15

if pagamento == 1:
    desconto += 0.05
elif pagamento == 3:
    desconto -= 0.05

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print("\n===== RESUMO DA COMPRA =====")
print(f"Valor do produto: R$ {valor:.2f}")
print(f"Desconto aplicado: {desconto*100:.1f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
print("=============================")

   Exercício.  8

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

peso1, peso2, peso3 = 2, 3, 5
media = (n1*peso1 + n2*peso2 + n3*peso3) / (peso1 + peso2 + peso3)

print("\n===== RESULTADO FINAL =====")
print(f"Notas: {n1}, {n2}, {n3}")
print(f"Média ponderada: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
    
   Exercício.  9

a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")

   Exercício.  10

renda = float(input("Digite sua renda mensal (R$): "))

if renda <= 2112:
    imposto = 0
elif renda <= 2826.65:
    imposto = renda * 0.075 - 158.40
elif renda <= 3751.05:
    imposto = renda * 0.15 - 370.40
elif renda <= 4664.68:
    imposto = renda * 0.225 - 651.73
else:
    imposto = renda * 0.275 - 884.96

if imposto < 0:
    imposto = 0

print(f"\nImposto de renda devido: R$ {imposto:.2f}")

   Exercício.  11

n = int(input("Digite um número N: "))

a, b = 0, 1
print("Sequência de Fibonacci:")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b


   Exercício.  12

n = int(input("Digite um número: "))

fat_for = 1
for i in range(1, n + 1):
    fat_for *= i

fat_while = 1
i = 1
while i <= n:
    fat_while *= i
    i += 1

print(f"\nFatorial de {n} (com FOR): {fat_for}")
print(f"Fatorial de {n} (com WHILE): {fat_while}")

   Exercício.  13

positivos = negativos = nulos = 0

while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    elif n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        nulos += 1

print(f"\nPositivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Nulos: {nulos}")

   Exercício.  14

numero = int(input("Digite o número para a tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"\nTabuada do {numero} de {inicio} até {fim}:")

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")

   Exercício.  15

mes = int(input("Digite um número de 1 a 12: "))

if mes == 1:
    nome, dias = "Janeiro", 31
elif mes == 2:
    nome, dias = "Fevereiro", 28
elif mes == 3:
    nome, dias = "Março", 31
elif mes == 4:
    nome, dias = "Abril", 30
elif mes == 5:
    nome, dias = "Maio", 31
elif mes == 6:
    nome, dias = "Junho", 30
elif mes == 7:
    nome, dias = "Julho", 31
elif mes == 8:
    nome, dias = "Agosto", 31
elif mes == 9:
    nome, dias = "Setembro", 30
elif mes == 10:
    nome, dias = "Outubro", 31
elif mes == 11:
    nome, dias = "Novembro", 30
elif mes == 12:
    nome, dias = "Dezembro", 31
else:
    nome, dias = None, None

if nome:
    print(f"\nMês: {nome}\nDias: {dias}")
else:
    print("\nNúmero inválido. Digite um valor entre 1 e 12.")

   Exercício.  16

print("=== Cálculo de Áreas ===")
print("1 - Quadrado")
print("2 - Triângulo")
print("3 - Círculo")
print("4 - Retângulo")

opcao = int(input("Escolha uma opção (1 a 4): "))

match opcao:
    case 1:
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"Área do quadrado: {area:.2f}")
    case 2:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print(f"Área do triângulo: {area:.2f}")
    case 3:
        raio = float(input("Digite o raio do círculo: "))
        area = 3.14159 * raio ** 2
        print(f"Área do círculo: {area:.2f}")
    case 4:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"Área do retângulo: {area:.2f}")
    case _:
        print("Opção inválida.")

   Exercício.  17

soma_pares = soma_impares = cont_pares = cont_impares = 0
maior = menor = None

while True:
    n = int(input("Digite um número (negativo para sair): "))
    if n < 0:
        break

    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

    if n % 2 == 0:
        soma_pares += n
        cont_pares += 1
    else:
        soma_impares += n
        cont_impares += 1

media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
media_impares = soma_impares / cont_impares if cont_impares > 0 else 0

print(f"\nMédia dos pares: {media_pares:.2f}")
print(f"Média dos ímpares: {media_impares:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

   Exercício.  18

a = b = c = nulo = 0

print("1-A | 2-B | 3-C | 0-Nulo | -1-Fim")

while True:
    voto = int(input("Voto: "))
    if voto == -1:
        break
    elif voto == 1:
        a += 1
    elif voto == 2:
        b += 1
    elif voto == 3:
        c += 1
    elif voto == 0:
        nulo += 1

print(f"\nA: {a} | B: {b} | C: {c} | Nulos: {nulo}")

if a > b and a > c:
    print("Vencedor: A")
elif b > a and b > c:
    print("Vencedor: B")
elif c > a and c > b:
    print("Vencedor: C")
else:
    print("Empate")

   Exercício.  19

nums = [int(input(f"Número {i+1}: ")) for i in range(10)]

for i in range(9):
    for j in range(i + 1, 10):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print("\nOrdem crescente:", nums)

   Exercício.  20

nomes = []
medias = []

for i in range(5):
    nomes.append(input(f"Nome do {i+1}º aluno: "))
    notas = [float(input(f"Nota {j+1}: ")) for j in range(3)]
    medias.append(sum(notas) / 3)

print("\n=== MÉDIAS ===")
for i in range(5):
    print(f"{nomes[i]}: {medias[i]:.2f}")

print(f"\nMédia geral: {sum(medias)/5:.2f}")

   Exercício.  21

numeros = [int(input(f"{i+1}º número: ")) for i in range(20)]
impares = [n for n in numeros if n % 2]

print("\nOriginais:", numeros)
print("Ímpares:", impares)

   Exercício.  22

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print(f"MDC de {x} e {y} = {mdc(x, y)}")

   Exercício.  23

def analisar(v):
    return max(v), min(v), sum(v)/len(v)

valores = [float(input(f"Valor {i+1}: ")) for i in range(5)]
maior, menor, media = analisar(valores)

print(f"\nMaior: {maior}\nMenor: {menor}\nMédia: {media:.2f}")

   Exercício.  24

def fatorial(n):
    return 1 if n <= 1 else n * fatorial(n - 1)

n = int(input("Número: "))
print(f"Fatorial de {n} = {fatorial(n)}")

   Exercício.  25

def soma_pares(v):
    return sum(n for n in v if n % 2 == 0)

v = [int(input(f"Número {i+1}: ")) for i in range(5)]
print(f"Soma dos pares: {soma_pares(v)}")

3ª lista de  Exercício. s.

  Exercício. s 1
import random

def coletar_dados(qtd=10):
    return [random.uniform(-10, 60) if random.random() > 0.1 else None for _ in range(qtd)]

def validar(dados, min_val=0, max_val=50):
    return [d if d is not None and min_val <= d <= max_val else None for d in dados]

def limpar(dados):
    media = sum(d for d in dados if d is not None) / sum(1 for d in dados if d is not None)
    return [d if d is not None else media for d in dados]

def armazenar(dados):
    print("Dados armazenados:", dados)

def pipeline_iot():
    dados = coletar_dados()
    dados = validar(dados)
    dados = limpar(dados)
    armazenar(dados)

pipeline_iot()

  Exercício. s 2

import unicodedata

def normalizar_nome(nome):
    nome = ' '.join(nome.split())    remove espaços extras
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode()    remove acentos
    return ' '.join(p.capitalize() for p in nome.lower().split())

print(normalizar_nome("  JOSÉ   dA   silva "))

  Exercício. s 3

def similaridade(n1, n2):
    comuns = sum(1 for c in n1 if c in n2)
    return comuns / max(len(n1), len(n2)) * 100

def consolidar_clientes(clientes):
    unificados = []
    for c in clientes:
        duplicado = False
        for u in unificados:
            if c['nasc'] == u['nasc'] and similaridade(c['nome'], u['nome']) >= 80:
                duplicado = True
                break
        if not duplicado:
            unificados.append(c)
    return unificados

clientes = [{'nome':'Ana Maria','nasc':'2000-01-01'},
            {'nome':'ana   maria ','nasc':'2000-01-01'},
            {'nome':'João','nasc':'1999-02-02'}]

print(consolidar_clientes(clientes))

  Exercício. s 4

def gerar_digito(id_base):
    pesos = [2,3,4,5,6,7,8,9]
    soma = sum(int(d)*pesos[i % 8] for i, d in enumerate(str(id_base)))
    dig = 11 - (soma % 11)
    return 0 if dig > 9 else dig

def gerar_id(id_base):
    return f"{id_base}-{gerar_digito(id_base)}"

print(gerar_id(123456))

  Exercício. s 5

import re

def validar_formulario(email, telefone, cep):
    erros = []
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        erros.append("Email inválido")
    if not re.match(r"^\d{10,11}$", telefone):
        erros.append("Telefone inválido")
    if not re.match(r"^\d{8}$", cep):
        erros.append("CEP inválido")
    print("Erros encontrados:" if erros else "Formulário válido")
    for e in erros: print("-", e)

validar_formulario("teste@", "123", "99999999")

  Exercício. s 6

def previsao_media_movel(vendas):
    medias = [sum(vendas[i-3:i])/3 for i in range(3, len(vendas)+1)]
    return medias[-1]

print(previsao_media_movel([100,120,130,140,160,170]))

  Exercício. s 7

def funil(visitas, leads, vendas):
    etapas = [visitas, leads, vendas]
    taxas = [etapas[i+1]/etapas[i]*100 for i in range(2)]
    perdas = [100 - t for t in taxas]
    pior = perdas.index(max(perdas))
    print(f"Perda maior entre etapa {pior+1} e {pior+2}: {perdas[pior]:.2f}%")

funil(1000, 300, 60)

  Exercício. s 8

import datetime

def dias_letivos(inicio, fim, feriados):
    di = datetime.datetime.strptime(inicio, "%d/%m/%Y")
    df = datetime.datetime.strptime(fim, "%d/%m/%Y")
    dias = 0
    feriados = set(feriados)
    while di <= df:
        if di.weekday() < 5 and di.strftime("%d/%m") not in feriados:
            dias += 1
        di += datetime.timedelta(days=1)
    return dias

print(dias_letivos("01/11/2025", "30/11/2025", ["15/11"]))

  Exercício. s 9

def boletim_medidores(medidores):
    consumos = [m['atual'] - m['anterior'] for m in medidores]
    media = sum(consumos)/len(consumos)
    desv = sum(abs(c - media) for c in consumos)/len(consumos)    aproximação simples
    for i, c in enumerate(consumos):
        anomalia = c > media + 2*desv
        print(f"Medidor {i+1}: Consumo={c:.1f} {'(ANOMALIA)' if anomalia else ''}")

medidores = [{'anterior':100, 'atual':150},
             {'anterior':200, 'atual':400},
             {'anterior':150, 'atual':180}]
boletim_medidores(medidores)

  Exercício. s 10

def frete_multimodal(trechos, peso, distancia):
    custo = sum(trechos.values())
    if peso > 30:
        custo *= 1.10
    if distancia > 800:
        custo *= 0.95
    return custo

print(f"Frete total: R$ {frete_multimodal({'rodoviario':200,'aereo':300}, 40, 900):.2f}")

  Exercício. s 11

def despacho_elevador(chamadas, andar_inicial=1, max_andar=10):
    direcao = 1
    andar = andar_inicial
    while chamadas:
        proximas = sorted([c for c in chamadas if (c - andar)*direcao >= 0], key=lambda x: abs(x-andar))
        if not proximas:
            direcao *= -1
            continue
        prox = proximas[0]
        print(f"Ir do andar {andar} para {prox}")
        andar = prox
        chamadas.remove(prox)
        if not any((c - andar)*direcao > 0 for c in chamadas):
            direcao *= -1

despacho_elevador([3,7,2,9])

  Exercício. s 12

def melhor_proposta(precos, prazos):
    p_min, t_min = min(precos), min(prazos)
    escores = [0.7*(p_min/p) + 0.3*(t_min/t) for p,t in zip(precos,prazos)]
    melhor = escores.index(max(escores))
    return melhor, escores[melhor]

print(melhor_proposta([1000,1200,900],[10,8,12]))

  Exercício. s 13

def prioridade_ticket(texto, impacto):
    texto = texto.lower()
    score = impacto
    if "erro" in texto or "parado" in texto:
        score += 2
    if score >= 6: return "Alta"
    elif score >= 3: return "Média"
    else: return "Baixa"

print(prioridade_ticket("Sistema parado e com erro", 4))

  Exercício. s 14

def gerador_linear_congruente(a, c, m, semente, n):
    x = semente
    for _ in range(n):
        x = (a*x + c) % m
        yield x/m

def verificar_integridade(registros):
    n = len(registros)
    indices = [int(r*n) for r in gerador_linear_congruente(17, 43, 100, 7, n//10)]
    amostra = [registros[i] for i in indices]
    nulos = sum(any(v is None for v in r.values()) for r in amostra)
    print(f"Amostra: {len(amostra)} registros, {nulos} com campos nulos")

registros = [{'id':1,'nome':'Ana'},{'id':2,'nome':None},{'id':3,'nome':'João'}]*10
verificar_integridade(registros)

  Exercício. s 15

def alocar_turmas(turmas, salas):
    turmas.sort(reverse=True)
    salas.sort(reverse=True)
    alocacao = {}
    for t in turmas:
        for s in salas:
            if s >= t:
                alocacao[t] = s
                salas.remove(s)
                break
    print("Alocações:", alocacao)

alocar_turmas([40,35,20],[50,30,45])

  Exercício. s 16

def simular_callcenter(prior, comum, n_atend=2):
    tempo = 0
    espera_p, espera_c = [], []
    while prior or comum:
        tempo += 1
        for _ in range(n_atend):
            if prior: espera_p.append(tempo - prior.pop(0))
            elif comum: espera_c.append(tempo - comum.pop(0))
    print(f"Tempo médio espera prioritária: {sum(espera_p)/len(espera_p):.1f}")
    print(f"Tempo médio espera comum: {sum(espera_c)/len(espera_c):.1f}")

simular_callcenter([1,2,3,4],[5,6,7])

  Exercício. s 17

def comprimir(txt):
    if not txt: return ""
    res, cont, prev = "", 1, txt[0]
    for c in txt[1:]:
        if c == prev: cont += 1
        else:
            res += f"{cont}{prev}"
            prev, cont = c, 1
    return res + f"{cont}{prev}"

def descomprimir(txt):
    res, num = "", ""
    for c in txt:
        if c.isdigit(): num += c
        else:
            res += c * int(num)
            num = ""
    return res

print(comprimir("AAABBCC"))
print(descomprimir("3A2B2C"))

  Exercício. s 18

def cifra_cesar(txt, k, modo="cripto"):
    if modo == "decripto": k = -k
    res = ""
    for c in txt:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            res += chr((ord(c)-base+k)%26 + base)
        else:
            res += c
    return res

msg = cifra_cesar("Ola Mundo!", 3)
print(msg)
print(cifra_cesar(msg, 3, "decripto"))

  Exercício. s 19

from collections import Counter

def analisar_logs(linhas):
    severidades = Counter()
    mensagens = Counter()
    for l in linhas:
        data, serv, sev, msg = l.split(";")
        severidades[sev] += 1
        mensagens[msg.strip()] += 1
    print("Por severidade:", severidades)
    print("Top 3 mensagens:", mensagens.most_common(3))

logs = [
    "2025-11-07;API;ERRO;Falha conexão",
    "2025-11-07;API;WARN;Tempo alto",
    "2025-11-07;API;ERRO;Falha conexão",
]
analisar_logs(logs)

  Exercício. s 20

def balanceado(expr):
    pares = {')':'(',']':'[','}':'{'}
    pilha = []
    for c in expr:
        if c in '([{': pilha.append(c)
        elif c in ')]}':
            if not pilha or pilha.pop() != pares[c]:
                return False
    return not pilha

print(balanceado("{[()]}"), balanceado("{[(])}"))

  Exercício. s 21

def mesclar(a, b):
    i=j=0; res=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]: res.append(a[i]); i+=1
        else: res.append(b[j]); j+=1
    res += a[i:] + b[j:]
    return res

print(mesclar([1,3,5],[2,4,6]))

  Exercício. s 22

def particao(v, ini, fim):
    pivo = v[fim]
    i = ini
    for j in range(ini, fim):
        if v[j] < pivo:
            v[i], v[j] = v[j], v[i]; i += 1
    v[i], v[fim] = v[fim], v[i]
    return i

def selecionar(v, k):
    ini, fim = 0, len(v)-1
    while True:
        p = particao(v, ini, fim)
        if p == k: return v[p]
        elif p < k: ini = p+1
        else: fim = p-1

def mediana(v):
    n = len(v)
    return selecionar(v[:], n//2) if n%2 else sum(sorted(v)[n//2-1:n//2+1])/2

print(mediana([7,2,1,6,3,5,4]))

  Exercício. s 23

def busca_binaria(v, x):
    ini, fim, comp = 0, len(v)-1, 0
    while ini <= fim:
        comp += 1
        m = (ini+fim)//2
        if v[m] == x: return m, comp
        elif v[m] < x: ini = m+1
        else: fim = m-1
    return -1, comp

print(busca_binaria([1,2,3,4,5,6,7], 6))

  Exercício. s 24

def rotacionar(m):
    n = len(m)
    for i in range(n):
        for j in range(i, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for linha in m:
        linha.reverse()
    return m

print(rotacionar([[1,2,3],[4,5,6],[7,8,9]]))

  Exercício. s 25

def menor_caminho(custos):
    n, m = len(custos), len(custos[0])
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = custos[0][0]
    for i in range(1,n): dp[i][0] = dp[i-1][0] + custos[i][0]
    for j in range(1,m): dp[0][j] = dp[0][j-1] + custos[0][j]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = custos[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

print(menor_caminho([[1,3,1],[1,5,1],[4,2,1]]))

  Exercício. s 26

class Gerador:
    def __init__(self, a, c, m, semente):
        self.a, self.c, self.m, self.x = a,c,m,semente
    def proximo(self):
        self.x = (self.a*self.x + self.c) % self.m
        return self.x

g = Gerador(17,43,100,7)
for _ in range(5):
    print(g.proximo())

  Exercício. s 27

def para_base10(num, base):
    return sum(int(d,16 if base==16 else 10)*base**i for i,d in enumerate(str(num)[::-1]))

def de_base10(num, base):
    dig = "0123456789ABCDEF"
    res = ""
    while num>0:
        res = dig[num%base]+res
        num//=base
    return res or "0"

print(de_base10(para_base10("A3",16),8))

  Exercício. s 28

def digito_boleto(codigo):
    pesos = [2,3,4,5,6,7,8,9]
    soma = sum(int(c)*pesos[i%8] for i,c in enumerate(codigo))
    r = soma % 11
    return 0 if r in (0,1) else 11 - r

def validar_linha(linha):
    base, dig = linha[:-1], int(linha[-1])
    return dig == digito_boleto(base)

print(digito_boleto("00190500954014481606906809350314337370000000100"))

  Exercício. s 29

def selecionar_tarefas(tarefas):
    tarefas.sort(key=lambda x:x[1])    ordenar pelo fim
    fim = 0
    selecionadas = []
    for ini,f in tarefas:
        if ini >= fim:
            selecionadas.append((ini,f))
            fim = f
    return selecionadas

print(selecionar_tarefas([(8,9),(9,11),(10,12),(13,14),(11,13)]))

  Exercício. s 30

def tabela_csv(texto):
    linhas = [l.split(';') for l in texto.strip().split('\n')]
    larguras = [max(len(c) for c in col) for col in zip(*linhas)]
    for l in linhas:
        print(" | ".join(c.ljust(larguras[i]) for i,c in enumerate(l)))

csv = "Nome;Idade;Cidade\nAna;22;São Paulo\nJoão;30;Rio"
tabela_csv(csv)

4ª lista de  Exercício. s.

  Exercício. s 1

  Algoritmo: sequência de passos para resolver um problema
  Fluxograma: representação gráfica do algoritmo (caixas e setas)
  Pseudocódigo: descrição textual próxima à programação

  Exercício. s 2

  Início
  → Solicitar operação
  → Validar conta/saldo
  → Se válido → Gerar comprovante → Imprimir → Fim
  → Se inválido → Mostrar erro → Fim


  Exercício. s 3

horas = int(input("Horas: "))
print("Minutos:", horas * 60)
print("Segundos:", horas * 3600)

  Exercício. s 4

v = float(input("Volume (L): "))
q = float(input("Vazão (L/min): "))
print("Tempo necessário:", v / q, "minutos")

  Exercício. s 5

senha = "1234"
for i in range(3):
    if input("Digite a senha: ") == senha:
        print("Acesso permitido")
        break
else:
    print("Acesso bloqueado")

  Exercício. s 6

l = float(input("Largura: "))
c = float(input("Comprimento: "))
area = l * c
print("Área:", area, "m²\nValor: R$", area * 250)

  Exercício. s 7

n = float(input("Número: "))
print("Dobro:", n*2, "Triplo:", n*3, "Metade:", n/2)

  Exercício. s 8

d = float(input("Distância (km): "))
t = float(input("Tempo (h): "))
print("Velocidade média:", d/t, "km/h")

  Exercício. s 9

v = float(input("Valor da compra: R$ "))
print("À vista (5% desc): R$", v*0.95)
print("3x sem juros: R$", v/3)

  Exercício. s 10

d = float(input("Distância (km): "))
l = float(input("Combustível gasto (L): "))
print("Consumo médio:", d/l, "km/L")

  Exercício. s 11

t = float(input("Temperatura °C: "))
if t < 18: print("Abaixo do ideal")
elif t <= 26: print("Ideal")
else: print("Acima do ideal")

  Exercício. s 12

idade = int(input("Idade: "))
if idade <= 12: print("Infantil")
elif idade <= 17: print("Juvenil")
elif idade <= 59: print("Adulto")
else: print("Sênior")

  Exercício. s 13

a, b, c = map(float, input("Lados (a b c): ").split())
if a+b>c and a+c>b and b+c>a: print("Forma triângulo")
else: print("Não forma triângulo")

  Exercício. s 14

v = float(input("Valor: R$ "))
p = input("Forma (dinheiro/cartao/parcelado): ").lower()
if p == "dinheiro": v *= 0.9
elif p == "cartao": v *= 0.95
print("Valor final: R$", v)

  Exercício. s 15
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura**2)
print("IMC:", imc)
if imc < 18.5: print("Abaixo do peso")
elif imc < 25: print("Peso ideal")
elif imc < 30: print("Sobrepeso")
else: print("Obesidade")

  Exercício. s 16

for i in range(2, 101, 2):
    print(i, end=" ")

  Exercício. s 17
s = 0
for i in range(10):
    s += float(input(f"Número {i+1}: "))
print("Soma:", s, "Média:", s/10)

  Exercício. s 18
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

  Exercício. s 19
s = c = 0
while True:
    i = int(input("Idade (0 sai): "))
    if i == 0: break
    s += i; c += 1
print("Média:", s/c if c else 0)

  Exercício. s 20
pos = neg = zero = 0
while True:
    n = float(input("Número (999 sai): "))
    if n == 999: break
    if n > 0: pos += 1
    elif n < 0: neg += 1
    else: zero += 1
print("Pos:", pos, "Neg:", neg, "Zero:", zero)

  Exercício. s 21
nomes = [input("Nome: ") for _ in range(5)]
print("Ordem alfabética:", sorted(nomes))

  Exercício. s 22
notas = []
for i in range(5):
    aluno = [float(input(f"Nota {j+1} do aluno {i+1}: ")) for j in range(4)]
    notas.append(aluno)
medias = [sum(a)/4 for a in notas]
print("Médias:", medias, "Média geral:", sum(medias)/5)

  Exercício. s 23
nums = [float(input("Número: ")) for _ in range(10)]
m = sum(nums)/len(nums)
print("Maiores que a média:", [x for x in nums if x > m])

  Exercício. s 24
a = input("Lista 1 (sep. por vírgula): ").split(",")
b = input("Lista 2 (sep. por vírgula): ").split(",")
print("Comuns:", list(set(a) & set(b)))

  Exercício. s 25
m = [[int(input(f"Elemento [{i}][{j}]: ")) for j in range(3)] for i in range(3)]
print("Soma diagonal:", m[0][0] + m[1][1] + m[2][2])

  Exercício. s 26
def fatorial(n):
    r = 1
    for i in range(2, n+1): r *= i
    return r

print(fatorial(int(input("Número: "))))

  Exercício. s 27
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

print(mdc(int(input("A: ")), int(input("B: "))))

  Exercício. s 28
def analisa(lista):
    return max(lista), min(lista), sum(lista)/len(lista)

notas = [float(input("Nota: ")) for _ in range(5)]
print(analisa(notas))

  Exercício. s 29
def perfeito(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

print(perfeito(int(input("Número: "))))

  Exercício. s 30
def ler():
    return [float(input("Valor: ")) for _ in range(5)]

def maior(v): return max(v)
def media(v): return sum(v)/len(v)

v = ler()
print("Maior:", maior(v), "Média:", media(v))

 fim :)

