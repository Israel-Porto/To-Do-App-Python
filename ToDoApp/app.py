import customtkinter as ctk
import tkinter
from tkinter import *
from tkinter import messagebox 

window = ctk.CTk('black')
window.geometry("350x500")
window.maxsize(350, 500)
window.title("To-Do App v1.0")

estilo = {
    "fontes" : {
        "grande" : ('Lucida Sans', 24, 'bold'),
        "media" : ('Lucida Sans', 20, 'bold'),
        "pequena" : ('Lucida Sans', 12, 'bold')
    },
    "cores" : {
        "azul" : '#1A2CEB',
        "vermelho" : '#EB1A1A',
        "verde" : '#2FEB64',
    }
}

def adicionar_tarefa():
    nova_tarefa = tarefa.get()
    
    if nova_tarefa:
        lista_tarefas.insert(0, nova_tarefa)
        tarefa.delete(0, END)
        salvar_tarefas()
    else:
        messagebox.showerror('Erro no App', 'Digite uma tarefa')
    

def remover_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()
    
    if tarefa_selecionada:
        lista_tarefas.delete(tarefa_selecionada)
        salvar_tarefas()
    else:
        messagebox.showerror('Erro no App', 'Selecione uma tarefa')
        
def salvar_tarefas():
    with open('tarefas.txt', 'w') as arquivo:
        tarefas = lista_tarefas.get(0, END)
        
        for tarefa in tarefas:
            arquivo.write(tarefa + '\n')
            
def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as arquivo:
            tarefas = arquivo.readlines()
        
            for tarefa in tarefas:
                lista_tarefas.insert(0, tarefa.strip())         
    except:
        messagebox.showerror("Erro", "Não é possivel carregar tarefas")
                
            
ctk.CTkLabel(window, text='To-Do App', font=estilo['fontes']['grande'], text_color=estilo['cores']['verde'], anchor='center').pack(pady=10)

botoes_frame = ctk.CTkFrame(window, fg_color='black', width=250, height=30)
botoes_frame.pack(pady=30)

add_tarefas = ctk.CTkButton(botoes_frame, text='Adicionar tarefa', fg_color=estilo['cores']['azul'], width=100, height=30, command=adicionar_tarefa)
add_tarefas.grid(row=0, column=0, padx=20)

del_tarefas = ctk.CTkButton(botoes_frame, text='Remover tarefa', fg_color=estilo['cores']['vermelho'], width=100, height=30, command=remover_tarefa)
del_tarefas.grid(row=0, column=1, padx=20)

tarefa = ctk.CTkEntry(window, placeholder_text='Digite uma nova tarefa', width=250, height=30)
tarefa.pack(pady=10)

ctk.CTkLabel(window, text='Tarefas pendentes', font=estilo['fontes']['media'], text_color=estilo['cores']['azul']).pack(pady=5)

lista_tarefas = Listbox(window, width=32, height=13, font=estilo['fontes']['pequena'])
lista_tarefas.pack(pady=5)

carregar_tarefas()
window.mainloop()