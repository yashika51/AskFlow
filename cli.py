import click
import requests
from pyfiglet import Figlet

__author__ = "Team 2 Sprint-4"

@click.group()
def main():
    """
    CLI for querying StackExchange API
    """
f = Figlet(font='slant')
print(f.renderText('AskFlow CLI'))

@main.command()
@click.argument('query')
def search(query):
    pass 

if __name__ == "__main__":
    main()