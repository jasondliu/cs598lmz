import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()
import time
import threading

from ai_chatbot.app import start_app
from ai_chatbot.actions import actions
from ai_chatbot.log import logger
from ai_chatbot.tasks.training import train_agent
from ai_chatbot.tasks.send_messages import send_messages
from ai_chatbot.tasks.prediction import predict_new_messages


def main():

    instruction_actions = {
        "head": actions.head_action,
        "simple": actions.simple_action,
        "add_to_circle": actions.add_to_circle_action,
        "detect_name": actions.detect_name_action,
        "name": actions.name_action
    }

    while True:
        # Wait for running all ai_chatbot
        while len(threading.enumerate()) > 1:
            time.sleep(0.5)

        # Start ai_chatbot
        logger.debug("Starting application...")
       
