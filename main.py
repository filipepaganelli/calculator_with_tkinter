import os
import time
import sys
import tkinter as tk

root = tk.Tk()

root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

"""
entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

label_result = tk.Label(root, text="Result:")

label_result.pack(pady=10)
"""
#Funções da operações
class Calculadora():
    """
        #Funções de operações matemáticas
        @staticmethod
        def somar(): 
            try:
                a = entry1.get()
                b = entry2.get()
                result = a+b
                label_result.config(text=f"Resultado: {result}")  # atualiza o label
            except ValueError:
                label_result.config(text="Digite apenas números válidos!")

            #return print(f" O resultado é: {round((a+b),2)}")
            """
    @staticmethod
    def subtrair(a,b):
        return print(f" O resultado é: {round((a-b),2)}")
    @staticmethod
    def dividir(a,b):
        return print(f" O resultado é: {round((a/b),2)}")
    @staticmethod
    def multiplicar(a,b):
        return print(f" O resultado é: {round((a*b),2)}")
    @staticmethod
    def raiz(a,b):
        return print(f" O resultado é: {round(b**(1/a),2)}")
    
    #Função de validação de input   
    @staticmethod  
    def validar_input(pergunta: str, valor_minimo: int):
        while True:
            
            try:
                
                valor = int(input(pergunta))
                if valor < valor_minimo:
                    print(f"Digite um valor maior que {valor_minimo}")
                    
                    continue
                else:
                    return valor
            except ValueError:
                print('Letras ou caracteres não são aceitáveis. Digite uma opção válida!')
                
                     

def efeito_digitacao(texto):
    """
    Simula o efeito de digitação em uma linha de texto.
    """
    for caractere in texto:
        sys.stdout.write(caractere)  # Imprime um caractere sem pular linha
        sys.stdout.flush()           # Força a impressão imediata
        time.sleep(0.05)  

def menu():
    while True:       
        try:
        
            opcao = int(input("""
            Qual operação deseja fazer?\n                 
            1-Somar
            2-Substrair
            3-Multiplicar
            4-Dividir
            5-Raiz                          
            0-Sair\n
            >>>Digite aqui: """))

            if opcao not in (0,1,2,3,4,5):
                efeito_digitacao("\n ATENÇÃO!! Digite apenas um dos números do menu!")
                time.sleep(0.5)
                continue
            
            else:
                return opcao
            
                
        except ValueError:
            print('Letras ou caracteres não são aceitáveis. Digite uma opção válida!')
            os.system("cls")
            continue




def rodar_calculadora():
    while True:
        opcao = menu()
        if opcao == 0:
            efeito_digitacao("\nObrigado por usar nossa calculadora! ;)")
            return 0

        # Para soma, subtração e multiplicação, mínimo é 0
        if opcao in (1, 2, 3):
            v1 = Calculadora.validar_input("Insira o primeiro valor: ", 0)
            v2 = Calculadora.validar_input("Insira o segundo valor: ", 0)
            if opcao == 1:
                Calculadora.somar(v1, v2)
            elif opcao == 2:
                Calculadora.subtrair(v1, v2)
            elif opcao == 3:
                Calculadora.multiplicar(v1, v2)

        elif opcao == 4:
            v1 = Calculadora.validar_input("Insira o primeiro valor: ", 0)
            v2 = Calculadora.validar_input("Insira o segundo valor: ", 1)
            Calculadora.dividir(v1, v2)

        elif opcao == 5:
            v1 = Calculadora.validar_input("Insira o coeficiente da raiz: ", 1)
            v2 = Calculadora.validar_input("Insira o número que deseja descobrir a raiz: ", 1)
            Calculadora.raiz(v1, v2)





"""
button_sum = tk.Button(root, text="+", command= Calculadora.somar)
button_sum.pack(pady = 5)
"""
display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, width=20, borderwidth=5, justify="right")
display.grid(row=1,column=0, columnspan=4, padx=5, pady=5)


def insert_number_on_display(value):
    display_var.set(display_var.get() + str(value))


def clean_display():
    display_var.set("")

def calculate_result():
    try:
        result= str(eval(display_var.get()))
        display_var.set(result)
    
    except:
        display_var.set("Error!")
#Buttons of numbers 
btn_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: insert_number_on_display("7"))
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: insert_number_on_display("8") )
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: insert_number_on_display("9") )
btn_9.grid(row=3, column=2)

#Buttons of numbers 
btn_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: insert_number_on_display("4") )
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: insert_number_on_display("5") )
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: insert_number_on_display("6") )
btn_6.grid(row=4, column=2)

#Buttons of numbers 
btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: insert_number_on_display("1") )
btn_1.grid(row=5, column=0)
btn_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: insert_number_on_display("2") )
btn_2.grid(row=5, column=1)
btn_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: insert_number_on_display("3") )
btn_3.grid(row=5, column=2)

#Buttons of numbers 
btn_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: insert_number_on_display("0") )
btn_0.grid(row=6, column=0)

#Buttons of signs 
btn_7 = tk.Button(root, text="/", width=5, height=2, command=lambda: insert_number_on_display("/"))
btn_7.grid(row=3, column=3)
btn_8 = tk.Button(root, text="x", width=5, height=2, command=lambda: insert_number_on_display("*") )
btn_8.grid(row=4, column=3)
btn_9 = tk.Button(root, text="-", width=5, height=2, command=lambda: insert_number_on_display("-") )
btn_9.grid(row=5, column=3)
btn_9 = tk.Button(root, text="+", width=5, height=2, command=lambda: insert_number_on_display("+") )
btn_9.grid(row=6, column=3)
btn_9 = tk.Button(root, text="=", width=5, height=2, command=lambda: calculate_result())
btn_9.grid(row=6, column=2)
btn_9 = tk.Button(root, text=".", width=5, height=2, command=lambda: insert_number_on_display(".") )
btn_9.grid(row=6, column=1)









root.mainloop()

"""
if __name__ == "__main__":

 
    rodar_calculadora()
"""
