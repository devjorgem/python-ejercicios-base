negative=0
positive=0
listOfNumbers = list(map(int, input("escribe varios numeros separados por coma: ").split(' ')))

for i in (listOfNumbers):
    if i<0:
        negative+=1
    else:
        positive+=1
print(f"positivo {positive} y negativo {negative}")