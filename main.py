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
    EC2server = '18.218.148.230'
    key_location= "C:\\Users\\FG10\\.ssh\\id_rsa"
    root = "ubuntu"
    update= 'sudo apt update && sudo apt upgrade'  ## https://www.codegrepper.com/code-examples/objectivec/sudo+apt-get+update+%26%26+sudo+apt-get+upgrade
    EC2server = Server(EC2server, key_location, root, update)
    # TODO - Call Ping method and print the results

###http://docs.paramiko.org/en/stable/api/client.html
    print("\nUpdating server using ssh from paramiko")
    ssh_result = EC2server.upgrade()
    print(''.join(ssh_result))
    print(EC2server.ping())

