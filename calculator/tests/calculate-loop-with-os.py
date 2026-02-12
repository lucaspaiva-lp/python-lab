import os
x = input("Entrada do primeiro valor: ")
y = input("Entrada do segundo valor: ")
os.system("clear")
try:
    value1 = int(x)
    value2 = int(y)
    print("Value 1: ",value1)
    print("Value 2: ", value2)
    print("O resultado do calculo é: ", value1 + value2)
except ValueError:
    try:
        value3 = float(x)
        value4 = float(y)
        print("Value 3: ", value3)
        print("Value 4: ", value4)
        print("O resultado do calculo é: ", value3 + value4)
    except ValueError:
        print("Invalid input")
os.system("python3 calculate.py")