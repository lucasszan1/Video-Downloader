import yt_dlp
from rich.prompt import Prompt
from rich.console import Console

class VideoDownloader:
    def __init__(self, path='./'):
        self.path = path
        self.console = Console()

    def get_video_link(self):
        return Prompt.ask("[bold green]Paste the URL of the video you want to download here [/bold green][bold red]or digit 'q' to quit: [/bold red]")

    def config_options_both(self):
        return {
                'outtmpl': f'{self.path}/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            }
    
    def config_options_only_audio(self):
        return {
                'outtmpl': f'{self.path}/%(title)s.%(ext)s',
                'format': 'bestaudio',
            }
    
    def config_options_only_video(self):
        return {
                'outtmpl': f'{self.path}/%(title)s.%(ext)s',
                'format': 'bestvideo',
            }
    
    def download_video(self, link, ydl_options):
         with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([link])
    
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


        

       
