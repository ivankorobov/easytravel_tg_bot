from loader import bot
import handlers

result_find = dict()
my_step_time = {'y': 'год', 'm': 'месяц', 'd': 'день'}

if __name__ == '__main__':

    bot.polling(none_stop=True)
