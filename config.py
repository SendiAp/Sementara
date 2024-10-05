import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", "20211998"))

    API_HASH = os.environ.get("API_HASH", "beeeebe74c0c467c47c6ac4a1c9d75b5")

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6626958529:AAEPm42AevBDyBZQ5sM9i1zpElktUBwHGKM")

    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME")
