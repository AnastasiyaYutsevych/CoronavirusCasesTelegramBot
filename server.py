from bot import telegram_chatbot
from scraper import cases


bot = telegram_chatbot("config.cfg")


def make_reply(msg,from_):
    reply = None
    if msg is not None:
        if msg == "/cases":
            bot.send_message("Please enter the country you would like to see data on",from_)
        else:
            if msg.lower()== "usa" or msg.lower()== "united states":
                msg = 'us'
            data = cases(msg)
            reply= data.stats()
        if msg== '/start':
            reply= "Hi \nThis is coronavirus cases bot \nType /cases to see the number of cases in your country"
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message,from_)
            bot.send_message(reply, from_)
