def soma(a, b): 
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero, não pode.")
    return a/b

def testeAB():
    # global a
    # global b

    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: ")) 
    print("O Primeiro valor é maior que o segundo")
    

    if a > b:
        print("certo")

    else:
            print("Deu Zebra: o primeiro valor deve ser maior que o segundo.")
        
    while a < b  or a == b:
            print("deu erro")
            a = float(input("Insira o primeiro valor: "))
            b = float(input("Insira o segundo valor: "))
            print(a,b)

    return a,b
                
resultado = testeAB()
a, b = resultado
resultado1 = soma(a, b)
resultado2 = subtracao(a, b)
resultado3 = multiplicacao(a, b)
resultado4 = divisao(a, b)

print(f"{resultado1:.3f}, {resultado2:.3f}, {resultado3:.3f}, {resultado4:.3f}")

