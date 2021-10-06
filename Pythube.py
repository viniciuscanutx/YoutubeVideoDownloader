# Importando Bibliotecas
from pytube import YouTube
from time import sleep
from pytube.cli import on_progress

while True:

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

    print('Obs:\nUse 1 Para Sim\nUse 2 Para Não.')
    print('----------------------------------------------------------------------')
    enter = input('Deseja baixar outro video?: ')

    if enter == '2':
        sleep(1)
        break

    elif enter == '1':
        sleep(1)

    else:
        print('Opção Incorreta!')
        sleep(2)
        break
