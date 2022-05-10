import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set to True to see thread on each line of logging
LOG_THREAD_INFO = False

# Webfinger Client Config
ENABLE_BLOCKCHAIN_HOSTNAME = False
FALLBACK_BLOCKCHAIN_SERVERS = []

# Enable RabbitMQ or Rocket.chat
ENABLE_ROCKETCHAT = True
ROCKET_CHAT_URL = 'http://brain.komtrade.com'

# Important that this is the same as is configured under Settings -> Advanced View -> RabbitMQ in Rocket.chat
# Configured by setting RABBIT_MQ_HOST=ip:port, while provisioning
#ROCKET_CHAT_MESSAGE_QUEUE = 'livechat'

# Assume requested, in case it is not being sent by rocketchat server
# If forced, it will always be added as context
# If not forced but configured as a rasa default, it will be added as context
# If not forced and not default, will only be added
