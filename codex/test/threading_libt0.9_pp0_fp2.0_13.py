import threading
threading.stack_size(1)

# Global variables
PUSH_URL = "https://api.pushbullet.com/v2/pushes"

# BLE Scanner (needs to be global or else BLE scan doesn't work)
adv_scanner = Raw_BLE_Scanner()

def push_message(title: str, body: str, api_key: str) -> None:
    """ Push a message to your phone/tablet

    :param title: Title of the notification
    :param body: Message of the notification
    :param api_key: Pushbullet API key
    :return: None
    """
    headers={'Access-Token': api_key, 'Content-Type': 'application/json'}
    data_json = json.dumps({"type": "note", "title": title, "body": body})
    requests.post(PUSH_URL, data=data_json, headers=headers)
    return

