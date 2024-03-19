from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print(f'a hipotenusa vai medir {hip:.2f}')