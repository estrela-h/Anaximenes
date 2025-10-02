import random
from tkinter import *
from interface import answer

nome_bot = "Anaxímenes"
print(f"Olá, eu sou {nome_bot}, o bot!")

def pedra_papel_tesoura(jogada_user, nome_user, jogada_bot):
    if jogada_user == "pedra":
        answer.config(text=f"{nome_user} ganhou com {jogada_user}.")
    elif jogada_user == "papel":
        answer.config(text=f"{nome_user} ganhou com {jogada_user}.")
    elif jogada_user == "tesoura":
        answer.config(text=f"{nome_user} ganhou com {jogada_user}.")
    else:
        answer.config(text=f"Anaxímenes ganhou com {jogada_bot}.")
