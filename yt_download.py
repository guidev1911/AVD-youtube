import yt_dlp

url = input("Digite a URL do vídeo do YouTube: ")
download_option = input("Digite 'audio' para baixar só o áudio ou 'video' para baixar o vídeo: ").strip().lower()

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  
    'verbose': True,  
    'extractaudio': True, 
    'audioquality': 192,  
    'format': 'bestaudio/best',  
}

if download_option == 'audio':
    ydl_opts['format'] = 'bestaudio/best' 
elif download_option == 'video':
    ydl_opts['format'] = 'best'  
else:
    print("Opção inválida. Escolha 'audio' ou 'video'.")
    exit()
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"{download_option.capitalize()} baixado com sucesso!")
except Exception as e:
    print(f"Erro ao baixar o conteúdo: {e}")
