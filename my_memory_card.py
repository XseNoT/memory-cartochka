#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import randint, shuffle

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.total += 1
        print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    resultat()
 
def vaprosi():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False)  
    RadioGroup.setExclusive(True)

def click_OK():
    '''определяет, надо ли показать другой вопрос либо проверить ответ на этот'''
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def resultat():
    #показать панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    vaprosi() 

question_list = []
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
question_list.append(q1)

q2 = Question('Какая валентность у водорода?', '1', '5', '7', '16')
question_list.append(q2)

q3 = Question('Сколько лет Шреку?', '30', '45', '78', '54')
question_list.append(q3)

q4 = Question('Угадай', 'килька', '654', 'кердык', 'потная-подмыха')
question_list.append(q4)

q5 = Question('Полное имя Пикассо?', 'Па́бло Дие́го Хосе́ Франси́ско де Па́ула Хуа́н Непомусе́но Мари́я де лос Реме́диос Сиприа́но де ла Санти́сима Тринида́д Ма́ртир Патри́сио Руи́с-и-Пика́ссо', 'аЛег', 'Пабло Пикассо', 'Джим Керри')
question_list.append(q5)

q6 = Question('Первый миллиардер мира', 'Джон Дэ́висон Рокфе́ллер', 'Генри Форд', 'Марк Цукерберг', 'Ферруччо Ламборгини')
question_list.append(q6)

q7 = Question('Первая в мире видеоигра', 'Tennis for Two', 'Принц Персии', 'Need for speed Most wanted', 'Sonic')
question_list.append(q7)

q8 = Question('В каком году вышел тетрис?', '1984', '1986', '1990', '1977')
question_list.append(q8)

q9 = Question('Формула серной кислоты', 'H₂SO₄', 'H₂O', 'Li₃N', 'Na₃PO₄')
question_list.append(q9)

q10 = Question('В каком году закончилась династия Рюриковичей?', '1598', '1600', '1587', '1590')
question_list.append(q10)

q11 = Question('Первый президент Америки', 'Джордж Вашингтон', 'Дональд Трамп', 'Барак Обама', 'Джон Кеннеди')
question_list.append(q11)

q12 = Question('Самая быстрая машина в мире', 'Czinger 21C', 'Bugatti Veyron', 'Lamborghini Aventador', 'Volkswagen Beetle')
question_list.append(q12)

q13 = Question('Как будет привет на азбуке морзе?', '•−−• •−• •• •−− • −', '•−−• −−− −•− •−', '−•− •− −•−   −•• • •−•• •− ••−−••', '−•• • •−• −••− −− •• −−•− •')
question_list.append(q13)

q14 = Question('Авокадо это', 'Фрукт', 'Овощь', 'Я', 'Гриб')
question_list.append(q14)

q15 = Question('Какой самый распространенный язык программировнаия в мире?', 'Python', 'С++', 'JavaScript', 'HTML')
question_list.append(q15)

q16 = Question('Что такое тормозной башмак?', 'Средство для торможения поезда', 'Деталь в машине', 'Башмак для тормоза', 'Да')
question_list.append(q16)

q17 = Question('Что такое рекурсия?', 'Программа которая вызывает саму себя', 'А я че знаю что-ли?', 'Симметричное изображение', 'Заболевание')
question_list.append(q17)

q18 = Question('Когда изобретена перваяв мире вакцина?', '1796', '1800', '1880', '1689')
question_list.append(q18)

q19 = Question('Самая продаваемая вещь в мире', 'Кубик Рубика', 'Айфон', 'Кола', 'Вода')
question_list.append(q19)

q20 = Question('Самая дорогая криптовалюта в мире', 'Биткойн', 'Эфир', 'Кронос', 'Флоу')
question_list.append(q20)


def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint (0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)



app = QApplication([])

btn_OK = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
lb_Question = QLabel('Самый сложный вопрос в мире!')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_OK)
q = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
ask(q)
window.score = 0
window.total = 0
window.resize(400, 300)
window.show()
app.exec()