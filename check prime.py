
counter=0
number=int(input("number: "))
for i in range(2,number+1):
    if number%i==0:
        counter+=1
if counter>1:
    print("no es primo")
else:
    
    print("es primo")

