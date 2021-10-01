# from rich.progress import track
from rich.console import Console
from time import sleep

# for tarefa in track(range(10), 'Processando...'):
#     sleep(2)

console = Console()

def criar_arquivo():
    for i in range(10):
        with open(f'arquivo{i}.txt', 'w') as file:
            file.write('Criamos um novo arquivo')
            sleep(1)
            console.log(f'Tarefa {i} finalizada!')

with console.status('[green]Realizando a tarefa...[/]') as arquivo:
    criar_arquivo()
    