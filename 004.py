msg = input("dite algo: ")
print(f"o tipo primitivo desse valor e {type(msg)}")
print(f"so tem espacos? {msg.isspace()}")
# quando nao tiver () depois de uma varialvel, ela e um atrubuto e nao um metodo ou funcao
print(f"e um numero? {msg.isnumeric()}")
print(f"e alfabetico? {msg.isalpha()}")
print(f"e alfanumerico? {msg.isalnum()}")
print(f"esta em maiuscula? {msg.isupper()}")
print(f"esta em minuscula? {msg.islower()}")
print(f"esta capitalizada? {msg.istitle()}")