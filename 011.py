larg = float(input('digite a largura da parede: '))
alt = float(input('digite a altura da parede : '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensao de {}x{} e area de {}m2, sendo assim para pintar esta parede sera necessario {}l de tinta'.format(larg, alt, area, tinta))