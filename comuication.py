import telebot


TOKEN = '8645762118:AAHyr4XajrmKzGE41bdDB-TvICuYK530CXY'
bot = telebot.TeleBot(TOKEN)
chatId = '5360897820'
# Comando de inicio
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡Hola! Soy Miguel, tu asistente virtual. ¿En qué puedo ayudarte hoy?')

# Comando de Agendar Trabajos
@bot.message_handler(commands=['agendar_trabajo'])
def send_agendar_trabajo(message):
    msg = bot.reply_to(message, """OK. Manda los datos del trabajo para añadirlo. Por favor, usa este formato:
    
1. Cliente
2. Dirección
3. Fecha
4. Contacto
5. Encargado1, Encargado2, Encargado3""")
    
    bot.register_next_step_handler(message,procesar_datos_trabajo)

def procesar_datos_trabajo(message):
    datos = message.chat.id
    bot.send_message(chatId,message.chat.id)
    #bot.reply_to(message, f"¡Recibido! He registrado los datos: \n\n{datos}")
if __name__ == '__main__':
    print("¡El bot está en marcha!")
    bot.polling()