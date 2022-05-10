import codecs
codecs.register_error('myerror', codecs.ignore_errors)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это бот, который помогает посчитать калории в еде. Чтобы начать, отправьте мне фотографию блюда и вашу дневную норму калорий.")
    bot.send_message(message.chat.id,"Чтобы изменить дн
