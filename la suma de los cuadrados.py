def square(squares):
    suma =0 
    for i in range(1,squares+1):
        suma =suma+ i*i
    return suma
numero=int(input("numero: "))  
print(square(numero))