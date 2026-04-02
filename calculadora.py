import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('400x400') # Ajustei o tamanho para ficar mais proporcional
janela.configure(bg='#1c1c1c')


def clicou(valor):
    visor.insert(tk.END, valor)

def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, resultado)
    except:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")

def deletar():
    visor.delete(0, tk.END)


# Configuração do Visor
visor = tk.Entry(janela, font=('Arial', 24), bg='#333333', fg='white', borderwidth=0, justify='right')
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Configurações de estilo comuns
estilo_num = {'bg': '#333333', 'fg': 'white', 'font': ('Arial', 14), 'width': 5, 'height': 2}
estilo_op = {'bg': '#ff9500', 'fg': 'white', 'font': ('Arial', 14), 'width': 5, 'height': 2}

# --- LINHA 1 (7, 8, 9 e /) ---
tk.Button(janela, text='7', **estilo_num, command=lambda: clicou('7')).grid(row=1, column=0, padx=2, pady=2)
tk.Button(janela, text='8', **estilo_num, command=lambda: clicou('8')).grid(row=1, column=1, padx=2, pady=2)
tk.Button(janela, text='9', **estilo_num, command=lambda: clicou('9')).grid(row=1, column=2, padx=2, pady=2)
tk.Button(janela, text='/', **estilo_op, command=lambda: clicou('/')).grid(row=1, column=3, padx=2, pady=2)

# --- LINHA 2 (4, 5, 6 e *) ---
tk.Button(janela, text='4', **estilo_num, command=lambda: clicou('4')).grid(row=2, column=0, padx=2, pady=2)
tk.Button(janela, text='5', **estilo_num, command=lambda: clicou('5')).grid(row=2, column=1, padx=2, pady=2)
tk.Button(janela, text='6', **estilo_num, command=lambda: clicou('6')).grid(row=2, column=2, padx=2, pady=2)
tk.Button(janela, text='*', **estilo_op, command=lambda: clicou('*')).grid(row=2, column=3, padx=2, pady=2)

# --- LINHA 3 (1, 2, 3 e -) ---
tk.Button(janela, text='1', **estilo_num, command=lambda: clicou('1')).grid(row=3, column=0, padx=2, pady=2)
tk.Button(janela, text='2', **estilo_num, command=lambda: clicou('2')).grid(row=3, column=1, padx=2, pady=2)
tk.Button(janela, text='3', **estilo_num, command=lambda: clicou('3')).grid(row=3, column=2, padx=2, pady=2)
tk.Button(janela, text='-', **estilo_op, command=lambda: clicou('-')).grid(row=3, column=3, padx=2, pady=2)

# --- LINHA 4 (0, C e +) ---
tk.Button(janela, text='0', **estilo_num, command=lambda: clicou('0')).grid(row=4, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
tk.Button(janela, text='C', **estilo_num, command=deletar).grid(row=4, column=2, padx=2, pady=2)
tk.Button(janela, text='+', **estilo_op, command=lambda: clicou('+')).grid(row=4, column=3, padx=2, pady=2)

# --- LINHA 5 (Botão de Igual expandido) ---
tk.Button(janela, text='=', **estilo_op, command=calcular).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=10)

janela.mainloop()