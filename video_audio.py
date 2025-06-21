import yt_dlp
from rich.prompt import Prompt
from rich.console import Console

console = Console()
class VideoDownloader:
    def __init__(self, path_both="videoaudio", path_audio="audio", path_video="video"):
        self.paths = {
            "both": path_both,
            "video": path_video,
            "audio": path_audio,
        }
        self.console = Console()

#Função que obtem o link que o usuario mandar atraves do promp.ask.
    def get_video_link(self):
        return Prompt.ask("[bold green]Paste the URL of the video you want to download here [/bold green][bold red]or digit 'q' to quit: [/bold red]")


#Função que monta o outtmpl para qualquer das situações escolhidas pelo usuario
    def output_template(self, type: str) -> str :
        return f"{self.paths[type]}/%(title)s.%(ext)s'"


#função que define as configurações de download, essa é para download do video e do audio.
    def config_options_both(self):
        return {
                'outtmpl': self.output_template('both'),
                'format': 'bestvideo+bestaudio/best',
                'quiet': True,
                'no_warnings': True,
                'merge_output_format': 'mp4',
            }
    
#função que define as configurações de download, essa é somente para o audio.
    def config_options_only_audio(self):
        return {
                'quiet': True,
                'no_warnings': True,
                'outtmpl': self.output_template('audio'),
                'format': 'bestaudio',
            }
    
#Função que define as configurações de download, essa é somente para o video.
    def config_options_only_video(self):
        return {
                'outtmpl': self.output_template('video'),
                'format': 'bestvideo',
                'quiet': True,
                'no_warnings': True,
            }
    
#Função que realiza o download do video.
    def download_video(self, link, ydl_options):
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([link])

#Função que faz o download usando a função que tem como a configuração o download de ambos video/audio.
    def get_download_both(self):
        while True:
            link = self.get_video_link()
            if link.strip().lower() == 'q':
                self.console.print("[bold red]Returning to menu[/bold red]")
                break
            
            options = self.config_options_both()
            try:
                self.download_video(link, options)
                self.console.print("[bold green]Download completed![/bold green]")
            except Exception as e:
                self.console.print(f"[bold red]Download failed: {e}[/bold red]")

#Função que faz o download usando a função que tem como a configuração o download somente de audio.
    def get_download_audio(self):
        while True:
            link = self.get_video_link()
            if link.strip().lower() == 'q':
                self.console.print("[bold red]Returning to menu[/bold red]")
                break
            
            options = self.config_options_only_audio()
            try:
                self.download_video(link, options)
                self.console.print("[bold green]Download completed![/bold green]")
            except Exception as e:
                self.console.print(f"[bold red]Download failed: {e}[/bold red]")

#Função que faz o download usando a função que tem como a configuração o download somente de video.
    def get_download_video(self):
        while True:
            link = self.get_video_link()
            if link.strip().lower() == 'q':
                self.console.print("[bold red]Returning to menu[/bold red]")
                break
            
            options = self.config_options_only_video()
            try:
                self.download_video(link, options)
                self.console.print("[bold green]Download completed![/bold green]")
            except Exception as e:
                self.console.print(f"[bold red]Download failed: {e}[/bold red]")


        

       
