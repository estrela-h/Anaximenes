from tkinter import *

#Inicialização e configuração da janela 
janela1 = Tk()
janela1.title("Anaxímenes, o B0T")
janela1.geometry('500x500')
janela1.config(background="LightSkyBlue2")

apresentacao = Label(janela1, text="Olá, eu sou Anaxímenes,\n o B0T.", font=("Open Sans", 20), background="LightSkyBlue2")
apresentacao.pack(pady=20)
controle_perguntas, nome_user = 0, ""

#----------------------------------Conversação----------------------------------------|
#Função para mudar a cor do frame baseado na resposta do usuário
def cor(cor):
    cor_minuscula = cor.lower()
    if cor_minuscula == "azul":
        frame.config(background="DodgerBlue2")
        answer.config(background="DodgerBlue2")
        pergunta.config(background="DodgerBlue2")
    elif cor_minuscula == "vermelho":
        frame.config(background="red3")
    elif cor_minuscula == "verde":
        frame.config(background="forest green")
    elif cor_minuscula == "rosa":
        frame.config(background="maroon2")
    elif cor_minuscula == "roxo":
        frame.config(background="hot pink")
    else:
        answer.config(text="Não conheço essa cor.")

#Função de resposta ao usuário
def resposta():
    global controle_perguntas
    if res_user.get() and controle_perguntas == 0:
        answer.config(text=f"Olá, {res_user.get()}.")
        nome_user = res_user.get()
        res_user.delete(0, END)
        controle_perguntas += 1
    elif res_user.get() and controle_perguntas == 1:
        idade = int(res_user.get())
        answer.config(text=f"Nós temos quase {idade-1} \nano(s) de diferença.")
        res_user.delete(0, END)
        controle_perguntas += 1
    elif res_user.get() and controle_perguntas == 2:
        cor(res_user.get())
        answer.config(text=f"Eu também gosto\nde {res_user.get()}!")
        res_user.delete(0, END)
    else:
        answer.config(text="Você esqueceu\n de responder.")

#Função para continuar a conversa
def seguir():
    global controle_perguntas
    apresentacao.config(text="Bora conversar?", font=("Open Sans", 14))
    if controle_perguntas == 0:
        pergunta.config(text="Qual é o seu nome?")
        frame_input.pack(pady=20)
        answer.pack(pady=20)
        botao_seguir.pack(pady=20)
    elif controle_perguntas == 1:
        pergunta.config(text="Qual é a sua idade?")
        answer.config(text="")
    elif controle_perguntas == 2:
        pergunta.config(text="Qual a sua cor favorita?")
        answer.config(text="")

#Frame onde está a pergunta, resposta e botão de confirmação
frame = Frame(janela1, bg="sea green", width=700, )
frame.pack(pady=15)

#Pergunta
pergunta = Label(frame, text="", font=("Arial", 20), background="sea green", fg="white")
pergunta.pack(pady=20)

#Input nome do usuário
frame_input = Frame(frame, background="sea green", bd=5)
frame_input.pack_forget()

space1 = Label(frame_input, text="  ", background="sea green")
space1.grid(column=2, row=0)
space2 = Label(frame_input, text="  ", background="sea green")
space2.grid(column=0, row=0)
space3 = Label(frame_input, text="  ", background="sea green")
space3.grid(column=4, row=0)

res_user = Entry(frame_input, font=("Open Sans", 14))
res_user.grid(column=1, row=0)

#Botão de confirmação do nome
botao_confirmar = Button(frame_input, text="Confirmar", background="light sea green", command=resposta)
botao_confirmar.grid(column=3, row=0)

#Resposta do B0T
answer = Label(frame, text="", font=("Open Sans", 14), background="sea green")
answer.pack_forget()

#Botão para avançar na conversa
botao_seguir = Button(janela1, text="Seguir", background="aquamarine2", command=seguir)
botao_seguir.pack(side=RIGHT, padx=10, pady=50)

janela1.mainloop()