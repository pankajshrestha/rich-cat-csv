import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")

parser = argparse.ArgumentParser(description='Cat CSV file with Rich')
parser.add_argument('--log_level', default='INFO')
parser.add_argument('--csv_file_path', required=True)

args = parser.parse_args()
csv_file_path = args.csv_file_path

df = pd.read_csv(csv_file_path)
for col in df.columns:
    table.add_column(col)


for row in df.itertuples(index=False, name=None):
    row = [str(item) for item in row]
    table.add_row(*list(row))

console.print(table)
