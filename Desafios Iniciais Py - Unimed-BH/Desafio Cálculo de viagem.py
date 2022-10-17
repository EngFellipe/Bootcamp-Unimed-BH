valores = input().split()

tempo = int(valores[0])
velocidade = int(valores[1])

distancia = tempo*velocidade

litros = distancia/12

print(f"{litros:.3f}")