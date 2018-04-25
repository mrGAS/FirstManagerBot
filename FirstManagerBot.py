import requests
from time import sleep

url = "https://api.telegram.org/bot595571927:AAHEKfvwt5nxYSHf8fi75SUhZPYX5L_wBBQ/"

proxies = {'https': 'http://162.243.107.45:1080'}

def get_updates_json (request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', proxies=proxies)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def senf_mess (chat, text):
    params = {'chat_id': chat, 'text': text}
    response = request.post(url + 'sendMessage', data = params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while true:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()
