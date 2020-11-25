from subprocess import Popen , PIPE
import sys

#Takes in command, splits it, fetches result
def run_command(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err

#Process the output error to get search fields
def main(argv):
    #Get the command string from the first argument
    command_string = argv[0]

    #Run the program to check error on
    op, err = run_command(command_string)
    error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    #print(error_message)

    #If there's an error message, get the relevant info to search
    if error_message:
        relevant_info = error_message[2] #will split error into error type, and error info
        #Find what language the script is in
        determine_language()
        #Print all relevant search info
        print("Relevant information for search: ")
        print(relevant_info)
        return(relevant_info)
    else:
        print("There was no error with the script")


#Will extract relevant technology information for the search
def determine_language():
    #Check for npm
    #Check script file extension
    return

if __name__ == "__main__":
    main(sys.argv[1:])

