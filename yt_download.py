import yt_dlp
import tkinter as tk
from tkinter import messagebox

def baixar():
    url = entry_url.get()
    opcao = var_opcao.get()

    if not url:
        messagebox.showerror("Erro", "Digite a URL do vídeo.")
        return

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True,
    }

    if opcao == '1':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    elif opcao == '2':
        ydl_opts['format'] = 'best'
    else:
        messagebox.showerror("Erro", "Selecione uma opção válida.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar: {e}")

janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("400x200")

tk.Label(janela, text="URL do vídeo:").pack(pady=5)
entry_url = tk.Entry(janela, width=50)
entry_url.pack()

tk.Label(janela, text="Escolha o tipo de download:").pack(pady=5)

var_opcao = tk.StringVar()
tk.Radiobutton(janela, text="Áudio (MP3)", variable=var_opcao, value='1').pack()
tk.Radiobutton(janela, text="Vídeo", variable=var_opcao, value='2').pack()

tk.Button(janela, text="Baixar", command=baixar).pack(pady=10)

janela.mainloop()
