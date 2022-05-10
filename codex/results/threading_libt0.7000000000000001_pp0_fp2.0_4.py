import threading
threading.Thread(target = bot.polling(none_stop=True)).start()

# import requests as req
# import json
#
# url = "https://api.telegram.org/bot{}/".format(token)
#
# def send_message(chat_id, text):
#     url_request = url + "sendmessage?text={}&chat_id={}".format(text, chat_id)
#     req.get(url_request)
#
# def get_updates():
#     url_request = url + "getupdates"
#     response = req.get(url_request)
#     return json.loads(response.content)
#
# def get_message():
#     data = get_updates()
#     chat_id = data["result"][-1]["message"]["chat"]["id"]
#     message_text = data["result"][-1]["message"]["text"]
#     send_message(chat_id, message_text)
#
# while True:
#     send_message
