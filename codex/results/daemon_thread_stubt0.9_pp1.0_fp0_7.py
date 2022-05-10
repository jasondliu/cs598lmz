import sys, threading

def run():
    while True:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(api.tasks.polling())
        sleep(5)

threading.Thread(target=run).start()
print("Bot is running...")
