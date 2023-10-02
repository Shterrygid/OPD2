from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import Parser



def PyTeGrBot():
    API_TOKEN = '6321369352:AAGX3wENWOyfKfcsKOoih2vQHhmCr_JTpos'  # В одинарных кавычках размещаем токен, полученный от @BotFather.

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start', 'help'])
    async def process_start_command(message: types.Message):
        await message.reply("Вас приветствует бот, который ответит на Частые Вопросы для Первокурсника.")

        kb = [
            [types.KeyboardButton(text="Стипендия")],
            [types.KeyboardButton(text="Расписание/Карта корпусов ВУЗа")],
            [types.KeyboardButton(text="Документы для заявки в ВУЦ")],
            [types.KeyboardButton(text="Последние новости ОмГТУ")],
            [types.KeyboardButton(text="Группа в ВК")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                             resize_keyboard=True,
                                             input_field_placeholder="Какая же тема вас заинтересовала?"
                                             )

        await message.answer("Выберите одну из тем Частых Вопросов.", reply_markup=keyboard)

    @dp.message_handler(Text("Стипендия"))
    async def without_puree(message: types.Message):
        await message.reply("Стипендия — регулярное пособие учащимся. Подробнее о стипендии из вашего ВУЗа можно узнать здесь: \nhttps://www.omgtu.ru/sveden/grants/")

    @dp.message_handler(lambda message: message.text == "Расписание/Карта корпусов ВУЗа")
    async def without_puree(message: types.Message):
        await message.reply("Ознакомиться с расположением корпусов ВУЗа, а также с расписанием можно на этом сайте:\nhttps://rasp.omgtu.ru/")

    @dp.message_handler(Text("Документы для заявки в ВУЦ"))
    async def with_puree(message: types.Message):
        await message.reply("Вся необходимая информация о военном учебном центре находится в этом источнике:\nhttp://vuc.omgtu.ru/")

    @dp.message_handler(lambda message: message.text == "Последние новости ОмГТУ")
    async def without_puree(message: types.Message):
        await message.answer(str(Parser.parse()))

    @dp.message_handler(Text("Группа в ВК"))
    async def with_puree(message: types.Message):
        await message.reply("Источник различной и важной информации только в нашей группе ВКонтакте:\nhttps://vk.com/omskpoliteh")

    executor.start_polling(dp, skip_updates=True)
