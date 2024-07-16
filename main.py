import telebot
from telebot import types

bot = telebot.TeleBot("2013984642:AAENYF3qOYFbU-i0wFqO9neNLUu4RNNu7fk")

admin_id = 869656178
andrey_id = 829146128
delya = 666713566

#123
# TO_CHAT_ID = 869656178  # Не забудь подставить нужный id!

# работа с командой check
@bot.message_handler(commands=['check'])
def check(message):
    if message.from_user.id == admin_id:
        bot.send_message(message.chat.id,
                         'Приветствую, {0.first_name}!\nВаш статус - Хозяин!'.format(message.from_user, bot.get_me()))

    elif message.from_user.id == andrey_id:
        bot.send_message(message.chat.id,
                         'Приветствую, {0.first_name}!\nВаш статус - Сотрудник Сколково!'.format(message.from_user,
                                                                                                 bot.get_me()))

    elif message.from_user.id == delya:
        bot.send_message(message.chat.id,
                         'Приветствую, {0.first_name}!\nВаш статус - Собака сутулая!'.format(message.from_user,
                                                                                             bot.get_me()))

    else:
        bot.send_message(message.chat.id,
                         'Приветствую, {0.first_name}!\nВаш статус - Пользователь!'.format(message.from_user,
                                                                                           bot.get_me()))

    print(message.text, message.from_user.first_name, message.from_user.id)  # отсылка данных в консоль


# хелло
@bot.message_handler(commands=['hi', 'Hi'])
def send_hello(message):
    bot.send_message(message.chat.id, "Hello, world!")
    print(message.text, message.from_user.first_name, message.from_user.id)


# отправить фотку
@bot.message_handler(commands=['send'])
def send(message):
    photo = open('pict/edds.jpg', 'rb')

    bot.send_photo(message.chat.id, photo)
    bot.reply_to(message, "Держи фото логотипа ЕДДС")


# отправить список команд
@bot.message_handler(commands=['start'], content_types=['text'])
def commands(message):
    sti = open('static/welcome.webp', 'rb')
    klava = open('pict/start.png', 'rb')

    bot.send_sticker(message.chat.id, sti)
    if message.text.lower() == '/start':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🗓️ График дежурств")
        item2 = types.KeyboardButton("📑 Алгоритмы")
        item3 = types.KeyboardButton("❓ Что ты умеешь?")
        item4 = types.KeyboardButton("📞 Справочник Дежурных служб ☎")

        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, в нашем с тобой диалоге ты сможешь: "
                         "\n🗓️ посмотерть актуальный график дежурств , "
                         "\n📑 посмотреть алгоритмы , "
                         "\n☎ найти номер необходимой службы в справочнике служб"
                         "\n Все это ты сможешь спросить у меня с помощью клавиатуры. Приятоного пользования 😄 ".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)


# начальные кнопки клавиатуры под сообщением
@bot.message_handler(content_types=['text'])
def lalala(message):
    gr = open('pict/graf.jpg', 'rb')

    # график
    if message.chat.type == 'private':
        if message.text == '🗓️ График дежурств':
            bot.send_photo(message.chat.id, gr)
        # алгоритмы
        elif message.text == '📑 Алгоритмы':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("👨‍💻 Алгоритм опроса", callback_data='alg_opros')
            item2 = types.InlineKeyboardButton("🚒 Пожарная", callback_data='alg_fire')
            item3 = types.InlineKeyboardButton("🚓Полиция", callback_data='alg_police')
            item4 = types.InlineKeyboardButton("🚗🚛 ДТП", callback_data='alg_dtp')
            item5 = types.InlineKeyboardButton("🚑 Скорая помощь", callback_data='alg_med')
            item6 = types.InlineKeyboardButton("🚐 Газовая служба ", callback_data='alg_gaz')
            item7 = types.InlineKeyboardButton("🚿 Отключение систем жизнеобеспечения (ЖКХ)", callback_data='alg_gkh')
            item8 = types.InlineKeyboardButton("❓ Справка", callback_data='alg_spravka')
            item9 = types.InlineKeyboardButton("👮‍♂️🧟‍♂ Антитеррор", callback_data='alg_terr')
            item10 = types.InlineKeyboardButton("🌡️ Разбился градусник", callback_data='alg_gradus')
            item11 = types.InlineKeyboardButton("👨‍💻 🆘Создание заявки в ТП ВИЛИОН", callback_data='alg_vill')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)

            bot.send_message(message.chat.id, 'Какой алгоритм необходим?', reply_markup=markup)
        # справочник
        elif message.text == '📞 Справочник Дежурных служб ☎':
            bot.send_message(message.chat.id, 'Справочные телефоны:')
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("🚒 Пожарная", callback_data='fire')
            item2 = types.InlineKeyboardButton("🚓 Полиция ", callback_data='police')
            item3 = types.InlineKeyboardButton("🚑 Скорая помощь ", callback_data='med')
            item4 = types.InlineKeyboardButton("🚐  Рай. Газ ", callback_data='gaz')
            item5 = types.InlineKeyboardButton("💡 РРЭС (Электросети) ", callback_data='svet')
            item6 = types.InlineKeyboardButton("🚒🚨 АСФ ", callback_data='asf')
            item7 = types.InlineKeyboardButton("🚿 ЖКХ ", callback_data='gkh')
            item8 = types.InlineKeyboardButton("⚠ ДРСУ (Дорож. Служба)", callback_data='drsy')
            item9 = types.InlineKeyboardButton("‼ ЦУКС ", callback_data='cuks')
            item10 = types.InlineKeyboardButton("❗ ЦОВ ", callback_data='cov')
            item11 = types.InlineKeyboardButton("🚨 Частный эвакуатор ", callback_data='evo')
            item12 = types.InlineKeyboardButton("🔐 Вскрытие замков (частник) ", callback_data='zamki')
            item13 = types.InlineKeyboardButton("🆘 Тех. Поддержка ВИЛИОН", callback_data='vil')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

            bot.send_message(message.chat.id, 'Какая служба нужна?', reply_markup=markup)
        # команды
        elif message.text == '❓ Что ты умеешь?':
            bot.send_message(message.chat.id,
                             'Вот команды, которые я умею читать:'
                             '\n /start - стартовое приветствие'
                             '\n/help - помощь по командам '
                             '\n/send - отправить фотографию с шашки чата '
                             '\n/check - проверка статуса пользователя')

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

    print(message.text, message.from_user.first_name, message.from_user.id)


# ответ на насторение
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    opros = open('pict/algoritm/opros.png ', 'rb')
    poj = open('pict/algoritm/fire.png', 'rb')
    police = open('pict/algoritm/police.png', 'rb')
    dtp = open('pict/algoritm/dtp.png', 'rb')
    med = open('pict/algoritm/med.png', 'rb')
    gaz = open('pict/algoritm/gaz.png', 'rb')
    gkh = open('pict/algoritm/gkh.png ', 'rb')
    other = open('pict/algoritm/spravka.png ', 'rb')
    terr = open('pict/algoritm/terror.png ', 'rb')

    # алгоритмы
    try:
        if call.message:

            if call.data == 'alg_opros':
                bot.send_message(call.message.chat.id, 'Держи алгоритм опросника 👨‍💻')
                bot.send_photo(call.message.chat.id, opros)

            elif call.data == 'alg_fire':
                bot.send_message(call.message.chat.id, 'Держи алгоритм пожарной')
                bot.send_photo(call.message.chat.id, poj)

            elif call.data == 'alg_police':
                bot.send_message(call.message.chat.id, 'Держи алгоритм при необходимости привлечении полиции:')
                bot.send_photo(call.message.chat.id, police)

            elif call.data == 'alg_dtp':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, dtp)

            elif call.data == 'alg_med':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, med)

            elif call.data == 'alg_gaz':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, gaz)

            elif call.data == 'alg_gkh':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, gkh)

            elif call.data == 'alg_spravka':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, other)

            elif call.data == 'alg_terr':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                bot.send_photo(call.message.chat.id, terr)

            elif call.data == 'alg_gradus':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                #bot.send_photo(call.message.chat.id, )

            elif call.data == 'alg_vill':
                bot.send_message(call.message.chat.id, 'Держи алгоритм :')
                #bot.send_photo(call.message.chat.id, )

            # номера
            elif call.data == 'fire':
                bot.send_message(call.message.chat.id, '🚒 Держи номер пожарной части:\n 01 \n 7-32-01 ')

            elif call.data == 'police':
                bot.send_message(call.message.chat.id,
                                 '🚓 Держи номер ОМВД по ленинградскому району:\n 02 \n 7-32-02 8-999-437-97-09 ')

            elif call.data == 'med':
                bot.send_message(call.message.chat.id, '🚑 Держи номер скорой помощи:\n 03 \n 7-32-03 ')

            elif call.data == 'gaz':
                bot.send_message(call.message.chat.id, '🚐 Держи номер Рай. Газа:\n 04 \n 7-05-04 ')

            elif call.data == 'svet':
                bot.send_message(call.message.chat.id, '💡 Держи номер РРЭС:\n 7-23-42 \n 3-80-35 8-918-390-50-02 ')

            elif call.data == 'asf':
                bot.send_message(call.message.chat.id, '🚒🚨 Держи номер АСФ:\n 5-83-01 \n 8-918-210-22-02 ')

            elif call.data == 'gkh':
                bot.send_message(call.message.chat.id, '🚿 Держи номер ЖКХ:\n 7-25-31 \n 7-32-00 (ЧС) ')

            elif call.data == 'drsu':
                bot.send_message(call.message.chat.id, '⚠ Держи номер ДРСУ: 7-34-32 / - ')

            elif call.data == 'cuks':
                bot.send_message(call.message.chat.id,
                                 '‼ Держи номер ЦУКСа:\n 8-961-268-11-12  8-961-991-11-96\n'
                                 '---------------------------------------------------------'
                                 ' \n 8-861-259-40-72  8-861-259-02-22 ')

            elif call.data == 'cov':
                bot.send_message(call.message.chat.id, '❗ Держи номер ЦОВа:  8-938-510-10-00 / - ')

            elif call.data == 'evo':
                bot.send_message(call.message.chat.id, '🚨 Держи номер Эвакуатора:\n 9-918-452-33-35 \n 8-961-888-88-97 ')

            elif call.data == 'zamki':
                bot.send_message(call.message.chat.id, '🔐 Держи номер Вскрытия замков: 8-905-475-47-59  / - ')

            elif call.data == 'vil':
                bot.send_message(call.message.chat.id, '🆘 Держи номер Тех поддержки: 8-800-444-01-12 / - ')

            # remove inline buttons
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Будь внимателен!",
                                  reply_markup=None)

            # show alert
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="")

    except Exception as e:
        print(repr(e))


# bot.infinity_polling()
bot.polling(none_stop=True)
