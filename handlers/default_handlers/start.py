from loader import bot
from telebot import types


@bot.message_handler(commands=['start'])
def command_start(message):
    """ Функция бля запуска команды /start """

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} 👋\n'
                                      f'Я бот, с помощью которого можно быстро найти лучшие отели по всему миру.')
    get_menu(message)


def get_menu(message):
    """ Функция создает в телеграм боте функциональные кнопки меню """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_lowprice = types.KeyboardButton(text='/lowprice ⬇')
    button_highprice = types.KeyboardButton(text='/highprice ⬆')
    button_bestdeal = types.KeyboardButton(text='/bestdeal 💯')
    button_history = types.KeyboardButton(text='/history 📖')
    button_help = types.KeyboardButton(text='/help 🆘')
    markup.add(button_lowprice, button_highprice, button_bestdeal, button_history, button_help)
    bot.send_message(message.chat.id, text='<b>Главное меню</b>.\nВыберете команду:',
                     reply_markup=markup,
                     parse_mode='html')
