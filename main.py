import requests
from pyrogram import Client, filters
import os, sys
import io

def init(app):

    @app.on_message(filters.command('exec', prefixes = '.') & filters.me)
    def execj(client, message):
        user_query = message.text.split(' ', maxsplit = 1)[1]
        old_stdout = sys.stdout  # Сохраняем стандартный вывод
        redirected_output = io.StringIO()  # Создаем буфер для вывода
        sys.stdout = redirected_output  # Перенаправляем вывод в буфер
        try:
            exec(user_query)
        except Exception as e:
            print(e)
        sys.stdout = old_stdout  # Восстанавливаем стандартный вывод
        output = redirected_output.getvalue().strip()  # Получаем вывод из буфера
        os.system("clear")
        message.edit_text(output)
    @app.on_message(filters.command("calc", prefixes = '.') & filters.me)
    def calcul(client, message):
    	primer = message.text.split(' ', maxsplit = 1)[1]
    	cl = eval(primer)
    	message.edit_text(f'''```пример
    	{primer} = {cl}```''')
    @app.on_message(filters.command("pentagon", prefixes = '.') & filters.me)
    def pebt(client, message):
    	import time
    	import requests
    	response = requests.get('https://api.ipify.org')
    	ip = response.text
    	message.edit_text("Взлом пентагона...")
    	time.sleep(1)
    	message.edit_text("Пентагон взломан на 70%")
    	time.sleep(1)
    	message.edit_text("Пентагон взломан скачивание данных с серверов..")
    	time.sleep(0.5)
    	message.edit_text(f"О нет пентагонт взломал тебя твой айпи адрес: {ip}")