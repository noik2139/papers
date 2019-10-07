
import time
import os
from msvcrt import getch

def main_text(CLASS = "", TITLE = "", DATE = "",SEMESTER = "Önn Nr. 3"):

    with open('temp.txt', 'r', encoding='utf8') as file: 
        main = file.read().format(TITLE,DATE,CLASS,SEMESTER)

    return main

def this_semester():
    #finnur önn
    time_tuble = time.localtime()
    semester_now = 0
    year_start = 2018
    year = time_tuble[0]
    month = time_tuble[1]
    diff_year = year-year_start
    semester_now += diff_year*2
    if month > 7:
        semester_now += 1
    return "Önn Nr.{}".format(semester_now)

def this_day():
    #finnur dag
    time_tuble = time.localtime()
    time_str = "{0[0]}/{0[1]}/{0[2]}".format(time_tuble)
    return time_str

def print_green(text):
    print("\033[1;30;42m{}".format(text))

def print_n(text):
    print("\033[0;37;40m{}".format(text))


def select_folder():

    ls = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
    
    length = len(ls)
    select = 0
    green = length - select
    key = ''
    while key != b'\r':
        print("select class")
        green = length - select-1
        os.system("cls")
        print_n('["w"- upp/ "s"- down]')
        for file_name in ls:
            index = ls.index(file_name)
            if index == green:
                print_green(file_name)
            else:
                print_n(file_name)

        #til að búa til nýja skrá
        if green == length:
                print_green("Make new file")
        else:
            print_n("Make new file")

        print_n('')
        key = getch()

        if key == b'w' and green > 0:
            select += 1
        elif key == b's' and green <= length-1:
            select -= 1
    os.system("cls")
    if select == -1:
        class_name = input("name of class: ")
        os.system('mkdir "{}"'.format(class_name))
        os.system("cls")
        print("You made: {}".format(class_name))
        return class_name
    else:
        os.system("cls")
        print("þú valdir: {}".format(ls[green]))
        return ls[green]
        

def set_up():
    day = this_day()
    folder = select_folder()

    semester = this_semester()
    title = input("Title: ")
    file_name = os.getcwd() + '\\' + folder + '\\' + title + '.tex'
    text = main_text(folder, title, day, semester)
    file = open(file_name,"w", encoding='utf8')
    file.write(text)
    file.close()

set_up()