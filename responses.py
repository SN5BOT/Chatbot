from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message == '/start':
        return 'Currently available text to chat:\n1. Hello\n2. Hi\n3. Sup\n4. Who are you?\n5. Who are you\n6. Time\n7. Time?\nType any one of them:'
    elif user_message in ('hello','hi','sup'):
        return 'How are you doing'
    elif user_message in ('Hello','Hi','hello','hi'):
        return 'Hi, Loyal, do you need me to do translation for you?'
    elif user_message in ('How are you','how are you'):
        return 'I'm very well. Thanks! How are you doing?'
    elif user_message in ('who are you?','who are you'):
        return 'I am a bot made by Akash Papnai'
    elif user_message in ('time','time?'):
        return datetime.now().strftime("%d/%m/%y, %H:%M:%S")
    return 'I do not understand what you are saying'
