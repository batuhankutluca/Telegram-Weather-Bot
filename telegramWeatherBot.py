from telegram.ext import Updater, CommandHandler
import logging
import json
import requests
from geopy.geocoders import Nominatim

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Merhabalar, WeatherBot'a hoşgeldiniz, hava durumunu öğrenmek için /havadurumu komutunu kullanınız.")

def havadurumu(bot, update):
    if(len(update.message.text) > 12 ):
        try:
            location = update.message.text.split(' ')
            konum = location[1]
            geolocator = Nominatim()
            koordinat = geolocator.geocode(konum)
            api = 'https://api.darksky.net/forecast/your darksky api key/' + str(koordinat.latitude) + "," + str(koordinat.longitude)
            response = requests.get(api)
            json_data = json.loads(response.text)
            update.message.reply_text(json_data['currently']['summary'])
        except:
            update.message.reply_text("Hava durumunu öğrenmek istediğiniz " + konum + " bulunamadı. Lütfen tekrar deneyiniz.")
    else:
        update.message.reply_text("Lütfen geçerli bir konum giriniz.")
def main():
    updater = Updater('Your bot token here')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('havadurumu',havadurumu))
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()