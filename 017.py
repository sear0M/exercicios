op = float(input('digite i valor do cateto oposto; '))
adj = float(input('digite o valor do cateto adjacente: '))
hip = (op ** 2 + adj ** 2) ** (1/2)
print(f'a hipotenusa vai medir {hip:.2f}')