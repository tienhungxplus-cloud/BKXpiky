import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Token của bạn
TOKEN = "8679735939:AAHBVr6xcG7pWEEz5_Ls3BfCFTCyW8jLBuA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Tạo nút bấm mở Mini App
    markup = InlineKeyboardMarkup()
    # Tôi đổi sang link demo của chính Telegram để bạn chắc chắn thấy nó hoạt động
    web_info = WebAppInfo(url="https://play.famobi.com/om-nom-run") 
    
    btn = InlineKeyboardButton(text="🎮 Chơi Game Ngay", web_app=web_info)
    markup.add(btn)
    
    bot.send_message(message.chat.id, f"Chào {message.from_user.first_name}!\nNhấn nút dưới để mở App:", reply_markup=markup)

print("Bot đang chạy rồi nhé...")
bot.infinity_polling()
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body { background: #000; color: gold; text-align: center; font-family: 'Arial', sans-serif; overflow: hidden; }
        .coin { width: 150px; margin: 50px auto; cursor: pointer; transition: transform 0.1s; }
        .coin:active { transform: scale(0.9); }
        h1 { margin-top: 50px; }
    </style>
</head>
<body>
    <h1>BKX PIKY COIN</h1>
    <div id="coin" class="coin">
        <img src="https://cdn-icons-png.flaticon.com/512/2311/2311801.png" width="150">
    </div>
    <h2 id="score">0</h2>

    <script>
        let score = 0;
        const tg = window.Telegram.WebApp;
        tg.expand(); // Mở rộng app hết màn hình

        document.getElementById('coin').onclick = () => {
            score++;
            document.getElementById('score').innerText = score;
            tg.HapticFeedback.impactOccurred('medium'); // Rung nhẹ khi chạm
        };
    </script>
</body>
</html>

