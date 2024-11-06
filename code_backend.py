import main as m
from tkinter import *
from tkinter import ttk



def method_harrison_benedict(sex, age, height, weight, kfa=1):
    if sex == 'Мужской':
        return (66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)) * kfa
    elif sex == 'Женский':
        return (655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)) * kfa


def method_mifflin_sangeora(sex, age, height, weight, kfa=1):
    if sex == 'Мужской':
        return (((10 * weight) + (6.25 * height) - (5 * age)) + 5) * kfa
    elif sex == 'Женский':
        return (((10 * weight) + (6.25 * height) - (5 * age)) - 161) * kfa


def method_venuto(sex, age, height, weight, kfa=1):
    if sex == 'Мужской':
        return (66.5 + (13.7 * weight) + (5 * height) - (6.8 * age)) * kfa
    elif sex == 'Женский':
        return (665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)) * kfa
def method_voz():
    pass

res_calories = 0
def calculate_area():
    sex = m.choices_sex_combobox.get()
    age = float(m.age_entry.get())
    height = float(m.height_entry.get())
    weight = float(m.weight_entry.get())
    try:
        kfa = float(m.kfa_entry.get())
    except:
        kfa = 1
    selection = m.combobox.get()
    if selection == 'Формула Харрисона-Бенедикта':
        res = method_harrison_benedict(sex, age, height, weight, kfa)
    elif selection == 'Формула Миффлина-Сан Жеора':
        res = method_mifflin_sangeora(sex, age, height, weight, kfa)
    elif selection == 'Формула Тома Венуто':
        res = method_venuto(sex, age, height, weight, kfa)
    elif selection == 'Формула ВОЗ':
        res = method_voz(sex, age, height, weight, kfa)

    m.result_lbl_out.config(text=f'{round(res, 1)} Ккал')
    # round(res, 1)

def clear_area():
    m.age_entry.delete(0, END)
    m.height_entry.delete(0, END)
    m.weight_entry.delete(0, END)
    m.kfa_entry.delete(0, END)
    m.choices_sex_combobox.set(m.choices_sex[-1])
