import select
import socket
from sys import argv
from time import sleep
from threading import Thread


def get_msg(sock):
    """
    Получает сообщение и возвращает его.
    """
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print(data.decode('utf-8'))
        except ConnectionResetError:
            print('Сервер закрыт, невозможно получить сообщение')
            sock.close()
            return


def send_msg(sock):
    """
    Получает сообщения от пользователя и отправляет
