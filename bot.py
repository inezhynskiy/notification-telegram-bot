# telepot API: https://github.com/nickoala/telepot
import time
import re
import requests
import telepot
from pprint import pprint

class InformBot(telepot.Bot):
    def init(self, token):
        super(InformBot, self).init(token)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        pprint(msg)
        # chat id can be found with help of  @userinfobot, my sample id 617921901
        try:
            if re.search(u"\u041D\u0430\u043B\u043E\u0433", msg["text"]) or "Nalog" in msg["text"]:
                self.sendMessage(617921901, u"New usage of word \u041D\u0430\u043B\u043E\u0433 was detected in group chat Benelux")
        except KeyError:
            print("Received KeyError")

def get_token(secret_path):
    with open(secret_path) as f:
        return f.read().strip()

def main():
    print("Bot ready to use")
    bot = InformBot(get_token(".telegram_bot_secret"))
    bot.message_loop()
    while True:
        time.sleep(10)
if name == "main":
    main()
