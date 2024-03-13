from math import trunc
# para nao ter que importar todo o math usando o import math, se importa somento o comando a ser utilizado 
num = float(input('digite um numero: '))
print(f'o valor digitado foi {num} e sua porcao inteira e {math.trunc(num)}')

