import click
import requests
from pyfiglet import Figlet
#from get_error import main as get_error
from get_error import run_command
from search_answers import ask
import csv
import io

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
        print("")
        print("First answer:")
        print(answers[0])
        print("To show next answer type 'cli.py next'")
        
        return(relevant_info)
    else:
        print("There was no error with the script")

@main.command()
def next():
    #file = io.open('g4g.csv', 'r', newline ='', encoding="utf-8") 
    reader = csv.DictReader(io.open('g4g.csv', encoding="utf-8"))
    dictobj = next(reader)
    print(dictobj)
if __name__ == "__main__":
    main()
