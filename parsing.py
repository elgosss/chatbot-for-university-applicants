import re
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}

# Образование
url_admission = 'https://kpfu.ru/elabuga/abitur/n/'
req_admission = requests.get(url_admission, headers=headers)
soup_admission = BeautifulSoup(req_admission.text, 'lxml')
info_admission = soup_admission.find('div', class_='visit_link').find_all('p')

# Календарь абитуриента
url_calendar = 'https://admissions.kpfu.ru/priem-v-universitet/sroki-provedeniya-priema-bakalavriat/specialitet-magistratura'
req_calendar = requests.get(url_calendar, headers=headers)
soup_calendar = BeautifulSoup(req_calendar.text, 'lxml')
info_calendar = soup_calendar.find_all(class_='spoiler-content')
title_calendar = soup_calendar.find_all(class_='spoiler-title')

# Буду студентом!
url_be_student = 'https://admissions.kpfu.ru/priemnaya-komissiya/podacha-dokumentov-bakalavriat/specialitet'
req_be_student = requests.get(url_be_student, headers=headers)
soup_be_student = BeautifulSoup(req_be_student.text, 'lxml')
info_be_student = soup_be_student.find(class_='spoiler-content').find_all('p')

# Подача док-тов лично
url_offline = 'https://admissions.kpfu.ru/priemnaya-komissiya/podacha-dokumentov-bakalavriat/specialitet'
req_offline = requests.get(url_offline, headers=headers)
soup_offline = BeautifulSoup(req_offline.text, 'lxml')
info_offline = soup_offline.find(class_='spoiler-content').find_all('span')

# Поступление: количество мест, стоимость обучения, вступительные испытания
number_of_places = [0] * 90
cost_of_study = [0] * 90
entrance_tests = [0] * 90
computer_science, computer_science_for_foreign, computer_science_extr, computer_science_for_foreign_extr,\
    mechatronics, mechatronics_for_foreign, transport, transport_for_foreign, part_time_economics, part_time_economics_for_foreign,\
    full_time_economics, full_time_economics_for_foreign, full_time_law, full_time_law_for_foreign, part_time_law, part_time_law_for_foreign,\
    english_ped, english_ped_for_foreign, elementary_ped, elementary_ped_for_foreign,\
    gen_add_ped, gen_add_ped_for_foreign, technology_ped, technology_ped_for_foreign, cult_ped, cult_ped_for_foreign,\
    psycho_pre, psycho_pre_for_foreign, psycho_of_edu, psycho_of_edu_for_foreign, psycho_of_edu_extr, psycho_of_edu_for_foreign_extr,\
    psycho_of_edu_electro, psycho_of_edu_electro_for_foreign, automation, automation_for_foreign, graphic, graphic_for_foreign,\
    graphic_extr, graphic_for_foreign_extr, eng_two_pr, eng_two_pr_for_foreign, biology_two_pr, biology_two_pr_for_foreign,\
    add_edu, add_edu_for_foreign, elem_edu, elem_edu_for_foreign, tatar, tatar_for_foreign, english, english_for_foreign,\
    society, society_for_foreign, inform, inform_for_foreign, physics, physics_for_foreign, eng_lang, eng_lang_for_foreign,\
    litr, litr_for_foreign, life_safety, life_safety_for_foreign, sport, sport_for_foreign, china, china_for_foreign, deutsch, deutsch_for_foreign,\
    business_pedag, business_pedag_for_foreign, engin_pedag, engin_pedag_for_foreign, eng_in_poly, eng_in_poly_for_foreign, edu_poly, edu_poly_for_foreign,\
    project_p, project_p_for_foreign, prof_sport, prof_sport_for_foreign, rus_and_lit, rus_and_lit_for_foreign, edu_pre, edu_pre_for_foreign,\
    edu_managment, edu_managment_for_foreign, digit_edu, digit_edu_for_foreign = range(90)
# Бакалавриат
# Прикладная информатика:
# Очная
url_computer_science = 'https://kpfu.ru/elabuga/abitur/n/090303pe/pp'
req_computer_science = requests.get(url_computer_science, headers=headers)
soup_computer_science = BeautifulSoup(req_computer_science.text, 'lxml')
number_of_places_title = soup_computer_science.find(string=re.compile('Количество мест'))
number_of_places[computer_science] = soup_computer_science.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('td', string=re.compile('бюджет')).find_next_sibling('td')
number_of_places[computer_science_for_foreign] = soup_computer_science.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study_title = soup_computer_science.find(string=re.compile('Стоимость обучения в'))
cost_of_study[computer_science] = soup_computer_science.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[computer_science] = soup_computer_science.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')
# Заочная
number_of_places[computer_science_extr] = number_of_places[computer_science].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[computer_science_for_foreign_extr] = number_of_places[computer_science_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('td').find_next_sibling('td')

# Мехатроника и робототехника
url_mechatronics = 'https://kpfu.ru/elabuga/abitur/n/150306fmr/pp'
req_mechatronics = requests.get(url_mechatronics, headers=headers)
soup_mechatronics = BeautifulSoup(req_mechatronics.text, 'lxml')
number_of_places[mechatronics] = soup_mechatronics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[mechatronics_for_foreign] = soup_mechatronics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[mechatronics] = soup_mechatronics.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('p')
entrance_tests[mechatronics] = soup_mechatronics.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Технология транспортных процессов
url_transport = 'https://kpfu.ru/elabuga/abitur/n/230301pts/pp'
req_transport = requests.get(url_transport, headers=headers)
soup_transport = BeautifulSoup(req_transport.text, 'lxml')
number_of_places[transport] = soup_transport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[transport_for_foreign] = soup_transport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[transport] = soup_transport.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[transport] = soup_transport.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Экономика и финансы организаций (реализуется с применением электронного обучения и дистанционных технологий)
url_part_time_economics = 'https://kpfu.ru/elabuga/abitur/n/380301efd/pp'
req_part_time_economics = requests.get(url_part_time_economics, headers=headers)
soup_part_time_economics = BeautifulSoup(req_part_time_economics.text, 'lxml')
number_of_places[part_time_economics] = soup_part_time_economics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[part_time_economics_for_foreign] = soup_part_time_economics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[part_time_economics] = soup_part_time_economics.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[part_time_economics] = soup_part_time_economics.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Экономика и финансы организаций (с углублённым изучением иностранных языков)
url_full_time_economics = 'https://kpfu.ru/elabuga/abitur/n/380301efi/pp'
req_full_time_economics = requests.get(url_full_time_economics, headers=headers)
soup_full_time_economics = BeautifulSoup(req_full_time_economics.text, 'lxml')
number_of_places[full_time_economics] = soup_full_time_economics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[full_time_economics_for_foreign] = soup_full_time_economics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[full_time_economics] = soup_full_time_economics.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[full_time_economics] = soup_full_time_economics.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Юриспруденция (Гражданское право)
url_full_time_law = 'https://kpfu.ru/elabuga/abitur/n/400301jugp/pp'
req_full_time_law = requests.get(url_full_time_law, headers=headers)
soup_full_time_law = BeautifulSoup(req_full_time_law.text, 'lxml')
number_of_places[full_time_law] = soup_full_time_law.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[full_time_law_for_foreign] = soup_full_time_law.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[full_time_law] = soup_full_time_law.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[full_time_law] = soup_full_time_law.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Юриспруденция (Гражданское право (реализуется с применением электронного обучения и дистанционных технологий))
url_part_time_law = 'https://kpfu.ru/elabuga/abitur/n/400301jugpdt/pp'
req_part_time_law = requests.get(url_part_time_law, headers=headers)
soup_part_time_law = BeautifulSoup(req_part_time_law.text, 'lxml')
number_of_places[part_time_law] = soup_part_time_law.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[part_time_law_for_foreign] = soup_part_time_law.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[part_time_law] = soup_part_time_law.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[part_time_law] = soup_part_time_law.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Английский язык)
url_english_ped = 'https://kpfu.ru/elabuga/abitur/n/440301en/pp'
req_english_ped = requests.get(url_english_ped, headers=headers)
soup_english_ped = BeautifulSoup(req_english_ped.text, 'lxml')
number_of_places[english_ped] = soup_english_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[english_ped_for_foreign] = soup_english_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[english_ped] = soup_english_ped.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[english_ped] = soup_english_ped.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Начальное образование)
url_elementary_ped = 'https://kpfu.ru/elabuga/abitur/n/440301no/pp'
req_elementary_ped = requests.get(url_elementary_ped, headers=headers)
soup_elementary_ped = BeautifulSoup(req_elementary_ped.text, 'lxml')
number_of_places[elementary_ped] = soup_elementary_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[elementary_ped_for_foreign] = soup_elementary_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[elementary_ped] = soup_elementary_ped.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[elementary_ped] = soup_elementary_ped.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Общее и дополнительное образование в предметной области "Технология")
url_gen_add_ped = 'https://kpfu.ru/elabuga/abitur/n/440301odt/pp'
req_gen_add_ped = requests.get(url_gen_add_ped, headers=headers)
soup_gen_add_ped = BeautifulSoup(req_gen_add_ped.text, 'lxml')
number_of_places[gen_add_ped] = soup_gen_add_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[gen_add_ped_for_foreign] = soup_gen_add_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[gen_add_ped] = soup_gen_add_ped.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[gen_add_ped] = soup_gen_add_ped.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Технология и робототехника)
url_technology_ped = 'https://kpfu.ru/elabuga/abitur/n/440301trt/pp'
req_technology_ped = requests.get(url_technology_ped, headers=headers)
soup_technology_ped = BeautifulSoup(req_technology_ped.text, 'lxml')
number_of_places[technology_ped] = soup_technology_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[technology_ped_for_foreign] = soup_technology_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[technology_ped] = soup_technology_ped.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[technology_ped] = soup_technology_ped.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Физическая культура)
url_cult_ped = 'https://kpfu.ru/elabuga/abitur/n/440301fk/pp'
req_cult_ped = requests.get(url_cult_ped, headers=headers)
soup_cult_ped = BeautifulSoup(req_cult_ped.text, 'lxml')
number_of_places[cult_ped] = soup_cult_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[cult_ped_for_foreign] = soup_cult_ped.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[cult_ped] = soup_cult_ped.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[cult_ped] = soup_cult_ped.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Психолого-педагогическое образование (Психология и педагогика дошкольного образования)
url_psycho_pre = 'https://kpfu.ru/elabuga/abitur/n/440302ppdo/pp'
req_psycho_pre = requests.get(url_psycho_pre, headers=headers)
soup_psycho_pre = BeautifulSoup(req_psycho_pre.text, 'lxml')
number_of_places[psycho_pre] = soup_psycho_pre.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[psycho_pre_for_foreign] = soup_psycho_pre.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[psycho_pre] = soup_psycho_pre.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[psycho_pre] = soup_psycho_pre.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Психолого-педагогическое образование (Психология образования):
# Очная
url_psycho_of_edu = 'https://kpfu.ru/elabuga/abitur/n/440302po/pp'
req_psycho_of_edu = requests.get(url_psycho_of_edu, headers=headers)
soup_psycho_of_edu = BeautifulSoup(req_psycho_of_edu.text, 'lxml')
number_of_places[psycho_of_edu] = soup_psycho_of_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('td', string=re.compile('бюджет')).find_next_sibling('td')
number_of_places[psycho_of_edu_for_foreign] = soup_psycho_of_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[psycho_of_edu] = soup_psycho_of_edu.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[psycho_of_edu] = soup_psycho_of_edu.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')
# Заочная
number_of_places[psycho_of_edu_extr] = number_of_places[psycho_of_edu].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[psycho_of_edu_for_foreign_extr] = number_of_places[psycho_of_edu_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('td').find_next_sibling('td')

# Психолого-педагогическое образование (Психология образования (с применением электронного обучения и дистанционных образовательных технологий))
url_psycho_of_edu_electro = 'https://kpfu.ru/elabuga/abitur/n/440302podt/pp'
req_psycho_of_edu_electro = requests.get(url_psycho_of_edu_electro, headers=headers)
soup_psycho_of_edu_electro = BeautifulSoup(req_psycho_of_edu_electro.text, 'lxml')
number_of_places[psycho_of_edu_electro] = soup_psycho_of_edu_electro.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td')
number_of_places[psycho_of_edu_electro_for_foreign] = soup_psycho_of_edu_electro.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next('td')     # Не продусмотрено (если информация будет дополняться (?))
cost_of_study[psycho_of_edu_electro] = soup_psycho_of_edu_electro.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('p')
entrance_tests[psycho_of_edu_electro] = soup_psycho_of_edu_electro.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Профессиональное обучение (по отраслям) (Автоматизация энергетических систем)
url_count_automation = 'https://kpfu.ru/elabuga/abitur/n/440304aes/pp'
req_count_automation = requests.get(url_count_automation, headers=headers)
soup_count_automation = BeautifulSoup(req_count_automation.text, 'lxml')
number_of_places[automation] = soup_count_automation.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[automation_for_foreign] = soup_count_automation.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[automation] = soup_count_automation.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[automation] = soup_count_automation.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Профессиональное обучение (по отраслям) (Декорирование интерьера и графический дизайн):
# Очная
url_count_graphic = 'https://kpfu.ru/elabuga/abitur/n/440304digd/pp'
req_count_graphic = requests.get(url_count_graphic, headers=headers)
soup_count_graphic = BeautifulSoup(req_count_graphic.text, 'lxml')
number_of_places[graphic] = soup_count_graphic.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('td', string=re.compile('бюджет')).find_next_sibling('td')
number_of_places[graphic_for_foreign] = soup_count_graphic.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[graphic] = soup_count_graphic.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[graphic] = soup_count_graphic.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')
# Заочная
number_of_places[graphic_extr] = number_of_places[graphic].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[graphic_for_foreign_extr] = number_of_places[graphic_for_foreign].find_previous_sibling('td').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')

# Педагогическое образование (с двумя профилями подготовки) (Английский язык, родной (татарский) язык и литература)
url_count_eng_two_pr = 'https://kpfu.ru/elabuga/abitur/n/440305rla/pp'
req_count_eng_two_pr = requests.get(url_count_eng_two_pr, headers=headers)
soup_count_eng_two_pr = BeautifulSoup(req_count_eng_two_pr.text, 'lxml')
number_of_places[eng_two_pr] = soup_count_eng_two_pr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td')
number_of_places[eng_two_pr_for_foreign] = soup_count_eng_two_pr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next('td')             # Не продусмотрено
cost_of_study[eng_two_pr] = soup_count_eng_two_pr.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')     # Нет раздела "для иностранных граждан"
entrance_tests[eng_two_pr] = soup_count_eng_two_pr.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Биология и Химия)
url_count_biology_two_pr = 'https://kpfu.ru/elabuga/abitur/n/440305bh/pp'
req_count_biology_two_pr = requests.get(url_count_biology_two_pr, headers=headers)
soup_count_biology_two_pr = BeautifulSoup(req_count_biology_two_pr.text, 'lxml')
number_of_places[biology_two_pr] = soup_count_biology_two_pr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[biology_two_pr_for_foreign] = soup_count_biology_two_pr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[biology_two_pr] = soup_count_biology_two_pr.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[biology_two_pr] = soup_count_biology_two_pr.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Дошкольное образование и Дополнительное образование (художественное творчество))
url_count_add_edu = 'https://kpfu.ru/elabuga/abitur/n/440305dodo/pp'
req_count_add_edu = requests.get(url_count_add_edu, headers=headers)
soup_count_add_edu = BeautifulSoup(req_count_add_edu.text, 'lxml')
number_of_places[add_edu] = soup_count_add_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[add_edu_for_foreign] = soup_count_add_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[add_edu] = soup_count_add_edu.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[add_edu] = soup_count_add_edu.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Дошкольное образование и Начальное образование)
url_count_elem_edu = 'https://kpfu.ru/elabuga/abitur/n/440305dono/pp'
req_count_elem_edu = requests.get(url_count_elem_edu, headers=headers)
soup_count_elem_edu = BeautifulSoup(req_count_elem_edu.text, 'lxml')
number_of_places[elem_edu] = soup_count_elem_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[elem_edu_for_foreign] = soup_count_elem_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[elem_edu] = soup_count_elem_edu.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[elem_edu] = soup_count_elem_edu.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Дошкольное образование, родной (татарский) язык и литература)
url_count_tatar = 'https://kpfu.ru/elabuga/abitur/n/440305rldo/pp'
req_count_tatar = requests.get(url_count_tatar, headers=headers)
soup_count_tatar = BeautifulSoup(req_count_tatar.text, 'lxml')
number_of_places[tatar] = soup_count_tatar.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td')
number_of_places[tatar_for_foreign] = soup_count_tatar.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next('td')     # Не продусмотрено
cost_of_study[tatar] = soup_count_tatar.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')     # Нет раздела "для иностранных граждан"
entrance_tests[tatar] = soup_count_tatar.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (История и Иностранный (английский) язык)
url_count_english = 'https://kpfu.ru/elabuga/abitur/n/440305ii/pp'
req_count_english = requests.get(url_count_english, headers=headers)
soup_count_english = BeautifulSoup(req_count_english.text, 'lxml')
number_of_places[english] = soup_count_english.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[english_for_foreign] = soup_count_english.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[english] = soup_count_english.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[english] = soup_count_english.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (История и Обществознание)
url_count_society = 'https://kpfu.ru/elabuga/abitur/n/440305io/pp'
req_count_society = requests.get(url_count_society, headers=headers)
soup_count_society = BeautifulSoup(req_count_society.text, 'lxml')
number_of_places[society] = soup_count_society.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[society_for_foreign] = soup_count_society.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[society] = soup_count_society.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[society] = soup_count_society.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Математика и Информатика)
url_count_inform = 'https://kpfu.ru/elabuga/abitur/n/440305mi/pp'
req_count_inform = requests.get(url_count_inform, headers=headers)
soup_count_inform = BeautifulSoup(req_count_inform.text, 'lxml')
number_of_places[inform] = soup_count_inform.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[inform_for_foreign] = soup_count_inform.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[inform] = soup_count_inform.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[inform] = soup_count_inform.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Математика и Физика)
url_count_physics = 'https://kpfu.ru/elabuga/abitur/n/440305mf/pp'
req_count_physics = requests.get(url_count_physics, headers=headers)
soup_count_physics = BeautifulSoup(req_count_physics.text, 'lxml')
number_of_places[physics] = soup_count_physics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[physics_for_foreign] = soup_count_physics.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[physics] = soup_count_physics.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[physics] = soup_count_physics.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Русский язык и Иностранный (английский) язык)
url_count_eng_lang = 'https://kpfu.ru/elabuga/abitur/n/440305ra/pp'
req_count_eng_lang = requests.get(url_count_eng_lang, headers=headers)
soup_count_eng_lang = BeautifulSoup(req_count_eng_lang.text, 'lxml')
number_of_places[eng_lang] = soup_count_eng_lang.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[eng_lang_for_foreign] = soup_count_eng_lang.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[eng_lang] = soup_count_eng_lang.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[eng_lang] = soup_count_eng_lang.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Русский язык и Литература)
url_count_litr = 'https://kpfu.ru/elabuga/abitur/n/440305rl/pp'
req_count_litr = requests.get(url_count_litr, headers=headers)
soup_count_litr = BeautifulSoup(req_count_litr.text, 'lxml')
number_of_places[litr] = soup_count_litr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[litr_for_foreign] = soup_count_litr.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[litr] = soup_count_litr.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[litr] = soup_count_litr.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Физическая культура и безопасность жизнедеятельности)
url_count_life_safety = 'https://kpfu.ru/elabuga/abitur/n/440305fkb/pp'
req_count_life_safety = requests.get(url_count_life_safety, headers=headers)
soup_count_life_safety = BeautifulSoup(req_count_life_safety.text, 'lxml')
number_of_places[life_safety] = soup_count_life_safety.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[life_safety_for_foreign] = soup_count_life_safety.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[life_safety] = soup_count_life_safety.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[life_safety] = soup_count_life_safety.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (с двумя профилями подготовки) (Физическая культура и дополнительное образование (спортивная подготовка))
url_count_sport = 'https://kpfu.ru/elabuga/abitur/n/440305fkdosp/pp'
req_count_sport = requests.get(url_count_sport, headers=headers)
soup_count_sport = BeautifulSoup(req_count_sport.text, 'lxml')
number_of_places[sport] = soup_count_sport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[sport_for_foreign] = soup_count_sport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[sport] = soup_count_sport.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[sport] = soup_count_sport.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Лингвистика (Перевод и переводоведение (английский язык, китайский язык))
url_count_china = 'https://kpfu.ru/elabuga/abitur/n/450302ak/pp'
req_count_china = requests.get(url_count_china, headers=headers)
soup_count_china = BeautifulSoup(req_count_china.text, 'lxml')
number_of_places[china] = soup_count_china.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[china_for_foreign] = soup_count_china.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[china] = soup_count_china.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[china] = soup_count_china.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Лингвистика (Перевод и переводоведение (английский язык, немецкий язык))
url_count_deutsch = 'https://kpfu.ru/elabuga/abitur/n/450302ppan/pp'
req_count_deutsch = requests.get(url_count_china, headers=headers)
soup_count_deutsch = BeautifulSoup(req_count_china.text, 'lxml')
number_of_places[deutsch] = soup_count_deutsch.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[deutsch_for_foreign] = soup_count_deutsch.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[deutsch] = soup_count_deutsch.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[deutsch] = soup_count_deutsch.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Магистратура
# Педагогическое образование (Бизнес-педагогика)
url_count_business_pedag = 'https://kpfu.ru/elabuga/abitur/n/440401bp/pp'
req_count_business_pedag = requests.get(url_count_business_pedag, headers=headers)
soup_count_business_pedag = BeautifulSoup(req_count_business_pedag.text, 'lxml')
number_of_places[business_pedag] = soup_count_business_pedag.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[business_pedag_for_foreign] = soup_count_business_pedag.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[business_pedag] = soup_count_business_pedag.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[business_pedag] = soup_count_business_pedag.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Инженерная педагогика)
url_count_engin_pedag = 'https://kpfu.ru/elabuga/abitur/n/440401ip/pp'
req_count_engin_pedag = requests.get(url_count_engin_pedag, headers=headers)
soup_count_engin_pedag = BeautifulSoup(req_count_engin_pedag.text, 'lxml')
number_of_places[engin_pedag] = soup_count_engin_pedag.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[engin_pedag_for_foreign] = soup_count_engin_pedag.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[engin_pedag] = soup_count_engin_pedag.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[engin_pedag] = soup_count_engin_pedag.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Иностранный язык в лингвополикультурном образовательном пространстве)
url_count_eng_in_poly = 'https://kpfu.ru/elabuga/abitur/n/440401ilop/pp'
req_count_eng_in_poly = requests.get(url_count_eng_in_poly, headers=headers)
soup_count_eng_in_poly = BeautifulSoup(req_count_eng_in_poly.text, 'lxml')
number_of_places[eng_in_poly] = soup_count_eng_in_poly.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[eng_in_poly_for_foreign] = soup_count_eng_in_poly.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[eng_in_poly] = soup_count_eng_in_poly.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[eng_in_poly] = soup_count_eng_in_poly.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Полилингвальное образование)
url_count_edu_poly = 'https://kpfu.ru/elabuga/abitur/n/440401plo/pp'
req_count_edu_poly = requests.get(url_count_edu_poly, headers=headers)
soup_count_edu_poly = BeautifulSoup(req_count_edu_poly.text, 'lxml')
number_of_places[edu_poly] = soup_count_edu_poly.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[edu_poly_for_foreign] = soup_count_edu_poly.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[edu_poly] = soup_count_edu_poly.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[edu_poly] = soup_count_edu_poly.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Проектирование и оценка образовательных программ и процессов)
url_count_project_p = 'https://kpfu.ru/elabuga/abitur/n/440401popp/pp'
req_count_project_p = requests.get(url_count_project_p, headers=headers)
soup_count_project_p = BeautifulSoup(req_count_project_p.text, 'lxml')
number_of_places[project_p] = soup_count_project_p.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[project_p_for_foreign] = soup_count_project_p.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[project_p] = soup_count_project_p.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[project_p] = soup_count_project_p.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Профессиональная подготовка в области физической культуры и спорта)
url_count_prof_sport = 'https://kpfu.ru/elabuga/abitur/n/440401ppfks/pp'
req_count_prof_sport = requests.get(url_count_prof_sport, headers=headers)
soup_count_prof_sport = BeautifulSoup(req_count_prof_sport.text, 'lxml')
number_of_places[prof_sport] = soup_count_prof_sport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[prof_sport_for_foreign] = soup_count_prof_sport.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[prof_sport] = soup_count_prof_sport.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[prof_sport] = soup_count_prof_sport.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Русский язык и литература в межкультурной коммуникации)
url_count_rus_and_lit = 'https://kpfu.ru/elabuga/abitur/n/440401rlmk/pp'
req_count_rus_and_lit = requests.get(url_count_rus_and_lit, headers=headers)
soup_count_rus_and_lit = BeautifulSoup(req_count_rus_and_lit.text, 'lxml')
number_of_places[rus_and_lit] = soup_count_rus_and_lit.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[rus_and_lit_for_foreign] = soup_count_rus_and_lit.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[rus_and_lit] = soup_count_rus_and_lit.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[rus_and_lit] = soup_count_rus_and_lit.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Управление дошкольным образованием)
url_count_edu_pre = 'https://kpfu.ru/elabuga/abitur/n/440401udo/pp'
req_count_edu_pre = requests.get(url_count_edu_pre, headers=headers)
soup_count_edu_pre = BeautifulSoup(req_count_edu_pre.text, 'lxml')
number_of_places[edu_pre] = soup_count_edu_pre.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[edu_pre_for_foreign] = soup_count_edu_pre.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[edu_pre] = soup_count_edu_pre.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[edu_pre] = soup_count_edu_pre.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Управление образовательной организацией)
url_count_edu_managment = 'https://kpfu.ru/elabuga/abitur/n/440401uoo/pp'
req_count_edu_managment = requests.get(url_count_edu_managment, headers=headers)
soup_count_edu_managment = BeautifulSoup(req_count_edu_managment.text, 'lxml')
number_of_places[edu_managment] = soup_count_edu_managment.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[edu_managment_for_foreign] = soup_count_edu_managment.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[edu_managment] = soup_count_edu_managment.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[edu_managment] = soup_count_edu_managment.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')

# Педагогическое образование (Цифровое образование)
url_count_digit_edu = 'https://kpfu.ru/elabuga/abitur/n/440401zo/pp'
req_count_digit_edu = requests.get(url_count_digit_edu, headers=headers)
soup_count_digit_edu = BeautifulSoup(req_count_digit_edu.text, 'lxml')
number_of_places[digit_edu] = soup_count_digit_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
number_of_places[digit_edu_for_foreign] = soup_count_digit_edu.find(string=re.compile('Количество мест')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next_sibling('tr').\
    find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('td').find_next_sibling('td')
cost_of_study[digit_edu] = soup_count_digit_edu.find(string=re.compile('Стоимость обучения в')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').find_next('tr').find_next_sibling('tr').\
    find_next('td').find_next_sibling('td').find_next_sibling('td')
entrance_tests[digit_edu] = soup_count_digit_edu.find(string=re.compile('Вступительные испытания')).find_parent('tr').find_parent('tr').find_next_sibling('tr').find_next_sibling('tr').find_next('tr').find_next('tr').find_next_sibling('tr').find_next('td')
# --------------------------------------------------------------------------------------------------------------------------------------------

# src = req_admission.text
# with open('admission.html', 'w') as file:
#    file.write(src)
