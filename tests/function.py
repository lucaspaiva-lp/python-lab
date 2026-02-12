import os

while True:
    x = input("Entrada do primeiro valor: ")
    y = input("Entrada do segundo valor: ")
    try:
        value1 = int(x)
        value2 = int(y)
    except ValueError:
            value3 = float(x)
            value4 = float(y)
            break
    else:
        x == str
        y == str
        print("Valor inválido! Favor coloque apenas números.")
        continue
# TODO: Transforma a entrada do X e Y em INT or Float antes de chega na função de calculo.

def soma():
    try:
        value1 = int(x)
        value2 = int(y)
        print("1ª Valor: ", value1)   
        print("2ª Valor: ", value2)
        print("O resultado da soma é: ", value1 + value2)
    except ValueError:
        try:
            value3 = float(x)
            value4 = float(y)
            print("1ª Valor: ", value3)   
            print("2ª Valor: ", value4)
            print("O resultado da soma é: ", value3 + value4)
        except ValueError:
            print("Valor inválido!")

while True:
    choice = input("Você quer fazer qual tipo de calculo: ")

    if choice == "Soma":
        os.system("clear")
        soma()
        break
    elif choice == "Diminuir":
        pass
    elif choice == "Multiplicar":
        pass
    elif choice == "Dividir":
        pass
    else:
        print("Comando invalido, escolha entre (Somar, Diminuir, Multiplicar e Dividir).")