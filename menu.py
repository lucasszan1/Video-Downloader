from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console

console = Console()

class MainMenu ():
    def main_menu():
        while True:
            console.print(Panel.fit('[bold red]VIDEO DOWNLOADER[/bold red]', border_style="Black"))
            console.print("[bold green][ 1 ]Download Video and Audio[/bold green]")
            console.print("[bold green][ 2 ]Download Video[/bold green]")
            console.print("[bold green][ 3 ]Download Audio[/bold green]")
            console.print("[bold red][ 0 ]EXIT[/bold red]")
            choice = Prompt.ask("[bold green]>>>[/bold green]")
            return choice



        


