palabra="hannaha"
vocales=0
consonante=0
for i in palabra:
    if i in["a","e","i","o","u"]:
        vocales+=1
    else:
        consonante+=1
print(f"{vocales} y {consonante}")