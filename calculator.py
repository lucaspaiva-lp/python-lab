import os

# Manter a junção acima das opções de calculos, para manter a integridade definida.
def tratamento_do_input(text): # É necessário para melhor tratamento de entrada de STR.
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Valor inválido da function!")

def soma():
    try:
        value1 = int(x)
        value2 = int(y)
        print("1ª) Valor:", value1)   
        print("2ª) Valor:", value2)
        print("O resultado da soma é:", value1 + value2)
    except ValueError:
        try:
            value1 = float(x)
            value2 = float(y)
            print("1ª) Valor:", value1)   
            print("2ª) Valor:", value2)
            print("O resultado da soma é:", value1 + value2)
        except ValueError:
            print("Valor inválido!")
            
def diminuir():
    try:
        value1 = int(x)
        value2 = int(y)
        print("1ª) Valor:", value1)   
        print("2ª) Valor:", value2)
        print("O resultado da subtração é:", value1 - value2)
    except ValueError:
        try:
            value1 = float(x)
            value2 = float(y)
            print("Valores armazenados:")
            print("1ª) Valor:", value1)   
            print("2ª) Valor:", value2)
            print("O resultado da subtração é:", value1 - value2)
        except ValueError:
            print("Valor inválido!")
    
def multiplicar():
    try:
        value1 = int(x)
        value2 = int(y)
        print("Valores armazenados:")
        print("1ª) Valor:", value1)   
        print("2ª) Valor:", value2)
        print("O resultado da multiplicação é:", value1 * value2)
    except ValueError:
        try:
            value1 = float(x)
            value2 = float(y)
            print("Valores armazenados:")
            print("1ª) Valor:", value1)   
            print("2ª) Valor:", value2)
            print("O resultado da multiplicação é:", value1 * value2)
        except ValueError:
            print("Valor inválido!")

def dividir():
    try:
        value1 = int(x)
        value2 = int(y)
        print("Valores armazenados:")
        print("1ª) Valor:", value1)   
        print("2ª) Valor:", value2)
        print("O resultado da divisão é:", value1 / value2)
    except ValueError:
        try:
            value1 = float(x)
            value2 = float(y)
            print("\n")
            print("Valores armazenados:")
            print("1ª) Valor:", value1)   
            print("2ª) Valor:", value2)
            print("O resultado da divisão é:", value1 / value2)
        except ValueError:
            print("Valor inválido!")

os.system("clear")
while True:
    print("> Calculadora de multiplas funções <\n")

    x = tratamento_do_input("Insira o primeiro valor: ")
    y = tratamento_do_input("Insira o segundo valor: ")
    os.system("clear")

    while True:
        
        print("Menu da Calculadora\n")
        print("Escolha entre às opções de calculo, dê 1 a 4: ")
        print("1. Soma")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        # TODO: Implementa um retorno/reset caso usuário deseje retorna ou trocar os valores.
        choice = input("Usuário: ")
        
        if choice == "1":
            os.system("clear")
            print("> Resultado do calculo <")
            soma()
            break
        elif choice == "2":
            os.system("clear")
            print("> Resultado do calculo <")
            diminuir()
            break
        elif choice == "3":
            os.system("clear")
            print("> Resultado do calculo <")
            multiplicar()
            break
        elif choice == "4":
            os.system("clear")
            print("> Resultado do calculo <")
            dividir()
            break
        else:
            os.system("clear")
            print("Opção inválida, escolha entre 1 a 4.")
            print("")

    while True: # Loop de saida, para tratamento de erros.
        print("------------------------------------------")
        print("Você deseja calcula novamente outro valor?")
        print("1. Sim")
        print("2. Não")
        e_choice = input("Usuário: ")
        if e_choice == "1":
            os.system("clear")
            break
        elif e_choice == "2":
            break
        else:
            print("Error!")
    if e_choice == "1":
        continue
    break