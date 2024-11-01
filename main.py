from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk


#бэкэнд

def formula_select(event):
    selection = combobox.get()
    if selection == 'Формула Харрисона-Бенедикта':
       return method_harrison_benedict()
    elif selection == 'Формула Миффлина-Сан Жеора':
        return method_mifflin_sangeora()
    elif selection == 'Формула Кетч-МакАрдла':
        return method_ketch_makard()
    elif selection == 'Формула ВОЗ':
        return method_voz()

def method_harrison_benedict(sex, age, height, weight, kfa=1):
    if sex == 'Мужской':
        res_cal = (66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)) * kfa
    elif sex == 'Женский':
        res_cal = (655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)) * kfa
    return res_cal

def method_mifflin_sangeora(sex, age, height, weight, kfa=1):
    if sex == 'Мужской':
        res_cal = (((10 * weight) + (6.25 * height) - (5 * age))) + 5 * kfa
    elif sex == 'Женский':
        res_cal = (((10 * weight) + (6.25 * height) - (5 * age)) - 161) * kfa
    return res_cal

def method_ketch_makard():
    pass
def method_voz():
    pass

res_calories = 0
def calculate_area(sex, age, height, weight, kfa=0):
    pass






# Фронтэнд
window = Tk()
window.title('Калькулятор калорий')
window.geometry("400x400")


# настройка фрейма для всех элементов
frame = Frame(window, padx=10, pady=10, relief=SUNKEN, borderwidth=2)
frame.pack()

method_calc = Label(frame, text='Выберите формулу для расчета калорий')
method_calc.grid(row=1, column=1)
# method_calc.configure(text='Не выбирайте')

# настройка поля выбора формулы расчета
methods = ['Формула Харрисона-Бенедикта',
           'Формула Миффлина-Сан Жеора',
           'Формула Кетч-МакАрдла',
           'Формула ВОЗ']

combobox = ttk.Combobox(frame, values=methods, width=30, state='readonly')
combobox.grid(row=2, column=1)
combobox.set(methods[0])
combobox.bind('<<ComboboxSelected>>', formula_select)
# Поле "ПОЛ"
choice_sex_lbl = Label(frame, text='Выберите ваш пол')
choice_sex_lbl.grid(row=3, column=1, pady=10)
choices_sex = ['Мужской', 'Женский', 'Не выбрано']
choices_sex_combobox = ttk.Combobox(frame, values=choices_sex, width=10, state='readonly')
choices_sex_combobox.grid(row=3, column=2)
choices_sex_combobox.set(choices_sex[-1])
# choices_sex_combobox.bind('<<ComboboxSelected>>', select_sex)
# Поле "Возраст"
age_lbl = Label(frame, text='Введите ваш возраст')
age_lbl.grid(row=4,column=1, pady=10)
age_entry = Entry(frame)
age_entry.grid(row=4,column=2)

# Поле "Рост"
height_lbl = Label(frame, text='Введите ваш рост')
height_lbl.grid(row=5,column=1, pady=10)
height_entry = Entry(frame)
height_entry.grid(row=5,column=2)

# Поле "Вес"
weight_lbl = Label(frame, text='Введите ваш вес')
weight_lbl.grid(row=6,column=1, pady=10)
weight_entry = Entry(frame)
weight_entry.grid(row=6,column=2)
# Поле "КФА"
kfa_lbl = Label(frame, text='Введите коэффициент физ.активности')
kfa_lbl.grid(row=7,column=1, pady=10)
kfa_entry = Entry(frame)
kfa_entry.grid(row=7,column=2)


# Настройка кнопки
btn_calc = ttk.Button(
    frame,
    text='Рассчитать',
    command=calculate_area(choices_sex_combobox.get(), age_entry.get(), height_entry.get(), weight_entry.get(), kfa_entry.get()))
btn_calc.grid(row=8, column=2)

# Вывод результата

result_line_lbl = Label(frame, text='---------------------------------------------')
result_line_lbl.grid(row=9, column = 1)
result_lbl_title = Label(frame, text='Ваша суточная норма')
result_lbl_title.grid(row=10, column=1)
result_lbl_out = Label(frame, text=f'{res_calories} Ккал')
result_lbl_out.grid(row=10, column=2)


window.mainloop()