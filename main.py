# This is the template code for the CNA337 Final Project
# Francisco Espino, fgespino@student.rtc.edu
# CNA 337 Fall 2020

from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Francisco")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    EC2server = Server('3.19.63.224')
    # TODO - Call Ping method and print the results
    print(EC2server.ping())