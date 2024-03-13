km = float(input('quantos km foram percorridos: '))
dias = int(input('quantos dias o carro ficou alugado: '))
pago = (dias * 60) + (km * 0.15)

print(f'o tatal a pagar e de R${pago:.2f}')