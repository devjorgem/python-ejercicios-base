firstnumber = int(input("primer numero "))
secondnumber = int(input("second number "))
for i in range(1,firstnumber+1):
    for x in range (1,secondnumber+1):
        print(f"{i} x {x}={i*x}")
        if x== secondnumber:
            print(" ")