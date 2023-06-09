numerobuzz=3
numerofizz=5
def fizzbuzz(hasta):
    for i in range(1,hasta+1):
        if  i%3==0  and i%5==0:
            print("fizzbuzz")
        elif i%numerofizz==0:
            print("fizz")
        elif i%numerobuzz ==0:
            print("buzz")
        else:
            print(i)
fizzbuzz(100)