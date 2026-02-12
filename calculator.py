import os

os.system("clear")
while True:
    print("> Calculadora de multiplas funções <\n")
    ## FIXME: Falta implementa a falha que ocorre caso coloque STR na inserção inicial. -> Falha só aparece lá na frente
    x = input("Insira o primeiro valor:")
    y = input("Insira o segundo valor:")

    # Manter a junção acima das opções de calculos, para manter a integridade definida.
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

    while True:
        os.system("clear")
        
        print("Menu da Calculadora\n")
        print("Escolha entre às opções de calculo, dê 1 a 4: ")
        print("1. Soma")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        # TODO: Implementa um retorno/reset caso usuário deseje retorna ou trocar os valores.
        choice = input("Usuário:")
        
        if choice == "1":
            os.system("clear")
            soma()
            # TODO: Implementa todos os blocos de retorno ao calculo em uma função para limpar a aplicação.
            break
        elif choice == "2":
            os.system("clear")
            diminuir()
            break
        elif choice == "3":
            os.system("clear")
            multiplicar()
            break
        elif choice == "4":
            os.system("clear")
            dividir()
            break
        else:
            print("Opção inválida, escolha entre 1 a 4.")
    print("")
    print("Você deseja calcula novamente outro valor?")
    print("1. Sim")
    print("2. Não")
    e_choice = input("Usuário:")
    if e_choice == "1":
        os.system("clear")
        continue
    elif e_choice == "2":
        break
    break