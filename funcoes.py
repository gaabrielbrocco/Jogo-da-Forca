import os
import time
def limparTela():
    os.system('cls')
def aguarde(segundos=1):
    time.sleep(segundos)
def lerStr():
    while True:
        try:
             palavraChave = input("Informe a palavra chave: ")
             if len(palavraChave) <1 or not palavraChave.isalpha():
                  raise Exception
        except Exception:
            print("A palavra chave não pode conter números, espaços ou caracteres especiais.")
            aguarde(2)
            limparTela()
        else:
            break
    palavraChave=palavraChave.lower()
    return palavraChave
def maiorQueUm(mensagem):
     while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print("Informe ao menos dois caracteres!")
            aguarde()
            limparTela()
def limitarStr():
    while True:
        try:
             letra = input("Digite uma letra: ")
             if len(letra) != 1 or not letra.isalpha():
                  raise Exception
        except Exception:
            print("Informe apenas uma letra.")
            aguarde()
            limparTela()
        else:
            break
    letra=letra.lower()
    return letra