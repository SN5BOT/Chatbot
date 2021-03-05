from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    return msg
    

update_id = None

updates = bot.get_updates(offset=update_id)
updates = updates["result"]
if updates:
    update_id = updates[len(updates)-1]["update_id"]
    try:
        message = str(updates[len(updates)-1]["message"]["text"])
        print(message)
    except:
        message = None
    from_ = updates[len(updates)-1]["message"]["from"]["id"]
    reply = make_reply(message)
    print(from_,reply)
    bot.send_message(reply, from_)