# NOME: GABRIEL BROCCO DE OLIVEIRA     RA:1135058
# NOME: JEAN FOLLE VANZ                RA:1134254

from funcoes import limparTela,aguarde,lerStr,maiorQueUm,limitarStr
limparTela()
print('Seja Bem-Vindo ao Protótipo do Jogo da Forca')
aguarde(3)
while True:
    limparTela()
    print('Menu Principal\n(1) Jogar\n(2) Histórico de Partidas\n(3) Sair')
    opcao=input()
    if opcao=='3':
        break
    elif opcao=='1':
        limparTela()
        print('Informe os seguintes dados para iniciar o jogo:')
        desafiante=maiorQueUm('Nome do Desafiante: ')
        competidor=maiorQueUm('Nome do Competidor: ')
        print('Participantes Cadastrados!')
        aguarde(2)
        limparTela()
        print('Desafiante',desafiante,'informe a Palavra-Chave que o Competidor',competidor,'deverá tentar adivinhar: ')
        palavraChave=lerStr()
        print('Agora informe três(3) dicas:')
        dicas=[]
        dicas.append(maiorQueUm('Dica 1:'))
        dicas.append(maiorQueUm('Dica 2:'))
        dicas.append(maiorQueUm('Dica 3:'))
        print('Informações Gravadas')
        aguarde(2)
        limparTela()
        palavraOculta=['*' for letra in palavraChave]
        erros=0
        limiteErros=5
        while '*' in palavraOculta and erros<limiteErros:
            limparTela()
            print(' '.join(palavraOculta))
            print('Você tem',erros,'erros.')
            print('Competidor',competidor,'você deseja jogar ou pedir uma dica?')
            escolhaJogo=input('(1) Para jogar / (2) Para solicitar uma dica: ')
            if escolhaJogo=='1':
                limparTela()
                print(' '.join(palavraOculta))
                letra=limitarStr()
                if letra not in palavraChave:
                    erros+=1
                    print('Errou! Você tem',erros,'erros.')
                    aguarde()
                else:
                    for c in range(len(palavraChave)):
                        if palavraChave[c]==letra:
                            palavraOculta[c]=letra
            elif escolhaJogo=='2':
                if dicas:
                    limparTela()
                    print('Dica:',dicas.pop(0))
                    aguarde(3)
                    print(' '.join(palavraOculta))
                    letra=limitarStr()
                    if letra not in palavraChave:
                        erros+=1
                        print('Errou! Você tem',erros,'erros.')
                        aguarde()
                    else:
                        for c in range(len(palavraChave)):
                         if palavraChave[c]==letra:
                              palavraOculta[c]=letra
                else:
                    print('Não há mais dicas disponíveis')
                    aguarde(2)
            else:
                print('Escolha Inválida!')
                aguarde()
        if '*' not in palavraOculta:
            resultado='Vencedor:',competidor,', Perdedor:',desafiante
            print('O Competidor',competidor,'venceu!')
            aguarde(3)
            limparTela()
            arquivo=open('memorycard.txt','a')
            arquivo.write('Palavra: '+palavraChave+' / '+'Competidor (Vencedor):'+competidor+' / '+'Desafiante (Perdedor): '+desafiante+'\n')
            arquivo.close()
        else:
            resultado='Vencedor:',desafiante,', Perdedor:',competidor
            print('O Desafiante',desafiante,'venceu!','\n','A palavra era',palavraChave)
            aguarde(3)
            limparTela()
            arquivo=open('memorycard.txt','a')
            arquivo.write('Palavra: '+palavraChave+' / '+'Desafiante (Vencedor):'+desafiante+' / '+'Competidor (Perdedor): '+competidor+'\n')
            arquivo.close()
        fim=input('O jogo foi finalizado\n(1) Para jogar novamente\n(0) Para sair\n')
        if fim=='0':
            break
        else:
            pass
    elif opcao=='2':
        limparTela()
        try:
            arquivo = open("memorycard.txt","r")
            dados = arquivo.read()
            print('Segue o histórico de partidas:')
            print(dados)
            arquivo.close()
            aguarde(5)
        except:
            print("Nenhum dado encontrado")
            arquivo = open("memorycard.txt","w")
            arquivo.close()
            aguarde(2)
    else:
        print("Opção Inválida!")
        aguarde(2)