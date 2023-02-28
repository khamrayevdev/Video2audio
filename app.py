from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler, Updater
from func import mp4
API_TOKEN = '5932706480:AAFfzlTX9TF_i8Q-3cvElrES-gPPRJOjpGY'



def start(update, context):
    update.message.reply_text('Marhamat video yuboring...')
    return 1

def video(update, context):
    chat_id = update.message.chat_id
    rasm_id = update.message.video.file_id
    video = context.bot.get_file(rasm_id)
    mp4(video['file_path'])
    print(video['file_path'])
    context.bot.send_audio(chat_id, open('audio.mp3', 'rb'))
    return 1

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(Filters.video, video)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_hand)

    updater.start_polling()
    updater.idle()

main()