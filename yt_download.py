import yt_dlp

url = input("Digite a URL do vídeo do YouTube: ")
print("Escolha o tipo de download:")
print("1 - Áudio")
print("2 - Vídeo")
opcao = input("Digite 1 ou 2: ").strip()

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'verbose': True,
}

if opcao == '1':
    download_option = 'áudio'
    ydl_opts.update({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    })
elif opcao == '2':
    download_option = 'vídeo'
    ydl_opts['format'] = 'best'
else:
    print("Opção inválida. Digite 1 para áudio ou 2 para vídeo.")
    exit()

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"{download_option.capitalize()} baixado com sucesso!")
except Exception as e:
    print(f"Erro ao baixar o conteúdo: {e}")
