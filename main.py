# pip install emoji
# pip install -U aiogram
# https://surik00.gitbooks.io/aiogram-lessons/content/chapter2.html
# @test_for_students_bot
# from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton
import re

from parsing import info_admission, info_calendar, title_calendar, info_be_student, info_offline,\
    number_of_places_title, cost_of_study_title, number_of_places, cost_of_study, entrance_tests,\
    computer_science, computer_science_for_foreign, computer_science_extr, computer_science_for_foreign_extr,\
    mechatronics, mechatronics_for_foreign, transport, transport_for_foreign,\
    part_time_economics, part_time_economics_for_foreign, full_time_economics, full_time_economics_for_foreign,\
    full_time_law, full_time_law_for_foreign, part_time_law, part_time_law_for_foreign,\
    english_ped, english_ped_for_foreign, elementary_ped, elementary_ped_for_foreign,\
    gen_add_ped, gen_add_ped_for_foreign, technology_ped, technology_ped_for_foreign, cult_ped, cult_ped_for_foreign,\
    psycho_pre, psycho_pre_for_foreign, psycho_of_edu, psycho_of_edu_for_foreign, psycho_of_edu_extr, psycho_of_edu_for_foreign_extr,\
    psycho_of_edu_electro, psycho_of_edu_electro_for_foreign,\
    automation, automation_for_foreign, graphic, graphic_for_foreign,\
    graphic_extr, graphic_for_foreign_extr, eng_two_pr, eng_two_pr_for_foreign,\
    biology_two_pr, biology_two_pr_for_foreign, add_edu, add_edu_for_foreign,\
    elem_edu, elem_edu_for_foreign, tatar, tatar_for_foreign, english,\
    english_for_foreign, society, society_for_foreign, inform, inform_for_foreign,\
    physics, physics_for_foreign, eng_lang, eng_lang_for_foreign,\
    litr, litr_for_foreign, life_safety, life_safety_for_foreign, sport, sport_for_foreign,\
    china, china_for_foreign, deutsch, deutsch_for_foreign, business_pedag, business_pedag_for_foreign, engin_pedag, engin_pedag_for_foreign,\
    eng_in_poly, eng_in_poly_for_foreign, edu_poly, edu_poly_for_foreign,\
    project_p, project_p_for_foreign, prof_sport, prof_sport_for_foreign, rus_and_lit, rus_and_lit_for_foreign, edu_pre, edu_pre_for_foreign,\
    edu_managment, edu_managment_for_foreign, digit_edu, digit_edu_for_foreign

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

chp = 0
cht = 0
ch = 0
chz = 0
chx = 0

# Клавиатура
button_admission = KeyboardButton('Поступление')
button_education = KeyboardButton('Образование')
# button_feedback = KeyboardButton('Обратная связь')
button_submission_docs = KeyboardButton('Подача документов')
button_contacts = KeyboardButton('Контакты приёмной комиссии')
button_review = KeyboardButton('Отзыв о чат-боте')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.row(button_admission, button_education).add(button_contacts).row(button_submission_docs, button_review)


# Реакция на команду "start/go"
@dp.message_handler(commands=['go', 'start'])
async def process_start_command(message: types.Message):
    name_of_bot = await bot.get_me()
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEICcVkBw0vfCGPdxfSu6-bQSuTRyJ42QAChAkAAhhC7gjc_iclNDJtgC4E')
    await bot.send_message(message.from_user.id,
                           "Здравствуй, " + message.from_user.full_name + "!\n\n"
                           "Я - <b>" + name_of_bot.full_name + "</b>, "
                           "создан для того, чтобы помочь тебе с поиском необходимой "
                           "информации для поступления в Елабужский институт КФУ.\n\n"
                           "Выбери интересующий тебя блок.",
                           parse_mode='html', reply_markup=greet_kb)


# Обработка кнопки "Образование"
@dp.message_handler(lambda message: message.text == 'Образование')
async def process_education_btn(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Бакалавриат', callback_data='bakalavr')
    inline_btn_2 = InlineKeyboardButton('Магистратура', callback_data='magistr')
    inline_btn_3 = InlineKeyboardButton('Проф. тестирование', callback_data='pr_test')
    main_inline_kb = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3)
    info_admission[0] = info_admission[0].text.strip()
    nonBreakSpace = u'\xa0'
    #info_admission[0] = info_admission[0].replace(nonBreakSpace, ' ')
    reg_mag = re.findall(r'[0-9]{2}', info_admission[0])
    reg_mag1 = nonBreakSpace + reg_mag[2] + nonBreakSpace + 'программам бакалавриата и'
    if re.search(r'[0-9]{4}', info_admission[0])[0] in info_admission[0]:
        info_admission[0] = info_admission[0].replace(re.search(r'[0-9]{4}', info_admission[0])[0], '<b>' + re.search(r'[0-9]{4}', info_admission[0])[0] + '</b>')
    if re.search(r' и [0-9]{2} программам магистратуры', info_admission[0])[0] in info_admission[0]:
        info_admission_bak = info_admission[0].replace(re.search(r' и [0-9]{2} программам магистратуры', info_admission[0])[0], '')
    if reg_mag1 in info_admission[0]:
        info_admission_mag = info_admission[0].replace(reg_mag1, '')
    await bot.send_message(message.from_user.id, message.from_user.full_name + ", выбери интересующий тебя блок:\n", reply_markup=main_inline_kb)

    @dp.callback_query_handler(lambda c: c.data == 'bakalavr')
    async def process_callback_bakalavr(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn = InlineKeyboardButton('Направления подготовки', url='https://kpfu.ru/elabuga/abitur/n')
        inline_kb_areas_of_training_b = InlineKeyboardMarkup().add(inline_btn)
        await bot.send_message(callback_query.from_user.id,
                               "<b>Бакалавриат</b> - это базовый уровень высшего образования, где студенты получают "
                               "фундаментальную подготовку без узкой специализации.\n\n" + info_admission_bak,
                               parse_mode='html', reply_markup=inline_kb_areas_of_training_b)

    @dp.callback_query_handler(lambda c: c.data == 'magistr')
    async def process_callback_magistr(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn = InlineKeyboardButton('Направления подготовки', url='https://kpfu.ru/elabuga/abitur/n')
        inline_kb_areas_of_training_m = InlineKeyboardMarkup().add(inline_btn)
        await bot.send_message(callback_query.from_user.id,
                               "<b>Магистратура</b> - это второй уровень двухуровневой системы высшего "
                               "образования, которая готовит профессионалов с более углублённой специализацией, "
                               "способных на решение сложных задач.\n\n" + info_admission_mag,
                               parse_mode='html', reply_markup=inline_kb_areas_of_training_m)

    @dp.callback_query_handler(lambda c: c.data == 'pr_test')
    async def process_callback_magistr(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn = InlineKeyboardButton('Начать тестирование', callback_data='test')
        inline_kb_start_test = InlineKeyboardMarkup().add(inline_btn)
        await bot.send_message(callback_query.from_user.id,
                               "<b>Тест на профориентацию</b> по методике академика Е.А. Климова.\n\n"
                               "Внимательно прочитав оба утверждения, введи ту букву, "
                               "которая больше всего соответствует твоему желанию.",
                               parse_mode='html', reply_markup=inline_kb_start_test)

        @dp.callback_query_handler(lambda c1: c1.data == 'test')
        async def process_callback_test1(callback_query1: types.CallbackQuery):
            await callback_query1.message.delete()
            await bot.answer_callback_query(callback_query1.id)
            inline_btn_1a = InlineKeyboardButton('1А', callback_data='1a')
            inline_btn_1b = InlineKeyboardButton('1Б', callback_data='1b')
            inline_kb_answer_opt_1 = InlineKeyboardMarkup().add(inline_btn_1a, inline_btn_1b)
            await bot.send_message(callback_query1.from_user.id,
                                   "<b>1A</b>. Ухаживать за животными.\n"
                                   "<b>1Б</b>. Обслуживать машины, приборы (следить, регулировать).",
                                   parse_mode='html', reply_markup=inline_kb_answer_opt_1)

            @dp.callback_query_handler(lambda c2: c2.data in ['1a', '1b'])
            async def process_callback_test2(callback_query2: types.CallbackQuery):
                global chp, cht, ch, chz, chx
                if callback_query2.data == '1a':
                    chp += 1
                elif callback_query2.data == '1b':
                    cht += 1
                await callback_query2.message.delete()
                await bot.answer_callback_query(callback_query2.id)
                inline_btn_2a = InlineKeyboardButton('2А', callback_data='2a')
                inline_btn_2b = InlineKeyboardButton('2Б', callback_data='2b')
                inline_kb_answer_opt_2 = InlineKeyboardMarkup().add(inline_btn_2a, inline_btn_2b)
                await bot.send_message(callback_query2.from_user.id,
                                       "<b>2A</b>. Помогать больным людям, лечить их.\n"
                                       "<b>2Б</b>. Составлять таблицы, схемы, программы "
                                       "вычислительных машин.", parse_mode='html', reply_markup=inline_kb_answer_opt_2)

                @dp.callback_query_handler(lambda c3: c3.data in ['2a', '2b'])
                async def process_callback_test3(callback_query3: types.CallbackQuery):
                    global chp, cht, ch, chz, chx
                    if callback_query3.data == '2a':
                        ch += 1
                    elif callback_query3.data == '2b':
                        chz += 1
                    await callback_query3.message.delete()
                    await bot.answer_callback_query(callback_query3.id)
                    inline_btn_3a = InlineKeyboardButton('3А', callback_data='3a')
                    inline_btn_3b = InlineKeyboardButton('3Б', callback_data='3b')
                    inline_kb_answer_opt_3 = InlineKeyboardMarkup().add(inline_btn_3a, inline_btn_3b)
                    await bot.send_message(callback_query3.from_user.id,
                                           "<b>3A</b>. Следить за качеством книжных иллюстраций, "
                                           "плакатов, художественных открыток, грампластинок.\n"
                                           "<b>3Б</b>. Следить за состоянием, развитием растений.",
                                           parse_mode='html', reply_markup=inline_kb_answer_opt_3)

                    @dp.callback_query_handler(lambda c4: c4.data in ['3a', '3b'])
                    async def process_callback_test4(callback_query4: types.CallbackQuery):
                        global chp, cht, ch, chz, chx
                        if callback_query4.data == '3a':
                            chx += 1
                        elif callback_query4.data == '3b':
                            chp += 1
                        await callback_query4.message.delete()
                        await bot.answer_callback_query(callback_query4.id)
                        inline_btn_4a = InlineKeyboardButton('4А', callback_data='4a')
                        inline_btn_4b = InlineKeyboardButton('4Б', callback_data='4b')
                        inline_kb_answer_opt_4 = InlineKeyboardMarkup().add(inline_btn_4a, inline_btn_4b)
                        await bot.send_message(callback_query4.from_user.id,
                                               "<b>4A</b>. Обрабатывать материалы (дерево, ткань, пластмассу и т.д.).\n"
                                               "<b>4Б</b>. Доводить товары до потребителя (рекламировать, продавать).",
                                               parse_mode='html', reply_markup=inline_kb_answer_opt_4)

                        @dp.callback_query_handler(lambda c5: c5.data in ['4a', '4b'])
                        async def process_callback_test5(callback_query5: types.CallbackQuery):
                            global chp, cht, ch, chz, chx
                            if callback_query5.data == '4a':
                                cht += 1
                            elif callback_query5.data == '4b':
                                ch += 1
                            await callback_query5.message.delete()
                            await bot.answer_callback_query(callback_query5.id)
                            inline_btn_5a = InlineKeyboardButton('5А', callback_data='5a')
                            inline_btn_5b = InlineKeyboardButton('5Б', callback_data='5b')
                            inline_kb_answer_opt_5 = InlineKeyboardMarkup().add(inline_btn_5a, inline_btn_5b)
                            await bot.send_message(callback_query5.from_user.id,
                                                   "<b>5A</b>. Обсуждать научно-популярные книги, статьи.\n"
                                                   "<b>5Б</b>. Обсуждать художественные книги.",
                                                   parse_mode='html', reply_markup=inline_kb_answer_opt_5)

                            @dp.callback_query_handler(lambda c6: c6.data in ['5a', '5b'])
                            async def process_callback_test6(callback_query6: types.CallbackQuery):
                                global chp, cht, ch, chz, chx
                                if callback_query6.data == '5a':
                                    chz += 1
                                elif callback_query6.data == '5b':
                                    chx += 1
                                await callback_query6.message.delete()
                                await bot.answer_callback_query(callback_query6.id)
                                inline_btn_6a = InlineKeyboardButton('6А', callback_data='6a')
                                inline_btn_6b = InlineKeyboardButton('6Б', callback_data='6b')
                                inline_kb_answer_opt_6 = InlineKeyboardMarkup().add(inline_btn_6a, inline_btn_6b)
                                await bot.send_message(callback_query6.from_user.id,
                                                       "<b>6A</b>. Выращивать молодняк животных какой-либо породы.\n"
                                                       "<b>6Б</b>. Тренировать сверстников (или младших) в выполнении каких-либо"
                                                       " действий (трудовых, учебных, спортивных).",
                                                       parse_mode='html', reply_markup=inline_kb_answer_opt_6)

                                @dp.callback_query_handler(lambda c7: c7.data in ['6a', '6b'])
                                async def process_callback_test7(callback_query7: types.CallbackQuery):
                                    global chp, cht, ch, chz, chx
                                    if callback_query7.data == '6a':
                                        chp += 1
                                    elif callback_query7.data == '6b':
                                        ch += 1
                                    await callback_query7.message.delete()
                                    await bot.answer_callback_query(callback_query7.id)
                                    inline_btn_7a = InlineKeyboardButton('7А', callback_data='7a')
                                    inline_btn_7b = InlineKeyboardButton('7Б', callback_data='7b')
                                    inline_kb_answer_opt_7 = InlineKeyboardMarkup().add(inline_btn_7a, inline_btn_7b)
                                    await bot.send_message(callback_query7.from_user.id,
                                                           "<b>7A</b>. Копировать рисунки, изображения, настраивать музыкальные инструменты.\n"
                                                           "<b>7Б</b>. Управлять каким-либо грузовым, подъёмным, транспортным средством "
                                                           "(подъёмным краном, машиной и т.п.).",
                                                           parse_mode='html', reply_markup=inline_kb_answer_opt_7)

                                    @dp.callback_query_handler(lambda c8: c8.data in ['7a', '7b'])
                                    async def process_callback_test8(callback_query8: types.CallbackQuery):
                                        global chp, cht, ch, chz, chx
                                        if callback_query8.data == '7a':
                                            chx += 1
                                        elif callback_query8.data == '7b':
                                            cht += 1
                                        await callback_query8.message.delete()
                                        await bot.answer_callback_query(callback_query8.id)
                                        inline_btn_8a = InlineKeyboardButton('8А', callback_data='8a')
                                        inline_btn_8b = InlineKeyboardButton('8Б', callback_data='8b')
                                        inline_kb_answer_opt_8 = InlineKeyboardMarkup().add(inline_btn_8a, inline_btn_8b)
                                        await bot.send_message(callback_query8.from_user.id,
                                                               "<b>8A</b>. Сообщать, разъяснять людям нужные для них сведения в "
                                                               "справочном бюро, во время экскурсии и т.д.\n"
                                                               "<b>8Б</b>. Художественно оформлять выставки, витрины, участвовать "
                                                               "в подготовке концертов, пьес и т.п.",
                                                               parse_mode='html', reply_markup=inline_kb_answer_opt_8)

                                        @dp.callback_query_handler(lambda c9: c9.data in ['8a', '8b'])
                                        async def process_callback_test9(callback_query9: types.CallbackQuery):
                                            global chp, cht, ch, chz, chx
                                            if callback_query9.data == '8a':
                                                ch += 1
                                            elif callback_query9.data == '8b':
                                                chx += 1
                                            await callback_query9.message.delete()
                                            await bot.answer_callback_query(callback_query9.id)
                                            inline_btn_9a = InlineKeyboardButton('9А', callback_data='9a')
                                            inline_btn_9b = InlineKeyboardButton('9Б', callback_data='9b')
                                            inline_kb_answer_opt_9 = InlineKeyboardMarkup().add(inline_btn_9a, inline_btn_9b)
                                            await bot.send_message(callback_query9.from_user.id,
                                                                   "<b>9A</b>. Ремонтировать изделия, вещи (одежду, технику), жилище.\n"
                                                                   "<b>9Б</b>. Искать и исправлять ошибки в текстах, таблицах, рисунках.",
                                                                   parse_mode='html', reply_markup=inline_kb_answer_opt_9)

                                            @dp.callback_query_handler(lambda c10: c10.data in ['9a', '9b'])
                                            async def process_callback_test10(callback_query10: types.CallbackQuery):
                                                global chp, cht, ch, chz, chx
                                                if callback_query10.data == '9a':
                                                    cht += 1
                                                elif callback_query10.data == '9b':
                                                    chz += 1
                                                await callback_query10.message.delete()
                                                await bot.answer_callback_query(callback_query10.id)
                                                inline_btn_10a = InlineKeyboardButton('10А', callback_data='10a')
                                                inline_btn_10b = InlineKeyboardButton('10Б', callback_data='10b')
                                                inline_kb_answer_opt_10 = InlineKeyboardMarkup().add(inline_btn_10a, inline_btn_10b)
                                                await bot.send_message(callback_query10.from_user.id,
                                                                       "<b>10A</b>. Лечить животных.\n"
                                                                       "<b>10Б</b>. Выполнять расчёты, вычисления.",
                                                                       parse_mode='html', reply_markup=inline_kb_answer_opt_10)

                                                @dp.callback_query_handler(lambda c11: c11.data in ['10a', '10b'])
                                                async def process_callback_test11(callback_query11: types.CallbackQuery):
                                                    global chp, cht, ch, chz, chx
                                                    if callback_query11.data == '10a':
                                                        chp += 1
                                                    elif callback_query11.data == '10b':
                                                        chz += 1
                                                    await callback_query11.message.delete()
                                                    await bot.answer_callback_query(callback_query11.id)
                                                    inline_btn_11a = InlineKeyboardButton('11А', callback_data='11a')
                                                    inline_btn_11b = InlineKeyboardButton('11Б', callback_data='11b')
                                                    inline_kb_answer_opt_11 = InlineKeyboardMarkup().add(inline_btn_11a, inline_btn_11b)
                                                    await bot.send_message(callback_query11.from_user.id,
                                                                           "<b>11A</b>. Выводить новые сорта растений.\n"
                                                                           "<b>11Б</b>. Конструировать новые виды промышленных "
                                                                           "изделий (машины, одежду, дома и т.д.).",
                                                                           parse_mode='html', reply_markup=inline_kb_answer_opt_11)

                                                    @dp.callback_query_handler(lambda c12: c12.data in ['11a', '11b'])
                                                    async def process_callback_test12(callback_query12: types.CallbackQuery):
                                                        global chp, cht, ch, chz, chx
                                                        if callback_query12.data == '11a':
                                                            chp += 1
                                                        elif callback_query12.data == '11b':
                                                            cht += 1
                                                        await callback_query12.message.delete()
                                                        await bot.answer_callback_query(callback_query12.id)
                                                        inline_btn_12a = InlineKeyboardButton('12А', callback_data='12a')
                                                        inline_btn_12b = InlineKeyboardButton('12Б', callback_data='12b')
                                                        inline_kb_answer_opt_12 = InlineKeyboardMarkup().add(inline_btn_12a, inline_btn_12b)
                                                        await bot.send_message(callback_query12.from_user.id,
                                                                               "<b>12A</b>. Разбирать споры, ссоры между людьми, убеждать, "
                                                                               "разъяснять, поощрять, наказывать.\n"
                                                                               "<b>12Б</b>. Разбираться в чертежах, схемах, таблицах "
                                                                               "(проверять, уточнять, приводить в порядок).",
                                                                               parse_mode='html', reply_markup=inline_kb_answer_opt_12)

                                                        @dp.callback_query_handler(lambda c13: c13.data in ['12a', '12b'])
                                                        async def process_callback_test13(callback_query13: types.CallbackQuery):
                                                            global chp, cht, ch, chz, chx
                                                            if callback_query13.data == '12a':
                                                                ch += 1
                                                            elif callback_query13.data == '12b':
                                                                chz += 1
                                                            await callback_query13.message.delete()
                                                            await bot.answer_callback_query(callback_query13.id)
                                                            inline_btn_13a = InlineKeyboardButton('13А', callback_data='13a')
                                                            inline_btn_13b = InlineKeyboardButton('13Б', callback_data='13b')
                                                            inline_kb_answer_opt_13 = InlineKeyboardMarkup().add(inline_btn_13a, inline_btn_13b)
                                                            await bot.send_message(callback_query13.from_user.id,
                                                                                   "<b>13A</b>. Наблюдать, изучать работу кружков художественной самодеятельности.\n"
                                                                                   "<b>13Б</b>. Наблюдать, изучать жизнь микробов.",
                                                                                   parse_mode='html', reply_markup=inline_kb_answer_opt_13)

                                                            @dp.callback_query_handler(lambda c14: c14.data in ['13a', '13b'])
                                                            async def process_callback_test14(callback_query14: types.CallbackQuery):
                                                                global chp, cht, ch, chz, chx
                                                                if callback_query14.data == '13a':
                                                                    chx += 1
                                                                elif callback_query14.data == '13b':
                                                                    chp += 1
                                                                await callback_query14.message.delete()
                                                                await bot.answer_callback_query(callback_query14.id)
                                                                inline_btn_14a = InlineKeyboardButton('14А', callback_data='14a')
                                                                inline_btn_14b = InlineKeyboardButton('14Б', callback_data='14b')
                                                                inline_kb_answer_opt_14 = InlineKeyboardMarkup().add(inline_btn_14a, inline_btn_14b)
                                                                await bot.send_message(callback_query14.from_user.id,
                                                                                       "<b>14A</b>. Обслуживать, налаживать медицинские приборы и аппараты.\n"
                                                                                       "<b>14Б</b>. Оказывать людям медицинскую помощь при ранениях, "
                                                                                       "ушибах, ожогах и т.п.",
                                                                                       parse_mode='html', reply_markup=inline_kb_answer_opt_14)

                                                                @dp.callback_query_handler(lambda c15: c15.data in ['14a', '14b'])
                                                                async def process_callback_test15(callback_query15: types.CallbackQuery):
                                                                    global chp, cht, ch, chz, chx
                                                                    if callback_query15.data == '14a':
                                                                        cht += 1
                                                                    elif callback_query15.data == '14b':
                                                                        ch += 1
                                                                    await callback_query15.message.delete()
                                                                    await bot.answer_callback_query(callback_query15.id)
                                                                    inline_btn_15a = InlineKeyboardButton('15А', callback_data='15a')
                                                                    inline_btn_15b = InlineKeyboardButton('15Б', callback_data='15b')
                                                                    inline_kb_answer_opt_15 = InlineKeyboardMarkup().add(inline_btn_15a, inline_btn_15b)
                                                                    await bot.send_message(callback_query15.from_user.id,
                                                                                           "<b>15A</b>. Составлять точные описания, отчёты о наблюдаемых явлениях, "
                                                                                           "событиях, измеряемых объектах и др.\n"
                                                                                           "<b>15Б</b>. Художественно описывать, изображать события "
                                                                                           "наблюдаемые или представляемые.",
                                                                                           parse_mode='html', reply_markup=inline_kb_answer_opt_15)

                                                                    @dp.callback_query_handler(lambda c16: c16.data in ['15a', '15b'])
                                                                    async def process_callback_test16(callback_query16: types.CallbackQuery):
                                                                        global chp, cht, ch, chz, chx
                                                                        if callback_query16.data == '15a':
                                                                            chz += 1
                                                                        elif callback_query16.data == '15b':
                                                                            chx += 1
                                                                        await callback_query16.message.delete()
                                                                        await bot.answer_callback_query(callback_query16.id)
                                                                        inline_btn_16a = InlineKeyboardButton('16А', callback_data='16a')
                                                                        inline_btn_16b = InlineKeyboardButton('16Б', callback_data='16b')
                                                                        inline_kb_answer_opt_16 = InlineKeyboardMarkup().add(inline_btn_16a, inline_btn_16b)
                                                                        await bot.send_message(callback_query16.from_user.id,
                                                                                               "<b>16A</b>. Делать лабораторные анализы в больнице.\n"
                                                                                               "<b>16Б</b>. Принимать, осматривать больных, беседовать "
                                                                                               "с ними, назначать лечение.",
                                                                                               parse_mode='html', reply_markup=inline_kb_answer_opt_16)

                                                                        @dp.callback_query_handler(lambda c17: c17.data in ['16a', '16b'])
                                                                        async def process_callback_test17(callback_query17: types.CallbackQuery):
                                                                            global chp, cht, ch, chz, chx
                                                                            if callback_query17.data == '16a':
                                                                                chp += 1
                                                                            elif callback_query17.data == '16b':
                                                                                ch += 1
                                                                            await callback_query17.message.delete()
                                                                            await bot.answer_callback_query(callback_query17.id)
                                                                            inline_btn_17a = InlineKeyboardButton('17А', callback_data='17a')
                                                                            inline_btn_17b = InlineKeyboardButton('17Б', callback_data='17b')
                                                                            inline_kb_answer_opt_17 = InlineKeyboardMarkup().add(inline_btn_17a, inline_btn_17b)
                                                                            await bot.send_message(callback_query17.from_user.id,
                                                                                                   "<b>17A</b>. Красить или расписывать стены помещений, поверхность изделий.\n"
                                                                                                   "<b>17Б</b>. Осуществлять монтаж здания или "
                                                                                                   "сборку машин, приборов.",
                                                                                                   parse_mode='html', reply_markup=inline_kb_answer_opt_17)

                                                                            @dp.callback_query_handler(lambda c18: c18.data in ['17a', '17b'])
                                                                            async def process_callback_test18(callback_query18: types.CallbackQuery):
                                                                                global chp, cht, ch, chz, chx
                                                                                if callback_query18.data == '17a':
                                                                                    chx += 1
                                                                                elif callback_query18.data == '17b':
                                                                                    cht += 1
                                                                                await callback_query18.message.delete()
                                                                                await bot.answer_callback_query(callback_query18.id)
                                                                                inline_btn_18a = InlineKeyboardButton('18А', callback_data='18a')
                                                                                inline_btn_18b = InlineKeyboardButton('18Б', callback_data='18b')
                                                                                inline_kb_answer_opt_18 = InlineKeyboardMarkup().add(inline_btn_18a, inline_btn_18b)
                                                                                await bot.send_message(callback_query18.from_user.id,
                                                                                                       "<b>18A</b>. Организовывать походы людей в театры, музеи, на "
                                                                                                       "экскурсии, в туристические путешествия и т.п.\n"
                                                                                                       "<b>18Б</b>. Играть на сцене, принимать участие в концертах.",
                                                                                                       parse_mode='html', reply_markup=inline_kb_answer_opt_18)

                                                                                @dp.callback_query_handler(lambda c19: c19.data in ['18a', '18b'])
                                                                                async def process_callback_test19(callback_query19: types.CallbackQuery):
                                                                                    global chp, cht, ch, chz, chx
                                                                                    if callback_query19.data == '18a':
                                                                                        ch += 1
                                                                                    elif callback_query19.data == '18b':
                                                                                        chx += 1
                                                                                    await callback_query19.message.delete()
                                                                                    await bot.answer_callback_query(callback_query19.id)
                                                                                    inline_btn_19a = InlineKeyboardButton('19А', callback_data='19a')
                                                                                    inline_btn_19b = InlineKeyboardButton('19Б', callback_data='19b')
                                                                                    inline_kb_answer_opt_19 = InlineKeyboardMarkup().add(inline_btn_19a, inline_btn_19b)
                                                                                    await bot.send_message(callback_query19.from_user.id,
                                                                                                           "<b>19A</b>. Изготовлять по чертежам детали, изделия (машины, одежду), строить здания.\n"
                                                                                                           "<b>19Б</b>. Заниматься черчением, копировать карты, чертежи.",
                                                                                                           parse_mode='html', reply_markup=inline_kb_answer_opt_19)

                                                                                    @dp.callback_query_handler(lambda c20: c20.data in ['19a', '19b'])
                                                                                    async def process_callback_test20(callback_query20: types.CallbackQuery):
                                                                                        global chp, cht, ch, chz, chx
                                                                                        if callback_query20.data == '19a':
                                                                                            cht += 1
                                                                                        elif callback_query20.data == '19b':
                                                                                            chz += 1
                                                                                        await callback_query20.message.delete()
                                                                                        await bot.answer_callback_query(callback_query20.id)
                                                                                        inline_btn_20a = InlineKeyboardButton('20А', callback_data='20a')
                                                                                        inline_btn_20b = InlineKeyboardButton('20Б', callback_data='20b')
                                                                                        inline_kb_answer_opt_20 = InlineKeyboardMarkup().add(inline_btn_20a, inline_btn_20b)
                                                                                        await bot.send_message(callback_query20.from_user.id,
                                                                                                               "<b>20A</b>. Вести борьбу с болезнями растений, с вредителями леса, сада.\n"
                                                                                                               "<b>20Б</b>. Работать на машинах (пишущая машина, "
                                                                                                               "компьютер, телетайп, телефакс).",
                                                                                                               parse_mode='html', reply_markup=inline_kb_answer_opt_20)

                                                                                        @dp.callback_query_handler(lambda c21: c21.data in ['20a', '20b'])
                                                                                        async def process_callback_test21(callback_query21: types.CallbackQuery):
                                                                                            global chp, cht, ch, chz, chx
                                                                                            if callback_query21.data == '20a':
                                                                                                chp += 1
                                                                                            elif callback_query21.data == '20b':
                                                                                                chz += 1
                                                                                            await callback_query21.message.delete()
                                                                                            await bot.answer_callback_query(callback_query21.id)

                                                                                            max_value = max(chp, cht, ch, chz, chx)
                                                                                            if max_value == chp:
                                                                                                await bot.send_message(callback_query21.from_user.id,
                                                                                                                       "<b>Результат тестирования:</b>\n\n"
                                                                                                                       "<b>Человек — природа.</b>\n"
                                                                                                                       "Сюда входят профессии, в которых человек имеет дело с различными явлениями "
                                                                                                                       "неживой и живой природы, например, биолог, географ, геолог, математик, физик,"
                                                                                                                       " химик и другие профессии, относящиеся к "
                                                                                                                       " разряду естественных наук.", parse_mode='html')
                                                                                            if max_value == cht:
                                                                                                await bot.send_message(callback_query21.from_user.id,
                                                                                                                       "<b>Результат тестирования:</b>\n\n"
                                                                                                                       "<b>Человек — техника.</b>\n"
                                                                                                                       "В эту группу профессий включены различные виды трудовой деятельности, в "
                                                                                                                       "которых человек имеет дело с техникой, её использованием или "
                                                                                                                       "конструированием, например, профессия инженера, оператора, машиниста, "
                                                                                                                       "механизатора, сварщика и т.п.", parse_mode='html')
                                                                                            if max_value == ch:
                                                                                                await bot.send_message(callback_query21.from_user.id,
                                                                                                                       "<b>Результат тестирования:</b>\n\n"
                                                                                                                       "<b>Человек — человек.</b>\n"
                                                                                                                       "Сюда включены все виды профессий, предполагающих взаимодействие людей, "
                                                                                                                       "например, политика, религия, педагогика, психология, медицина, торговля, "
                                                                                                                       "право.", parse_mode='html')
                                                                                            if max_value == chz:
                                                                                                await bot.send_message(callback_query21.from_user.id,
                                                                                                                       "<b>Результат тестирования:</b>\n\n"
                                                                                                                       "<b>Человек — знаковая система.</b>\n"
                                                                                                                       "В эту группу включены профессии, касающиеся создания, изучения и "
                                                                                                                       "использования различных знаковых систем, например, лингвистика, языки "
                                                                                                                       "математического программирования, способы графического представления "
                                                                                                                       "результатов наблюдений и т.п.", parse_mode='html')
                                                                                            if max_value == chx:
                                                                                                await bot.send_message(callback_query21.from_user.id,
                                                                                                                       "<b>Результат тестирования:</b>\n\n"
                                                                                                                       "<b>Человек — художественный образ.</b>\n"
                                                                                                                       "Эта группа профессий представляет собой различные виды "
                                                                                                                       "художественно-творческого труда, например, литература, музыка, театр, "
                                                                                                                       "изобразительное искусство.", parse_mode='html')
                                                                                            chp = 0
                                                                                            cht = 0
                                                                                            ch = 0
                                                                                            chz = 0
                                                                                            chx = 0


# Обработка кнопки "Поступление"
@dp.message_handler(lambda message: message.text == 'Поступление')
async def process_admission_btn(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Проходные баллы', callback_data='passing_scores')
    inline_btn_2 = InlineKeyboardButton('Количество мест', callback_data='number_of_places')
    inline_btn_3 = InlineKeyboardButton('Стоимость обучения', callback_data='cost_of_education')
    inline_btn_4 = InlineKeyboardButton('Вступительные испытания', callback_data='entrance_tests')
    # inline_btn_5 = InlineKeyboardButton('Мой рейтинг', callback_data='my_rating')
    inline_btn_6 = InlineKeyboardButton('Расписание дней \"Открытых дверей\"', callback_data='schedule')
    inline_btn_7 = InlineKeyboardButton('Направления по выбранным экзаменам', callback_data='directions')
    inline_btn_8 = InlineKeyboardButton('Часто задаваемые вопросы', callback_data='faq')
    inline_btn_9 = InlineKeyboardButton('Календарь абитуриента', callback_data='calendar')
    main_inline_kb = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4,
                                                           inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9)
    await bot.send_message(message.from_user.id, message.from_user.full_name + ", выбери интересующий тебя блок:\n", reply_markup=main_inline_kb)

    # Часто задаваемые вопросы
    @dp.callback_query_handler(lambda c: c.data == 'faq')
    async def process_callback_faq(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               "<b>Часто задаваемые вопросы</b> находятся "
                               "<a href='https://admissions.kpfu.ru/selection-committee/faq'>здесь</a>.",
                               parse_mode='html')

    # Расписание дней "Открытых дверей"
    # https://admissions.kpfu.ru/priemnaya-komissiya/grafik-provedeniya-dney-otkrytykh-dverey
    @dp.callback_query_handler(lambda c: c.data == 'schedule')
    async def process_callback_schedule(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn_november = InlineKeyboardButton('Ноябрь 2022', callback_data='november')
        inline_kb_schedule = InlineKeyboardMarkup(row_width=1).add(inline_btn_november)
        await bot.send_message(callback_query.from_user.id,
                               "Елабужский институт КФУ приглашает принять участие в <b>Днях открытых дверей</b>.\n"
                               "В эти дни будущие абитуриенты и их родители смогут получить информацию о порядке поступления в КФУ, "
                               "условиях обучения, студенческой жизни.\n\n"
                               "По вопросам участия просьба обращаться в приёмную комиссию института по адресу: "
                               "Елабуга, ул. Казанская, 89, каб. 16, тел. +7 (85557) 7-55-62, +7 (85557) 7-54-66, "
                               "e-mail: priem_el@kpfu.ru, pkefkfu@gmail.com", parse_mode='html', reply_markup=inline_kb_schedule)

        @dp.callback_query_handler(lambda schedule: schedule.data in ['november'])
        async def callback_schedule(callback_query_schedule: types.CallbackQuery):
            await bot.answer_callback_query(callback_query_schedule.id)
            if callback_query_schedule.data == 'november':
                await bot.send_message(callback_query_schedule.from_user.id,
                                       "<b>Дата и время проведения:</b> 13 ноября 2022 г. 10:00\n\n"
                                       "<b>Место проведения:</b> г. Елабуга, ул. Казанская, 89\n\n"
                                       "<b>Контактное лицо:</b>\nОшкина Алеся Геннадьевна 89178839155", parse_mode='html')

    # Проходные баллы
    # https://admissions.kpfu.ru/sites/default/files/%D0%95%D0%BB%D0%B0%D0%B1%D1%83%D0%B3%D0%B0.pdf
    @dp.callback_query_handler(lambda c: c.data == 'passing_scores')
    async def process_callback_passing_scores(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn_techno_scores = InlineKeyboardButton('Инженерно-технологическое отделение', callback_data='techno_scores')
        inline_btn_foreign_scores = InlineKeyboardButton('Отделение иностранных языков', callback_data='foreign_scores')
        inline_btn_maths_scores = InlineKeyboardButton('Отделение математики и естественных наук', callback_data='maths_scores')
        inline_btn_psycho_scores = InlineKeyboardButton('Отделение психологии и педагогики', callback_data='psycho_scores')
        inline_btn_history_scores = InlineKeyboardButton('Отделение филологии и истории', callback_data='history_scores')
        inline_btn_law_scores = InlineKeyboardButton('Отделение экономических и юридических наук', callback_data='law_scores')
        inline_kb_passing_scores = InlineKeyboardMarkup(row_width=1).add(inline_btn_techno_scores, inline_btn_foreign_scores,
                                                                         inline_btn_maths_scores, inline_btn_psycho_scores,
                                                                         inline_btn_history_scores, inline_btn_law_scores)
        await bot.send_message(callback_query.from_user.id,
                               "Здесь ты найдешь <b>проходные баллы</b> поступивших в Елабужский институт КФУ в 2022 году.\n\n"
                               "Выбери нужное отделение:", parse_mode='html', reply_markup=inline_kb_passing_scores)

        @dp.callback_query_handler(lambda department: department.data in ['techno_scores', 'foreign_scores', 'maths_scores', 'psycho_scores',
                                                                          'history_scores', 'law_scores'])
        async def callback_department(callback_query_department: types.CallbackQuery):
            await bot.answer_callback_query(callback_query_department.id)
            if callback_query_department.data == 'techno_scores':
                inline_btn_pedagogigal = InlineKeyboardButton('Педагогическое образование', callback_data='pedagogigal')
                inline_btn_professional = InlineKeyboardButton('Профессиональное обучение (по отраслям)', callback_data='professional')
                inline_btn_transport = InlineKeyboardButton('Технология транспортных процессов', callback_data='transport')
                inline_kb_specialty = InlineKeyboardMarkup(row_width=1).add(inline_btn_pedagogigal, inline_btn_professional, inline_btn_transport)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужное направление подготовки/специальность:", reply_markup=inline_kb_specialty)

                @dp.callback_query_handler(lambda specialty: specialty.data in ['pedagogigal', 'professional', 'transport'])
                async def callback_specialty(callback_query_specialty: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_specialty.id)
                    if callback_query_specialty.data == 'pedagogigal':
                        inline_btn_gen_add = InlineKeyboardButton('Общее и доп. образование в пред. области \"Технология\"', callback_data='gen_add')
                        inline_btn_robot = InlineKeyboardButton('Технология и робототехника', callback_data='robot')
                        kb_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_gen_add, inline_btn_robot)
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_profile)

                        @dp.callback_query_handler(lambda profile: profile.data in ['gen_add', 'robot'])
                        async def proc_callback_profile(callback_query_profile: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile.id)
                            if callback_query_profile.data == 'gen_add':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогическое образование (профиль: Общее и дополнительное образование в предметной области \"Технология\")\n\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 234 (бюджет), 153 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 172 (бюджет)\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 89 (контракт)",
                                                       parse_mode='html')
                            elif callback_query_profile.data == 'robot':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогическое образование (профиль: Технология и робототехника)\n\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 105 (контракт)",
                                                       parse_mode='html')
                    elif callback_query_specialty.data == 'professional':
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Профессиональное обучение (по отраслям) (профиль: Декорирование интерьера и графический дизайн)\n\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 247 (бюджет), 193 (контракт)\n"
                                               "<b>Минимальный балл:</b> 223 (бюджет)\n\n"
                                               "<em>Для приёма иностранных граждан:</em>\n"
                                               "<b>Средний балл:</b> 126 (контракт)",
                                               parse_mode='html')
                    elif callback_query_specialty.data == 'transport':
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Технология транспортных процессов (профиль: Проектирование и управление интеллектуальными транспортными системами)\n\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 181 (контракт)",
                                               parse_mode='html')
            elif callback_query_department.data == 'foreign_scores':
                inline_btn_linguistics_eng_n_china = InlineKeyboardButton('Перевод и переводоведение (английский язык, китайский язык)', callback_data='eng_n_china')
                inline_btn_linguistics_eng_n_german = InlineKeyboardButton('Перевод и переводоведение (английский язык, немецкий язык)', callback_data='eng_n_german')
                kb_profile_linguistics_langs = InlineKeyboardMarkup(row_width=1).add(inline_btn_linguistics_eng_n_china, inline_btn_linguistics_eng_n_german)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужный профиль направления подготовки/специальности \"Лингвистика\":", reply_markup=kb_profile_linguistics_langs)

                @dp.callback_query_handler(lambda profile_langs: profile_langs.data in ['eng_n_china', 'eng_n_german'])
                async def proc_callback_profile_langs(callback_query_profile_langs: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_profile_langs.id)
                    if callback_query_profile_langs.data == 'eng_n_china':
                        await bot.send_message(callback_query_profile_langs.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Лингвистика (профиль: Перевод и переводоведение (английский язык, китайский язык))\n\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 269 (бюджет), 223 (контракт)\n"
                                               "<b>Минимальный балл:</b> 250 (бюджет)",
                                               parse_mode='html')
                    elif callback_query_profile_langs.data == 'eng_n_german':
                        await bot.send_message(callback_query_profile_langs.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Лингвистика (профиль: Перевод и переводоведение (английский язык, немецкий язык))\n\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 246 (бюджет), 210 (контракт)\n"
                                               "<b>Минимальный балл:</b> 231 (бюджет)\n\n"
                                               "<em>Для приёма иностранных граждан:</em>\n"
                                               "<b>Средний балл:</b> 137 (контракт)",
                                               parse_mode='html')
            elif callback_query_department.data == 'maths_scores':
                inline_btn_info_maths = InlineKeyboardButton('Прикладная информатика', callback_data='info_maths')
                inline_btn_professional_maths = InlineKeyboardButton('Профессиональное обучение', callback_data='professional_maths')
                inline_kb_specialty_maths = InlineKeyboardMarkup(row_width=1).add(inline_btn_info_maths, inline_btn_professional_maths)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужное направление подготовки/специальность:", reply_markup=inline_kb_specialty_maths)

                @dp.callback_query_handler(lambda specialty: specialty.data in ['info_maths', 'professional_maths'])
                async def callback_specialty(callback_query_specialty: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_specialty.id)
                    if callback_query_specialty.data == 'info_maths':
                        inline_btn_extramural = InlineKeyboardButton('Заочная', callback_data='extramural')
                        inline_btn_full_time = InlineKeyboardButton('Очная', callback_data='full_time')
                        inline_kb_studies = InlineKeyboardMarkup(row_width=1).add(inline_btn_extramural, inline_btn_full_time)
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=inline_kb_studies)

                        @dp.callback_query_handler(lambda studies: studies.data in ['extramural', 'full_time'])
                        async def callback_studies(callback_query_studies: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_studies.id)
                            if callback_query_studies.data == 'extramural':
                                await bot.send_message(callback_query_studies.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Прикладная информатика (профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 236 (бюджет), 181 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 169 (бюджет)\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 85 (контракт)",
                                                       parse_mode='html')
                            elif callback_query_studies.data == 'full_time':
                                await bot.send_message(callback_query_studies.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Прикладная информатика (профиль: Прикладная "
                                                       "информатика в экономике)\n\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 227 (бюджет)\n"
                                                       "<b>Минимальный балл:</b> 147 (бюджет)",
                                                       parse_mode='html')
                    elif callback_query_specialty.data == 'professional_maths':
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Профессиональное обучение (по отраслям) (профиль: Автоматизация энергетических систем)\n\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 243 (бюджет), 191 (контракт)\n"
                                               "<b>Минимальный балл:</b> 185 (бюджет)",
                                               parse_mode='html')
            elif callback_query_department.data == 'psycho_scores':
                inline_btn_pedagogigal_sc = InlineKeyboardButton('Педагогическое образование', callback_data='pedagogigal_sc')
                inline_btn_psycho_pedagogigal_sc = InlineKeyboardButton('Психолого-педагогическое образование', callback_data='psycho_pedagogigal_sc')
                inline_kb_specialty_sc = InlineKeyboardMarkup(row_width=1).add(inline_btn_pedagogigal_sc, inline_btn_psycho_pedagogigal_sc)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужное направление подготовки/специальность:", reply_markup=inline_kb_specialty_sc)

                @dp.callback_query_handler(lambda specialty: specialty.data in ['pedagogigal_sc', 'psycho_pedagogigal_sc'])
                async def callback_specialty(callback_query_specialty: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_specialty.id)
                    if callback_query_specialty.data == 'pedagogigal_sc':
                        inline_btn_basic_ed = InlineKeyboardButton('Начальное образование', callback_data='basic_ed')
                        inline_btn_phy_cult = InlineKeyboardButton('Физическая культура', callback_data='physical_cult')
                        inline_btn_techn_n_robot = InlineKeyboardButton('Технология и робототехника', callback_data='techn_n_robot')
                        inline_btn_two_prof = InlineKeyboardButton('С двумя профилями подготовки', callback_data='two_prof')
                        inline_kb_profile_ped = InlineKeyboardMarkup(row_width=1).add(inline_btn_basic_ed, inline_btn_phy_cult,
                                                                                      inline_btn_techn_n_robot, inline_btn_two_prof)
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=inline_kb_profile_ped)

                        @dp.callback_query_handler(lambda profile: profile.data in ['basic_ed', 'physical_cult', 'techn_n_robot', 'two_prof'])
                        async def pr_callback_profile(callback_query_profile: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile.id)
                            if callback_query_profile.data == 'basic_ed':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогические образование (профиль: Начальное образование)\n\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 225 (бюджет), 179 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 164 (бюджет)\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 87 (контракт)",
                                                       parse_mode='html')
                            elif callback_query_profile.data == 'physical_cult':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогическое образование (профиль: Физическая культура)\n\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 245 (бюджет), 171 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 205 (бюджет)\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 87 (контракт)",
                                                       parse_mode='html')
                            elif callback_query_profile.data == 'techn_n_robot':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогическое образование (профиль: Технология и робототехника)\n\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 218 (бюджет), 202 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 145 (бюджет)",
                                                       parse_mode='html')
                            elif callback_query_profile.data == 'two_prof':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Педагогическое образование (с двумя профилями подготовки)\n\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n\n"
                                                       "Профили: История и обществознание; История и иностранный (английский) язык; "
                                                       "Русский язык и литература; Русский язык и иностранный (английский) язык; "
                                                       "Математика и физика; Математика и информатика; Биология и химия; "
                                                       "Дошкольное образование и Начальное образование; "
                                                       "Дошкольное образование и Дополнительное образование (художественное творчество)\n"
                                                       "<b>Средний балл:</b> 218 (бюджет), 202 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 145 (бюджет)\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 114 (контракт)\n\n"
                                                       "Профили: Физическая культура и безопасность жизнедеятельности; "
                                                       "Физическая культура и дополнительное образование (спортивная подготовка)\n"
                                                       "<b>Средний балл:</b> 205 (бюджет), 141 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 158 (бюджет)\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 114 (контракт)",
                                                       parse_mode='html')
                    elif callback_query_specialty.data == 'psycho_pedagogigal_sc':
                        inline_btn_psy_n_ped = InlineKeyboardButton('Психология и педагогика дошкольного образования', callback_data='psy_n_ped')
                        inline_btn_psy = InlineKeyboardButton('Психология образования', callback_data='psy')
                        inline_kb_profile_psycho = InlineKeyboardMarkup(row_width=1).add(inline_btn_psy_n_ped, inline_btn_psy)
                        await bot.send_message(callback_query_specialty.from_user.id, 
                                               "Выбери нужный профиль:", reply_markup=inline_kb_profile_psycho)

                        @dp.callback_query_handler(lambda profile: profile.data in ['psy_n_ped', 'psy'])
                        async def pr_callback_profile(callback_query_profile: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile.id)
                            if callback_query_profile.data == 'psy_n_ped':
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Психолого-педагогическое образование (профиль: Психология и педагогика дошкольного образования)\n\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 251 (бюджет), 169 (контракт)\n"
                                                       "<b>Минимальный балл:</b> 215 (бюджет)",
                                                       parse_mode='html')
                            elif callback_query_profile.data == 'psy':
                                inline_btn_psy_full_time = InlineKeyboardButton('Очная', callback_data='psy_full_time')
                                inline_btn_psy_extramural = InlineKeyboardButton('Заочная', callback_data='psy_extramural')
                                inline_kb_form = InlineKeyboardMarkup(row_width=1).add(inline_btn_psy_full_time, inline_btn_psy_extramural)
                                await bot.send_message(callback_query_profile.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=inline_kb_form)
                                
                                @dp.callback_query_handler(lambda form: form.data in ['psy_extramural', 'psy_full_time'])
                                async def pr_callback_form(callback_query_form: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_form.id)
                                    if callback_query_form.data == 'psy_full_time':
                                        await bot.send_message(callback_query_form.from_user.id,
                                                               "<b>Выбрано:</b> "
                                                               "Психолого-педагогическое образование (профиль: Психология образования)\n\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Средний балл:</b> 225 (бюджет)\n"
                                                               "<b>Минимальный балл:</b> 137 (бюджет)",
                                                               parse_mode='html')
                                    elif callback_query_form.data == 'psy_extramural':
                                        await bot.send_message(callback_query_form.from_user.id,
                                                               "<b>Выбрано:</b> "
                                                               "Психолого-педагогическое образование (профиль: Психология образования)\n\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Средний балл:</b> 234 (бюджет), 174 (контракт)\n"
                                                               "<b>Минимальный балл:</b> 185 (бюджет)\n\n"
                                                               "<em>Для приёма иностранных граждан:</em>\n"
                                                               "<b>Средний балл:</b> 79 (контракт)",
                                                               parse_mode='html')
            elif callback_query_department.data == 'history_scores':
                inline_btn_preschool = InlineKeyboardButton('Дошкольное образование, родной язык и литература', callback_data='preschool')
                inline_btn_rus_n_lit = InlineKeyboardButton('Русский язык и литература', callback_data='rus_n_lit')
                inline_btn_eng_n_lit = InlineKeyboardButton('Англ. язык, родной язык и литература', callback_data='eng_n_lit')
                inline_kb_profile_his = InlineKeyboardMarkup(row_width=1).add(inline_btn_preschool, inline_btn_rus_n_lit, inline_btn_eng_n_lit)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужный профиль направления подготовки/специальности \"Педагогическое образование\":", reply_markup=inline_kb_profile_his)

                @dp.callback_query_handler(lambda profile: profile.data in ['preschool', 'rus_n_lit', 'eng_n_lit'])
                async def callback_profile(callback_query_profile: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_profile.id)
                    if callback_query_profile.data == 'preschool':
                        await bot.send_message(callback_query_profile.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Педагогические образование (с двумя профилями подготовки) "
                                               "(профиль: Дошкольное образование, родной (татарский) язык и литература)\n\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 231 (бюджет), 165 (контракт)\n"
                                               "<b>Минимальный балл:</b> 191 (бюджет)",
                                               parse_mode='html')
                    elif callback_query_profile.data == 'rus_n_lit':
                        await bot.send_message(callback_query_profile.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Педагогическое образование (с двумя профилями подготовки) "
                                               "(профиль: Русский язык и литература)\n\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 248 (бюджет), 194 (контракт)\n"
                                               "<b>Минимальный балл:</b> 163 (бюджет)\n\n"
                                               "<em>Для приёма иностранных граждан:</em>\n"
                                               "<b>Средний балл:</b> 87 (контракт)",
                                               parse_mode='html')
                    elif callback_query_profile.data == 'eng_n_lit':
                        await bot.send_message(callback_query_profile.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Педагогическое образование (с двумя профилями подготовки) "
                                               "(профиль: Английский язык, родной (татарский) язык и литература)\n\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 202 (бюджет)\n"
                                               "<b>Минимальный балл:</b> 176 (бюджет)",
                                               parse_mode='html')
            elif callback_query_department.data == 'law_scores':
                inline_btn_economics = InlineKeyboardButton('Экономика', callback_data='economics')
                inline_btn_jurisprudence = InlineKeyboardButton('Юриспруденция', callback_data='jurisprudence')
                inline_kb_specialty_law = InlineKeyboardMarkup(row_width=1).add(inline_btn_economics, inline_btn_jurisprudence)
                await bot.send_message(callback_query_department.from_user.id,
                                       "Выбери нужное направление подготовки/специальность:", reply_markup=inline_kb_specialty_law)

                @dp.callback_query_handler(lambda specialty: specialty.data in ['economics', 'jurisprudence'])
                async def callback_specialty(callback_query_specialty: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_specialty.id)
                    if callback_query_specialty.data == 'economics':
                        inline_btn_ec_full_time = InlineKeyboardButton('Очная', callback_data='ec_full_time')
                        inline_btn_ec_part_time = InlineKeyboardButton('Очно-заочная', callback_data='ec_part_time')
                        inline_kb_ec_form = InlineKeyboardMarkup(row_width=1).add(inline_btn_ec_full_time, inline_btn_ec_part_time)
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=inline_kb_ec_form)

                        @dp.callback_query_handler(lambda ec_form: ec_form.data in ['ec_full_time', 'ec_part_time'])
                        async def callback_ec_form(callback_query_form: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_form.id)
                            if callback_query_form.data == 'ec_full_time':
                                await bot.send_message(callback_query_form.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Экономика (профиль: Экономика и финансы организаций (с углублённым изучением иностранных языков))\n\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Средний балл:</b> 203 (контракт)\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 98 (контракт)",
                                                       parse_mode='html')
                            elif callback_query_form.data == 'ec_part_time':
                                await bot.send_message(callback_query_form.from_user.id,
                                                       "<b>Выбрано:</b> "
                                                       "Экономика (профиль: Экономика и финансы организаций (реализуется с применением дистанционных технологий))\n\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n\n"
                                                       "<em>Для приёма иностранных граждан:</em>\n"
                                                       "<b>Средний балл:</b> 82 (контракт)",
                                                       parse_mode='html')
                    elif callback_query_specialty.data == 'jurisprudence':
                        await bot.send_message(callback_query_specialty.from_user.id,
                                               "<b>Выбрано:</b> "
                                               "Юриспруденция (профиль: Гражданское право)\n\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Средний балл:</b> 142 (контракт)\n\n"
                                               "<em>Для приёма иностранных граждан:</em>\n"
                                               "<b>Средний балл:</b> 98 (контракт)",
                                               parse_mode='html')

    # Количество мест
    @dp.callback_query_handler(lambda c: c.data == 'number_of_places')
    async def process_callback_number_of_places(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn_edu_bakalavr = InlineKeyboardButton('Бакалавриат', callback_data='edu_bakalavr')
        inline_btn_edu_magistr = InlineKeyboardButton('Магистратура', callback_data='edu_magistr')
        inline_kb_level_of_study = InlineKeyboardMarkup(row_width=1).add(inline_btn_edu_bakalavr, inline_btn_edu_magistr)
        global number_of_places_title
        if 'г.' in number_of_places_title:
            number_of_places_title = number_of_places_title.replace('г.', 'году')
        if 'Количество мест' in number_of_places_title:
            number_of_places_title = number_of_places_title.replace('Количество мест', '<b>количество мест</b>')
        await bot.send_message(callback_query.from_user.id,
                               "Здесь ты найдёшь " + number_of_places_title + ".\n\n"
                               "Выбери нужный уровень обучения:", parse_mode='html', reply_markup=inline_kb_level_of_study)

        @dp.callback_query_handler(lambda direction_of_study: direction_of_study.data in ['edu_bakalavr', 'edu_magistr'])
        async def callback_direction_of_study(callback_query_direction_of_study: types.CallbackQuery):
            await bot.answer_callback_query(callback_query_direction_of_study.id)
            global number_of_places_title
            if 'количество' in number_of_places_title:
                number_of_places_title = number_of_places_title.replace('количество', 'Количество')
            if callback_query_direction_of_study.data == 'edu_bakalavr':
                inline_btn_info = InlineKeyboardButton('Прикладная информатика', callback_data='info_b')
                inline_btn_mechatronics = InlineKeyboardButton('Мехатроника и робототехника', callback_data='mechatronics_b')
                inline_btn_transport = InlineKeyboardButton('Технология транспортных процессов', callback_data='transport_b')
                inline_btn_economics = InlineKeyboardButton('Экономика', callback_data='economics_b')
                inline_btn_law = InlineKeyboardButton('Юриспруденция', callback_data='law_b')
                inline_btn_pedagogical = InlineKeyboardButton('Педагогическое образование', callback_data='pedagogical_b')
                inline_btn_psycho = InlineKeyboardButton('Психолого-педагогическое образование', callback_data='psycho_b')
                inline_btn_prof = InlineKeyboardButton('Профессиональное обучение (по отраслям)', callback_data='prof_b')
                inline_btn_ped_two_prof = InlineKeyboardButton('Педагогическое образование (с двумя профилями подготовки)', callback_data='ped_two_prof_b')
                inline_btn_linguistics = InlineKeyboardButton('Лингвистика', callback_data='linguistics_b')
                inline_kb_direction_of_study = InlineKeyboardMarkup(row_width=1).add(inline_btn_info, inline_btn_mechatronics, inline_btn_transport, inline_btn_economics,
                                                                                     inline_btn_law, inline_btn_pedagogical, inline_btn_psycho, inline_btn_prof,
                                                                                     inline_btn_ped_two_prof, inline_btn_linguistics)
                await bot.send_message(callback_query_direction_of_study.from_user.id,
                                       "Выбери нужное направление:", parse_mode='html', reply_markup=inline_kb_direction_of_study)

                @dp.callback_query_handler(lambda department: department.data in ['info_b', 'mechatronics_b', 'transport_b', 'economics_b',
                                                                                  'law_b', 'pedagogical_b', 'psycho_b', 'prof_b',
                                                                                  'ped_two_prof_b', 'linguistics_b'])
                async def callback_direction(callback_query_direction: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_direction.id)
                    if callback_query_direction.data == 'info_b':
                        inline_btn_full_time_info = InlineKeyboardButton('Очная', callback_data='full_time_info')
                        inline_btn_extramural_info = InlineKeyboardButton('Заочная', callback_data='extramural_info')
                        inline_kb_studies_info = InlineKeyboardMarkup(row_width=1).add(inline_btn_full_time_info, inline_btn_extramural_info)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=inline_kb_studies_info)

                        @dp.callback_query_handler(lambda studies_info: studies_info.data in ['full_time_info', 'extramural_info'])
                        async def callback_studies_info(callback_query_studies_info: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_studies_info.id)
                            if callback_query_studies_info.data == 'full_time_info':
                                await bot.send_message(callback_query_studies_info.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[computer_science].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[computer_science].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[computer_science].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[computer_science].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[computer_science_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[computer_science_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[computer_science_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[computer_science_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_studies_info.data == 'extramural_info':
                                await bot.send_message(callback_query_studies_info.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[computer_science_extr].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[computer_science_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[computer_science_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[computer_science_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[computer_science_for_foreign_extr].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[computer_science_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[computer_science_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[computer_science_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                    elif callback_query_direction.data == 'mechatronics_b':
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "15.03.06 Мехатроника и робототехника "
                                               "(профиль: Физические основы мехатроники и робототехники)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> очно-заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[mechatronics].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[mechatronics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[mechatronics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[mechatronics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[mechatronics_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[mechatronics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[mechatronics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[mechatronics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_direction.data == 'transport_b':
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "23.03.01 Технология транспортных процессов "
                                               "(профиль: Проектирование и управление интеллектуальными транспортными системами)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[transport].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[transport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[transport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[transport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[transport_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[transport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[transport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[transport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_direction.data == 'economics_b':
                        inline_btn_part_time_economics = InlineKeyboardButton('Очно-заочная', callback_data='part_time_economics')
                        inline_btn_full_time_economics = InlineKeyboardButton('Очная', callback_data='full_time_economics')
                        inline_kb_studies_economics = InlineKeyboardMarkup(row_width=1).add(inline_btn_part_time_economics, inline_btn_full_time_economics)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=inline_kb_studies_economics)

                        @dp.callback_query_handler(lambda studies_economics: studies_economics.data in ['part_time_economics', 'full_time_economics'])
                        async def callback_studies_economics(callback_query_studies_economics: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_studies_economics.id)
                            if callback_query_studies_economics.data == 'part_time_economics':
                                await bot.send_message(callback_query_studies_economics.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(реализуется с применением электронного обучения и дистанционных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[part_time_economics].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[part_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[part_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[part_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[part_time_economics_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[part_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[part_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[part_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_studies_economics.data == 'full_time_economics':
                                await bot.send_message(callback_query_studies_economics.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(с углублённым изучением иностранных языков))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[full_time_economics].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[full_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[full_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[full_time_economics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[full_time_economics_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[full_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[full_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[full_time_economics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                    elif callback_query_direction.data == 'law_b':
                        inline_btn_full_time_law_form = InlineKeyboardButton('Очная', callback_data='full_time_law_form')
                        inline_btn_part_time_law_form = InlineKeyboardButton('Очно-заочная', callback_data='part_time_law_form')
                        inline_kb_studies_law = InlineKeyboardMarkup(row_width=1).add(inline_btn_full_time_law_form, inline_btn_part_time_law_form)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=inline_kb_studies_law)

                        @dp.callback_query_handler(lambda studies_law: studies_law.data in ['full_time_law_form', 'part_time_law_form'])
                        async def callback_studies_law(callback_query_studies_law: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_studies_law.id)
                            if callback_query_studies_law.data == 'full_time_law_form':
                                await bot.send_message(callback_query_studies_law.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[full_time_law].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[full_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[full_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[full_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[full_time_law_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[full_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[full_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[full_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_studies_law.data == 'part_time_law_form':
                                await bot.send_message(callback_query_studies_law.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право (реализуется с применением "
                                                       "электронного обучения и дистанционных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[part_time_law].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[part_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[part_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[part_time_law].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[part_time_law_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[part_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[part_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[part_time_law_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                    elif callback_query_direction.data == 'pedagogical_b':
                        inline_btn_english_ped = InlineKeyboardButton('Английский язык', callback_data='english_ped')
                        inline_btn_elementary_ped = InlineKeyboardButton('Начальное образование', callback_data='elementary_ped')
                        inline_btn_gen_add_ped = InlineKeyboardButton('Общее и дополнительное образование в предметной области Технология', callback_data='gen_add_ped')
                        inline_btn_technology_ped = InlineKeyboardButton('Технология и робототехника', callback_data='technology_ped')
                        inline_btn_cult_ped = InlineKeyboardButton('Физическая культура', callback_data='cult_ped')
                        kb_profile_ped = InlineKeyboardMarkup(row_width=1).add(inline_btn_english_ped, inline_btn_elementary_ped, inline_btn_gen_add_ped,
                                                                               inline_btn_technology_ped, inline_btn_cult_ped)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_profile_ped)

                        @dp.callback_query_handler(lambda profile_ped: profile_ped.data in ['english_ped', 'elementary_ped', 'gen_add_ped', 'technology_ped', 'cult_ped'])
                        async def proc_callback_profile_ped(callback_query_profile_ped: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile_ped.id)
                            if callback_query_profile_ped.data == 'english_ped':
                                await bot.send_message(callback_query_profile_ped.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Английский язык)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[english_ped].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[english_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[english_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[english_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[english_ped_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[english_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[english_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[english_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_ped.data == 'elementary_ped':
                                await bot.send_message(callback_query_profile_ped.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Начальное образование)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[elementary_ped].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[elementary_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[elementary_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[elementary_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[elementary_ped_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[elementary_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[elementary_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[elementary_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_ped.data == 'gen_add_ped':
                                await bot.send_message(callback_query_profile_ped.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Общее и дополнительное образование в предметной области \"Технология\")\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[gen_add_ped].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[gen_add_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[gen_add_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[gen_add_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[gen_add_ped_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[gen_add_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[gen_add_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[gen_add_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_ped.data == 'technology_ped':
                                await bot.send_message(callback_query_profile_ped.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Технология и робототехника)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[technology_ped].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[technology_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[technology_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[technology_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[technology_ped_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[technology_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[technology_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[technology_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_ped.data == 'cult_ped':
                                await bot.send_message(callback_query_profile_ped.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Физическая культура)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[cult_ped].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[cult_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[cult_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[cult_ped].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[cult_ped_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[cult_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[cult_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[cult_ped_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                    elif callback_query_direction.data == 'psycho_b':
                        inline_btn_psycho_pre = InlineKeyboardButton('Психология и педагогика дошкольного образования', callback_data='psycho_pre')
                        inline_btn_psycho_of_edu = InlineKeyboardButton('Психология образования', callback_data='psycho_of_edu')
                        inline_btn_psycho_of_edu_electro = InlineKeyboardButton('Психология образования (с применением электронного обучения '
                                                                                'и дистанционных образовательных технологий)', callback_data='psycho_of_edu_electro')
                        kb_profile_psycho = InlineKeyboardMarkup(row_width=1).add(inline_btn_psycho_pre, inline_btn_psycho_of_edu, inline_btn_psycho_of_edu_electro)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_profile_psycho)

                        @dp.callback_query_handler(lambda profile_psycho: profile_psycho.data in ['psycho_pre', 'psycho_of_edu', 'psycho_of_edu_electro'])
                        async def proc_callback_profile_psycho(callback_query_profile_psycho: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile_psycho.id)
                            if callback_query_profile_psycho.data == 'psycho_pre':
                                await bot.send_message(callback_query_profile_psycho.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология и педагогика дошкольного образования)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[psycho_pre].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[psycho_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[psycho_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[psycho_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[psycho_pre_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[psycho_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[psycho_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[psycho_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_psycho.data == 'psycho_of_edu':
                                btn_full_time_psycho = InlineKeyboardButton('Очная', callback_data='full_time_psycho')
                                btn_extramural_psycho = InlineKeyboardButton('Заочная', callback_data='extramural_psycho')
                                kb_studies_psycho = InlineKeyboardMarkup(row_width=1).add(btn_full_time_psycho, btn_extramural_psycho)
                                await bot.send_message(callback_query_profile_psycho.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_studies_psycho)

                                @dp.callback_query_handler(lambda studies_psycho: studies_psycho.data in ['full_time_psycho', 'extramural_psycho'])
                                async def pr_callback_studies_psycho(callback_query_studies_psycho: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_studies_psycho.id)
                                    if callback_query_studies_psycho.data == 'full_time_psycho':
                                        await bot.send_message(callback_query_studies_psycho.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование (профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[psycho_of_edu].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[psycho_of_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[psycho_of_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[psycho_of_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[psycho_of_edu_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[psycho_of_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[psycho_of_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[psycho_of_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_studies_psycho.data == 'extramural_psycho':
                                        await bot.send_message(callback_query_studies_psycho.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование (профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[psycho_of_edu_extr].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[psycho_of_edu_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[psycho_of_edu_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[psycho_of_edu_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[psycho_of_edu_for_foreign_extr].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[psycho_of_edu_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[psycho_of_edu_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[psycho_of_edu_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                            elif callback_query_profile_psycho.data == 'psycho_of_edu_electro':
                                await bot.send_message(callback_query_profile_psycho.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология образования (с применением электронного обучения "
                                                       "и дистанционных образовательных технологий)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[psycho_of_edu_electro].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[psycho_of_edu_electro].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[psycho_of_edu_electro].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[psycho_of_edu_electro].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                       find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + number_of_places[psycho_of_edu_electro_for_foreign].text.strip(),
                                                       parse_mode='html')
                    elif callback_query_direction.data == 'prof_b':
                        inline_btn_automation = InlineKeyboardButton('Автоматизация энергетических систем', callback_data='automation')
                        inline_btn_graphic_design = InlineKeyboardButton('Декорирование интерьера и графический дизайн', callback_data='graphic_design')
                        kb_profile_prof = InlineKeyboardMarkup(row_width=1).add(inline_btn_automation, inline_btn_graphic_design)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_profile_prof)

                        @dp.callback_query_handler(lambda profile_prof: profile_prof.data in ['automation', 'graphic_design'])
                        async def proc_callback_profile_prof(callback_query_profile_prof: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile_prof.id)
                            if callback_query_profile_prof.data == 'automation':
                                await bot.send_message(callback_query_profile_prof.from_user.id,
                                                       "44.03.04 Профессиональное обучение (по отраслям) "
                                                       "(профиль: Автоматизация энергетических систем)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[automation].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[automation].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[automation].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[automation].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[automation_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[automation_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[automation_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[automation_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_prof.data == 'graphic_design':
                                btn_full_time_graphic_form = InlineKeyboardButton('Очная', callback_data='full_time_graphic_form')
                                btn_extramural_graphic_form = InlineKeyboardButton('Заочная', callback_data='extramural_graphic_form')
                                kb_studies_graphic = InlineKeyboardMarkup(row_width=1).add(btn_full_time_graphic_form, btn_extramural_graphic_form)
                                await bot.send_message(callback_query_direction.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_studies_graphic)

                                @dp.callback_query_handler(lambda studies_graphic: studies_graphic.data in ['full_time_graphic_form', 'extramural_graphic_form'])
                                async def callback_studies_graphic(callback_query_studies_graphic: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_studies_graphic.id)
                                    if callback_query_studies_graphic.data == 'full_time_graphic_form':
                                        await bot.send_message(callback_query_studies_graphic.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[graphic].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[graphic].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[graphic].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[graphic].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[graphic_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[graphic_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[graphic_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[graphic_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_studies_graphic.data == 'extramural_graphic_form':
                                        await bot.send_message(callback_query_studies_graphic.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[graphic_extr].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[graphic_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[graphic_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[graphic_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[graphic_for_foreign_extr].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[graphic_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[graphic_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[graphic_for_foreign_extr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                    elif callback_query_direction.data == 'ped_two_prof_b':
                        inline_btn_eng = InlineKeyboardButton('Английский язык, родной (татарский) язык и литература', callback_data='eng_two_pr')
                        inline_btn_biology = InlineKeyboardButton('Биология и Химия', callback_data='biology_two_pr')
                        inline_btn_pre = InlineKeyboardButton('Дошкольное образование и ...', callback_data='pre_two_pr')
                        inline_btn_history = InlineKeyboardButton('История и ...', callback_data='history_two_pr')
                        inline_btn_maths = InlineKeyboardButton('Математика и ...', callback_data='maths_two_pr')
                        inline_btn_rus = InlineKeyboardButton('Русский язык и ...', callback_data='rus_two_pr')
                        inline_btn_physical_cult = InlineKeyboardButton('Физическая культура и ...', callback_data='physical_cult_two_pr')
                        kb_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_eng, inline_btn_biology, inline_btn_pre, inline_btn_history,
                                                                           inline_btn_maths, inline_btn_rus, inline_btn_physical_cult)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_profile)

                        @dp.callback_query_handler(lambda profile_two_pr: profile_two_pr.data in ['eng_two_pr', 'biology_two_pr', 'pre_two_pr',
                                                                                                  'history_two_pr', 'maths_two_pr', 'rus_two_pr',
                                                                                                  'physical_cult_two_pr'])
                        async def proc_callback_profile_two_pr(callback_query_profile_two_pr: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_profile_two_pr.id)
                            if callback_query_profile_two_pr.data == 'eng_two_pr':
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Английский язык, родной (татарский) язык и литература)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[eng_two_pr].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[eng_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[eng_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[eng_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + number_of_places[eng_two_pr_for_foreign].text.strip(),
                                                       parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'biology_two_pr':
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Биология и Химия)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[biology_two_pr].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[biology_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[biology_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[biology_two_pr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[biology_two_pr_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[biology_two_pr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[biology_two_pr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[biology_two_pr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'pre_two_pr':
                                inline_btn_add_edu = InlineKeyboardButton('Дополнительное образование '
                                                                          '(художественное творчество)', callback_data='add_edu')
                                inline_btn_elem_edu = InlineKeyboardButton('Начальное образование', callback_data='elem_edu')
                                inline_btn_tatar = InlineKeyboardButton('Родной (татарский) язык и литература', callback_data='tatar')
                                kb_two_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_add_edu, inline_btn_elem_edu, inline_btn_tatar)
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Дошкольное образование и ...", reply_markup=kb_two_profile)

                                @dp.callback_query_handler(lambda two_profile: two_profile.data in ['add_edu', 'elem_edu', 'tatar'])
                                async def proc_callback_two_profile(callback_query_two_profile: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_two_profile.id)
                                    if callback_query_two_profile.data == 'add_edu':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Дополнительное образование "
                                                               "(художественное творчество))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[add_edu].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[add_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[add_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[add_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[add_edu_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[add_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[add_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[add_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'elem_edu':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Начальное образование)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[elem_edu].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[elem_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[elem_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[elem_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[elem_edu_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[elem_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[elem_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[elem_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'tatar':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование, родной (татарский) язык и литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет 6 месяцев\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[tatar].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[tatar].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[tatar].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[tatar].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + number_of_places[tatar_for_foreign].text.strip(),
                                                               parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'history_two_pr':
                                inline_btn_english = InlineKeyboardButton('Иностранный (английский) язык', callback_data='english')
                                inline_btn_society = InlineKeyboardButton('Обществознание', callback_data='society')
                                kb_two_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_english, inline_btn_society)
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "История и ...", reply_markup=kb_two_profile)

                                @dp.callback_query_handler(lambda two_profile: two_profile.data in ['english', 'society'])
                                async def proc_callback_two_profile(callback_query_two_profile: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_two_profile.id)
                                    if callback_query_two_profile.data == 'english':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[english].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[english].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[english].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[english].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[english_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[english_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[english_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[english_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'society':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Обществознание)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[society].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[society].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[society].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[society].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[society_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[society_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[society_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[society_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'maths_two_pr':
                                inline_btn_life_inform = InlineKeyboardButton('Информатика', callback_data='inform')
                                inline_btn_physics = InlineKeyboardButton('Физика', callback_data='physics')
                                kb_two_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_life_inform, inline_btn_physics)
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Математика и ...", reply_markup=kb_two_profile)

                                @dp.callback_query_handler(lambda two_profile: two_profile.data in ['inform', 'physics'])
                                async def proc_callback_two_profile(callback_query_two_profile: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_two_profile.id)
                                    if callback_query_two_profile.data == 'inform':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Информатика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[inform].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[inform].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[inform].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[inform].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[inform_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[inform_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[inform_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[inform_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'physics':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Физика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[physics].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[physics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[physics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[physics].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[physics_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[physics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[physics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[physics_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'rus_two_pr':
                                inline_btn_life_eng_lang = InlineKeyboardButton('Иностранный (английский) язык', callback_data='eng_lang')
                                inline_btn_litr = InlineKeyboardButton('Литература', callback_data='litr')
                                kb_two_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_life_eng_lang, inline_btn_litr)
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Русский язык и ...", reply_markup=kb_two_profile)

                                @dp.callback_query_handler(lambda two_profile: two_profile.data in ['eng_lang', 'litr'])
                                async def proc_callback_two_profile(callback_query_two_profile: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_two_profile.id)
                                    if callback_query_two_profile.data == 'eng_lang':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[eng_lang].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[eng_lang].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[eng_lang].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[eng_lang].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[eng_lang_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[eng_lang_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[eng_lang_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[eng_lang_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'litr':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и Литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[litr].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[litr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[litr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[litr].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[litr_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[litr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[litr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[litr_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                            elif callback_query_profile_two_pr.data == 'physical_cult_two_pr':
                                inline_btn_life_safety = InlineKeyboardButton('Безопасность жизнедеятельности', callback_data='life_safety')
                                inline_btn_sport = InlineKeyboardButton('Дополнительное образование (спортивная подготовка)', callback_data='sport')
                                kb_two_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_life_safety, inline_btn_sport)
                                await bot.send_message(callback_query_profile_two_pr.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Физическая культура и ...", reply_markup=kb_two_profile)

                                @dp.callback_query_handler(lambda two_profile: two_profile.data in ['life_safety', 'sport'])
                                async def proc_callback_two_profile(callback_query_two_profile: types.CallbackQuery):
                                    await bot.answer_callback_query(callback_query_two_profile.id)
                                    if callback_query_two_profile.data == 'life_safety':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и безопасность жизнедеятельности)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[life_safety].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[life_safety].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[life_safety].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[life_safety].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[life_safety_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[life_safety_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[life_safety_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                                               find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[life_safety_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                                    elif callback_query_two_profile.data == 'sport':
                                        await bot.send_message(callback_query_two_profile.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и дополнительное образование (спортивная подготовка))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + number_of_places_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[sport].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>бюджет:</b> " + number_of_places[sport_for_foreign].text.strip() + "\n"
                                                               "           <b>особая квота:</b> " + number_of_places[sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "           <b>целевые места:</b> " + number_of_places[sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>договор:</b> " + number_of_places[sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                    elif callback_query_direction.data == 'linguistics_b':
                        inline_btn_china = InlineKeyboardButton('Английский язык, китайский язык', callback_data='china')
                        inline_btn_deutsch = InlineKeyboardButton('Английский язык, немецкий язык', callback_data='deutsch')
                        kb_languages = InlineKeyboardMarkup(row_width=1).add(inline_btn_china, inline_btn_deutsch)
                        await bot.send_message(callback_query_direction.from_user.id,
                                               "Выбери нужные языки:", reply_markup=kb_languages)

                        @dp.callback_query_handler(lambda lang: lang.data in ['china', 'deutsch'])
                        async def proc_callback_languages(callback_query_languages: types.CallbackQuery):
                            await bot.answer_callback_query(callback_query_languages.id)
                            if callback_query_languages.data == 'china':
                                await bot.send_message(callback_query_languages.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, китайский язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[china].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[china].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[china].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[china].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[china_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[china_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[china_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[china_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif callback_query_languages.data == 'deutsch':
                                await bot.send_message(callback_query_languages.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, немецкий язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + number_of_places_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[deutsch].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[deutsch].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[deutsch].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[deutsch].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>бюджет:</b> " + number_of_places[deutsch_for_foreign].text.strip() + "\n"
                                                       "           <b>особая квота:</b> " + number_of_places[deutsch_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "           <b>целевые места:</b> " + number_of_places[deutsch_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>договор:</b> " + number_of_places[deutsch_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
            elif callback_query_direction_of_study.data == 'edu_magistr':
                inline_btn_business_pedag = InlineKeyboardButton('Бизнес-педагогика', callback_data='business_pedag')
                inline_btn_engin_pedag = InlineKeyboardButton('Инженерная педагогика', callback_data='engin_pedag')
                inline_btn_eng_in_poly = InlineKeyboardButton('Иностранный язык в лингвополикультурном образовательном пространстве', callback_data='eng_in_poly')
                inline_btn_edu_poly = InlineKeyboardButton('Полилингвальное образование', callback_data='edu_poly')
                inline_btn_project_p = InlineKeyboardButton('Проектирование и оценка образовательных программ и процессов', callback_data='project_p')
                inline_btn_prof_sport = InlineKeyboardButton('Профессиональная подготовка в области физической культуры и спорта', callback_data='prof_sport')
                inline_btn_rus_and_lit = InlineKeyboardButton('Русский язык и литература в межкультурной коммуникации', callback_data='rus_and_lit')
                inline_btn_edu_pre = InlineKeyboardButton('Управление дошкольным образованием', callback_data='edu_pre')
                inline_btn_edu_managment = InlineKeyboardButton('Управление образовательной организацией', callback_data='edu_managment')
                inline_btn_digit_edu = InlineKeyboardButton('Цифровое образование', callback_data='digit_edu')
                kb_profile_in_mag = InlineKeyboardMarkup(row_width=1).add(inline_btn_business_pedag, inline_btn_engin_pedag, inline_btn_eng_in_poly, inline_btn_edu_poly,
                                                                          inline_btn_project_p, inline_btn_prof_sport, inline_btn_rus_and_lit, inline_btn_edu_pre,
                                                                          inline_btn_edu_managment, inline_btn_digit_edu)
                await bot.send_message(callback_query_direction_of_study.from_user.id,
                                       "Выбери нужный профиль:", reply_markup=kb_profile_in_mag)

                @dp.callback_query_handler(lambda mag_profile: mag_profile.data in ['business_pedag', 'engin_pedag', 'eng_in_poly', 'edu_poly', 'project_p', 'prof_sport',
                                                                                    'rus_and_lit', 'edu_pre', 'edu_managment', 'digit_edu'])
                async def proc_callback_mag_profile(callback_query_mag_profile: types.CallbackQuery):
                    await bot.answer_callback_query(callback_query_mag_profile.id)
                    if callback_query_mag_profile.data == 'business_pedag':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Бизнес-педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[business_pedag].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[business_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[business_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[business_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[business_pedag_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[business_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[business_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[business_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'engin_pedag':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Инженерная педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[engin_pedag].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[engin_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[engin_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[engin_pedag].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[engin_pedag_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[engin_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[engin_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[engin_pedag_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'eng_in_poly':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Иностранный язык в "
                                               "лингвополикультурном образовательном пространстве)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[eng_in_poly].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[eng_in_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[eng_in_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[eng_in_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[eng_in_poly_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[eng_in_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[eng_in_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[eng_in_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'edu_poly':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Полилингвальное образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_poly].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_poly].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_poly_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_poly_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'project_p':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Проектирование и оценка "
                                               "образовательных программ и процессов)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[project_p].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[project_p].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[project_p].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[project_p].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[project_p_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[project_p_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[project_p_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[project_p_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'prof_sport':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Профессиональная подготовка в области физической культуры и спорта)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[prof_sport].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[prof_sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[prof_sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[prof_sport].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[prof_sport_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[prof_sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[prof_sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[prof_sport_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'rus_and_lit':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Русский язык и литература в межкультурной коммуникации)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[rus_and_lit].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[rus_and_lit].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[rus_and_lit].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[rus_and_lit].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[rus_and_lit_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[rus_and_lit_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[rus_and_lit_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[rus_and_lit_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'edu_pre':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Управление дошкольным образованием)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_pre].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_pre].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_pre_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_pre_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'edu_managment':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование (профиль: Управление образовательной организацией)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_managment].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_managment].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_managment].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_managment].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[edu_managment_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[edu_managment_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[edu_managment_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[edu_managment_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').
                                               find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
                    elif callback_query_mag_profile.data == 'digit_edu':
                        await bot.send_message(callback_query_mag_profile.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Цифровое образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + number_of_places_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[digit_edu].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[digit_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[digit_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[digit_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>бюджет:</b> " + number_of_places[digit_edu_for_foreign].text.strip() + "\n"
                                               "           <b>особая квота:</b> " + number_of_places[digit_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "           <b>целевые места:</b> " + number_of_places[digit_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>договор:</b> " + number_of_places[digit_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find('td').find_next_sibling('td').text.strip() + "\n",
                                               parse_mode='html')
    
    # Стоимость обучения
    @dp.callback_query_handler(lambda c: c.data == 'cost_of_education')
    async def process_callback_cost_of_education(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn_bak_cost = InlineKeyboardButton('Бакалавриат', callback_data='bak_cost')
        inline_btn_mag_cost = InlineKeyboardButton('Магистратура', callback_data='mag_cost')
        inline_kb_cost_of_education = InlineKeyboardMarkup(row_width=1).add(inline_btn_bak_cost, inline_btn_mag_cost)
        global cost_of_study_title
        if 'в' in cost_of_study_title:
            cost_of_study_title = cost_of_study_title.replace('в', 'за')
        if 'г.' in cost_of_study_title:
            cost_of_study_title = cost_of_study_title.replace('г. ', 'год')
        if '*' in cost_of_study_title:
            cost_of_study_title = cost_of_study_title.replace('*', '')
        if 'Стоимость обучения' in cost_of_study_title:
            cost_of_study_title = cost_of_study_title.replace('Стоимость обучения', '<b>стоимость обучения</b>')
        await bot.send_message(callback_query.from_user.id,
                               "Приказы о стоимости на учебный год выходят в начале периода подачи документов на поступление, "
                               "поэтому здесь указана " + cost_of_study_title + ", она является ориентировочной.\n\n"
                               "Выбери нужный уровень обучения:", parse_mode='html', reply_markup=inline_kb_cost_of_education)

        @dp.callback_query_handler(lambda direction_of_study: direction_of_study.data in ['bak_cost', 'mag_cost'])
        async def callback_direction_of_study(query_direction_of_study: types.CallbackQuery):
            await bot.answer_callback_query(query_direction_of_study.id)
            global cost_of_study_title
            if 'стоимость' in cost_of_study_title:
                cost_of_study_title = cost_of_study_title.replace('стоимость', 'Стоимость')
            if query_direction_of_study.data == 'bak_cost':
                inline_btn_info_cost = InlineKeyboardButton('Прикладная информатика', callback_data='info_cost')
                inline_btn_mechatronics_cost = InlineKeyboardButton('Мехатроника и робототехника', callback_data='mechatronics_cost')
                inline_btn_transport_cost = InlineKeyboardButton('Технология транспортных процессов', callback_data='transport_cost')
                inline_btn_economics_cost = InlineKeyboardButton('Экономика', callback_data='economics_cost')
                inline_btn_jurisprudence_cost = InlineKeyboardButton('Юриспруденция', callback_data='jurisprudence_cost')
                inline_btn_ped_cost = InlineKeyboardButton('Педагогическое образование', callback_data='ped_cost')
                inline_btn_psycho_ped_cost = InlineKeyboardButton('Психолого-педагогическое образование', callback_data='psycho_ped_cost')
                inline_btn_prof_cost = InlineKeyboardButton('Профессиональное обучение (по отраслям)', callback_data='prof_cost')
                inline_btn_ped_two_cost = InlineKeyboardButton('Педагогическое образование (с двумя профилями подготовки)', callback_data='ped_two_cost')
                inline_btn_linguistics_cost = InlineKeyboardButton('Лингвистика', callback_data='linguistics_cost')
                kb_bak_direction = InlineKeyboardMarkup(row_width=1).add(inline_btn_info_cost, inline_btn_mechatronics_cost, inline_btn_transport_cost,
                                                                         inline_btn_economics_cost, inline_btn_jurisprudence_cost, inline_btn_ped_cost,
                                                                         inline_btn_psycho_ped_cost, inline_btn_prof_cost, inline_btn_ped_two_cost,
                                                                         inline_btn_linguistics_cost)
                await bot.send_message(query_direction_of_study.from_user.id,
                                       "Выбери нужное направление:", reply_markup=kb_bak_direction)

                @dp.callback_query_handler(lambda direction_cost: direction_cost.data in ['info_cost', 'mechatronics_cost', 'transport_cost', 'economics_cost',
                                                                                          'jurisprudence_cost', 'ped_cost', 'psycho_ped_cost', 'prof_cost',
                                                                                          'ped_two_cost', 'linguistics_cost'])
                async def callback_direction_cost(query_direction_cost: types.CallbackQuery):
                    await bot.answer_callback_query(query_direction_cost.id)
                    if query_direction_cost.data == 'info_cost':
                        btn_full_time_info_cost = InlineKeyboardButton('Очная', callback_data='full_time_info_cost')
                        btn_extramural_info_cost = InlineKeyboardButton('Заочная', callback_data='extramural_info_cost')
                        kb_form_of_edu_info = InlineKeyboardMarkup(row_width=1).add(btn_full_time_info_cost, btn_extramural_info_cost)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_info)

                        @dp.callback_query_handler(lambda form_of_edu_info: form_of_edu_info.data in ['full_time_info_cost', 'extramural_info_cost'])
                        async def cb_form_of_edu_info(query_form_of_edu_info: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_info.id)
                            if query_form_of_edu_info.data == 'full_time_info_cost':
                                await bot.send_message(query_form_of_edu_info.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[computer_science].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[computer_science].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[computer_science].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[computer_science].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_form_of_edu_info.data == 'extramural_info_cost':
                                await bot.send_message(query_form_of_edu_info.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[computer_science].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[computer_science].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[computer_science].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[computer_science].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                    elif query_direction_cost.data == 'mechatronics_cost':
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "15.03.06 Мехатроника и робототехника "
                                               "(профиль: Физические основы мехатроники и робототехники)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> очно-заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n" + cost_of_study[mechatronics].text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost.data == 'transport_cost':
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "23.03.01 Технология транспортных процессов "
                                               "(профиль: Проектирование и управление интеллектуальными транспортными системами)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[transport].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[transport].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[transport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[transport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost.data == 'economics_cost':
                        btn_part_time_ec_cost = InlineKeyboardButton('Очно-заочная', callback_data='part_time_ec_cost')
                        btn_full_time_ec_cost = InlineKeyboardButton('Очная', callback_data='full_time_ec_cost')
                        kb_form_of_edu_ec = InlineKeyboardMarkup(row_width=1).add(btn_part_time_ec_cost, btn_full_time_ec_cost)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_ec)

                        @dp.callback_query_handler(lambda form_of_edu_ec: form_of_edu_ec.data in ['part_time_ec_cost', 'full_time_ec_cost'])
                        async def cb_form_of_edu_ec(query_form_of_edu_ec: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_ec.id)
                            if query_form_of_edu_ec.data == 'part_time_ec_cost':
                                await bot.send_message(query_form_of_edu_ec.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(реализуется с применением электронного обучения и дистанционных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[part_time_economics].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[part_time_economics].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[part_time_economics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[part_time_economics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_form_of_edu_ec.data == 'full_time_ec_cost':
                                await bot.send_message(query_form_of_edu_ec.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(с углублённым изучением иностранных языков))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[full_time_economics].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[full_time_economics].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[full_time_economics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[full_time_economics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                    elif query_direction_cost.data == 'jurisprudence_cost':
                        btn_full_time_juri_cost = InlineKeyboardButton('Очная', callback_data='full_time_juri_cost')
                        btn_part_time_juri_cost = InlineKeyboardButton('Очно-заочная', callback_data='part_time_juri_cost')
                        kb_form_of_edu_juri = InlineKeyboardMarkup(row_width=1).add(btn_full_time_juri_cost, btn_part_time_juri_cost)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_juri)

                        @dp.callback_query_handler(lambda form_of_edu_juri: form_of_edu_juri.data in ['full_time_juri_cost', 'part_time_juri_cost'])
                        async def cb_form_of_edu_juri(query_form_of_edu_juri: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_juri.id)
                            if query_form_of_edu_juri.data == 'full_time_juri_cost':
                                await bot.send_message(query_form_of_edu_juri.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[full_time_law].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[full_time_law].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[full_time_law].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[full_time_law].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_form_of_edu_juri.data == 'part_time_juri_cost':
                                await bot.send_message(query_form_of_edu_juri.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[part_time_law].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[part_time_law].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[part_time_law].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[part_time_law].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                    elif query_direction_cost.data == 'ped_cost':
                        btn_english_edu_b_profile = InlineKeyboardButton('Английский язык', callback_data='english_edu_b_profile')
                        btn_elem_edu_b_profile = InlineKeyboardButton('Начальное образование', callback_data='elem_edu_b_profile')
                        btn_gen_add_b_profile = InlineKeyboardButton('Общее и дополнительное образование в '
                                                                     'предметной области Технология', callback_data='gen_add_b_profile')
                        btn_tech_b_profile = InlineKeyboardButton('Технология и робототехника', callback_data='tech_b_profile')
                        btn_phy_cult_b_profile = InlineKeyboardButton('Физическая культура', callback_data='phy_cult_b_profile')
                        kb_bak_profile_ped = InlineKeyboardMarkup(row_width=1).add(btn_english_edu_b_profile, btn_elem_edu_b_profile,
                                                                                   btn_gen_add_b_profile, btn_tech_b_profile, btn_phy_cult_b_profile)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_profile_ped)

                        @dp.callback_query_handler(lambda profile_ped_b_cost: profile_ped_b_cost.data in ['english_edu_b_profile', 'elem_edu_b_profile',
                                                                                                          'gen_add_b_profile', 'tech_b_profile', 'phy_cult_b_profile'])
                        async def callback_profile_b_cost(query_profile_b_cost: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_b_cost.id)
                            if query_profile_b_cost.data == 'english_edu_b_profile':
                                await bot.send_message(query_profile_b_cost.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Английский язык)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[english_ped].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[english_ped].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[english_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[english_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_b_cost.data == 'elem_edu_b_profile':
                                await bot.send_message(query_profile_b_cost.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Начальное образование)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[elementary_ped].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[elementary_ped].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[elementary_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[elementary_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_b_cost.data == 'gen_add_b_profile':
                                await bot.send_message(query_profile_b_cost.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Общее и дополнительное образование в предметной области \"Технология\")\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[gen_add_ped].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[gen_add_ped].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[gen_add_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[gen_add_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_b_cost.data == 'tech_b_profile':
                                await bot.send_message(query_profile_b_cost.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Технология и робототехника)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[technology_ped].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[technology_ped].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[technology_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[technology_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_b_cost.data == 'phy_cult_b_profile':
                                await bot.send_message(query_profile_b_cost.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Физическая культура)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[cult_ped].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[cult_ped].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[cult_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[cult_ped].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                    elif query_direction_cost.data == 'psycho_ped_cost':
                        btn_psycho_of_pre_b_profile = InlineKeyboardButton('Психология и педагогика дошкольного образования', callback_data='psycho_of_pre_b_profile')
                        btn_psycho_of_edu_b_profile = InlineKeyboardButton('Психология образования', callback_data='psycho_of_edu_b_profile')
                        btn_psycho_electro_b_profile = InlineKeyboardButton('Психология образования (с применением электронного обучения и дистанционных '
                                                                            'образовательных технологий)', callback_data='psycho_electro_b_profile')
                        kb_bak_profile_psy_ped = InlineKeyboardMarkup(row_width=1).add(btn_psycho_of_pre_b_profile, btn_psycho_of_edu_b_profile,
                                                                                       btn_psycho_electro_b_profile)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_profile_psy_ped)

                        @dp.callback_query_handler(lambda profile_psycho_b_cost: profile_psycho_b_cost.data in ['psycho_of_pre_b_profile', 'psycho_of_edu_b_profile',
                                                                                                                'psycho_electro_b_profile'])
                        async def callback_profile_psycho_b_cost(query_profile_psycho_b_cost: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_psycho_b_cost.id)
                            if query_profile_psycho_b_cost.data == 'psycho_of_pre_b_profile':
                                await bot.send_message(query_profile_psycho_b_cost.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология и педагогика дошкольного образования)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[psycho_pre].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[psycho_pre].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[psycho_pre].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[psycho_pre].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_psycho_b_cost.data == 'psycho_of_edu_b_profile':
                                btn_full_time_psy_of_edu_cost = InlineKeyboardButton('Очная', callback_data='full_time_psy_of_edu_cost')
                                btn_extramural_psy_of_edu_cost = InlineKeyboardButton('Заочная', callback_data='extramural_psy_of_edu_cost')
                                kb_profile_psy_of_edu = InlineKeyboardMarkup(row_width=1).add(btn_full_time_psy_of_edu_cost, btn_extramural_psy_of_edu_cost)
                                await bot.send_message(query_direction_cost.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_profile_psy_of_edu)

                                @dp.callback_query_handler(lambda profile_of_edu_psy: profile_of_edu_psy.data in ['full_time_psy_of_edu_cost',
                                                                                                                  'extramural_psy_of_edu_cost'])
                                async def cb_profile_of_edu_psy(query_profile_of_edu_psy: types.CallbackQuery):
                                    await bot.answer_callback_query(query_profile_of_edu_psy.id)
                                    if query_profile_of_edu_psy.data == 'full_time_psy_of_edu_cost':
                                        await bot.send_message(query_profile_of_edu_psy.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование "
                                                               "(профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[psycho_of_edu].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[psycho_of_edu].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_profile_of_edu_psy.data == 'extramural_psy_of_edu_cost':
                                        await bot.send_message(query_profile_of_edu_psy.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование "
                                                               "(профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[psycho_of_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                            elif query_profile_psycho_b_cost.data == 'psycho_electro_b_profile':
                                await bot.send_message(query_profile_psycho_b_cost.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология образования (с применением электронного обучения и "
                                                       "дистанционных образовательных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n" + cost_of_study[psycho_of_edu_electro].text.strip(),
                                                       parse_mode='html')
                    elif query_direction_cost.data == 'prof_cost':
                        btn_automation_b_profile_prof = InlineKeyboardButton('Автоматизация энергетических систем', callback_data='automation_b_profile_prof')
                        btn_graphic_des_b_profile_prof = InlineKeyboardButton('Декорирование интерьера и графический дизайн', callback_data='graphic_des_b_profile_prof')
                        kb_bak_profile_prof = InlineKeyboardMarkup(row_width=1).add(btn_automation_b_profile_prof, btn_graphic_des_b_profile_prof)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_profile_prof)

                        @dp.callback_query_handler(lambda profile_prof_b_cost: profile_prof_b_cost.data in ['automation_b_profile_prof', 'graphic_des_b_profile_prof'])
                        async def callback_profile_prof_b_cost(query_profile_prof_b_cost: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_prof_b_cost.id)
                            if query_profile_prof_b_cost.data == 'automation_b_profile_prof':
                                await bot.send_message(query_profile_prof_b_cost.from_user.id,
                                                       "44.03.04 Профессиональное обучение (по отраслям) "
                                                       "(профиль: Автоматизация энергетических систем)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[automation].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[automation].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[automation].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[automation].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_profile_prof_b_cost.data == 'graphic_des_b_profile_prof':
                                btn_full_time_graph_cost = InlineKeyboardButton('Очная', callback_data='full_time_graph_cost')
                                btn_extramural_graph_cost = InlineKeyboardButton('Заочная', callback_data='extramural_graph_cost')
                                kb_form_of_edu_graph = InlineKeyboardMarkup(row_width=1).add(btn_full_time_graph_cost, btn_extramural_graph_cost)
                                await bot.send_message(query_direction_cost.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_graph)

                                @dp.callback_query_handler(lambda form_of_edu_graph: form_of_edu_graph.data in ['full_time_graph_cost', 'extramural_graph_cost'])
                                async def cb_form_of_edu_graph(query_form_of_edu_graph: types.CallbackQuery):
                                    await bot.answer_callback_query(query_form_of_edu_graph.id)
                                    if query_form_of_edu_graph.data == 'full_time_graph_cost':
                                        await bot.send_message(query_form_of_edu_graph.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[graphic].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[graphic].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[graphic].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[graphic].find_parent('tr').find_parent('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_form_of_edu_graph.data == 'extramural_graph_cost':
                                        await bot.send_message(query_form_of_edu_graph.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[graphic].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[graphic].find_parent('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[graphic].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[graphic].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                    elif query_direction_cost.data == 'ped_two_cost':
                        btn_eng_b_two_profile = InlineKeyboardButton('Английский язык, родной (татарский) язык и литература', callback_data='eng_b_two_profile')
                        btn_biol_b_two_profile = InlineKeyboardButton('Биология и Химия', callback_data='biol_b_two_profile')
                        btn_pre_b_two_profile = InlineKeyboardButton('Дошкольное образование и ...', callback_data='pre_b_two_profile')
                        btn_history_b_two_profile = InlineKeyboardButton('История и ...', callback_data='history_b_two_profile')
                        btn_maths_b_two_profile = InlineKeyboardButton('Математика и ...', callback_data='maths_b_two_profile')
                        btn_rus_b_two_profile = InlineKeyboardButton('Русский язык и ...', callback_data='rus_b_two_profile')
                        btn_phys_b_two_profile = InlineKeyboardButton('Физическая культура и ...', callback_data='phys_b_two_profile')
                        kb_bak_two_profile = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_two_profile, btn_biol_b_two_profile, btn_pre_b_two_profile,
                                                                                   btn_history_b_two_profile, btn_maths_b_two_profile, btn_rus_b_two_profile,
                                                                                   btn_phys_b_two_profile)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_two_profile)

                        @dp.callback_query_handler(lambda two_profile_b_cost: two_profile_b_cost.data in ['eng_b_two_profile', 'biol_b_two_profile',
                                                                                                          'pre_b_two_profile', 'history_b_two_profile',
                                                                                                          'maths_b_two_profile', 'rus_b_two_profile', 'phys_b_two_profile'])
                        async def callback_two_profile_b_cost(query_two_profile_b_cost: types.CallbackQuery):
                            await bot.answer_callback_query(query_two_profile_b_cost.id)
                            if query_two_profile_b_cost.data == 'eng_b_two_profile':
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Английский язык, родной (татарский) язык и литература)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[eng_two_pr].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[eng_two_pr].find_next_sibling('td').text.strip() + "\n",
                                                       parse_mode='html')
                            elif query_two_profile_b_cost.data == 'biol_b_two_profile':
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Биология и Химия)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[biology_two_pr].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[biology_two_pr].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[biology_two_pr].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[biology_two_pr].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_two_profile_b_cost.data == 'pre_b_two_profile':
                                btn_add_b_2_profile = InlineKeyboardButton('Дополнительное образование (художественное творчество)', callback_data='add_b_2_profile')
                                btn_elem_b_2_profile = InlineKeyboardButton('Начальное образование', callback_data='elem_b_2_profile')
                                btn_tatar_b_2_profile = InlineKeyboardButton('Родной (татарский) язык и литература', callback_data='tatar_b_2_profile')
                                kb_bak_2_profile = InlineKeyboardMarkup(row_width=1).add(btn_add_b_2_profile, btn_elem_b_2_profile, btn_tatar_b_2_profile)
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Дошкольное образование и ...", reply_markup=kb_bak_2_profile)

                                @dp.callback_query_handler(lambda profile_b_cost_2: profile_b_cost_2.data in ['add_b_2_profile', 'elem_b_2_profile', 'tatar_b_2_profile'])
                                async def callback_2_profile_b_cost(query_2_profile_b_cost: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_cost.id)
                                    if query_2_profile_b_cost.data == 'add_b_2_profile':
                                        await bot.send_message(query_2_profile_b_cost.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Дополнительное образование "
                                                               "(художественное творчество))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[add_edu].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[add_edu].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[add_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[add_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost.data == 'elem_b_2_profile':
                                        await bot.send_message(query_2_profile_b_cost.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Начальное образование)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[elem_edu].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[elem_edu].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[elem_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[elem_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost.data == 'tatar_b_2_profile':
                                        await bot.send_message(query_2_profile_b_cost.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование, родной (татарский) язык и литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет 6 месяцев\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[tatar].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[tatar].find_next_sibling('td').text.strip() + "\n",
                                                               parse_mode='html')
                            elif query_two_profile_b_cost.data == 'history_b_two_profile':
                                btn_eng_b_2_profile_his = InlineKeyboardButton('Иностранный (английский) язык', callback_data='eng_b_2_profile_his')
                                btn_society_b_2_profile_his = InlineKeyboardButton('Обществознание', callback_data='society_b_2_profile_his')
                                kb_bak_2_profile_his = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_2_profile_his, btn_society_b_2_profile_his)
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "История и ...", reply_markup=kb_bak_2_profile_his)

                                @dp.callback_query_handler(lambda profile_b_cost_2_his: profile_b_cost_2_his.data in ['eng_b_2_profile_his', 'society_b_2_profile_his'])
                                async def callback_2_profile_b_cost_his(query_2_profile_b_cost_his: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_cost_his.id)
                                    if query_2_profile_b_cost_his.data == 'eng_b_2_profile_his':
                                        await bot.send_message(query_2_profile_b_cost_his.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[english].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[english].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[english].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[english].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost_his.data == 'society_b_2_profile_his':
                                        await bot.send_message(query_2_profile_b_cost_his.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Обществознание)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[society].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[society].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[society].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[society].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                            elif query_two_profile_b_cost.data == 'maths_b_two_profile':
                                btn_info_b_2_profile_maths = InlineKeyboardButton('Информатика', callback_data='info_b_2_profile_maths')
                                btn_physics_b_2_profile_maths = InlineKeyboardButton('Физика', callback_data='physics_b_2_profile_maths')
                                kb_bak_2_profile_maths = InlineKeyboardMarkup(row_width=1).add(btn_info_b_2_profile_maths, btn_physics_b_2_profile_maths)
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Математика и ...", reply_markup=kb_bak_2_profile_maths)

                                @dp.callback_query_handler(lambda profile_b_cost_2_maths: profile_b_cost_2_maths.data in ['info_b_2_profile_maths',
                                                                                                                          'physics_b_2_profile_maths'])
                                async def callback_2_profile_b_cost_maths(query_2_profile_b_cost_maths: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_cost_maths.id)
                                    if query_2_profile_b_cost_maths.data == 'info_b_2_profile_maths':
                                        await bot.send_message(query_2_profile_b_cost_maths.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Информатика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[inform].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[inform].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[inform].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[inform].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost_maths.data == 'physics_b_2_profile_maths':
                                        await bot.send_message(query_2_profile_b_cost_maths.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Физика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[physics].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[physics].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[physics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[physics].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                            elif query_two_profile_b_cost.data == 'rus_b_two_profile':
                                btn_eng_b_2_profile_rus = InlineKeyboardButton('Иностранный (английский) язык', callback_data='eng_b_2_profile_rus')
                                btn_lit_b_2_profile_rus = InlineKeyboardButton('Литература', callback_data='lit_b_2_profile_rus')
                                kb_bak_2_profile_rus = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_2_profile_rus, btn_lit_b_2_profile_rus)
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Русский язык и ...", reply_markup=kb_bak_2_profile_rus)

                                @dp.callback_query_handler(lambda profile_b_cost_2_rus: profile_b_cost_2_rus.data in ['eng_b_2_profile_rus',
                                                                                                                      'lit_b_2_profile_rus'])
                                async def callback_2_profile_b_cost_rus(query_2_profile_b_cost_rus: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_cost_rus.id)
                                    if query_2_profile_b_cost_rus.data == 'eng_b_2_profile_rus':
                                        await bot.send_message(query_2_profile_b_cost_rus.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[eng_lang].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[eng_lang].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[eng_lang].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[eng_lang].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost_rus.data == 'lit_b_2_profile_rus':
                                        await bot.send_message(query_2_profile_b_cost_rus.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и Литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[litr].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[litr].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[litr].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[litr].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                            elif query_two_profile_b_cost.data == 'phys_b_two_profile':
                                btn_safe_b_2_profile_phys = InlineKeyboardButton('Безопасность жизнедеятельности', callback_data='safe_b_2_profile_phys')
                                btn_sport_b_2_profile_phys = InlineKeyboardButton('Дополнительное образование '
                                                                                  '(спортивная подготовка)', callback_data='sport_b_2_profile_phys')
                                kb_bak_2_profile_phys = InlineKeyboardMarkup(row_width=1).add(btn_safe_b_2_profile_phys, btn_sport_b_2_profile_phys)
                                await bot.send_message(query_two_profile_b_cost.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Физическая культура и ...", reply_markup=kb_bak_2_profile_phys)

                                @dp.callback_query_handler(lambda profile_b_cost_2_phys: profile_b_cost_2_phys.data in ['safe_b_2_profile_phys',
                                                                                                                        'sport_b_2_profile_phys'])
                                async def callback_2_profile_b_cost_phys(query_2_profile_b_cost_phys: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_cost_phys.id)
                                    if query_2_profile_b_cost_phys.data == 'safe_b_2_profile_phys':
                                        await bot.send_message(query_2_profile_b_cost_phys.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и безопасность жизнедеятельности)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[life_safety].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[life_safety].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[life_safety].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[life_safety].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                                    elif query_2_profile_b_cost_phys.data == 'sport_b_2_profile_phys':
                                        await bot.send_message(query_2_profile_b_cost_phys.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и дополнительное образование (спортивная подготовка))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>" + cost_of_study_title + ":</b>\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[sport].text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[sport].find_next_sibling('td').text.strip() + "\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       <b>для 1 курса:</b> " + cost_of_study[sport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                               "       <b>общая:</b> " + cost_of_study[sport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                               parse_mode='html')
                    elif query_direction_cost.data == 'linguistics_cost':
                        btn_lang_b_eng_china = InlineKeyboardButton('Английский язык, китайский язык', callback_data='lang_b_eng_china')
                        btn_lang_b_eng_de = InlineKeyboardButton('Английский язык, немецкий язык', callback_data='lang_b_eng_de')
                        kb_bak_lang = InlineKeyboardMarkup(row_width=1).add(btn_lang_b_eng_china, btn_lang_b_eng_de)
                        await bot.send_message(query_direction_cost.from_user.id,
                                               "Выбери нужные языки:", reply_markup=kb_bak_lang)

                        @dp.callback_query_handler(lambda bak_lang_cost: bak_lang_cost.data in ['lang_b_eng_china', 'lang_b_eng_de'])
                        async def callback_bak_lang_cost(query_bak_lang_cost: types.CallbackQuery):
                            await bot.answer_callback_query(query_bak_lang_cost.id)
                            if query_bak_lang_cost.data == 'lang_b_eng_china':
                                await bot.send_message(query_bak_lang_cost.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, китайский язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[china].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[china].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[china].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[china].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
                            elif query_bak_lang_cost.data == 'lang_b_eng_de':
                                await bot.send_message(query_bak_lang_cost.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, немецкий язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>" + cost_of_study_title + ":</b>\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[deutsch].text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[deutsch].find_next_sibling('td').text.strip() + "\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       <b>для 1 курса:</b> " + cost_of_study[deutsch].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                                       "       <b>общая:</b> " + cost_of_study[deutsch].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                                       parse_mode='html')
            elif query_direction_of_study.data == 'mag_cost':
                inline_btn_business_cost_mag = InlineKeyboardButton('Бизнес-педагогика', callback_data='business_cost_mag')
                inline_btn_engin_cost_mag = InlineKeyboardButton('Инженерная педагогика', callback_data='engin_cost_mag')
                inline_btn_eng_in_poly_cost_mag = InlineKeyboardButton('Иностранный язык в лингвополикультурном '
                                                                       'образовательном пространстве', callback_data='eng_in_poly_cost_mag')
                inline_btn_poly_cost_mag = InlineKeyboardButton('Полилингвальное образование', callback_data='poly_cost_mag')
                inline_btn_project_cost_mag = InlineKeyboardButton('Проектирование и оценка образовательных программ и процессов', callback_data='project_cost_mag')
                inline_btn_prof_cost_mag = InlineKeyboardButton('Профессиональная подготовка в области физической культуры и спорта', callback_data='prof_cost_mag')
                inline_btn_rus_lit_cost_mag = InlineKeyboardButton('Русский язык и литература в межкультурной коммуникации', callback_data='rus_lit_cost_mag')
                inline_btn_pre_cost_mag = InlineKeyboardButton('Управление дошкольным образованием', callback_data='pre_cost_mag')
                inline_btn_managment_of_edu_cost_mag = InlineKeyboardButton('Управление образовательной организацией', callback_data='managment_of_edu_cost_mag')
                inline_btn_digit_cost_mag = InlineKeyboardButton('Цифровое образование', callback_data='digit_cost_mag')
                in_kb_mag_profile = InlineKeyboardMarkup(row_width=1).add(inline_btn_business_cost_mag, inline_btn_engin_cost_mag, inline_btn_eng_in_poly_cost_mag,
                                                                          inline_btn_poly_cost_mag, inline_btn_project_cost_mag, inline_btn_prof_cost_mag,
                                                                          inline_btn_rus_lit_cost_mag, inline_btn_pre_cost_mag, inline_btn_managment_of_edu_cost_mag,
                                                                          inline_btn_digit_cost_mag)
                await bot.send_message(query_direction_of_study.from_user.id,
                                       "Выбери нужный профиль:", reply_markup=in_kb_mag_profile)

                @dp.callback_query_handler(lambda direction_cost_m: direction_cost_m.data in ['business_cost_mag', 'engin_cost_mag', 'eng_in_poly_cost_mag',
                                                                                              'poly_cost_mag', 'project_cost_mag', 'prof_cost_mag', 'rus_lit_cost_mag',
                                                                                              'pre_cost_mag', 'managment_of_edu_cost_mag', 'digit_cost_mag'])
                async def callback_direction_cost_m(query_direction_cost_m: types.CallbackQuery):
                    await bot.answer_callback_query(query_direction_cost_m.id)
                    if query_direction_cost_m.data == 'business_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Бизнес-педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[business_pedag].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[business_pedag].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[business_pedag].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[business_pedag].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'engin_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Инженерная педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[engin_pedag].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[engin_pedag].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[engin_pedag].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[engin_pedag].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'eng_in_poly_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Иностранный язык в лингвополикультурном образовательном пространстве)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[eng_in_poly].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[eng_in_poly].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[eng_in_poly].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[eng_in_poly].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'poly_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Полилингвальное образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_poly].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_poly].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_poly].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_poly].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'project_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Проектирование и оценка образовательных программ и процессов)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[project_p].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[project_p].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[project_p].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[project_p].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'prof_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Профессиональная подготовка в области физической культуры и спорта)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[prof_sport].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[prof_sport].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[prof_sport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[prof_sport].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'rus_lit_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Русский язык и литература в межкультурной коммуникации)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[rus_and_lit].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[rus_and_lit].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[rus_and_lit].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[rus_and_lit].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'pre_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Управление дошкольным образованием)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_pre].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_pre].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_pre].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_pre].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'managment_of_edu_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Управление образовательной организацией)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_managment].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_managment].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[edu_managment].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[edu_managment].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')
                    elif query_direction_cost_m.data == 'digit_cost_mag':
                        await bot.send_message(query_direction_cost_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Цифровое образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>" + cost_of_study_title + ":</b>\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[digit_edu].text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[digit_edu].find_next_sibling('td').text.strip() + "\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       <b>для 1 курса:</b> " + cost_of_study[digit_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').text.strip() + "\n"
                                               "       <b>общая:</b> " + cost_of_study[digit_edu].find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.strip(),
                                               parse_mode='html')

    # Вступительные испытания
    @dp.callback_query_handler(lambda c: c.data == 'entrance_tests')
    async def process_callback_entrance_tests(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        inline_btn_bak_entrance_tests = InlineKeyboardButton('Бакалавриат', callback_data='bak_entrance_tests')
        inline_btn_mag_entrance_tests = InlineKeyboardButton('Магистратура', callback_data='mag_entrance_tests')
        inline_kb_entrance_tests = InlineKeyboardMarkup(row_width=1).add(inline_btn_bak_entrance_tests, inline_btn_mag_entrance_tests)
        await bot.send_message(callback_query.from_user.id,
                               "Здесь ты найдешь информацию про <b>вступительные испытания</b>.\n"
                               "Если в одной строке указано несколько предметов/баллов, абитуриент может выбрать экзамен "
                               "по результатам ЕГЭ по одному из этих предметов по своему усмотрению.\n\n"
                               "Выбери нужный уровень обучения:", parse_mode='html', reply_markup=inline_kb_entrance_tests)

        @dp.callback_query_handler(lambda level_of_study_entrance: level_of_study_entrance.data in ['bak_entrance_tests', 'mag_entrance_tests'])
        async def callback_level_of_study_entrance(query_level_of_study_entrance: types.CallbackQuery):
            await bot.answer_callback_query(query_level_of_study_entrance.id)
            if query_level_of_study_entrance.data == 'bak_entrance_tests':
                inline_btn_info_entrance_tests = InlineKeyboardButton('Прикладная информатика', callback_data='info_entrance_tests')
                inline_btn_mech_entrance_tests = InlineKeyboardButton('Мехатроника и робототехника', callback_data='mech_entrance_tests')
                inline_btn_techno_entrance_tests = InlineKeyboardButton('Технология транспортных процессов', callback_data='techno_entrance_tests')
                inline_btn_economics_entrance_tests = InlineKeyboardButton('Экономика', callback_data='economics_entrance_tests')
                inline_btn_jurisprudence_entrance_tests = InlineKeyboardButton('Юриспруденция', callback_data='jurisprudence_entrance_tests')
                inline_btn_ped_entrance_tests = InlineKeyboardButton('Педагогическое образование', callback_data='ped_entrance_tests')
                inline_btn_psycho_entrance_tests = InlineKeyboardButton('Психолого-педагогическое образование', callback_data='psycho_entrance_tests')
                inline_btn_prof_entrance_tests = InlineKeyboardButton('Профессиональное обучение (по отраслям)', callback_data='prof_entrance_tests')
                inline_btn_ped_two_entrance_tests = InlineKeyboardButton('Педагогическое образование '
                                                                         '(с двумя профилями подготовки)', callback_data='ped_two_entrance_tests')
                inline_btn_ling_entrance_tests = InlineKeyboardButton('Лингвистика', callback_data='ling_entrance_tests')
                kb_entrance_tests_direc = InlineKeyboardMarkup(row_width=1).add(inline_btn_info_entrance_tests, inline_btn_mech_entrance_tests,
                                                                                inline_btn_techno_entrance_tests, inline_btn_economics_entrance_tests,
                                                                                inline_btn_jurisprudence_entrance_tests, inline_btn_ped_entrance_tests,
                                                                                inline_btn_psycho_entrance_tests, inline_btn_prof_entrance_tests,
                                                                                inline_btn_ped_two_entrance_tests, inline_btn_ling_entrance_tests)
                await bot.send_message(query_level_of_study_entrance.from_user.id,
                                       "Выбери нужное направление:", reply_markup=kb_entrance_tests_direc)

                @dp.callback_query_handler(lambda direction_entrance: direction_entrance.data in ['info_entrance_tests', 'mech_entrance_tests', 'techno_entrance_tests',
                                                                                                  'economics_entrance_tests', 'jurisprudence_entrance_tests',
                                                                                                  'ped_entrance_tests', 'psycho_entrance_tests', 'prof_entrance_tests',
                                                                                                  'ped_two_entrance_tests', 'ling_entrance_tests'])
                async def callback_direction_entrance(query_direction_entrance: types.CallbackQuery):
                    await bot.answer_callback_query(query_direction_entrance.id)
                    if query_direction_entrance.data == 'info_entrance_tests':
                        btn_full_time_info_entrance = InlineKeyboardButton('Очная', callback_data='full_time_info_entrance')
                        btn_extramural_info_entrance = InlineKeyboardButton('Заочная', callback_data='extramural_info_entrance')
                        kb_form_of_edu_info_entrance = InlineKeyboardMarkup(row_width=1).add(btn_full_time_info_entrance, btn_extramural_info_entrance)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_info_entrance)

                        @dp.callback_query_handler(lambda form_of_edu_info_entrance: form_of_edu_info_entrance.data in ['full_time_info_entrance',
                                                                                                                        'extramural_info_entrance'])
                        async def cb_form_of_edu_info_entrance(query_form_of_edu_info_entrance: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_info_entrance.id)
                            if query_form_of_edu_info_entrance.data == 'full_time_info_entrance':
                                await bot.send_message(query_form_of_edu_info_entrance.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[computer_science].text.strip() + " (" + entrance_tests[computer_science].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].
                                                       find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace(' *', '') + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                       find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').
                                                       find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                       find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                       find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').
                                                       find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_form_of_edu_info_entrance.data == 'extramural_info_entrance':
                                await bot.send_message(query_form_of_edu_info_entrance.from_user.id,
                                                       "09.03.03 Прикладная информатика "
                                                       "(профиль: Прикладная информатика в экономике)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').
                                                       text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').
                                                       text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                       find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').
                                                       find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                       find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                       find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[computer_science].find_parent('tr').find_parent('tr').find_parent('tr').
                                                       find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                       find_next('td').find_next_sibling('td').text.strip() + ")\n",
                                                       parse_mode='html')
                    elif query_direction_entrance.data == 'mech_entrance_tests':
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "15.03.06 Мехатроника и робототехника "
                                               "(профиль: Физические основы мехатроники и робототехники)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> очно-заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + entrance_tests[mechatronics].text.strip() + " (" + entrance_tests[mechatronics].find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[mechatronics].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[mechatronics].find_parent('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[mechatronics].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[mechatronics].find_parent('tr').
                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace('*', '') + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[mechatronics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[mechatronics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[mechatronics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[mechatronics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_entrance.data == 'techno_entrance_tests':
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "23.03.01 Технология транспортных процессов "
                                               "(профиль: Проектирование и управление интеллектуальными транспортными системами)\n\n"
                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + entrance_tests[transport].text.strip() + " (" + entrance_tests[transport].find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[transport].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[transport].find_parent('tr').
                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[transport].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[transport].find_parent('tr').
                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[transport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[transport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                               "       " + entrance_tests[transport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[transport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_entrance.data == 'economics_entrance_tests':
                        btn_part_time_ec_ent = InlineKeyboardButton('Очно-заочная', callback_data='part_time_ec_ent')
                        btn_full_time_ec_ent = InlineKeyboardButton('Очная', callback_data='full_time_ec_ent')
                        kb_form_of_edu_ec_ent = InlineKeyboardMarkup(row_width=1).add(btn_part_time_ec_ent, btn_full_time_ec_ent)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_ec_ent)

                        @dp.callback_query_handler(lambda form_of_edu_ec_ent: form_of_edu_ec_ent.data in ['part_time_ec_ent', 'full_time_ec_ent'])
                        async def cb_form_of_edu_ec_ent(query_form_of_edu_ec_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_ec_ent.id)
                            if query_form_of_edu_ec_ent.data == 'part_time_ec_ent':
                                await bot.send_message(query_form_of_edu_ec_ent.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(реализуется с применением электронного обучения и дистанционных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[part_time_economics].text.strip() + " (" + entrance_tests[part_time_economics].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_economics].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_economics].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_economics].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[part_time_economics].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace('*', '') + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[part_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_form_of_edu_ec_ent.data == 'full_time_ec_ent':
                                await bot.send_message(query_form_of_edu_ec_ent.from_user.id,
                                                       "38.03.01 Экономика (профиль: Экономика и финансы организаций "
                                                       "(с углублённым изучением иностранных языков))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[full_time_economics].text.strip() + " (" + entrance_tests[full_time_economics].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_economics].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_economics].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_economics].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[full_time_economics].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace('*', '') + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[full_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_economics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                    elif query_direction_entrance.data == 'jurisprudence_entrance_tests':
                        btn_full_time_juri_entrance = InlineKeyboardButton('Очная', callback_data='full_time_juri_entrance')
                        btn_part_time_juri_entrance = InlineKeyboardButton('Очно-заочная', callback_data='part_time_juri_entrance')
                        kb_form_of_edu_juri_entrance = InlineKeyboardMarkup(row_width=1).add(btn_full_time_juri_entrance, btn_part_time_juri_entrance)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_juri_entrance)

                        @dp.callback_query_handler(lambda form_of_edu_juri_entrance: form_of_edu_juri_entrance.data in ['full_time_juri_entrance',
                                                                                                                        'part_time_juri_entrance'])
                        async def cb_form_of_edu_juri_entrance(query_form_of_edu_juri_entrance: types.CallbackQuery):
                            await bot.answer_callback_query(query_form_of_edu_juri_entrance.id)
                            if query_form_of_edu_juri_entrance.data == 'full_time_juri_entrance':
                                await bot.send_message(query_form_of_edu_juri_entrance.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[full_time_law].text.strip() + " (" + entrance_tests[full_time_law].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_law].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_law].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_law].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[full_time_law].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[full_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[full_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[full_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_form_of_edu_juri_entrance.data == 'part_time_juri_entrance':
                                await bot.send_message(query_form_of_edu_juri_entrance.from_user.id,
                                                       "40.03.01 Юриспруденция (профиль: Гражданское право (реализуется с применением электронного "
                                                       "обучения и дистанционных технологий))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[part_time_law].text.strip() + " (" + entrance_tests[part_time_law].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_law].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_law].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_law].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[part_time_law].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[part_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[part_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[part_time_law].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                    elif query_direction_entrance.data == 'ped_entrance_tests':
                        btn_eng_b_profile_ent = InlineKeyboardButton('Английский язык', callback_data='eng_b_profile_ent')
                        btn_elem_edu_b_profile_ent = InlineKeyboardButton('Начальное образование', callback_data='elem_edu_b_profile_ent')
                        btn_gen_add_b_profile_ent = InlineKeyboardButton('Общее и дополнительное образование в '
                                                                         'предметной области \"Технология\"', callback_data='gen_add_b_profile_ent')
                        btn_tech_b_profile_ent = InlineKeyboardButton('Технология и робототехника', callback_data='tech_b_profile_ent')
                        btn_phy_cult_b_profile_ent = InlineKeyboardButton('Физическая культура', callback_data='phy_cult_b_profile_ent')
                        kb_bak_profile_ped_ent = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_profile_ent, btn_elem_edu_b_profile_ent, btn_gen_add_b_profile_ent,
                                                                                       btn_tech_b_profile_ent, btn_phy_cult_b_profile_ent)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_profile_ped_ent)

                        @dp.callback_query_handler(lambda profile_ped_b_ent: profile_ped_b_ent.data in ['eng_b_profile_ent', 'elem_edu_b_profile_ent',
                                                                                                        'gen_add_b_profile_ent', 'tech_b_profile_ent',
                                                                                                        'phy_cult_b_profile_ent'])
                        async def callback_profile_b_ent(query_profile_b_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_b_ent.id)
                            if query_profile_b_ent.data == 'eng_b_profile_ent':
                                await bot.send_message(query_profile_b_ent.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Английский язык)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[english_ped].text.strip() + " (" + entrance_tests[english_ped].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[english_ped].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[english_ped].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[english_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[english_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_b_ent.data == 'elem_edu_b_profile_ent':
                                await bot.send_message(query_profile_b_ent.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Начальное образование)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[elementary_ped].text.strip() + " (" + entrance_tests[elementary_ped].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[elementary_ped].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elementary_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[elementary_ped].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elementary_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[elementary_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elementary_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[elementary_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elementary_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_b_ent.data == 'gen_add_b_profile_ent':
                                await bot.send_message(query_profile_b_ent.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Общее и дополнительное образование в предметной области \"Технология\")\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[gen_add_ped].text.strip() + " (" + entrance_tests[gen_add_ped].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[gen_add_ped].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[gen_add_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[gen_add_ped].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[gen_add_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[gen_add_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[gen_add_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[gen_add_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[gen_add_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_b_ent.data == 'tech_b_profile_ent':
                                await bot.send_message(query_profile_b_ent.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Технология и робототехника)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[technology_ped].text.strip() + " (" + entrance_tests[technology_ped].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[technology_ped].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[technology_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[technology_ped].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[technology_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[technology_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[technology_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[technology_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[technology_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_b_ent.data == 'phy_cult_b_profile_ent':
                                await bot.send_message(query_profile_b_ent.from_user.id,
                                                       "44.03.01 Педагогическое образование "
                                                       "(профиль: Физическая культура)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[cult_ped].text.strip() + " (" + entrance_tests[cult_ped].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[cult_ped].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[cult_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[cult_ped].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[cult_ped].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[cult_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[cult_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[cult_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[cult_ped].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                    elif query_direction_entrance.data == 'psycho_entrance_tests':
                        btn_psycho_of_pre_b_profile_ent = InlineKeyboardButton('Психология и педагогика дошкольного '
                                                                               'образования', callback_data='psycho_of_pre_b_profile_ent')
                        btn_psycho_of_edu_b_profile_ent = InlineKeyboardButton('Психология образования', callback_data='psycho_of_edu_b_profile_ent')
                        btn_psycho_electro_b_profile_ent = InlineKeyboardButton('Психология образования (с применением электронного '
                                                                                'обучения и дистанционных образовательных технологий)',
                                                                                callback_data='psycho_electro_b_profile_ent')
                        kb_bak_profile_psy_ped_ent = InlineKeyboardMarkup(row_width=1).add(btn_psycho_of_pre_b_profile_ent, btn_psycho_of_edu_b_profile_ent,
                                                                                           btn_psycho_electro_b_profile_ent)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_profile_psy_ped_ent)

                        @dp.callback_query_handler(lambda profile_psycho_b_ent: profile_psycho_b_ent.data in ['psycho_of_pre_b_profile_ent',
                                                                                                              'psycho_of_edu_b_profile_ent',
                                                                                                              'psycho_electro_b_profile_ent'])
                        async def callback_profile_psycho_b_ent(query_profile_psycho_b_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_psycho_b_ent.id)
                            if query_profile_psycho_b_ent.data == 'psycho_of_pre_b_profile_ent':
                                await bot.send_message(query_profile_psycho_b_ent.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология и педагогика дошкольного образования)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[psycho_pre].text.strip() + " (" + entrance_tests[psycho_pre].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_pre].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_pre].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_pre].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_pre].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[psycho_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_psycho_b_ent.data == 'psycho_of_edu_b_profile_ent':
                                btn_full_time_psy_of_edu_ent = InlineKeyboardButton('Очная', callback_data='full_time_psy_of_edu_ent')
                                btn_extramural_psy_of_edu_ent = InlineKeyboardButton('Заочная', callback_data='extramural_psy_of_edu_ent')
                                kb_profile_psy_of_edu_ent = InlineKeyboardMarkup(row_width=1).add(btn_full_time_psy_of_edu_ent, btn_extramural_psy_of_edu_ent)
                                await bot.send_message(query_profile_psycho_b_ent.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_profile_psy_of_edu_ent)

                                @dp.callback_query_handler(lambda profile_of_edu_psy_ent: profile_of_edu_psy_ent.data in ['full_time_psy_of_edu_ent',
                                                                                                                          'extramural_psy_of_edu_ent'])
                                async def cb_profile_of_edu_psy_ent(query_form_of_edu_psy_ent: types.CallbackQuery):
                                    await bot.answer_callback_query(query_form_of_edu_psy_ent.id)
                                    if query_form_of_edu_psy_ent.data == 'full_time_psy_of_edu_ent':
                                        await bot.send_message(query_form_of_edu_psy_ent.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование "
                                                               "(профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[psycho_of_edu].text.strip() + " (" + entrance_tests[psycho_of_edu].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[psycho_of_edu].
                                                               find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace('*', '') + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                               find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').
                                                               find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                               find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].
                                                               find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_form_of_edu_psy_ent.data == 'extramural_psy_of_edu_ent':
                                        await bot.send_message(query_form_of_edu_psy_ent.from_user.id,
                                                               "44.03.02 Психолого-педагогическое образование "
                                                               "(профиль: Психология образования)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').
                                                               text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').
                                                               text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                               find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').
                                                               find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                               find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu].find_parent('tr').find_parent('tr').find_parent('tr').
                                                               find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n",
                                                               parse_mode='html')
                            elif query_profile_psycho_b_ent.data == 'psycho_electro_b_profile_ent':
                                await bot.send_message(query_profile_psycho_b_ent.from_user.id,
                                                       "44.03.02 Психолого-педагогическое образование "
                                                       "(профиль: Психология образования (с применением электронного обучения и "
                                                       "дистанционных образовательных технологий)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очно-заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[psycho_of_edu_electro].text.strip() + " (" + entrance_tests[psycho_of_edu_electro].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu_electro].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[psycho_of_edu_electro].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip().replace('*', '') + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[psycho_of_edu_electro].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                    elif query_direction_entrance.data == 'prof_entrance_tests':
                        btn_automation_b_ent_prof = InlineKeyboardButton('Автоматизация энергетических систем', callback_data='automation_b_ent_prof')
                        btn_graphic_des_b_ent_prof = InlineKeyboardButton('Декорирование интерьера и графический дизайн', callback_data='graphic_des_b_ent_prof')
                        kb_bak_ent_prof = InlineKeyboardMarkup(row_width=1).add(btn_automation_b_ent_prof, btn_graphic_des_b_ent_prof)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_ent_prof)

                        @dp.callback_query_handler(lambda profile_prof_b_ent: profile_prof_b_ent.data in ['automation_b_ent_prof', 'graphic_des_b_ent_prof'])
                        async def callback_profile_prof_b_ent(query_profile_prof_b_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_profile_prof_b_ent.id)
                            if query_profile_prof_b_ent.data == 'automation_b_ent_prof':
                                await bot.send_message(query_profile_prof_b_ent.from_user.id,
                                                       "44.03.04 Профессиональное обучение (по отраслям) "
                                                       "(профиль: Автоматизация энергетических систем)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> заочная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[automation].text.strip() + " (" + entrance_tests[automation].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[automation].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[automation].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[automation].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[automation].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[automation].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[automation].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[automation].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[automation].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_profile_prof_b_ent.data == 'graphic_des_b_ent_prof':
                                btn_full_time_graph_entrance = InlineKeyboardButton('Очная', callback_data='full_time_graph_entrance')
                                btn_extramural_graph_entrance = InlineKeyboardButton('Заочная', callback_data='extramural_graph_entrance')
                                kb_form_of_edu_graph_entrance = InlineKeyboardMarkup(row_width=1).add(btn_full_time_graph_entrance, btn_extramural_graph_entrance)
                                await bot.send_message(query_profile_prof_b_ent.from_user.id,
                                                       "Выбери нужную форму обучения:", reply_markup=kb_form_of_edu_graph_entrance)

                                @dp.callback_query_handler(lambda form_of_edu_graph_entrance: form_of_edu_graph_entrance.data in ['full_time_graph_entrance',
                                                                                                                                  'extramural_graph_entrance'])
                                async def cb_form_of_edu_graph_entrance(query_form_of_edu_graph_entrance: types.CallbackQuery):
                                    await bot.answer_callback_query(query_form_of_edu_graph_entrance.id)
                                    if query_form_of_edu_graph_entrance.data == 'full_time_graph_entrance':
                                        await bot.send_message(query_form_of_edu_graph_entrance.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[graphic].text.strip() + " (" + entrance_tests[graphic].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].
                                                               find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                               find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').
                                                               find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').
                                                               find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').
                                                               find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_form_of_edu_graph_entrance.data == 'extramural_graph_entrance':
                                        await bot.send_message(query_form_of_edu_graph_entrance.from_user.id,
                                                               "44.03.04 Профессиональное обучение (по отраслям) "
                                                               "(профиль: Декорирование интерьера и графический дизайн)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 4 года 6 месяцев\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').
                                                               text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').
                                                               text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                               find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').
                                                               find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').
                                                               find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[graphic].find_parent('tr').find_parent('tr').find_parent('tr').
                                                               find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('table').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').
                                                               find_next('td').find_next_sibling('td').text.strip() + ")\n",
                                                               parse_mode='html')
                    elif query_direction_entrance.data == 'ped_two_entrance_tests':
                        btn_eng_b_two_ent = InlineKeyboardButton('Английский язык, родной (татарский) язык и литература', callback_data='eng_b_two_ent')
                        btn_biol_b_two_ent = InlineKeyboardButton('Биология и Химия', callback_data='biol_b_two_ent')
                        btn_pre_b_two_ent = InlineKeyboardButton('Дошкольное образование и ...', callback_data='pre_b_two_ent')
                        btn_history_b_two_ent = InlineKeyboardButton('История и ...', callback_data='history_b_two_ent')
                        btn_maths_b_two_ent = InlineKeyboardButton('Математика и ...', callback_data='maths_b_two_ent')
                        btn_rus_b_two_ent = InlineKeyboardButton('Русский язык и ...', callback_data='rus_b_two_ent')
                        btn_phys_b_two_ent = InlineKeyboardButton('Физическая культура и ...', callback_data='phys_b_two_ent')
                        kb_bak_two_ent = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_two_ent, btn_biol_b_two_ent, btn_pre_b_two_ent,
                                                                               btn_history_b_two_ent, btn_maths_b_two_ent, btn_rus_b_two_ent,
                                                                               btn_phys_b_two_ent)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужный профиль:", reply_markup=kb_bak_two_ent)

                        @dp.callback_query_handler(lambda two_profile_b_ent: two_profile_b_ent.data in ['eng_b_two_ent', 'biol_b_two_ent',
                                                                                                        'pre_b_two_ent', 'history_b_two_ent',
                                                                                                        'maths_b_two_ent', 'rus_b_two_ent', 'phys_b_two_ent'])
                        async def callback_two_profile_b_ent(query_two_profile_b_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_two_profile_b_ent.id)
                            if query_two_profile_b_ent.data == 'eng_b_two_ent':
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Английский язык, родной (татарский) язык и литература)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[eng_two_pr].text.strip() + " (" + entrance_tests[eng_two_pr].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[eng_two_pr].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_two_pr].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[eng_two_pr].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_two_pr].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_two_profile_b_ent.data == 'biol_b_two_ent':
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                       "(профиль: Биология и Химия)\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[biology_two_pr].text.strip() + " (" + entrance_tests[biology_two_pr].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[biology_two_pr].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[biology_two_pr].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[biology_two_pr].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[biology_two_pr].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[biology_two_pr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[biology_two_pr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[biology_two_pr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[biology_two_pr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_two_profile_b_ent.data == 'pre_b_two_ent':
                                btn_add_b_2_ent = InlineKeyboardButton('Дополнительное образование (художественное творчество)', callback_data='add_b_2_ent')
                                btn_elem_b_2_ent = InlineKeyboardButton('Начальное образование', callback_data='elem_b_2_ent')
                                btn_tatar_b_2_ent = InlineKeyboardButton('Родной (татарский) язык и литература', callback_data='tatar_b_2_ent')
                                kb_bak_2_ent = InlineKeyboardMarkup(row_width=1).add(btn_add_b_2_ent, btn_elem_b_2_ent, btn_tatar_b_2_ent)
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Дошкольное образование и ...", reply_markup=kb_bak_2_ent)

                                @dp.callback_query_handler(lambda profile_b_ent_2: profile_b_ent_2.data in ['add_b_2_ent', 'elem_b_2_ent', 'tatar_b_2_ent'])
                                async def callback_2_profile_b_ent(query_2_profile_b_ent: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_ent.id)
                                    if query_2_profile_b_ent.data == 'add_b_2_ent':
                                        await bot.send_message(query_2_profile_b_ent.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Дополнительное образование "
                                                               "(художественное творчество))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[add_edu].text.strip() + " (" + entrance_tests[add_edu].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[add_edu].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[add_edu].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[add_edu].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[add_edu].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[add_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[add_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[add_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[add_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent.data == 'elem_b_2_ent':
                                        await bot.send_message(query_2_profile_b_ent.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование и Начальное образование)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[elem_edu].text.strip() + " (" + entrance_tests[elem_edu].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[elem_edu].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elem_edu].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[elem_edu].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[elem_edu].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[elem_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elem_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[elem_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[elem_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent.data == 'tatar_b_2_ent':
                                        await bot.send_message(query_2_profile_b_ent.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Дошкольное образование, родной (татарский) язык и литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> заочная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет 6 месяцев\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[tatar].text.strip() + " (" + entrance_tests[tatar].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[tatar].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[tatar].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[tatar].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[tatar].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                            elif query_two_profile_b_ent.data == 'history_b_two_ent':
                                btn_eng_b_2_ent_his = InlineKeyboardButton('Иностранный (английский) язык', callback_data='eng_b_2_ent_his')
                                btn_society_b_2_ent_his = InlineKeyboardButton('Обществознание', callback_data='society_b_2_ent_his')
                                kb_bak_2_ent_his = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_2_ent_his, btn_society_b_2_ent_his)
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "История и ...", reply_markup=kb_bak_2_ent_his)

                                @dp.callback_query_handler(lambda profile_b_ent_2_his: profile_b_ent_2_his.data in ['eng_b_2_ent_his', 'society_b_2_ent_his'])
                                async def callback_2_profile_b_ent_his(query_2_profile_b_ent_his: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_ent_his.id)
                                    if query_2_profile_b_ent_his.data == 'eng_b_2_ent_his':
                                        await bot.send_message(query_2_profile_b_ent_his.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[english].text.strip() + " (" + entrance_tests[english].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[english].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[english].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[english].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[english].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[english].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[english].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent_his.data == 'society_b_2_ent_his':
                                        await bot.send_message(query_2_profile_b_ent_his.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: История и Обществознание)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[society].text.strip() + " (" + entrance_tests[society].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[society].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[society].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[society].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[society].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[society].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[society].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[society].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[society].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                            elif query_two_profile_b_ent.data == 'maths_b_two_ent':
                                btn_info_b_2_ent_maths = InlineKeyboardButton('Информатика', callback_data='info_b_2_ent_maths')
                                btn_physics_b_2_ent_maths = InlineKeyboardButton('Физика', callback_data='physics_b_2_ent_maths')
                                kb_bak_2_ent_maths = InlineKeyboardMarkup(row_width=1).add(btn_info_b_2_ent_maths, btn_physics_b_2_ent_maths)
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Математика и ...", reply_markup=kb_bak_2_ent_maths)

                                @dp.callback_query_handler(lambda profile_b_ent_2_maths: profile_b_ent_2_maths.data in ['info_b_2_ent_maths',
                                                                                                                        'physics_b_2_ent_maths'])
                                async def callback_2_profile_b_ent_maths(query_2_profile_b_ent_maths: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_ent_maths.id)
                                    if query_2_profile_b_ent_maths.data == 'info_b_2_ent_maths':
                                        await bot.send_message(query_2_profile_b_ent_maths.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Информатика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[inform].text.strip() + " (" + entrance_tests[inform].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[inform].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[inform].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[inform].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[inform].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[inform].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[inform].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[inform].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[inform].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent_maths.data == 'physics_b_2_ent_maths':
                                        await bot.send_message(query_2_profile_b_ent_maths.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Математика и Физика)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[physics].text.strip() + " (" + entrance_tests[physics].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[physics].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[physics].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[physics].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[physics].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[physics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[physics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[physics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[physics].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                            elif query_two_profile_b_ent.data == 'rus_b_two_ent':
                                btn_eng_b_2_ent_rus = InlineKeyboardButton('Иностранный (английский) язык', callback_data='eng_b_2_ent_rus')
                                btn_lit_b_2_ent_rus = InlineKeyboardButton('Литература', callback_data='lit_b_2_ent_rus')
                                kb_bak_2_ent_rus = InlineKeyboardMarkup(row_width=1).add(btn_eng_b_2_ent_rus, btn_lit_b_2_ent_rus)
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Русский язык и ...", reply_markup=kb_bak_2_ent_rus)

                                @dp.callback_query_handler(lambda profile_b_ent_2_rus: profile_b_ent_2_rus.data in ['eng_b_2_ent_rus',
                                                                                                                    'lit_b_2_ent_rus'])
                                async def callback_2_profile_b_ent_rus(query_2_profile_b_ent_rus: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_ent_rus.id)
                                    if query_2_profile_b_ent_rus.data == 'eng_b_2_ent_rus':
                                        await bot.send_message(query_2_profile_b_ent_rus.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и иностранный (английский) язык)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[eng_lang].text.strip() + " (" + entrance_tests[eng_lang].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[eng_lang].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_lang].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[eng_lang].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[eng_lang].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[eng_lang].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_lang].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[eng_lang].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_lang].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent_rus.data == 'lit_b_2_ent_rus':
                                        await bot.send_message(query_2_profile_b_ent_rus.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Русский язык и Литература)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[litr].text.strip() + " (" + entrance_tests[litr].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[litr].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[litr].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[litr].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[litr].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[litr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[litr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[litr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[litr].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                            elif query_two_profile_b_ent.data == 'phys_b_two_ent':
                                btn_safe_b_2_ent_phys = InlineKeyboardButton('Безопасность жизнедеятельности', callback_data='safe_b_2_ent_phys')
                                btn_sport_b_2_ent_phys = InlineKeyboardButton('Дополнительное образование '
                                                                              '(спортивная подготовка)', callback_data='sport_b_2_ent_phys')
                                kb_bak_2_ent_phys = InlineKeyboardMarkup(row_width=1).add(btn_safe_b_2_ent_phys, btn_sport_b_2_ent_phys)
                                await bot.send_message(query_two_profile_b_ent.from_user.id,
                                                       "Выбери нужный профиль:\n\n"
                                                       "Физическая культура и ...", reply_markup=kb_bak_2_ent_phys)

                                @dp.callback_query_handler(lambda profile_b_ent_2_phys: profile_b_ent_2_phys.data in ['safe_b_2_ent_phys',
                                                                                                                      'sport_b_2_ent_phys'])
                                async def callback_2_profile_b_ent_phys(query_2_profile_b_ent_phys: types.CallbackQuery):
                                    await bot.answer_callback_query(query_2_profile_b_ent_phys.id)
                                    if query_2_profile_b_ent_phys.data == 'safe_b_2_ent_phys':
                                        await bot.send_message(query_2_profile_b_ent_phys.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и безопасность жизнедеятельности)\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[life_safety].text.strip() + " (" + entrance_tests[life_safety].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[life_safety].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[life_safety].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[life_safety].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[life_safety].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[life_safety].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[life_safety].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[life_safety].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[life_safety].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                                    elif query_2_profile_b_ent_phys.data == 'sport_b_2_ent_phys':
                                        await bot.send_message(query_2_profile_b_ent_phys.from_user.id,
                                                               "44.03.05 Педагогическое образование (с двумя профилями подготовки) "
                                                               "(профиль: Физическая культура и дополнительное образование (спортивная подготовка))\n\n"
                                                               "<b>Уровень обучения:</b> бакалавриат\n"
                                                               "<b>Форма обучения:</b> очная\n"
                                                               "<b>Продолжительность обучения:</b> 5 лет\n\n"
                                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                               "   <em>для граждан Российской Федерации:</em>\n"
                                                               "       " + entrance_tests[sport].text.strip() + " (" + entrance_tests[sport].find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[sport].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[sport].find_parent('tr').
                                                               find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[sport].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[sport].find_parent('tr').
                                                               find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "   <em>для иностранных граждан:</em>\n"
                                                               "       " + entrance_tests[sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                               "       " + entrance_tests[sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                               find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                               parse_mode='html')
                    elif query_direction_entrance.data == 'ling_entrance_tests':
                        btn_lang_b_eng_china_ent = InlineKeyboardButton('Английский язык, китайский язык', callback_data='lang_b_eng_china_ent')
                        btn_lang_b_eng_de_ent = InlineKeyboardButton('Английский язык, немецкий язык', callback_data='lang_b_eng_de_ent')
                        kb_bak_lang_ent = InlineKeyboardMarkup(row_width=1).add(btn_lang_b_eng_china_ent, btn_lang_b_eng_de_ent)
                        await bot.send_message(query_direction_entrance.from_user.id,
                                               "Выбери нужные языки:", reply_markup=kb_bak_lang_ent)

                        @dp.callback_query_handler(lambda bak_lang_ent: bak_lang_ent.data in ['lang_b_eng_china_ent', 'lang_b_eng_de_ent'])
                        async def callback_bak_lang_ent(query_bak_lang_ent: types.CallbackQuery):
                            await bot.answer_callback_query(query_bak_lang_ent.id)
                            if query_bak_lang_ent.data == 'lang_b_eng_china_ent':
                                await bot.send_message(query_bak_lang_ent.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, китайский язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[china].text.strip() + " (" + entrance_tests[china].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[china].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[china].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[china].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[china].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[china].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[china].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[china].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[china].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
                            elif query_bak_lang_ent.data == 'lang_b_eng_de_ent':
                                await bot.send_message(query_bak_lang_ent.from_user.id,
                                                       "45.03.02 Лингвистика "
                                                       "(профиль: Перевод и переводоведение (английский язык, немецкий язык))\n\n"
                                                       "<b>Уровень обучения:</b> бакалавриат\n"
                                                       "<b>Форма обучения:</b> очная\n"
                                                       "<b>Продолжительность обучения:</b> 4 года\n\n"
                                                       "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                                       "   <em>для граждан Российской Федерации:</em>\n"
                                                       "       " + entrance_tests[deutsch].text.strip() + " (" + entrance_tests[deutsch].find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[deutsch].find_parent('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[deutsch].find_parent('tr').
                                                       find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[deutsch].find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip().replace('*', '') + " (" + entrance_tests[deutsch].find_parent('tr').
                                                       find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "   <em>для иностранных граждан:</em>\n"
                                                       "       " + entrance_tests[deutsch].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[deutsch].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")\n"
                                                       "       " + entrance_tests[deutsch].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                                       find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[deutsch].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                                       find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                                       parse_mode='html')
            elif query_level_of_study_entrance.data == 'mag_entrance_tests':
                inline_btn_business_ent_mag = InlineKeyboardButton('Бизнес-педагогика', callback_data='business_ent_mag')
                inline_btn_engin_ent_mag = InlineKeyboardButton('Инженерная педагогика', callback_data='engin_ent_mag')
                inline_btn_eng_in_poly_ent_mag = InlineKeyboardButton('Иностранный язык в лингвополикультурном '
                                                                      'образовательном пространстве', callback_data='eng_in_poly_ent_mag')
                inline_btn_poly_ent_mag = InlineKeyboardButton('Полилингвальное образование', callback_data='poly_ent_mag')
                inline_btn_prj_ent_mag = InlineKeyboardButton('Проектирование и оценка образовательных программ и процессов', callback_data='prj_ent_mag')
                inline_btn_prof_ent_mag = InlineKeyboardButton('Профессиональная подготовка в области физической культуры и спорта', callback_data='prof_ent_mag')
                inline_btn_rus_lit_ent_mag = InlineKeyboardButton('Русский язык и литература в межкультурной коммуникации', callback_data='rus_lit_ent_mag')
                inline_btn_pre_ent_mag = InlineKeyboardButton('Управление дошкольным образованием', callback_data='pre_ent_mag')
                inline_btn_managment_of_edu_ent_mag = InlineKeyboardButton('Управление образовательной организацией', callback_data='managment_of_edu_ent_mag')
                inline_btn_digit_ent_mag = InlineKeyboardButton('Цифровое образование', callback_data='digit_ent_mag')
                kb_mag_profile_ent = InlineKeyboardMarkup(row_width=1).add(inline_btn_business_ent_mag, inline_btn_engin_ent_mag, inline_btn_eng_in_poly_ent_mag,
                                                                           inline_btn_poly_ent_mag, inline_btn_prj_ent_mag, inline_btn_prof_ent_mag,
                                                                           inline_btn_rus_lit_ent_mag, inline_btn_pre_ent_mag, inline_btn_managment_of_edu_ent_mag,
                                                                           inline_btn_digit_ent_mag)
                await bot.send_message(query_level_of_study_entrance.from_user.id,
                                       "Выбери нужный профиль:", reply_markup=kb_mag_profile_ent)

                if 'Вступительное' in entrance_tests[business_pedag].text.strip():
                    info_entrance_business_pedag_2 = entrance_tests[business_pedag].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[engin_pedag].text.strip():
                    info_entrance_engin_pedag_2 = entrance_tests[engin_pedag].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[eng_in_poly].text.strip():
                    info_entrance_eng_in_poly_2 = entrance_tests[eng_in_poly].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[edu_poly].text.strip():
                    info_entrance_edu_poly_2 = entrance_tests[edu_poly].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[project_p].text.strip():
                    info_entrance_project_p_2 = entrance_tests[project_p].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[prof_sport].text.strip():
                    info_entrance_prof_sport_2 = entrance_tests[prof_sport].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[rus_and_lit].text.strip():
                    info_entrance_rus_and_lit_2 = entrance_tests[rus_and_lit].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[edu_pre].text.strip():
                    info_entrance_edu_pre_2 = entrance_tests[edu_pre].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[edu_managment].text.strip():
                    info_entrance_edu_managment_2 = entrance_tests[edu_managment].text.strip().replace('Вступительное', 'вступительное')
                if 'Вступительное' in entrance_tests[digit_edu].text.strip():
                    info_entrance_digit_edu_2 = entrance_tests[digit_edu].text.strip().replace('Вступительное', 'вступительное')

                @dp.callback_query_handler(lambda direction_ent_m: direction_ent_m.data in ['business_ent_mag', 'engin_ent_mag', 'eng_in_poly_ent_mag', 'poly_ent_mag',
                                                                                            'prj_ent_mag', 'prof_ent_mag', 'rus_lit_ent_mag', 'pre_ent_mag',
                                                                                            'managment_of_edu_ent_mag', 'digit_ent_mag'])
                async def callback_direction_ent_m(query_direction_ent_m: types.CallbackQuery):
                    await bot.answer_callback_query(query_direction_ent_m.id)
                    if query_direction_ent_m.data == 'business_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Бизнес-педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_business_pedag_2 + " (" + entrance_tests[business_pedag].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[business_pedag].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[business_pedag].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'engin_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Инженерная педагогика)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_engin_pedag_2 + " (" + entrance_tests[engin_pedag].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[engin_pedag].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[engin_pedag].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'eng_in_poly_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Иностранный язык в лингвополикультурном образовательном пространстве)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_eng_in_poly_2 + " (" + entrance_tests[eng_in_poly].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[eng_in_poly].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[eng_in_poly].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'poly_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Полилингвальное образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_edu_poly_2 + " (" + entrance_tests[edu_poly].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[edu_poly].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[edu_poly].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'prj_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Проектирование и оценка образовательных программ и процессов)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_project_p_2 + " (" + entrance_tests[project_p].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[project_p].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[project_p].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'prof_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Профессиональная подготовка в области физической культуры и спорта)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_prof_sport_2 + " (" + entrance_tests[prof_sport].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[prof_sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[prof_sport].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'rus_lit_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Русский язык и литература в межкультурной коммуникации)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_rus_and_lit_2 + " (" + entrance_tests[rus_and_lit].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[rus_and_lit].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[rus_and_lit].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'pre_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Управление дошкольным образованием)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> заочная\n"
                                               "<b>Продолжительность обучения:</b> 2 года 6 месяцев\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_edu_pre_2 + " (" + entrance_tests[edu_pre].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[edu_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[edu_pre].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'managment_of_edu_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Управление образовательной организацией)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_edu_managment_2 + " (" + entrance_tests[edu_managment].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[edu_managment].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[edu_managment].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')
                    elif query_direction_ent_m.data == 'digit_ent_mag':
                        await bot.send_message(query_direction_ent_m.from_user.id,
                                               "44.04.01 Педагогическое образование "
                                               "(профиль: Цифровое образование)\n\n"
                                               "<b>Уровень обучения:</b> магистратура\n"
                                               "<b>Форма обучения:</b> очная\n"
                                               "<b>Продолжительность обучения:</b> 2 года\n\n"
                                               "<b>Вступительные испытания</b> (предмет и минимальный балл):\n"
                                               "   <em>для граждан Российской Федерации:</em>\n"
                                               "       " + info_entrance_digit_edu_2 + " (" + entrance_tests[digit_edu].find_next_sibling('td').text.strip() + ")\n"
                                               "   <em>для иностранных граждан:</em>\n"
                                               "       " + entrance_tests[digit_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').find_next_sibling('table').find_next_sibling('table').find_next('tr').
                                               find_next('tr').find_next_sibling('tr').find_next('td').text.strip() + " (" + entrance_tests[digit_edu].find_parent('tr').find_parent('tr').find_parent('tr').find_parent('table').
                                               find_next_sibling('table').find_next_sibling('table').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td').text.strip() + ")",
                                               parse_mode='html')

    # https://kpf1u.ru/elabuga/abitur/bachelor/pp/sroki-provedeniya-priema
    # https://admissions.kpfu.ru/priem-v-universitet/sroki-provedeniya-priema-bakalavriat/specialitet-magistratura
    # Календарь абитуриента
    @dp.callback_query_handler(lambda c: c.data == 'calendar')
    async def process_callback_calendar(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        btn_b_c_prog = InlineKeyboardButton('Бакалавриат', callback_data='b_c_prog')
        btn_m_c_prog = InlineKeyboardButton('Магистратура', callback_data='m_c_prog')
        kb_c_prog = InlineKeyboardMarkup(row_width=1).add(btn_b_c_prog, btn_m_c_prog)
        await bot.send_message(callback_query.from_user.id,
                               "Здесь ты найдёшь сроки приёма на обучение в КФУ в рамках контрольных цифр, "
                               "а также по договорам об оказании платных образовательных услуг по очной, очно-заочной, "
                               "заочной формам обучения.\n\n"
                               "Выбери необходимую программу обучения:", reply_markup=kb_c_prog)
        
        @dp.callback_query_handler(lambda program_of_study: program_of_study.data in ['b_c_prog', 'm_c_prog'])
        async def callback_program_of_study(query_program_of_study: types.CallbackQuery):
            await bot.answer_callback_query(query_program_of_study.id)
            for i in range(6):
                info_calendar[i] = info_calendar[i].text.strip()
                if ')-' in info_calendar[i]:
                    info_calendar[i] = info_calendar[i].replace(')-', ') -')
                if '-1' in info_calendar[i]:
                    info_calendar[i] = info_calendar[i].replace('-1', '- 1')
                if '-2' in info_calendar[i]:
                    info_calendar[i] = info_calendar[i].replace('-2', '- 2')
                if 'прием' in info_calendar[i]:
                    info_calendar[i] = info_calendar[i].replace('прием', 'приём')
                if '–' in info_calendar[i]:
                    info_calendar[i] = info_calendar[i].replace('–', '-')
            if query_program_of_study.data == 'b_c_prog':
                btn_b_budget = InlineKeyboardButton('Бюджетная', callback_data='b_budget')
                btn_b_under_contract = InlineKeyboardButton('По договору', callback_data='b_under_contract')
                kb_b_basis_of_edu = InlineKeyboardMarkup(row_width=1).add(btn_b_budget, btn_b_under_contract)
                await bot.send_message(query_program_of_study.from_user.id,
                                       "Выбери необходимую основу обучения:", reply_markup=kb_b_basis_of_edu)

                @dp.callback_query_handler(lambda b_basis_of_edu: b_basis_of_edu.data in ['b_budget', 'b_under_contract'])
                async def callback_b_basis_of_edu(query_b_basis_of_edu: types.CallbackQuery):
                    await bot.answer_callback_query(query_b_basis_of_edu.id)
                    if query_b_basis_of_edu.data == 'b_budget':
                        await bot.send_message(query_b_basis_of_edu.from_user.id, "<b>" + title_calendar[0].text.strip() + ":</b>\n\n" + info_calendar[0],
                                               parse_mode='html')
                    elif query_b_basis_of_edu.data == 'b_under_contract':
                        await bot.send_message(query_b_basis_of_edu.from_user.id, "<b>" + title_calendar[1].text.strip() + ":</b>\n\n" + info_calendar[1],
                                               parse_mode='html')
            elif query_program_of_study.data == 'm_c_prog':
                btn_full_n_part_time_m = InlineKeyboardButton('Очная и очно-заочная', callback_data='full_n_part_time_m')
                btn_extramural_m_c = InlineKeyboardButton('Заочная', callback_data='extramural_m_c')
                kb_c_form_m = InlineKeyboardMarkup(row_width=1).add(btn_full_n_part_time_m, btn_extramural_m_c)
                await bot.send_message(query_program_of_study.from_user.id,
                                       "Выбери необходимую форму обучения:", reply_markup=kb_c_form_m)

                @dp.callback_query_handler(lambda c_form_m: c_form_m.data in ['full_n_part_time_m', 'extramural_m_c'])
                async def callback_c_form_m(query_c_form_m: types.CallbackQuery):
                    await bot.answer_callback_query(query_c_form_m.id)
                    if query_c_form_m.data == 'full_n_part_time_m':
                        btn_m_budget_full = InlineKeyboardButton('Бюджетная', callback_data='m_budget_full')
                        btn_m_under_contract_full = InlineKeyboardButton('По договору', callback_data='m_under_contract_full')
                        kb_m_basis_of_edu_full = InlineKeyboardMarkup(row_width=1).add(btn_m_budget_full, btn_m_under_contract_full)
                        await bot.send_message(query_c_form_m.from_user.id,
                                               "Выбери необходимую основу обучения:", reply_markup=kb_m_basis_of_edu_full)

                        @dp.callback_query_handler(lambda m_basis_of_edu_full: m_basis_of_edu_full.data in ['m_budget_full',
                                                                                                            'm_under_contract_full'])
                        async def callback_m_basis_of_edu_full(query_m_basis_of_edu_full: types.CallbackQuery):
                            await bot.answer_callback_query(query_m_basis_of_edu_full.id)
                            if query_m_basis_of_edu_full.data == 'm_budget_full':
                                await bot.send_message(query_m_basis_of_edu_full.from_user.id, "<b>" + title_calendar[2].text.strip() + ":</b>\n\n" + info_calendar[2],
                                                       parse_mode='html')
                            elif query_m_basis_of_edu_full.data == 'm_under_contract_full':
                                await bot.send_message(query_m_basis_of_edu_full.from_user.id, "<b>" + title_calendar[3].text.strip() + ":</b>\n\n" + info_calendar[3],
                                                       parse_mode='html')
                    elif query_c_form_m.data == 'extramural_m_c':
                        btn_m_budget_extr = InlineKeyboardButton('Бюджетная', callback_data='m_budget_extr')
                        btn_m_under_contract_extr = InlineKeyboardButton('По договору', callback_data='m_under_contract_extr')
                        kb_m_basis_of_edu_extr = InlineKeyboardMarkup(row_width=1).add(btn_m_budget_extr, btn_m_under_contract_extr)
                        await bot.send_message(query_c_form_m.from_user.id,
                                               "Выбери необходимую основу обучения:", reply_markup=kb_m_basis_of_edu_extr)

                        @dp.callback_query_handler(lambda m_basis_of_edu_extr: m_basis_of_edu_extr.data in ['m_budget_extr',
                                                                                                            'm_under_contract_extr'])
                        async def callback_m_basis_of_edu_extr(query_m_basis_of_edu_extr: types.CallbackQuery):
                            await bot.answer_callback_query(query_m_basis_of_edu_extr.id)
                            if query_m_basis_of_edu_extr.data == 'm_budget_extr':
                                await bot.send_message(query_m_basis_of_edu_extr.from_user.id, "<b>" + title_calendar[4].text.strip() + ":</b>\n\n" + info_calendar[4],
                                                       parse_mode='html')
                            elif query_m_basis_of_edu_extr.data == 'm_under_contract_extr':
                                await bot.send_message(query_m_basis_of_edu_extr.from_user.id, "<b>" + title_calendar[5].text.strip() + ":</b>\n\n" + info_calendar[5],
                                                       parse_mode='html')

    # Направления по сданным экзаменам
    @dp.callback_query_handler(lambda c: c.data == 'directions')
    async def process_callback_directions(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        btn_d_rus = InlineKeyboardButton('Для граждан Российской Федерации', callback_data='d_rus')
        btn_d_foreign = InlineKeyboardButton('Для иностранных граждан', callback_data='d_foreign')
        kb_directions = InlineKeyboardMarkup(row_width=1).add(btn_d_rus, btn_d_foreign)
        await bot.send_message(callback_query.from_user.id,
                               "Здесь ты найдёшь список направлений по планируемым к сдаче экзаменам.", reply_markup=kb_directions)
        
        @dp.callback_query_handler(lambda d_nationality: d_nationality.data in ['d_rus', 'd_foreign'])
        async def callback_d_nationality(query_d_nationality: types.CallbackQuery):
            await bot.answer_callback_query(query_d_nationality.id)
            if query_d_nationality.data == 'd_rus':
                btn_d_rus_math_n_phys = InlineKeyboardButton('Математика и физика', callback_data='d_rus_math_n_phys')
                btn_d_rus_math_n_info = InlineKeyboardButton('Математика и информатика', callback_data='d_rus_math_n_info')
                btn_d_rus_math_n_social = InlineKeyboardButton('Математика и обществознание', callback_data='d_rus_math_n_social')
                btn_d_rus_math_n_bio = InlineKeyboardButton('Математика и биология', callback_data='d_rus_math_n_bio')
                btn_d_rus_math = InlineKeyboardButton('Математика', callback_data='d_rus_math')
                btn_d_rus_social_eng = InlineKeyboardButton('Обществознание и английский язык', callback_data='d_rus_social_eng')
                btn_d_rus_social_history = InlineKeyboardButton('Обществознание и история', callback_data='d_rus_social_history')
                btn_d_rus_social_bio = InlineKeyboardButton('Обществознание и биология', callback_data='d_rus_social_bio')
                btn_d_rus_social_n_other = InlineKeyboardButton('Обществознание и химия/физика/литер./геогр./информатика', callback_data='d_rus_social_n_other')
                btn_d_rus_social = InlineKeyboardButton('Обществознание', callback_data='d_rus_social')
                btn_d_rus_eng_n_lit = InlineKeyboardButton('Английский язык и литература', callback_data='d_rus_eng_n_lit')
                kb_d_rus = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_n_phys, btn_d_rus_math_n_info, btn_d_rus_math_n_social, btn_d_rus_math_n_bio, btn_d_rus_math,
                                                                 btn_d_rus_social_eng, btn_d_rus_social_history, btn_d_rus_social_bio, btn_d_rus_social_n_other,
                                                                 btn_d_rus_social, btn_d_rus_eng_n_lit)
                await bot.send_message(query_d_nationality.from_user.id,
                                       "Выбери планируемые к сдаче/сданные экзамены (помимо русского языка):", reply_markup=kb_d_rus)
                
                @dp.callback_query_handler(lambda d_rus_directions: d_rus_directions.data in ['d_rus_math_n_phys', 'd_rus_math_n_info', 'd_rus_math_n_social', 'd_rus_math_n_bio',
                                                                                        'd_rus_math', 'd_rus_social_eng', 'd_rus_social_history', 'd_rus_social_bio',
                                                                                        'd_rus_social_n_other', 'd_rus_social', 'd_rus_eng_n_lit'])
                async def callback_d_rus_directions(query_d_rus_directions: types.CallbackQuery):
                    await bot.answer_callback_query(query_d_rus_directions.id)
                    if query_d_rus_directions.data == 'd_rus_math_n_phys':
                        btn_d_rus_math_n_phys_full = InlineKeyboardButton('Очная', callback_data='d_rus_math_n_phys_full')
                        btn_d_rus_math_n_phys_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_math_n_phys_part')
                        btn_d_rus_math_n_phys_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_math_n_phys_extr')
                        kb_d_rus_math_n_phys = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_n_phys_full, btn_d_rus_math_n_phys_part, btn_d_rus_math_n_phys_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_math_n_phys)

                        @dp.callback_query_handler(lambda d_rus_math_n_phys: d_rus_math_n_phys.data in ['d_rus_math_n_phys_full', 'd_rus_math_n_phys_part', 'd_rus_math_n_phys_extr'])
                        async def callback_d_rus_math_n_phys(query_d_rus_math_n_phys: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_math_n_phys.id)
                            if query_d_rus_math_n_phys.data == 'd_rus_math_n_phys_full':
                                await bot.send_message(query_d_rus_math_n_phys.from_user.id, "По выбранным экзаменам (русский язык, математика и физика) на очной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>09.03.03</b> Прикладная информатика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/090303pe'>"
                                                       "«Прикладная информатика в экономике»</a>", parse_mode='html')
                            elif query_d_rus_math_n_phys.data == 'd_rus_math_n_phys_part':
                                await bot.send_message(query_d_rus_math_n_phys.from_user.id, "По выбранным экзаменам (русский язык, математика и физика) на очно-заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>15.03.06</b> Мехатроника и робототехника, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/150306fmr'>"
                                                       "«Физические основы мехатроники и робототехники»</a>", parse_mode='html')
                            elif query_d_rus_math_n_phys.data == 'd_rus_math_n_phys_extr':
                                await bot.send_message(query_d_rus_math_n_phys.from_user.id, "По выбранным экзаменам (русский язык, математика и физика) на заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>23.03.01</b> Технология транспортных процессов, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/230301pts'>"
                                                       "«Проектирование и управление интеллектуальными транспортными системами»</a>",
                                                       parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_math_n_info':
                        btn_d_rus_math_n_info_full = InlineKeyboardButton('Очная', callback_data='d_rus_math_n_info_full')
                        btn_d_rus_math_n_info_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_math_n_info_part')
                        btn_d_rus_math_n_info_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_math_n_info_extr')
                        kb_d_rus_math_n_info = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_n_info_full, btn_d_rus_math_n_info_part, btn_d_rus_math_n_info_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_math_n_info)

                        @dp.callback_query_handler(lambda d_rus_math_n_info: d_rus_math_n_info.data in ['d_rus_math_n_info_full', 'd_rus_math_n_info_part', 'd_rus_math_n_info_extr'])
                        async def callback_d_rus_math_n_info(query_d_rus_math_n_info: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_math_n_info.id)
                            if query_d_rus_math_n_info.data == 'd_rus_math_n_info_full':
                                await bot.send_message(query_d_rus_math_n_info.from_user.id, "По выбранным экзаменам (русский язык, математика и информатика) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>09.03.03</b> Прикладная информатика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/090303pe'>"
                                                       "«Прикладная информатика в экономике»</a>\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efi'>"
                                                       "«Экономика и финансы организаций (с углубленным изучением иностранных языков)»</a>", parse_mode='html')
                            elif query_d_rus_math_n_info.data == 'd_rus_math_n_info_part':
                                await bot.send_message(query_d_rus_math_n_info.from_user.id, "По выбранным экзаменам (русский язык, математика и информатика) на очно-заочной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>15.03.06</b> Мехатроника и робототехника, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/150306fmr'>"
                                                       "«Физические основы мехатроники и робототехники»</a>\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efd'>"
                                                       "«Экономика и финансы организаций (реализуется с применением электронного обучения и дистанционных технологий)»</a>", parse_mode='html')
                            elif query_d_rus_math_n_info.data == 'd_rus_math_n_info_extr':
                                await bot.send_message(query_d_rus_math_n_info.from_user.id, "По выбранным экзаменам (русский язык, математика и информатика) на заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>09.03.03</b> Прикладная информатика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/090303pe'>"
                                                       "«Прикладная информатика в экономике»</a>",
                                                       parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_math_n_social':
                        btn_d_rus_math_n_social_full = InlineKeyboardButton('Очная', callback_data='d_rus_math_n_social_full')
                        btn_d_rus_math_n_social_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_math_n_social_part')
                        btn_d_rus_math_n_social_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_math_n_social_extr')
                        kb_d_rus_math_n_social = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_n_social_full, btn_d_rus_math_n_social_part, btn_d_rus_math_n_social_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_math_n_social)

                        @dp.callback_query_handler(lambda d_rus_math_n_social: d_rus_math_n_social.data in ['d_rus_math_n_social_full', 'd_rus_math_n_social_part', 'd_rus_math_n_social_extr'])
                        async def callback_d_rus_math_n_social(query_d_rus_math_n_social: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_math_n_social.id)
                            if query_d_rus_math_n_social.data == 'd_rus_math_n_social_full':
                                await bot.send_message(query_d_rus_math_n_social.from_user.id, "По выбранным экзаменам (русский язык, математика и обществознание) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efi'>"
                                                       "«Экономика и финансы организаций (с углубленным изучением иностранных языков)»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                                       "«Технология и робототехника»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                                       "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>", parse_mode='html')
                            elif query_d_rus_math_n_social.data == 'd_rus_math_n_social_part':
                                await bot.send_message(query_d_rus_math_n_social.from_user.id, "По выбранным экзаменам (русский язык, математика и обществознание) на очно-заочной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efd'>"
                                                       "«Экономика и финансы организаций (реализуется с применением электронного обучения и дистанционных технологий)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>", parse_mode='html')
                            elif query_d_rus_math_n_social.data == 'd_rus_math_n_social_extr':
                                await bot.send_message(query_d_rus_math_n_social.from_user.id, "По выбранным экзаменам (русский язык, математика и обществознание) на заочной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301no'>"
                                                       "«Начальное образование»</a>\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304aes'>"
                                                       "«Автоматизация энергетических систем»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_math_n_bio':
                        btn_d_rus_math_n_bio_full = InlineKeyboardButton('Очная', callback_data='d_rus_math_n_bio_full')
                        btn_d_rus_math_n_bio_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_math_n_bio_part')
                        kb_d_rus_math_n_bio = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_n_bio_full, btn_d_rus_math_n_bio_part)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_math_n_bio)

                        @dp.callback_query_handler(lambda d_rus_math_n_bio: d_rus_math_n_bio.data in ['d_rus_math_n_bio_full', 'd_rus_math_n_bio_part'])
                        async def callback_d_rus_math_n_bio(query_d_rus_math_n_bio: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_math_n_bio.id)
                            if query_d_rus_math_n_bio.data == 'd_rus_math_n_bio_full':
                                await bot.send_message(query_d_rus_math_n_bio.from_user.id, "По выбранным экзаменам (русский язык, математика и биология) на очной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302po'>"
                                                       "«Психология образования»</a>", parse_mode='html')
                            elif query_d_rus_math_n_bio.data == 'd_rus_math_n_bio_part':
                                await bot.send_message(query_d_rus_math_n_bio.from_user.id, "По выбранным экзаменам (русский язык, математика и биология) на очно-заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302podt'>"
                                                       "«Психология образования (с применением электронного обучения и дистанционных образовательных технологий)»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_math':
                        btn_d_rus_math_full = InlineKeyboardButton('Очная', callback_data='d_rus_math_full')
                        btn_d_rus_math_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_math_extr')
                        kb_d_rus_math = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_math_full, btn_d_rus_math_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_math)

                        @dp.callback_query_handler(lambda d_rus_math: d_rus_math.data in ['d_rus_math_full', 'd_rus_math_extr'])
                        async def callback_d_rus_math(query_d_rus_math: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_math.id)
                            if query_d_rus_math.data == 'd_rus_math_full':
                                await bot.send_message(query_d_rus_math.from_user.id, "По выбранным экзаменам (русский язык и математика) на очной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304digd'>"
                                                       "«Декорирование интерьера и графический дизайн»</a> (примечание: + рисунок)", parse_mode='html')
                            elif query_d_rus_math.data == 'd_rus_math_extr':
                                await bot.send_message(query_d_rus_math.from_user.id, "По выбранным экзаменам (русский язык и математика) на заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304digd'>"
                                                       "«Декорирование интерьера и графический дизайн»</a> (примечание: + рисунок)", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_social_eng':
                        btn_d_rus_social_eng_full = InlineKeyboardButton('Очная', callback_data='d_rus_social_eng_full')
                        btn_d_rus_social_eng_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_social_eng_part')
                        btn_d_rus_social_eng_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_social_eng_extr')
                        kb_d_rus_social_eng = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_social_eng_full, btn_d_rus_social_eng_part, btn_d_rus_social_eng_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_social_eng)

                        @dp.callback_query_handler(lambda d_rus_social_eng: d_rus_social_eng.data in ['d_rus_social_eng_full', 'd_rus_social_eng_part', 'd_rus_social_eng_extr'])
                        async def callback_d_rus_social_eng(query_d_rus_social_eng: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_social_eng.id)
                            if query_d_rus_social_eng.data == 'd_rus_social_eng_full':
                                await bot.send_message(query_d_rus_social_eng.from_user.id, "По выбранным экзаменам (русский язык, обществознание и английский язык) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugp'>«Гражданское право»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                                       "«Технология и робототехника»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                                       "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ak'>"
                                                       "«Перевод и переводоведение (английский язык, китайский язык)»</a>\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ppan'>"
                                                       "«Перевод и переводоведение (английский язык, немецкий язык)»</a>", parse_mode='html')
                            elif query_d_rus_social_eng.data == 'd_rus_social_eng_part':
                                await bot.send_message(query_d_rus_social_eng.from_user.id, "По выбранным экзаменам (русский язык, обществознание и английский язык) на очно-заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugpdt'>"
                                                       "«Гражданское право (реализуется с применением электронного обучения и дистанционных технологий)»</a>", parse_mode='html')
                            elif query_d_rus_social_eng.data == 'd_rus_social_eng_extr':
                                await bot.send_message(query_d_rus_social_eng.from_user.id, "По выбранным экзаменам (русский язык, обществознание и английский язык) на заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301en'>"
                                                       "«Английский язык»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_social_history':
                        btn_d_rus_social_history_full = InlineKeyboardButton('Очная', callback_data='d_rus_social_history_full')
                        btn_d_rus_social_history_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_social_history_part')
                        kb_d_rus_social_history = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_social_history_full, btn_d_rus_social_history_part)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_social_history)

                        @dp.callback_query_handler(lambda d_rus_social_history: d_rus_social_history.data in ['d_rus_social_history_full', 'd_rus_social_history_part'])
                        async def callback_d_rus_social_history(query_d_rus_social_history: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_social_history.id)
                            if query_d_rus_social_history.data == 'd_rus_social_history_full':
                                await bot.send_message(query_d_rus_social_history.from_user.id, "По выбранным экзаменам (русский язык, обществознание и история) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugp'>«Гражданское право»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                                       "«Технология и робототехника»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                                       "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>", parse_mode='html')
                            elif query_d_rus_social_history.data == 'd_rus_social_history_part':
                                await bot.send_message(query_d_rus_social_history.from_user.id, "По выбранным экзаменам (русский язык, обществознание и история) на очно-заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugpdt'>"
                                                       "«Гражданское право (реализуется с применением электронного обучения и дистанционных технологий)»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_social_bio':
                        btn_d_rus_social_bio_full = InlineKeyboardButton('Очная', callback_data='d_rus_social_bio_full')
                        btn_d_rus_social_bio_part = InlineKeyboardButton('Очно-заочная', callback_data='d_rus_social_bio_part')
                        btn_d_rus_social_bio_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_social_bio_extr')
                        kb_d_rus_social_bio = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_social_bio_full, btn_d_rus_social_bio_part, btn_d_rus_social_bio_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_social_bio)

                        @dp.callback_query_handler(lambda d_rus_social_bio: d_rus_social_bio.data in ['d_rus_social_bio_full', 'd_rus_social_bio_part', 'd_rus_social_bio_extr'])
                        async def callback_d_rus_social_bio(query_d_rus_social_bio: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_social_bio.id)
                            if query_d_rus_social_bio.data == 'd_rus_social_bio_full':
                                await bot.send_message(query_d_rus_social_bio.from_user.id, "По выбранным экзаменам (русский язык, обществознание и биология) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                                       "«Технология и робототехника»</a>\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302po'>"
                                                       "«Психология образования»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                                       "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>", parse_mode='html')
                            elif query_d_rus_social_bio.data == 'd_rus_social_bio_part':
                                await bot.send_message(query_d_rus_social_bio.from_user.id, "По выбранным экзаменам (русский язык, обществознание и биология) на очно-заочной форме обучения "
                                                       "можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302podt'>"
                                                       "«Психология образования (с применением электронного обучения и дистанционных образовательных технологий)»</a>", parse_mode='html')
                            elif query_d_rus_social_bio.data == 'd_rus_social_bio_extr':
                                await bot.send_message(query_d_rus_social_bio.from_user.id, "По выбранным экзаменам (русский язык, обществознание и биология) на заочной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302ppdo'>"
                                                       "«Психология и педагогика дошкольного образования»</a>\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302po'>"
                                                       "«Психология образования»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_social_n_other':
                        await bot.send_message(query_d_rus_directions.from_user.id, "По выбранным экзаменам (русский язык, обществознание и химия/физика/литература/география/информатика) "
                                               "на очной форме обучения можно поступить на следующие направления:\n\n"
                                               "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                               "«Технология и робототехника»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                               "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                               "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                               "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_social':
                        btn_d_rus_social_full = InlineKeyboardButton('Очная', callback_data='d_rus_social_full')
                        btn_d_rus_social_extr = InlineKeyboardButton('Заочная', callback_data='d_rus_social_extr')
                        kb_d_rus_social = InlineKeyboardMarkup(row_width=1).add(btn_d_rus_social_full, btn_d_rus_social_extr)
                        await bot.send_message(query_d_rus_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_rus_social)

                        @dp.callback_query_handler(lambda d_rus_social: d_rus_social.data in ['d_rus_social_full', 'd_rus_social_extr'])
                        async def callback_d_rus_social(query_d_rus_social: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_rus_social.id)
                            if query_d_rus_social.data == 'd_rus_social_full':
                                await bot.send_message(query_d_rus_social.from_user.id, "По выбранным экзаменам (русский языки и обществознание) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rldo'>"
                                                       "«Английский язык, родной (татарский) язык и литература»</a> "
                                                       "(примечание: + татарский язык (внутреннее испытание профессиональной направленности))\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305fkb'>"
                                                       "«Физическая культура и безопасность жизнедеятельности»</a> "
                                                       "(примечание: + физическая культура (внутреннее испытание профессиональной направленности))\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305fkdosp'>"
                                                       "«Физическая культура и дополнительное образование (спортивная подготовка)»</a> "
                                                       "(примечание: + физическая культура (внутреннее испытание профессиональной направленности))", parse_mode='html')
                            elif query_d_rus_social.data == 'd_rus_social_extr':
                                await bot.send_message(query_d_rus_social.from_user.id, "По выбранным экзаменам (русский язык и обществознание) на заочной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301odt'>"
                                                       "«Общее и дополнительное образование в предметной области \"Технология\"»</a> "
                                                       "(примечание: + профессиональное испытание «Технология»)\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301fk'>"
                                                       "«Физическая культура»</a> (примечание: + физическая культура (внутреннее испытание профессиональной направленности))\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rldo'>"
                                                       "«Дошкольное образование, родной (татарский) язык и литература»</a> "
                                                       "(примечание: + татарский язык (внутреннее испытание профессиональной направленности))", parse_mode='html')
                    elif query_d_rus_directions.data == 'd_rus_eng_n_lit':
                        await bot.send_message(query_d_rus_directions.from_user.id, "По выбранным экзаменам (русский язык, английский язык и литература) на очной форме обучения "
                                                       "можно поступить на следующие направления:\n\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ak'>"
                                                       "«Перевод и переводоведение (английский язык, китайский язык)»</a>\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ppan'>"
                                                       "«Перевод и переводоведение (английский язык, немецкий язык)»</a>", parse_mode='html')
            elif query_d_nationality.data == 'd_foreign':
                btn_d_foreign_info = InlineKeyboardButton('Информатика', callback_data='d_foreign_info')
                btn_d_foreign_math = InlineKeyboardButton('Математика', callback_data='d_foreign_math')
                btn_d_foreign_social = InlineKeyboardButton('Обществознание', callback_data='d_foreign_social')
                btn_d_foreign_bio = InlineKeyboardButton('Биология', callback_data='d_foreign_bio')
                btn_d_foreign_eng = InlineKeyboardButton('Английский язык', callback_data='d_foreign_eng')
                kb_d_foreign = InlineKeyboardMarkup(row_width=1).add(btn_d_foreign_info, btn_d_foreign_math, btn_d_foreign_social, btn_d_foreign_bio, btn_d_foreign_eng)
                await bot.send_message(query_d_nationality.from_user.id,
                                       "Выбери планируемые к сдаче/сданные экзамены (помимо русского языка):", reply_markup=kb_d_foreign)
                
                @dp.callback_query_handler(lambda d_foreign_directions: d_foreign_directions.data in ['d_foreign_info', 'd_foreign_math', 'd_foreign_social', 
                                                                                              'd_foreign_bio', 'd_foreign_eng'])
                async def callback_d_foreign_directions(query_d_foreign_directions: types.CallbackQuery):
                    await bot.answer_callback_query(query_d_foreign_directions.id)
                    if query_d_foreign_directions.data == 'd_foreign_info':
                        btn_d_foreign_info_full = InlineKeyboardButton('Очная', callback_data='d_foreign_info_full')
                        btn_d_foreign_info_extr = InlineKeyboardButton('Заочная', callback_data='d_foreign_info_extr')
                        kb_d_foreign_info = InlineKeyboardMarkup(row_width=1).add(btn_d_foreign_info_full, btn_d_foreign_info_extr)
                        await bot.send_message(query_d_foreign_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_foreign_info)

                        @dp.callback_query_handler(lambda d_foreign_info: d_foreign_info.data in ['d_foreign_info_full', 'd_foreign_info_extr'])
                        async def callback_d_foreign_info(query_d_foreign_info: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_foreign_info.id)
                            if query_d_foreign_info.data == 'd_foreign_info_full':
                                await bot.send_message(query_d_foreign_info.from_user.id, "По выбранным экзаменам (русский язык и информатика) на очной форме обучения "
                                                       "для иностранных граждан можно поступить на следующее направление:\n\n"
                                                       "<b>09.03.03</b> Прикладная информатика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/090303pe'>"
                                                       "«Прикладная информатика в экономике»</a>", parse_mode='html')
                            elif query_d_foreign_info.data == 'd_foreign_info_extr':
                                await bot.send_message(query_d_foreign_info.from_user.id, "По выбранным экзаменам (русский язык и информатика) на заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующее направление:\n\n"
                                                       "<b>09.03.03</b> Прикладная информатика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/090303pe'>"
                                                       "«Прикладная информатика в экономике»</a>", parse_mode='html')
                    elif query_d_foreign_directions.data == 'd_foreign_math':
                        btn_d_foreign_math_full = InlineKeyboardButton('Очная', callback_data='d_foreign_math_full')
                        btn_d_foreign_math_part = InlineKeyboardButton('Очно-заочная', callback_data='d_foreign_math_part')
                        btn_d_foreign_math_extr = InlineKeyboardButton('Заочная', callback_data='d_foreign_math_extr')
                        kb_d_foreign_math = InlineKeyboardMarkup(row_width=1).add(btn_d_foreign_math_full, btn_d_foreign_math_part, btn_d_foreign_math_extr)
                        await bot.send_message(query_d_foreign_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_foreign_math)

                        @dp.callback_query_handler(lambda d_foreign_math: d_foreign_math.data in ['d_foreign_math_full', 'd_foreign_math_part', 'd_foreign_math_extr'])
                        async def callback_d_foreign_math(query_d_foreign_math: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_foreign_math.id)
                            if query_d_foreign_math.data == 'd_foreign_math_full':
                                await bot.send_message(query_d_foreign_math.from_user.id, "По выбранным экзаменам (русский язык и математика) на очной форме обучения "
                                                       "для иностранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efi'>"
                                                       "«Экономика и финансы организаций (с углубленным изучением иностранных языков)»</a>", parse_mode='html')
                            elif query_d_foreign_math.data == 'd_foreign_math_part':
                                await bot.send_message(query_d_foreign_math.from_user.id, "По выбранным экзаменам (русский язык и математика) на очно-заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>15.03.06</b> Мехатроника и робототехника, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/150306fmr'>"
                                                       "«Физические основы мехатроники и робототехники»</a>\n"
                                                       "<b>38.03.01</b> Экономика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/380301efd'>"
                                                       "«Экономика и финансы организаций (реализуется с применением электронного обучения и дистанционных технологий)»</a>", parse_mode='html')
                            elif query_d_foreign_math.data == 'd_foreign_math_extr':
                                await bot.send_message(query_d_foreign_math.from_user.id, "По выбранным экзаменам (русский язык и математика) на заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующее направление:\n\n"
                                                       "<b>23.03.01</b> Технология транспортных процессов, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/230301ptse'>"
                                                       "«Проектирование и управление интеллектуальными транспортными системами»</a>\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304aes'>"
                                                       "«Автоматизация энергетических систем»</a>\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304digd'>"
                                                       "«Декорирование интерьера и графический дизайн»</a>",
                                                       parse_mode='html')
                    elif query_d_foreign_directions.data == 'd_foreign_social':
                        btn_d_foreign_social_full = InlineKeyboardButton('Очная', callback_data='d_foreign_social_full')
                        btn_d_foreign_social_part = InlineKeyboardButton('Очно-заочная', callback_data='d_foreign_social_part')
                        btn_d_foreign_social_extr = InlineKeyboardButton('Заочная', callback_data='d_foreign_social_extr')
                        kb_d_foreign_social_bio = InlineKeyboardMarkup(row_width=1).add(btn_d_foreign_social_full, btn_d_foreign_social_part, btn_d_foreign_social_extr)
                        await bot.send_message(query_d_foreign_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_foreign_social_bio)

                        @dp.callback_query_handler(lambda d_foreign_social: d_foreign_social.data in ['d_foreign_social_full', 'd_foreign_social_part', 'd_foreign_social_extr'])
                        async def callback_d_foreign_social(query_d_foreign_social: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_foreign_social.id)
                            if query_d_foreign_social.data == 'd_foreign_social_full':
                                await bot.send_message(query_d_foreign_social.from_user.id, "По выбранным экзаменам (русский язык и обществознание) на очной форме обучения "
                                                       "для иностранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugp'>"
                                                       "«Гражданское право»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301trt'>"
                                                       "«Технология и робототехника»</a>\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302po'>"
                                                       "«Психология образования»</a>\n"
                                                       "<b>44.03.04</b> Профессиональное обучение (по отраслям), профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440304digd'>"
                                                       "«Декорирование интерьера и графический дизайн»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305bh'>«Биология и Химия»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dodo'>"
                                                       "«Дошкольное образование и Дополнительное образование (художественное творчество)»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305dono'>«Дошкольное образование и Начальное образование»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ii'>«История и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305io'>«История и Обществознание»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mi'>«Математика и Информатика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305mf'>«Математика и Физика»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305ra'>«Русский язык и Иностранный (английский) язык»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305rl'>«Русский язык и Литература»</a>\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305fkb'>«Физическая культура и безопасность жизнедеятельности»</a> "
                                                       "(примечание: + физическая культура (внутреннее испытание профессиональной направленности))\n"
                                                       "<b>44.03.05</b> Педагогическое образование (с двумя профилями подготовки), профиль: "
                                                       "<a href='https://kpfu.ru/elabuga/abitur/n/440305fkdosp'>«Физическая культура и дополнительное образование (спортивная подготовка)»</a> "
                                                       "(примечание: + физическая культура (внутреннее испытание профессиональной направленности))", parse_mode='html')
                            elif query_d_foreign_social.data == 'd_foreign_social_part':
                                await bot.send_message(query_d_foreign_social.from_user.id, "По выбранным экзаменам (русский язык и обществознание) на очно-заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующее направление:\n\n"
                                                       "<b>40.03.01</b> Юриспруденция, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/400301jugpdt'>"
                                                       "«Гражданское право (реализуется с применением электронного обучения и дистанционных технологий)»</a>", parse_mode='html')
                            elif query_d_foreign_social.data == 'd_foreign_social_extr':
                                await bot.send_message(query_d_foreign_social.from_user.id, "По выбранным экзаменам (русский язык и обществознание) на заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301en'>"
                                                       "«Английский язык»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301no'>"
                                                       "«Начальное образование»</a>\n"
                                                       "<b>44.03.01</b> Педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440301odt'>"
                                                       "«Общее и дополнительное образование в предметной области \"Технология\"»</a>", parse_mode='html')
                    elif query_d_foreign_directions.data == 'd_foreign_bio':
                        btn_d_foreign_bio_part = InlineKeyboardButton('Очно-заочная', callback_data='d_foreign_bio_part')
                        btn_d_foreign_bio_extr = InlineKeyboardButton('Заочная', callback_data='d_foreign_bio_extr')
                        kb_d_foreign_bio = InlineKeyboardMarkup(row_width=1).add(btn_d_foreign_bio_part, btn_d_foreign_bio_extr)
                        await bot.send_message(query_d_foreign_directions.from_user.id, "Выбери форму обучения:", reply_markup=kb_d_foreign_bio)

                        @dp.callback_query_handler(lambda d_foreign_bio: d_foreign_bio.data in ['d_foreign_bio_part', 'd_foreign_bio_extr'])
                        async def callback_d_foreign_bio(query_d_foreign_bio: types.CallbackQuery):
                            await bot.answer_callback_query(query_d_foreign_bio.id)
                            if query_d_foreign_bio.data == 'd_foreign_bio_part':
                                await bot.send_message(query_d_foreign_bio.from_user.id, "По выбранным экзаменам (русский язык и биология) на очно-заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующее направление:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302podt'>"
                                                       "«Психология образования (с применением электронного обучения и дистанционных образовательных технологий)»</a>", parse_mode='html')
                            elif query_d_foreign_bio.data == 'd_foreign_bio_extr':
                                await bot.send_message(query_d_foreign_bio.from_user.id, "По выбранным экзаменам (русский язык и биология) на заочной форме обучения "
                                                       "для иностранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302ppdo'>"
                                                       "«Психология и педагогика дошкольного образования»</a>\n"
                                                       "<b>44.03.02</b> Психолого-педагогическое образование, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/440302po'>"
                                                       "«Психология образования»</a>", parse_mode='html')
                    elif query_d_foreign_directions.data == 'd_foreign_eng':
                        await bot.send_message(query_d_foreign_directions.from_user.id, "По выбранным экзаменам (русский язык и английский язык) на очной форме обучения "
                                                       "для инстранных граждан можно поступить на следующие направления:\n\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ak'>"
                                                       "«Перевод и переводоведение (английский язык, китайский язык)»</a>\n"
                                                       "<b>45.03.02</b> Лингвистика, профиль: <a href='https://kpfu.ru/elabuga/abitur/n/450302ppan'>"
                                                       "«Перевод и переводоведение (английский язык, немецкий язык)»</a>", parse_mode='html')

# Обработка кнопки "Подача документов"
@dp.message_handler(lambda message: message.text == 'Подача документов')
async def process_submission_docs_btn(message: types.Message):
    btn_sub_online = InlineKeyboardButton('Онлайн', callback_data='sub_online')
    btn_sub_offline = InlineKeyboardButton('Лично', callback_data='sub_offline')
    kb_sub_docs = InlineKeyboardMarkup(row_width=1).add(btn_sub_online, btn_sub_offline)
    await bot.send_message(message.from_user.id, message.from_user.full_name + ", выбери способ подачи документов:\n", reply_markup=kb_sub_docs)

    info_offline[16] = info_offline[16].text.strip()
    if 'каб.1' in info_offline[16]:
        info_offline[16] = info_offline[16].replace('каб.1', 'каб. 1')

    @dp.callback_query_handler(lambda c: c.data in ['sub_online', 'sub_offline'])
    async def process_callback_sub_docs(callback_query_sub_docs: types.CallbackQuery):
        await bot.answer_callback_query(callback_query_sub_docs.id)
        if callback_query_sub_docs.data == 'sub_online':
            btn_sub_online_be_student = InlineKeyboardButton('Сеть КФУ \"Буду студентом!\"', callback_data='sub_online_be_student')
            btn_sub_online_gos = InlineKeyboardButton('Портал Госуслуги', url='https://www.gosuslugi.ru/vuzonline')
            kb_sub_docs_online = InlineKeyboardMarkup(row_width=1).add(btn_sub_online_be_student, btn_sub_online_gos)
            await bot.send_message(message.from_user.id, "Способы онлайн-подачи документов:\n", reply_markup=kb_sub_docs_online)

            info_be_student[0] = info_be_student[0].text.strip()
            if 'он-лайн' in info_be_student[0]:
                info_be_student[0] = info_be_student[0].replace('он-лайн', 'онлайн')
            if 'прием' in info_be_student[0]:
                info_be_student[0] = info_be_student[0].replace('прием', 'приём')

            @dp.callback_query_handler(lambda be_student: be_student.data == 'sub_online_be_student')
            async def callback_sub_docs_online_be_student(query_sub_docs_online_be_student: types.CallbackQuery):
                await bot.answer_callback_query(query_sub_docs_online_be_student.id)
                await bot.send_message(message.from_user.id, "<a href='https://abiturient.kpfu.ru/'>Сеть КФУ \"Буду студентом!\"</a>\n\n" + info_be_student[0],
                                       parse_mode='html')
        elif callback_query_sub_docs.data == 'sub_offline':
            await bot.send_message(message.from_user.id, "Подача документов лично проходит по адресу: " + info_offline[16])


# Обработка кнопки "Контакты приёмной комиссии"
@dp.message_handler(lambda message: message.text == 'Контакты приёмной комиссии')
async def process_admission_btn(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('VK', url='https://vk.com/ei_kfu')
    inline_btn_2 = InlineKeyboardButton('YouTube', url='https://www.youtube.com/user/elabugastudio/videos')
    inline_kb = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)
    await bot.send_message(message.from_user.id,
                           message.from_user.full_name + ", благодарим тебя за интерес к поступлению в Елабужский институт КФУ.\n\n"
                           "📌 <b>Контакты</b>:\n"
                           "Телефоны: +7 (85557) 7-55-62, +7 (85557) 7-54-66\n"
                           "Электронная почта: priem_el@kpfu.ru\n"
                           "Альтернативная электронная почта: pkefkfu@gmail.com\n"
                           "Адрес местонахождения приёмной комиссии: "
                           "Республика Татарстан, г. Елабуга, ул. Казанская, д. 89, каб. 16\n"
                           "Почтовый адрес: ул. Казанская, д. 89, каб. 16, г. Елабуга, РТ, "
                           "Российская Федерация (для приёмной комиссии). Индекс 423604\n"
                           "Режим работы: пн.-пт.: с 8:00 до 18:00 ч. Перерыв с 12:00 до 13:00 ч. "
                           "Сб.: с 8:00 до 13:00 ч. Выходной: воскресенье.\n\n",
                           parse_mode='html', reply_markup=inline_kb)


# Обработка кнопки "Отзыв о чат-боте"
@dp.message_handler(lambda message: message.text == 'Отзыв о чат-боте')
async def process_admission_btn(message: types.Message):
    await bot.send_message(message.from_user.id,
                           message.from_user.full_name + ", если есть желание, можешь оставить отзыв на наш чат-бот. "
                           "Будем благодарны!\n\n"
                           "<a href='https://forms.gle/ahJRa2rER6S3eUjr5'>Google-форма на отзыв</a>",
                           parse_mode='html')


# Реакция на команду "help"
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Для работы чат-бота введи <b>/go</b> или <b>/start</b>.\n\n"
                           "В блоке <b>\"Образование\"</b> ты сможешь найти информацию о направлениях подготовки по двум уровням обучения: "
                           "бакалавриату и магистратуре, а также пройти тест на профориентацию.\n\n"
                           "В блоке <b>\"Поступление\"</b> можно найти информацию о проходных баллах, количестве мест, стоимости обучения, "
                           "вступительных испытаниях по всем направлениям подготовки. Также есть возможность посмотреть направления "
                           "подготовки по выбранным экзаменам, часто задаваемые вопросы. В подблоке \"Календарь абитуриента\" "
                           "содержатся даты приёма на обучение в вуз.\n\n"
                           "В блоке <b>\"Подача документов\"</b> ты сможешь подать необходимые документы для поступления онлайн: через портал Госуслуг, либо через сеть "
                           "КФУ \"Буду студентом!\", также можно подать документы лично по указанному адресу.\n\n"
                           "В блоке <b>\"Отзыв о чат-боте\"</b> по желанию можно оставить свой отзыв.\n\n"
                           "В блоке <b>\"Контакты приёмной комиссии\"</b> находятся телефон, электронная почта, адрес и режим работы приёмной комиссии", parse_mode='html')


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)
