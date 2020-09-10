import config
import telebot

#from aiogram import Bot, Dispatcher, executor, types

from SqlDB import SqlDB

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['zapomni'])
def fill_db(message):
    bot.send_message(message.chat.id, "Пока не могу, сори((")

@bot.message_handler(commands=['teper_ya'])
def change_name(message):
    db = SqlDB('users.db')
    name_set = str(message.text).split('-')
    if (len(name_set) == NameSetSize):
        if (db.check_user(message.from_user.id)):
            # если юзера нет в базе, добавляем его
                db.change_users_name(message.from_user.id, name_set[1])
                bot.send_message(message.chat.id, "Теперь ты " + name_set[1])
        else:
            db.add_user(message.from_user.id, name_set[1])
            bot.send_message(message.chat.id, "Теперь ты " + name_set[1])
    else:
        bot.send_message(message.chat.id, "Теперь ты проклят и тебя зовут None")
    db.close()

@bot.message_handler(commands=['zapomni_menya'])
def add_user(message):
    db = SqlDB('users.db')
    if (not db.check_user(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        name_set = str(message.text).split('-')
        if(len(name_set) == NameSetSize):
            db.add_user(message.from_user.id, name_set[1])
            bot.send_message(message.chat.id, "Теперь ты " + name_set[1])
        else:
            bot.send_message(message.chat.id, "Теперь ты проклят и тебя зовут None")
    else:
        bot.send_message(message.chat.id, "Я тебя помню, ты " + str(db.get_users_name(message.from_user.id)))
    db.close()


@bot.message_handler(commands=['kto_ya'])
def kto_on(message):
    bot.send_message(message.chat.id, "Тааааак сейчас узнаем")
    db = SqlDB('users.db')
    name = db.get_users_name(message.from_user.id)
    print(message.from_user.id)

    if (len(name) > 0):
            bot.send_message(message.chat.id, "Все понятно, ты - " + str(name[0]))
    else:
        bot.send_message(message.chat.id, "Незнаю(((")
    db.close()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()