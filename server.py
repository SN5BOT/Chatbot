from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg, name):
    if msg is not None and "hello".upper() in msg.upper():
        return "Hi"
    return "Hello "+name
    

update_id = None

updates = bot.get_updates(offset=update_id)
updates = updates["result"]
if updates:
    update_id = updates[len(updates)-1]["update_id"]
    try:
        message = str(updates[len(updates)-1]["message"]["text"])
        name = str(updates[len(updates)-1]['message']["chat"]["first_name"])
        print(message)
    except:
        message = None
        name = None
    from_ = updates[len(updates)-1]["message"]["from"]["id"]
    reply = make_reply(message, name)
    print(from_,reply)
    bot.send_message(reply, from_)