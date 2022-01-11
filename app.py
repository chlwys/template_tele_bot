from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import csv
import json
import random
import requests

updater = Updater(token='PUT TOKEN HERE')


# Don't touch this code! 
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def fromJson(title):
    with open("./responses.json", "r") as read_file:
        data = json.load(read_file)
    result = data[title]
    return result

def messOut(number, title):
    listIn = fromJson(title)
    strIn = listIn[str(number)]
    return strIn

def getResponse(number, sentiment):
    response = 'default'
    if (sentiment == 0):
        # good
        response = messOut(number, 'good')
    elif (sentiment == 1):
        # netural
        response = messOut(number, 'netural')
    elif (sentiment == 2):
        # mixed
        response = messOut(number, 'mixed')
    elif (sentiment == 3):
        # bad
        response = messOut(number, 'bad')

    return response

def getMessage(update, context):

    # this reads the message sent. you won't need it unless you want to do
    # something with it
    mess = update.message.text
    mess = mess.lower()

    # Change responses in responses.json!
    
    # range of random responses
    randNum = random.randrange(0, 6)

    # sentiment: 0 is good, 1 is netural, 2 is mixed, 3 is bad
    # remove this if you want – right now it directs to good
    sentiment = 0

    namedResponse = getResponse(randNum, sentiment)

    context.bot.sendMessage(chat_id=update.effective_chat.id, text=namedResponse)
        
 

def start(update, context):
    # this is the message when the user starts the program
    startString = "Hello, World!"
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=startString)

message_handler = MessageHandler(Filters.text & (~Filters.command), getMessage)
start_handler = CommandHandler('start', start)

if __name__ == '__main__':

    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

        
    
