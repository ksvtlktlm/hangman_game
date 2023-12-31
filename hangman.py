import random


def get_word():
    index = random.randint(0, len(word_list))
    return word_list[index].upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    print('Давайте играть в угадайку слов!')
    tries = 6
    print('У вас 6 попыток, чтобы отгадать слово.')
    print(display_hangman(tries))
    l = len(word)
    print('_ ' * l)
    guessed_letters = []
    guessed_words = []
    guessed = False
    while tries > 0:
        print('Введите букву или слово целиком: ')
        ans = input().upper()
        if not ans.isalpha():
            print('Вводить какие-либо символы, кроме букв, запрещено.')
            continue

        show = ''

        if ans in guessed_letters:
            print('Эту букву вы уже вводили!')
            continue
            print(show)
        elif len(ans) == 1:
            if ord(ans) not in range(ord('А'), ord('Я')):
                print('Загаданное слово на русском языке.')
                continue
            if ans in word:
                guessed_letters.append(ans)
                for i in range(len(word)):
                    if word[i] in guessed_letters:
                        show += word[i]
                        if show == word:
                            guessed = True
                            print('Поздравляем, вы угадали слово!')
                            tries = 0
                            break
                    else:
                        show += '_'
            else:
                guessed_letters.append(ans)
                print('Этой буквы нет в загаданном слове.')
                tries -= 1
                print(show)
                print(display_hangman(tries))
        else:
            if ans == word:
                guessed = True
                print('Поздравляем, вы угадали слово!')
                break
            else:
                if ans in guessed_words:
                    print('Это слово вы уже пытались ввести.')
                    tries -= 1
                    print(show)
                    print(display_hangman(tries))
                    continue
                else:
                    guessed_words.append(ans)
                    print('Нет, загадано другое слово.')
                    tries -= 1
                    print(show)
                    print(display_hangman(tries))
                    continue

        print(show)
    if tries == 0:
        print(f'Попытки кончились! В этот раз не повезло :( \nЗагаданное слово - {word} ')


def continue_game():
    while True:
        word = get_word()
        print('Игра окончена! Хотите сыграть еще раз? "д" - да, "н" - нет...')
        ans = input()
        if ans == 'д' or ans == 'l':
            play(word)
        if ans == 'н' or ans == 'y':
            print('До следующего раза!')
            break


word_list = ['почта', 'домино', 'декор', 'сигнал', 'техника', 'проверка', 'математика', 'география', 'год', 'человек',
             'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место', 'вопрос', 'лицо', 'глаз', 'страна',
             'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова', 'система', 'вид', 'конец', 'отношение', 'город',
             'часть', 'женщина', 'проблема', 'земля', 'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец',
             'история', 'нога', 'вода', 'война', 'возможность', 'компания', 'результат', 'дверь', 'бог', 'народ',
             'область', 'число', 'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд',
             'деньга', 'уровень', 'начало', 'государство', 'тол', 'средство', 'связь', 'имя', 'президент', 'форма',
             'путь', 'организация', 'качество', 'действие', 'статья', 'общество', 'ситуация', 'деятельность', 'школа',
             'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель', 'программа', 'муж',
             'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок', 'предприятие', 'партия', 'роль', 'смысл',
             'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр', 'внимание', 'производство',
             'квартира', 'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната', 'семья', 'сын', 'смерть',
             'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор', 'окно', 'ответ', 'совет',
             'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план', 'проект', 'глава', 'материал',
             'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль', 'наука', 'документ', 'неделя', 'вещь',
             'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'член', 'ход', 'стена', 'директор', 'плечо',
             'опыт', 'встреча', 'принцип', 'событие', 'структура', 'количество', 'товарищ', 'создание', 'значение',
             'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример', 'лес', 'исследование',
             'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат', 'представитель',
             'борьба', 'использование', 'шаг', 'игра', 'участие', 'территория', 'край', 'размер', 'номер', 'район',
             'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь',
             'направление', 'позиция', 'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик',
             'фильм', 'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт', 'церковь', 'завод',
             'фирма', 'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух',
             'музыка', 'способ', 'хозяин', 'поле', 'доллар', 'память', 'природа', 'дерево', 'оценка', 'объем',
             'картина', 'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант',
             'берег', 'модель', 'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол',
             'зрение', 'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство', 'солнце', 'автомобиль',
             'родитель', 'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'ум', 'море',
             'удар', 'знание', 'солдат', 'миллион', 'строительство', 'технология', 'председатель', 'сон', 'сознание',
             'бумага', 'реформа', 'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок',
             'услуга', 'поэт', 'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет',
             'представление', 'площадь', 'генерал', 'господин', 'дочь', 'понятие', 'кабинет', 'безопасность', 'фонд',
             'сфера', 'папа', 'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика',
             'сумма', 'контроль', 'парень', 'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь',
             'нос', 'волос', 'ухо', 'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето',
             'камень', 'здание', 'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня',
             'депутат', 'проведение', 'рот', 'масса', 'комиссия', 'цвет', 'рассказ', 'функция', 'определение', 'мужик',
             'обеспечение', 'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение',
             'победа', 'товар', 'воля', 'зона', 'предел', 'целое', 'личность', 'офицер', 'влияние', 'поддержка',
             'ответственность', 'цветок', 'праздник', 'немец', 'бой', 'сестра', 'господь', 'учитель', 'многое', 'рамка',
             'практика', 'показатель', 'метр', 'войско', 'частность', 'особенность', 'снег', 'комитет', 'налог', 'акт',
             'отдел', 'карман', 'вывод', 'норма', 'читатель', 'этап', 'сравнение', 'прошлое', 'фамилия', 'кухня',
             'заявление', 'доля', 'пункт', 'студент', 'учет', 'впечатление', 'доход', 'вирус', 'клетка', 'удовольствие',
             'теория', 'враг', 'собрание', 'бутылка', 'расчет', 'го', 'режим', 'множество', 'клуб', 'попытка', 'зуб',
             'сеть', 'семь', 'министерство', 'прием', 'боль', 'сожаление', 'кожа', 'субъект', 'знак', 'актер', 'ресурс',
             'акция', 'газ', 'журналист', 'звук', 'передача', 'здоровье', 'администрация', 'болезнь', 'детство',
             'мастер', 'выборы', 'зима', 'подход', 'поиск', 'механизм', 'выражение', 'скорость', 'ощущение',
             'стоимость', 'коридор', 'ошибка', 'лидер', 'карта', 'заседание', 'глубина', 'хлеб', 'поверхность',
             'энергия', 'нарушение', 'реализация', 'революция', 'поведение', 'профессор', 'исполнение', 'заместитель',
             'суть', 'станция', 'реакция', 'десяток', 'столица', 'формирование', 'поколение', 'дума', 'существование',
             'продажа', 'список', 'способность', 'противник', 'схема', 'долг', 'режиссер', 'отличие', 'колено', 'дед',
             'свойство', 'этаж', 'секунда', 'фактор', 'житель', 'явление', 'высота', 'сосед', 'усилие', 'рождение',
             'расход', 'остров', 'фигура', 'наличие', 'дядя', 'милиция', 'растение', 'существо', 'черт', 'бабушка',
             'законодательство', 'собственность', 'отрасль', 'слеза', 'волна', 'стекло', 'традиция', 'январь',
             'оборудование', 'зависимость', 'фраза', 'декабрь', 'сведение', 'трубка', 'сентябрь', 'университет',
             'командир', 'храм', 'повышение', 'стиль', 'артист', 'больница', 'одежда', 'охрана', 'водка', 'кодекс',
             'имущество', 'птица', 'переход', 'красота', 'клиент', 'толпа', 'адрес', 'отделение', 'октябрь', 'чудо',
             'счастье', 'улыбка', 'ужас', 'аппарат', 'корабль', 'родина', 'животное', 'черта', 'известие', 'понимание',
             'тень', 'апрель', 'коллега', 'преступление', 'рыба', 'кресло', 'запах']
word = get_word()
play(word)
continue_game()