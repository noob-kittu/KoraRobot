import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "You are gorgeous.",
    "You are lovely.",
    "You do not need makeup. You are already so naturally beautiful.",
    "You have the most beautiful smile.",
    "You have such a talent for putting together the most gorgeous outfits.",
    "There is something about being with you that makes me want to be the best person that I can be.",
    "You are the reason that I wake up every day with a huge smile on my face.",
    "You are my greatest adventure.",
    "Without you standing by my side, my life would have no meaning or purpose.",
    "Whenever I need a friend to talk to, you are the first person I turn to.",
    "ou are the very meaning of friendship.",
    "You are what I call a forever friend.",
    "True friends are like diamonds. And you are the most precious diamond of all.",
    "You cannot choose your family, but you can choose your friends. And I sure am glad that I chose you. Thank you for being my friend.",

  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /respect  🤬.
"""

__mod_name__ = "Respect"

DARK_HANDLER = DisableAbleCommandHandler("respect", respect)

dispatcher.add_handler(RESPECT_HANDLER)
