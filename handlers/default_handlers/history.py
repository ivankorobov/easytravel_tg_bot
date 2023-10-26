from loader import bot
import sqlite3


@bot.message_handler(commands=['history'])
def command_history(message):
    """ Функция для запуска команды /history """

    bot.send_message(message.chat.id, text=f'<u>История поиска:</u>', parse_mode='html')
    conn = sqlite3.connect('history.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_history;")
    all_results = cur.fetchall()
    history_str = ''
    for i_num, all_results in enumerate(all_results):
        if message.from_user.id in all_results:
            history_str += f'︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵\n' \
                           f'Время и дата: {all_results[2]}\n' \
                           f'Команда: {all_results[1]}\n' \
                           f'Список отелей: {all_results[3]}\n'\
                           f'︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶\n\n'
    if history_str == '':
        bot.send_message(message.chat.id, text='Вы ничего не искали.\nИстория поиска пуста.')
    else:
        bot.send_message(message.chat.id, text=history_str)
