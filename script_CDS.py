#!/usr/bin/env python3

# Importa o módulo sys para que possamos usar argumentos da linha de comando
import sys

# Verifica se o número de argumentos está correto (espera-se 7: uma sequência de DNA e 6 números)
if len(sys.argv) != 8:
    print('Por favor, insira uma sequência de DNA e seis números inteiros.')
    exit(1)  # Para o programa se o número de argumentos estiver errado

# Pega os argumentos da linha de comando
DNA = sys.argv[1]  # O primeiro argumento é a sequência de DNA
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

# Coloca a sequência de DNA em letras maiúsculas para evitar problemas com letras minúsculas
DNA = DNA.upper()

# Calcula o tamanho da sequência de DNA
tamanho = len(DNA)

# Verifica se todos os argumentos (exceto a sequência) são números inteiros e se estão dentro do tamanho da sequência
if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
    # Converte os argumentos de texto para números inteiros
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6)

    # Verifica se os números são positivos e menores ou iguais ao tamanho do DNA
    if not (0 < n1 <= tamanho and 0 < n2 <= tamanho and 0 < n3 <= tamanho and 0 < n4 <= tamanho and 0 < n5 <= tamanho and 0 < n6 <= tamanho):
        print('Os números devem ser positivos e não maiores que o tamanho da sequência de DNA.')
        exit(1)  # Para o programa se os números não estiverem corretos
else:
    print('Por favor, insira seis números inteiros.')
    exit(1)  # Para o programa se os argumentos não forem números inteiros

# Extrai a primeira parte da sequência, chamada de CDS1, usando os números fornecidos
cds1 = DNA[n1-1:n2]  # O -1 é porque as posições no Python começam no zero

# Verifica se CDS1 começa com 'ATG'
if not cds1.startswith('ATG'):
    print('CDS1 não começa com o códon ATG.')
    exit(1)  # Para o programa se CDS1 não começar com 'ATG'

# Extrai a segunda parte da sequência, chamada de CDS2
cds2 = DNA[n3-1:n4]

# Extrai a terceira parte da sequência, chamada de CDS3
cds3 = DNA[n5-1:n6]

# Verifica se CDS3 termina com um dos códons de parada: 'TAG', 'TAA' ou 'TGA'
if cds3[-3:] not in ['TAG', 'TAA', 'TGA']:
    print('CDS3 não termina com um códon de parada.')
    exit(1)  # Para o programa se CDS3 não terminar com um códon de parada

# Junta (concatena) as três partes: CDS1, CDS2 e CDS3
sequencia_final = cds1 + cds2 + cds3

# Imprime a sequência final
print('Sequência concatenada:', sequencia_final)

