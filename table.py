from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title='Filmes favoritos')

table.add_column('Nome', justify='left', style='red')
table.add_column('Data de Lançamento', style='green')
table.add_column('Faturamento' , style='purple')

table.add_row('Piratas do caribe'
, '2005', '1293931031')
table.add_row('Homem de ferro'
, '2002', '99999999999')

console.print(table)