from rich.console import Console
from menu import MainMenu
from video_audio import VideoDownloader
from utilities import clear_terminal


clear_terminal()
console = Console()

def main():

    menu = MainMenu
    downloader = VideoDownloader()
    
    while True:
        choice = menu.main_menu()
        if choice == "0":
            console.print("[bold red] Quit [/bold red]")
            break
        elif choice == "1":
            downloader.get_download_both()
        elif choice == "2":
            downloader.get_download_video()
        elif choice == "3":
            downloader.get_download_audio()

if __name__ == "__main__":
    main()
