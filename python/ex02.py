import math

a = b = c = 0
delta = rdelta = x1 = x2 = 0.0
try:
    print("Digite o valor de A, B, C")
    a = int(input())
    b = int(input())
    c = int(input())
    delta = b * b - 4 * a * c
    try:
        rdelta = math.sqrt(delta)
        x1 = (-b + rdelta) / (2 * a)
        x2 = (-b - rdelta) / (2 * a)
        print(f"delta =e {delta}")
        print(f"x1 é {x1}")
        print(f"x2 é {x2}")
    except ValueError:
        print("Erro! Delta negativo")
except ValueError:
    print("Erro! Somente números inteiros")