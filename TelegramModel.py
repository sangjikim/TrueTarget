from datetime import datetime
import time
import telegram

class TelegramModel():
    
    def __init__(self):
        self.chat_token = "5131391843:AAHQuOkHuRDLUJRV_t4LJlqaeELkh4q5bb0"
        self.bot = telegram.Bot(token = self.chat_token)
        self.user_lst = []
    
    def get_userupdate(self): #유저 업데이트 하는 함수
        updates = self.bot.getUpdates()
        user_set = set()
        for u in updates:
            user_set.add(u.message['chat']['id'])
            self.user_lst = list(user_set)

    def send_message(self,text): #메세지 보내는 함수
        self.get_userupdate()
        for usr in self.user_lst:
            self.bot.sendMessage(chat_id = usr, text=text)