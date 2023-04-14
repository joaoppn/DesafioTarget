frase = input("Escreva algo para ser invertido:")
newfrase = ""
for i in range(len(frase),0, -1):
    newfrase = newfrase+frase[i-1]

print(newfrase)