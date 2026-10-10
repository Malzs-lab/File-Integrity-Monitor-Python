import tkinter as tk
import hashlib
import threading
import time
from tkinter import messagebox
monitorando = False
caminho = r"C:\Users\email\OneDrive\Documentos\Desktop\CyberSecurityProjects\teste.txt"

def motor_de_monitoramento():
    with open(caminho, "rb") as f:
        conteudo = f.read()
    hash_conteudo = hashlib.sha256(conteudo).hexdigest()

    statuslabel.config(text="Status: Vigiando arquivo...", fg="green")

    while monitorando:
        time.sleep(3)
        if not monitorando:
            break
        with open(caminho, "rb") as f:
            conteudo = f.read()
        hash_conteudo_atual = hashlib.sha256(conteudo).hexdigest()
        if not monitorando:
                    break
        if hash_conteudo_atual != hash_conteudo:
            statuslabel.config(text="Status: Anomalia detectada!", fg="red")
            print("\033[33m O conteúdo do arquivo foi alterado!")
            print("\033[32mHash original:", f"{hash_conteudo}")
            print("\033[31mHash atual:", f"{hash_conteudo_atual}")
            print("\033[33m-------------------------------")
            hash_conteudo = hash_conteudo_atual
def vigiararquivos():
    global monitorando
    monitorando = True
    botaoiniciar.config(state="disabled", text="Monitor Ativo")
    botaoparar.config(state="normal")
    threading.Thread(target=motor_de_monitoramento, daemon=True).start()

def parar_monitoramento():
    global monitorando
    monitorando = False
    statuslabel.config(
        text="Status: Aguardando possível breach...", fg="yellow"
    )
    botaoiniciar.config(state="normal", text="Iniciar Monitoramento")
    botaoparar.config(state="disabled")

janela = tk.Tk()
janela.configure(bg="black")
janela.title("Monitoramento de Arquivos Confidenciais")
janela.geometry("500x400")

titulo = tk.Label(janela, text="Monitoramento de Arquivos Confidenciais", font=("OpenSans", 18, "bold"), fg="green", bg="black")
titulo.pack(pady=10)

statuslabel = tk.Label(janela, text="Status: Aguardando possível breach...", font=("OpenSans", 14), fg="yellow", bg="black")
statuslabel.pack(pady=10)

botaoiniciar = tk.Button(janela, text="Iniciar Monitoramento", font=("OpenSans", 14, "bold"), command=vigiararquivos, fg="gray", bg="black")
botaoiniciar.pack(pady=10)

botaoparar = tk.Button(janela, text="Parar para Investigação", font=("OpenSans", 14, "bold"), command=parar_monitoramento, fg="red", bg="black", state="disabled")
botaoparar.pack(pady=10)

janela.mainloop()