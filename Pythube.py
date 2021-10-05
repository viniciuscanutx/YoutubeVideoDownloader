# Importando Bibliotecas
from pytube import YouTube
from time import sleep
from pytube.cli import on_progress
import moviepy.editor as mp

while True:

    print('----------------------------------------------------------------------')
    print('Olá, escolha o que deseja baixar usando os comandos abaixo.')
    print('----------------------------------------------------------------------')
    print('1- Video\n2- Música')
    print('----------------------------------------------------------------------')
    decis = input('Digite o que você deseja baixar:  ')

    if decis == '1':
        link = input('Cole o link do video do YouTube que deseja baixar: ')
        yt = YouTube(link, on_progress_callback=on_progress)
        title = yt.title
        print('----------------------------------------------------------------------')
        print('Titulo =  ', title)
        print('----------------------------------------------------------------------')
        print('Baixando...')
        video = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        yt.download()
        sleep(1)
        print('----------------------------------------------------------------------')
        print('Arquivo baixado.')
        print('----------------------------------------------------------------------')
        print('\n\n')

    elif decis == '2':
        link = input('Cole o link da Musica do YouTube que deseja baixar: ')
        yt = YouTube(link, on_progress_callback=on_progress)
        title = yt.title
        print('----------------------------------------------------------------------')
        print('Titulo =  ', title)
        print('----------------------------------------------------------------------')
        print('Baixando...')
        video = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        yt.download()
        sleep(1)
        print('----------------------------------------------------------------------')
        print('Convertendo para mp3...')
        print('----------------------------------------------------------------------')
        my_clip = mp.VideoFileClip(r"videotest.mov")
        my_clip.audio.write_audiofile(r"my_result.mp3")

    else:
        print('Opção Incorreta')
        sleep(2)
        break

    print('Obs:\nUse 1 Para Sim\nUse 2 Para Não.')
    print('----------------------------------------------------------------------')
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
