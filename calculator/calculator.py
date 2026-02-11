import os
os.system("clear")
print("> Calculadora de multiplas funções <\n")
x = input("Insira o primeiro valor: ")
y = input("Insira o segundo valor: ")

def soma():
    try:
        value1 = int(x)
        value2 = int(y)
        print("1ª) Valor: ", value1)   
        print("2ª) Valor: ", value2)
        print("O resultado da soma é: ", value1 + value2)
    except ValueError:
        try:
            value3 = float(x)
            value4 = float(y)
            print("1ª) Valor: ", value3)   
            print("2ª) Valor: ", value4)
            print("O resultado da soma é: ", value3 + value4)
        except ValueError:
            print("Valor inválido!")
            
def diminuir():
    pass
def multiplicar():
    pass
def dividir():
    pass


while True:
    os.system("clear")
    
    print("Menu da Calculadora\n")
    print("1. Soma")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    choice = input("Escolha entre às opções de calculo, dê 1 a 4: \n")
    if choice == "1":
        os.system("clear")
        soma()
        print("\n")
        print("Você deseja calcula novamente outro valor?")
        print("1. Sim")
        print("2. Não")
        e_choice = input("")
        if e_choice == "1":
            os.system("python calculator.py")
        elif e_choice == "2":
            break
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    else:
        print("Opção inválida, escolha entre 1 a 4.")