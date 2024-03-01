nota1 = float(input("digite a primeira nota do anluno: "))
nota2 = float(input("digite a segunda nota do aluno: "))
media = ((nota1 + nota2) / 2)
print(f"a media entre {nota1} e {nota2} e {(round(media, 1))}")     

#pode arredondar com round, sendo o numero depois da virgula a quantia de casas decimais
#podemos arredondar com :.xf, sendo o x a quantia de casas decimais exemplo refazendo o round de cima
#print(f"a media entre {nota1} e {nota2} e {media:.1f}")