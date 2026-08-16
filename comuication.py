import telebot
import logic


TOKEN = '8645762118:AAHyr4XajrmKzGE41bdDB-TvICuYK530CXY'
bot = telebot.TeleBot(TOKEN)
chatId = '5360897820'
sesiones_activas = set()

# Comando de inicio

def check_auth(message):
    if message.from_user.id not in sesiones_activas:
        bot.reply_to(message, "⚠️ Por favor, inicia la conversación enviando /start para autenticarte.")
        return False
    return True




@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if logic.es_usuario_autorizado(user_id):
        sesiones_activas.add(user_id)
        bot.reply_to(message, '¡Hola! Soy Miguel, tu asistente virtual. Ya estás autenticado. ¿En qué puedo ayudarte hoy?')
    else:
        bot.reply_to(message, 'Lo siento, no tienes permiso para acceder a este bot. 🚫')


@bot.message_handler(commands=['agendar_trabajo'])
def send_agendar_trabajo(message):
    if not check_auth(message): return
    msg = bot.reply_to(message, """OK. Manda los datos del trabajo para añadirlo. Por favor, usa este formato:
        
    1. Cliente
    2. Dirección
    3. Fecha
    4. Contacto
    5. Encargado1, Encargado2, Encargado3""")
    
    
    
    # Registramos esta función interna como el siguiente paso
    bot.register_next_step_handler(msg, logic.agregar_trabajo)


@bot.message_handler(commands=['agregar_tarea'])
def send_agregar_tarea(message):
        if not check_auth(message): return
        msg = bot.reply_to(message, """OK. Manda los datos de la tarea para añadirlo. Por favor, usa este formato:
1. Titulo
2. Descripcion      
3. Responsable
4. Estado""")
        bot.register_next_step_handler(msg, logic.agregar_tarea)


def manejar_resultado(resultado, message):
        if resultado is True:
            bot.reply_to(message, "¡Listo! Se ha guardado correctamente. ✅")
        elif resultado is False:
            bot.reply_to(message, "Uy, hubo un problema técnico al guardar. Inténtalo de nuevo. 😅")
        elif resultado is None:
            bot.reply_to(message, "El formato no es correcto. Asegúrate de seguir el formato. 📝")

@bot.message_handler(commands=['mis_tareas'])
def send_mistareas(message):
    if not check_auth(message): return
    user_id = message.from_user.id
    tareas = logic.obtener_tareas_por_usuario(user_id)
    if tareas is None:
        bot.reply_to(message, "😕 No te encuentro en mi base de datos. ¡Habla con el administrador!")
        return

    if not tareas:
        bot.reply_to(message, "🎉 ¡Felicidades! No tienes ninguna tarea pendiente.")
    else:
        mensaje = "📋 **Tus tareas pendientes:**\n\n"
        for t in tareas:
            mensaje += f"🔹 *{t['titulo']}*\n"
        bot.reply_to(message, mensaje, parse_mode='Markdown')


if __name__ == '__main__':
    print("Bot funcionando")
    bot.polling()

