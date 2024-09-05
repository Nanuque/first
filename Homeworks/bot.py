import telebot # type: ignore
import random

bot = telebot.TeleBot("7433701467:AAH5xY7kgEOoCpkcw50vg6gLDx6tEUyB3dA")
#/start - Бот має привітатись
@bot.message_handler(commands=["start", "hello"])
def start_handler(message:telebot.types.Message):
    bot.send_message(message.chat.id, "Hello, I am bot !!!")
# Списки для зберігання запитів, скарг та пропозицій
questions = []
reports = []
offers = []

# ID адміністратора
admin_id ='1029994066'   # Вставте свій chat ID

# Обробка команд від користувачів
@bot.message_handler(commands=['question'])
def handle_question(message):
    question_text = message.text[len('/question '):]
    questions.append(question_text)
    bot.send_message(admin_id, f"Нове запитання: {question_text}")
    bot.reply_to(message, "Ваше запитання було надіслане адміністратору.")

@bot.message_handler(commands=['report'])
def handle_report(message):
    report_text = message.text[len('/report '):]
    reports.append(report_text)
    bot.send_message(admin_id, f"Нова скарга: {report_text}")
    bot.reply_to(message, "Ваша скарга була надіслана адміністратору.")

@bot.message_handler(commands=['offer'])
def handle_offer(message):
    offer_text = message.text[len('/offer '):]
    offers.append(offer_text)
    bot.send_message(admin_id, f"Нова пропозиція: {offer_text}")
    bot.reply_to(message, "Ваша пропозиція була надіслана адміністратору.")

# Обробка команд від адміністратора
@bot.message_handler(commands=['allquestions'])
def handle_all_questions(message):
    if str(message.chat.id) == admin_id:
        if questions:
            all_questions = "\n".join(questions)
            bot.send_message(admin_id, f"Усі запитання:\n{all_questions}")
        else:
            bot.send_message(admin_id, "Немає запитань.")
    else:
        bot.reply_to(message, "Ця команда доступна лише адміністратору.")

@bot.message_handler(commands=['allreports'])
def handle_all_reports(message):
    if str(message.chat.id) == admin_id:
        if reports:
            all_reports = "\n".join(reports)
            bot.send_message(admin_id, f"Усі скарги:\n{all_reports}")
        else:
            bot.send_message(admin_id, "Немає скарг.")
    else:
        bot.reply_to(message, "Ця команда доступна лише адміністратору.")

@bot.message_handler(commands=['alloffers'])
def handle_all_offers(message):
    if str(message.chat.id) == admin_id:
        if offers:
            all_offers = "\n".join(offers)
            bot.send_message(admin_id, f"Усі пропозиції:\n{all_offers}")
        else:
            bot.send_message(admin_id, "Немає пропозицій.")
    else:
        bot.reply_to(message, "Ця команда доступна лише адміністратору.")

@bot.message_handler(commands=["help"])
def help_handler(message: telebot.types.Message):
    help_text = (
        "Ось список команд, які я можу виконувати:\n"
        "/start - Почати спілкування з ботом\n"
        "/help - Показати цей список команд\n"
        "/number - Отримати випадкове число від 0 -100\n"
        "/coin - Кинути монету\n"
        "/question - Задати питання\n"
        "/report - Поскаржитись\n"
        "/offer - Запропонувати\n"
        
    )
    bot.send_message(message.chat.id, help_text)

    
@bot.message_handler(commands=['coin']) # моливість кинути монетку і отримати рандомний результат
def coin_handler(message):
    result = random.choice(["Орел", "Решка"])
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['number'])
def number_handler(message):
    result = random.randint(0, 100)
    bot.send_message(message.chat.id, f"Ваше випадкове число: {result}")

# Запуск бота
bot.polling()


