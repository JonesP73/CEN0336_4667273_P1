#!/usr/bin/env python3

# Solicita ao usuário o tamanho inicial da população, taxa de crescimento e número de anos
P0 = input("Digite o tamanho inicial da população: ")
r = input("Digite a taxa de crescimento anual (em decimal): ")
t = input("Digite o número de anos: ")

# Verifica se as entradas são numéricas e converte para os tipos corretos
if P0.replace('.', '', 1).isdigit() and r.replace('.', '', 1).isdigit() and t.isdigit():
    P0 = float(P0)
    r = float(r)
    t = int(t)

    # Verifica se os valores são positivos e válidos
    if P0 > 0 and r >= 0 and t > 0:
        # Loop para calcular o tamanho da população a cada ano
        for ano in range(1, t + 1):
            populacao = P0 * ((1 + r) ** ano)
            print(f"Ano {ano}: {populacao:.6f}")
    else:
        print("Erro: O tamanho inicial da população e o número de anos devem ser positivos, e a taxa de crescimento não pode ser negativa.")
else:
    print("Erro: Certifique-se de inserir valores numéricos válidos.")

