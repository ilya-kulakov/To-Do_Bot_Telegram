import telebot
import random

token = "Токен бота"

bot = telebot.TeleBot(token)

random_tasks = ["Рандоманя задача", "Рандомная задача", "Рандомная задача", "Рандомная задача"]

HELP = """
/help - Вывести список доступных команд
/add - Добавить задачу в список (Название запрашиваем у пользователя)
/show - Вывести все добавленные задачи
/random - добавить случайную задачу на сегодня
"""
tasks = {}

def add_todo(date, task):
    #Дата есть в словаре
    #Добавляем в список задачу
  if date in tasks:
       tasks[date].append(task)

  else:
      #Даты в словаре нет
      #Добавляем задачу с ключом date
      tasks[date]=[]
      tasks[date].append(task)
#Берется след.идущая функция и регистрируется в каестве обработчика
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "Сегодня"
    task = random.choice(random_tasks)
    add_todo("Сегодня", task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    i = 0
    if date in tasks:
        text = date.upper() + "\n"
        for i, task in enumerate(tasks[date]):
            text = text + "[ "+ (str(i + 1)) + " ] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


#Постоянно обращается к серверам Телеграма
bot.polling(none_stop=True)
