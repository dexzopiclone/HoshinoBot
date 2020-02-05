from os import path

import nonebot
import config
import hoshino

bot = hoshino.init(config)
app = bot.asgi

if __name__ == '__main__':
    bot.run()