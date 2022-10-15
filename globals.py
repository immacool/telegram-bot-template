import os


TOKEN = 'YOUR_TOKEN'
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_PATH = os.path.join(FILE_DIR, 'users.json')
PROJECT_NAME = 'YOUR_PROJECT_NAME'
LOG_FILE = os.path.join(FILE_DIR, f'{PROJECT_NAME}.log')

MSG_WELCOME = 'Привет! Я бот.'
MSG_UNKNOWN_COMMAND = 'Неизвестная команда.'