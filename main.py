
try:
    import orjson as json
except ImportError:
    import json

import logging

from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from globals import *


def get_users() -> dict:
    with open(USERS_PATH, 'r') as f:
        users = json.load(f)
    return users

async def save_users() -> None:
    with open(USERS_PATH, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)
        
def get_user_id(update: Update):
    return update.effective_user.id


users = get_users()


def auth_required(kwargs: dict = {}):
    def decorator(func):
        async def wrapper(update: Update, context: ContextTypes):
            user_id = get_user_id(update)
            if user_id not in users:
                users[user_id] = {} # create user and add initial data
                await save_users()
                await update.message.reply_text(MSG_WELCOME)
                return
            
            # additional conditions here
            # ...
            
            return func(update, context, user_id)
        return wrapper
    return decorator


@auth_required()
async def start(update: Update, context: ContextTypes, user_id: int):
    await update.message.reply_text('Hello, world!')
    

async def unknown_command(update: Update, context: ContextTypes):
    update.message.reply_text(MSG_UNKNOWN_COMMAND)


async def error_handler(update: Update, context: ContextTypes):
    logging.error(f'{update} ---> {context.error}')


def main() -> None:
    application = (Application.builder().token(TOKEN).build())

    application.add_handler(CommandHandler("start", start))

    # application.add_handler(CallbackQueryHandler(function, pattern='pattern'))

    unknown_handler = MessageHandler(filters.COMMAND, unknown_command)
    application.add_handler(unknown_handler)
    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
