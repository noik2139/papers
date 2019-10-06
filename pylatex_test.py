
import time
import os
from msvcrt import getch

def main_text(CLASS = "", TITLE = "", DATE = "",SEMESTER = "Önn Nr. 3"):
    main = ''' 
    \\documentclass[12pt]{{article}}
    \\usepackage[T1]{{fontenc}}
    \\usepackage{{natbib}}
    \\usepackage{{url}}
    \\usepackage[utf8x]{{inputenc}}
    \\usepackage{{amsmath}}
    \\usepackage{{graphicx}}
    \\graphicspath{{{{images/}}}}
    \\usepackage{{parskip}}
    \\usepackage{{fancyhdr}}
    \\usepackage{{vmargin}}
    \\setmarginsrb{{3 cm}}{{2.5 cm}}{{3 cm}}{{2.5 cm}}{{1 cm}}{{1.5 cm}}{{1 cm}}{{1.5 cm}}
    \\linespread{{1.15}}
    \\usepackage{{subcaption}} 
    \\usepackage[font=footnotesize]{{caption}}


    \\title{{{0}}}								 
    \\author{{Nói Kristjánsson}}			
    \\date{{{1}}}											

    \\makeatletter
    \\let\\thetitle\\@title
    \\let\\theauthor\\@author
    \\let\\thedate\\@date
    \\makeatother

    \\pagestyle{{fancy}}
    \\fancyhf{{}}
    %\\rhead{{\\theauthor}}
    \\lhead{{\\thetitle}}
    \\cfoot{{\\thepage}}


    \\begin{{document}}

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \\begin{{titlepage}}
        \\centering
        \\vspace*{{0.5 cm}}
        \\includegraphics[scale = 1.15]{{HR_logo_midjad_hires.jpg}}\\\\[1.0 cm]	% University Logo
        \\textsc{{\\Large {2}}}\\\\[0.5 cm]				% Course Code   
        \\textsc{{\\large {3}}}\\\\[0.5 cm]				% Course Name
        \\rule{{\\linewidth}}{{0.2 mm}} \\\\[0.4 cm]
        {{ \\huge \\bfseries \\thetitle}}\\\\
        \\rule{{\\linewidth}}{{0.2 mm}} \\\\[1.5 cm]
        
        \\begin{{minipage}}{{0.4\\textwidth}}
            \\begin{{flushleft}} \\large
                \\emph{{Höfundur:}}\\\\
                \\theauthor
                \\end{{flushleft}}
                \\end{{minipage}}~
                \\begin{{minipage}}{{0.4\\textwidth}}
                \\begin{{flushright}} \\large
                                        % Your Student Number
            \\end{{flushright}}
        \\end{{minipage}}\\\\[2 cm]
        
        {{\\large \\thedate}}\\\\[2 cm]
    
        \\vfill
        
    \\end{{titlepage}}


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \\end{{document}}
    '''.format(TITLE,DATE,CLASS,SEMESTER)

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
        print("green: {}".format(green))
        print("select: {}".format(select))
        key = getch()

        if key == b'w' and green > 0:
            select += 1
        elif key == b's' and green <= length-1:
            select -= 1
    os.system("cls")
    if select == -1:
        class_name = input("name of class: ")
        os.system("mkdir {}".format(class_name))
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