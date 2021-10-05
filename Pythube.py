# Importando Bibliotecas
from pytube import YouTube
from time import sleep
from pytube.cli import on_progress

while True:

    print('Olá, escolha o que deseja baixar usando os comandos abaixo.')

    print('1- Video\n2- Música')
    decis = input('Digite o que você deseja baixar:  ')

    if decis == '1':
        link = input('Cole o link do video do YouTube que deseja baixar: ')
        yt = YouTube(link, on_progress_callback=on_progress)
        title = yt.title
        print('Titulo =  ', title)
        print('Baixando...')
        video = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        yt.download()
        sleep(1)
        print('Arquivo baixado.')

    elif decis == '2':
        print('Baixando musica...')

    else:
        print('Opção Incorreta')
        sleep(2)
        break

    print('Use 1 Para sim\nUse 2 Para não.')
    enter = input('Deseja baixar outro video ou musica?  ')

    if enter == '2':
        sleep(1)
        break

    elif enter == '1':
        sleep(1)

    else:
        print('Opção Incorreta!')
        sleep(2)
        break
