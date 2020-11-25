import click
import requests
from pyfiglet import Figlet, figlet_format
from termcolor import cprint
#from get_error import main as get_error
from get_error import run_command
from search_answers import ask

__author__ = "Team 2 Sprint-4"

@click.group()
def main():
    """
    CLI for querying StackExchange API
    """
    
cprint(figlet_format('AskFlow CLI', font='slant'), "cyan")

@main.command()
@click.argument('query')
def search(query):
    #python cli.py search "python error_test.py"
    #Should run Arlyn's error extraction scripts and return the error search terms
    #Get the command string from the first argument
    command_string = query

    #Run the program to check error on
    op, err = run_command(command_string)
    error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    #print(error_message)

    #If there's an error message, get the relevant info to search
    if error_message:
        relevant_info = error_message.split(":") #will split error into error type, and error info

        #Print all relevant search info
        print("Relevant information for search: ")
        print(relevant_info)
        a=ask(relevant_info)
        answers=a.get_answer()
        print(answers[0])
        return(relevant_info)
    else:
        print("There was no error with the script")

        
if __name__ == "__main__":
    main()
