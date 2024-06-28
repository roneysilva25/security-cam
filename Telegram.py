import json
from requests import get

class Telegram:
    def __init__(self):
        __secretsFile = json.loads(open("secrets.json", "r", encoding="utf-8").read())
        self.__telegramToken = __secretsFile["telegram-token"]
        self.__telegramId = __secretsFile["telegram-id"]
        self.__caption = "Movimento Detectado"
    
    def sendFile(self, path, type):
        if type == "foto":
            with open(path, 'rb') as im:
                foto = {'photo':im}
                get(f'https://api.telegram.org/bot{self.__telegramToken}/sendPhoto?chat_id={self.__telegramId}&caption={self.__caption}', files=foto)
        elif type == "video":    
            with open(path, 'rb') as v:
                vid = {'video':v}
                get(f'https://api.telegram.org/bot{self.__telegramToken}/sendVideo?chat_id={self.__telegramId}', files=vid)