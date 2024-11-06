from tkinter import *
from tkinter import ttk
import code_backend as b

# Основное окно
window = Tk()
window.title('Калькулятор калорий')
window.geometry("400x400")


# настройка фрейма для всех элементов
frame = Frame(window, height=300, padx=10, pady=10)
frame.pack()



#настройка поля выбора формулы расчета
method_calc = Label(frame, text='Выберите формулу для расчета калорий')
method_calc.grid(row=1, column=1)
methods = ['Формула Харрисона-Бенедикта',
           'Формула Миффлина-Сан Жеора',
           'Формула Тома Венуто']

combobox = ttk.Combobox(frame, values=methods, width=30, state='readonly')
combobox.grid(row=2, column=1)
combobox.set(methods[0])



# Поле "ПОЛ"
choice_sex_lbl = Label(frame, text='Выберите ваш пол')
choice_sex_lbl.grid(row=3, column=1, pady=10)
choices_sex = ['Мужской', 'Женский', 'Не выбрано']
choices_sex_combobox = ttk.Combobox(frame, values=choices_sex, width=10, state='readonly')
choices_sex_combobox.grid(row=3, column=2)
choices_sex_combobox.set(choices_sex[-1])



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

# Настройка кнопки очистки полей
btn_clear = ttk.Button(
    frame,
    text ='Очистить',
    command = b.clear_area)
btn_clear.grid(row=8, column=1)



# Настройка кнопки расчета
btn_calc = ttk.Button(
    frame,
    text='Рассчитать',
    command=b.calculate_area)
btn_calc.grid(row=8, column=2)

# Вывод результата
result_line_lbl = Label(frame, text='---------------------------------------------')
result_line_lbl.grid(row=9, column = 1)
result_lbl_title = Label(frame, text='Ваша суточная норма')
result_lbl_title.grid(row=10, column=1)
result_lbl_out = Label(frame, text=f'0 Ккал')
result_lbl_out.grid(row=10, column=2)




window.mainloop()