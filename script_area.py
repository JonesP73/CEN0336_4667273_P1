#!/usr/bin/env python3

# Importa o módulo sys para capturar os argumentos da linha de comando
import sys

# Verifica se foram fornecidos exatamente 2 argumentos além do nome do script
if len(sys.argv) != 3:
    print("Erro: Você deve fornecer exatamente dois números inteiros como argumentos.")
    sys.exit(1)

# Captura os argumentos fornecidos pelo usuário
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Verifica se os argumentos são números inteiros positivos
if not (arg1.isdigit() and arg2.isdigit()):
    print("Erro: Ambos os valores devem ser números inteiros positivos.")
    sys.exit(1)

# Converte os argumentos para inteiros
a = int(arg1)
b = int(arg2)

# Verifica se os valores estão dentro do intervalo permitido (menores que 500)
if a >= 500 or b >= 500:
    print("Erro: Ambos os valores devem ser menores que 500.")
    sys.exit(1)

# Calcula a área do triângulo retângulo usando a fórmula A = ab / 2
area = (a * b) / 2

# Exibe o resultado formatado
print(f"A área do triângulo retângulo com lados a={a} e b={b}, é {area}")

