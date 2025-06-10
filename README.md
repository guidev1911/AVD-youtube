
# YouTube Downloader com yt-dlp

Este projeto é um script Python que permite baixar vídeos ou áudios do YouTube utilizando a biblioteca `yt-dlp`.

> ⚠️ **Este programa foi desenvolvido para rodar apenas no sistema operacional Windows.**

## 📌 Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes componentes:

### 🔧 Instalando o FFmpeg (opcional, porém recomendado)

O FFmpeg é necessário para garantir a melhor qualidade de áudio e vídeo nos downloads.  
Sem o FFmpeg, o programa ainda funcionará e fará os downloads, mas apresentará um erro informando a ausência do FFmpeg, e a qualidade dos arquivos pode ser inferior.

Baixe e instale o `FFmpeg` a partir do site oficial:

- [**Download do FFmpeg**](https://ffmpeg.org/download.html)

Após a instalação, adicione o diretório `bin` do FFmpeg às variáveis de ambiente do sistema:

#### 📌 Como configurar no Windows:

1. Extraia os arquivos para um diretório (por exemplo: `C:\ffmpeg`)
2. Adicione o caminho `C:\ffmpeg\bin` à variável de ambiente **Path** do sistema.

---

## 🚀 Como Usar

1. Navegue até a pasta `dist/` e execute o programa `yt_dowloader.exe`.
2. Insira a URL do vídeo do YouTube quando solicitado.
3. Escolha a opção de download:
   - Selecione **audio** para baixar apenas o áudio.
   - Selecione **video** para baixar o vídeo completo.
4. Os arquivos baixados serão salvos automaticamente na pasta `dist/`.

---

## 📁 Estrutura

- `dist/yt_dowloader.exe` → Arquivo executável principal.
- `dist/` → Pasta onde os vídeos e áudios baixados serão salvos.

---

## 🤝 Contribuição

Fique à vontade para contribuir com melhorias! Basta abrir um **Pull Request** ou relatar problemas na aba **Issues**.
