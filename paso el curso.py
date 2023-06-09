matematica=float(input("nota matematica:"))
fisica=float(input("nota fisica:"))
quimica=float(input("nota quimica:"))
religion=float(input("nota religion:"))
promedio=(matematica+fisica+quimica+religion)/4
if promedio<3.5:
    print("usted reprobo el curso")
else:
    print("usted aprobo el curso ")