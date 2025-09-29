import requests
import telebot
import time

telegram_token = ''
bot = telebot.TeleBot(telegram_token)

chat_id = ''

collection_symbol = ''

api_url = f'"Api_url"{collection_symbol}/stats'

price_drop_threshold = -5

def send_telegram_message(message):
    bot.send_message(chat_id, message)

def check_price():
    last_price = None

    while True:
        try:
            response = requests.get(api_url)
            data = response.json()

            current_price = data['floorPrice'] / 1_000_000_000

            if last_price is not None:
                price_change = ((current_price - last_price) / last_price) * 100

                if price_change <= price_drop_threshold:
                    message = f'Price drop in {price_change:.2f}%: New price {current_price:.2f} SOL'
                    send_telegram_message(message)

            last_price = current_price

        except Exception as e:
            print(f'Error: {e}')

        time.sleep(300)


if __name__ == '__main__':
    check_price()
