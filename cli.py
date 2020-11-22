import click
import requests
from pyfiglet import Figlet
from get_error import main as get_error
from get_error import run_command

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
     main(query) #Where query should actually be the command to run a program
    #python cli.py search "python error_test.py"
    #Should run Arlyn's error extraction scripts and return the error search terms
if __name__ == "__main__":
    main()
