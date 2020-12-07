import os
import paramiko
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, EC2server, key_file, root, upgrade_command): #This will open automatically user and will to generate upgrade command
        # TODO -

        self.EC2server = EC2server  # comes from def__init__
        self.key_file = key_file # comes from def__init__
        self.root = root # comes from def__init__
        self.command = upgrade_command # comes from def__init__


    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 4 %s" % self.EC2server)
        return self.EC2server

    def upgrade(self):
        # TODO - Use os module to ping the server

        #  The code below will create a ssh client with paramiko and host policy
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ##https://www.programcreek.com/python/example/6085/paramiko.AutoAddPolicy

        # Code below will connect to the server EC2
        ssh_client.connect(hostname=self.EC2server, username=self.root, key_filename=self.key_file)

        # executable code for ssh
        stdin, stdout, stderr = ssh_client.exec_command(self.command)   ## http://docs.paramiko.org/en/stable/api/channel.html

        # Return to close the channel of execution
        result = stdout.readlines() + stderr.readlines()  ## http://docs.paramiko.org/en/stable/api/channel.html

        #  The close code will to disconnect the ssh
        ssh_client.close()

        return result