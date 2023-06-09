espacio=0
cantidad=int(input("numero:"))
space=cantidad
for i in range (1,cantidad+1)[::-1]:
    if i%3==0 or i==1:
        print((" "*espacio +"*"*i+" "*espacio))
        espacio+=1