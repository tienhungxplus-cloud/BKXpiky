import telebot
from flask import Flask, request

# Token của bạn
TOKEN = "8679735939:AAHBVr6xcG..." # Giữ nguyên Token cũ của bạn vào đây
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Chào bạn! Bot đã chạy trên Vercel thành công.")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # Thay 'bk-xpiky.vercel.app' bằng link Vercel của bạn
    bot.set_webhook(url='https://bk-xpiky.vercel.app/' + TOKEN)
    return "Bot đang chạy...", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
