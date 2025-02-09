# YouTube Downloader com yt-dlp

Este projeto é um script Python que permite baixar vídeos ou áudios do YouTube utilizando a biblioteca `yt-dlp`.

## 📌 Pré-requisitos

Antes de executar o script, certifique-se de ter instalado os seguintes componentes:

- **Python** (versão 3.6 ou superior)
- **yt-dlp**
- **FFmpeg**

### 🔧 Instalando o yt-dlp

```sh
pip install yt-dlp
```

### 🔧 Instalando o FFmpeg

Baixe e instale o `FFmpeg` a partir do site oficial:

- [**Download do FFmpeg**](https://ffmpeg.org/download.html)

Após a instalação, adicione o diretório `bin` do FFmpeg às variáveis de ambiente do sistema:

#### 📌 No Windows:

1. Extraia os arquivos baixados para um diretório (exemplo: `C:\\ffmpeg`)
2. Adicione `C:\\ffmpeg\\bin` ao **Path** nas variáveis de ambiente do sistema.

#### 📌 No Linux:

```sh
sudo apt install ffmpeg
```

## 🚀 Como Usar

1. Execute o script Python:

```sh
python yt_download.py
```

2. Insira a URL do vídeo do YouTube quando solicitado.
3. Escolha a opção de download:
   - Digite **audio** para baixar apenas o áudio.
   - Digite **video** para baixar o vídeo completo.
4. O arquivo será baixado no mesmo diretório do script.

## 🤝 Contribuição

Fique à vontade para contribuir com melhorias! Basta abrir um **Pull Request** ou relatar problemas na aba **Issues**.

