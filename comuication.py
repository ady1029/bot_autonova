import telebot
import logic


TOKEN = '8645762118:AAHyr4XajrmKzGE41bdDB-TvICuYK530CXY'
bot = telebot.TeleBot(TOKEN)
chatId = '5360897820'
# Comando de inicio
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡Hola! Soy Miguel, tu asistente virtual. ¿En qué puedo ayudarte hoy?')


@bot.message_handler(commands=['agendar_trabajo'])
def send_agendar_trabajo(message):
    msg = bot.reply_to(message, """OK. Manda los datos del trabajo para añadirlo. Por favor, usa este formato:
        
    1. Cliente
    2. Dirección
    3. Fecha
    4. Contacto
    5. Encargado1, Encargado2, Encargado3""")
    
    def manejar_resultado(message):
        resultado = logic.agregar_trabajo(message)
        if resultado is True:
            bot.reply_to(message, "¡Listo! El trabajo se ha guardado correctamente. ✅")
        elif resultado is False:
            bot.reply_to(message, "Uy, hubo un problema técnico al guardar. Inténtalo de nuevo. 😅")
        else:
            bot.reply_to(message, "El formato no es correcto. Asegúrate de seguir los 5 puntos. 📝")
    
    # Registramos esta función interna como el siguiente paso
    bot.register_next_step_handler(msg, manejar_resultado)


@bot.message_handler(commands=['agregar_tarea'])
def send_agregar_tarea(message):
        msg = bot.reply_to(message, """OK. Manda los datos de la tarea para añadirlo. Por favor, usa este formato:
    
1. Titulo
2. Descripcion      
3. Responsable
4. Estado""")

if __name__ == '__main__':
    print("Bot funcionando")
    bot.polling()