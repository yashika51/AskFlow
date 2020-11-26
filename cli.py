import click
import requests
from pyfiglet import Figlet, figlet_format
from termcolor import cprint
#from get_error import main as get_error
from get_error import run_command
from search_answers import ask
from colorama import init
import csv
import io

__author__ = "Team 2 Sprint-4"

@click.group()
@click.version_option("1.0.0")
def main():
    """
    CLI for querying StackExchange API
    """
    init(convert=True)
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
        #print("Relevant information for search: ")
        #print(relevant_info)
        a=ask(relevant_info)
        answers=a.get_answer()

        #Print the first answer
        print_answer(1, answers[0])
        print("To show next answer type 'python cli.py next'")
        
        return(relevant_info)
    else:
        print("There was no error with the script")


def print_answer(answer_num, answer):
    colors = ['green','magenta']
    print('\n')
    print("Answer #" + str(answer_num))
    click.echo(click.style(f"        ************** ", fg=colors[0]))
    click.echo(click.style(answer, fg=colors[1]))


@main.command()
def next():
    file = io.open('g4g.csv', encoding="utf-8")
    reader = csv.DictReader(file)

    on_next = False
    case_list = []

    #Create a dictionary from the file
    for row in reader:
        case_list.append(row)

    #Find the next answer
    result_to_return = ""
    count=0
    for row in case_list:
        count+=1
        if on_next:
            row['Current'] = 'True'
            on_next = False
            result_to_return = row
            break
        if row['Current'] == 'True':
            #Check if it's the last one
            if count != len(case_list):
                row['Current'] = 'False'
            on_next = True


    #If there's a next answer
    if result_to_return != "":
        #Print the next answer
        print_answer(result_to_return['Number'], result_to_return['Answer'])
        #print("Answer #" + result_to_return['Number'])
        #print(result_to_return['Answer'])
        #Set the next answer in the file
        file = io.open('g4g.csv', 'w', newline ='', encoding="utf-8") 
        with file: 
            # identifying header   
            header = ['Number', 'Answer', 'Current'] 
            writer = csv.DictWriter(file, fieldnames = header) 
            writer.writeheader() 
            # writing data row-wise into the csv file
            for row in case_list:
                writer.writerow(row)
    else:
        print("There is no next answer. Try to go to a previous answer with [python cli.py previous]")


# Go to previous answer
@main.command()
def previous():
    file = io.open('g4g.csv', encoding="utf-8")
    reader = csv.DictReader(file)

    on_previous = False
    case_list = []

    #Create a dictionary from the file
    for row in reader:
        case_list.append(row)

    #Find the next answer
    result_to_return = ""
    count = 0
    for row in reversed(case_list):
        count+=1
        if on_previous:
            row['Current'] = 'True'
            on_previous = False
            result_to_return = row
            break
        if row['Current'] == 'True':
            #Check if it's the last one
            if count != len(case_list):
                row['Current'] = 'False'
            on_previous = True


    #If there's a next answer
    if result_to_return != "":
        #Print the next answer
        print_answer(result_to_return['Number'], result_to_return['Answer'])
        #print("Answer #" + result_to_return['Number'])
        #print(result_to_return['Answer'])
        #Set the next answer in the file
        file = io.open('g4g.csv', 'w', newline ='', encoding="utf-8") 
        with file: 
            # identifying header   
            header = ['Number', 'Answer', 'Current'] 
            writer = csv.DictWriter(file, fieldnames = header) 
            writer.writeheader() 
            # writing data row-wise into the csv file
            for row in case_list:
                writer.writerow(row)
    else:
        print("There is no previous answer. Try to go to the next answer with [python cli.py next]")
    
if __name__ == "__main__":
    main()
