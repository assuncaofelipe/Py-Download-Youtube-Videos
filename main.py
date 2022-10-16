from pytube.cli import on_progress
from pytube import YouTube

link = input('Entre com seu link: ')

# para mostrar o progresso do download
yt = YouTube(link, on_progress_callback=on_progress)

# para mostrar o título de video
print('titulo: ', yt.title)

# para mostrar que ja iniciou o download
print('baixando...')

# faz o download da melhor resolução
ys = yt.streams.get_highest_resolution().download()

print('Baixado!', link)