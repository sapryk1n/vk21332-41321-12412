import vk_api
import datetime # работа с датой и временем
import time

while True:
    vk = vk_api.VkApi(token = "a368e2d6b1814280fcd81d06b5f1208730c6dbdfb2c51f96bf088f393a470cc683fa57445c01217d42df7")
    delta = datetime.timedelta(hours=10, minutes=0)  # разница от UTC.
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»
    nowtime = t.strftime("%H:%M")  # текущее время
    nowdate = t.strftime("%d.%m.%Y")  # текущая дата
    if nowtime < t.strftime("12:00") and nowtime > t.strftime("07:00"):
        vk.method("status.set", {"text": " ● " + nowtime + " ● - Good Morning!"})
    else:
        vk.method("status.set", {"text": " ● " + nowtime + " ● - Whisky 24/7"})
    time.sleep(25)  # погружаем скрипт в «сон» на 25 секунд
