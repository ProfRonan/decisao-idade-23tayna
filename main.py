idade= int(input("digite sua idade"))
if idade<= 0:
    print("impossivel!")
elif idade<= 18:
    print("não precisa se alistar")
elif idade>= 18 and idade<= 65:  
    print("não esqueça de voltar na proxima eleição")
elif idade>= 65:
    print("vá descansar")
else:
    print("eita!")