cont = 0
while True:
    try:
        print("Digite valor de QI")
        print("ou 0 para parar")
        qi = int(input())
        if qi == 0:
            break
        if qi < 140:
            continue
        cont += 1
    except ValueError:
        print("Erro! Apenas números inteiros")
print(f"Quantidade de gênios é {cont}")