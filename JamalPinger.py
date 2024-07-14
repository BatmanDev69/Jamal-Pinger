import os
import subprocess
from rich import print
from rich.console import Console
from rich.panel import Panel

# Ascii Art
ascii_art = r"""
     ____.                     .__    __________.__                             
    |    |____    _____ _____  |  |   \______   \__| ____    ____   ___________ 
    |    \__  \  /     \\__  \ |  |    |     ___/  |/    \  / ___\_/ __ \_  __ \
/\__|    |/ __ \|  Y Y  \/ __ \|  |__  |    |   |  |   |  \/ /_/  >  ___/|  | \/
\________(____  /__|_|  (____  /____/  |____|   |__|___|  /\___  / \___  >__|   
              \/      \/     \/                         \//_____/      \/       
"""

# Function to ping an IP address
def ping_ip(ip, repeat):
    count = "-t" if repeat else "-n 1"
    try:
        while True:
            # Run the ping command
            process = subprocess.Popen(f"ping {count} {ip}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    if "Request timed out" in output or "Destination host unreachable" in output:
                        print("[bold green]Ip down[/bold green]")
                    else:
                        print(f"[bold green]{output.strip()}[/bold green]")

            if not repeat:
                break
    except KeyboardInterrupt:
        print("[bold red]\nPing stopped by user.[/bold red]")

# Main function
def main():
    console = Console()
    
    # Print the ASCII Art in pink
    console.print(Panel(ascii_art, style="bold magenta"))
    
    # Get IP to ping
    console.print("Ip to ping >> ", style="bold purple", end="")
    ip = input().strip()
    
    # Validate IP format
    if not ip:
        console.print("[bold red]Invalid IP address. Exiting...[/bold red]")
        return
    
    # Ask if repeat ping
    console.print("repeat ping? (y/n) >> ", style="bold purple", end="")
    repeat = input().strip().lower() == 'y'
    
    # Ping the IP address
    ping_ip(ip, repeat)

if __name__ == "__main__":
    main()
