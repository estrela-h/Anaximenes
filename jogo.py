import random
import time
import interface
interface

nome_bot = "Anaxímenes"
print(f"Olá, eu sou {nome_bot}, o bot!")

#Fazer função do jogo
"""
#Jogo - Pedra, Papel e Tesoura
start = "S"
while start != "sim" or "não":
  answer_user = (input("Você gostaria de jogar pedra, papel e tesoura? Responda com sim ou não.\n").strip())
  print("-" * 43)
  answer = answer_user.lower()
  if answer == "sim":
    jogar = "S"
    while jogar != "S" or jogar != "P" or jogar != "T":
      jogada_user = str(input("Tecle {S} para jogar pedra.\nTecle {P} para jogar papel.\nTecle {T} para jogar tesoura.\nTecle {X} para sair do jogo.\n> ").upper())
      print("-" * 43)
      time.sleep(1.0)
      jogada_nospace = jogada_user.strip()
      if jogada_nospace == "S" or jogada_nospace == "P" or jogada_nospace == "T":
        opcoes = "SPT"
        jogada_bot = "".join(random.sample
                            (opcoes, 1))
        print(f"{nome_bot} - {jogada_bot} x {jogada_nospace} - {nome_user}")
        if jogada_bot == jogada_nospace:
          print("Deu empate!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "S" and jogada_nospace == "P":
          print(f"{nome_user} ganhou com papel!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "P" and jogada_nospace == "S":
          print(f"{nome_bot} ganhou com papel!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "T" and jogada_nospace == "P":
          print(f"{nome_bot} ganhou com tesoura!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "P" and jogada_nospace == "T":
          print(f"{nome_user} ganhou com tesoura!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "T" and jogada_nospace == "S":
          print(f"{nome_user} ganhou com pedra!\n", "|<<>>|" * 6)
          time.sleep(1.0)
        elif jogada_bot == "S" and jogada_nospace == "T":
          print(f"{nome_bot} ganhou com pedra!\n", "|<<>>|" * 6)
          time.sleep(1.0)
      elif jogada_nospace == "X":
        print("Fim de jogo.\n", "|<<>>|" * 6)
        time.sleep(1.0)
        break
      else:
        print("Não reconheço a sua resposta.")
  elif answer == "não":
    print("Certo.\n", "|<<x>>|" * 6)
    break
  else:
    print("Não reconheço a sua resposta.")"""
print("Até mais! (•u•)")