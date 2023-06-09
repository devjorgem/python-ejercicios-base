number=int(input("numero: "))
exponente=int(input("exponente: "))
suma=0
for i in range(1,number+1):
    suma+=i**exponente
print(suma)
