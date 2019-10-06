'''til að gera nýja skrá í latex'''
import time
import pylatex
time_tuble = time.localtime()[0:3]
time_str = "{0[0]}/{0[1]}/{0[2]}".format(time_tuble)



def def_text():
    doc = Document('basic')
    doc.documentclass = Command(
        'documentclass',
        options=['12pt', 'landscape'],
        arguments=['article'],
    )

doc.data.append(Package("caratula"))


def text():
    main_tex = '''
    \\documentclass[12pt]{article}
    \\usepackage[T1]{fontenc}
    \\usepackage{natbib}
    \\usepackage{url}
    \\usepackage[utf8x]{inputenc}
    \\usepackage{amsmath}
    \\usepackage{graphicx}
    \\graphicspath{{images/}}
    \\usepackage{parskip}
    \\usepackage{fancyhdr}
    \\usepackage{vmargin}
    \\setmarginsrb{3 cm}{2.5 cm}{3 cm}{2.5 cm}{1 cm}{1.5 cm}{1 cm}{1.5 cm}
    \\linespread{1.15}
    \\usepackage{subcaption} 
    \\usepackage[font=footnotesize]{caption}


    \\title{Glósur}								 
    \\author{Nói Kristjánsson}			
    \\date{19.9.2019}											

    \\makeatletter
    \\let\\thetitle\@title
    \\let\\theauthor\@author
    \\let\\thedate\@date
    \\makeatother

    \pagestyle{fancy}
    \\fancyhf{}
    %\rhead{\theauthor}
    \\lhead{\\thetitle}
    \cfoot{\\thepage}


    \\begin{document}

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \\begin{titlepage}
        \\centering
        \\vspace*{0.5 cm}
        \\includegraphics[scale = 1.15]{HR_logo_midjad_hires.jpg}\\[1.0 cm]	% University Logo
        \\textsc{\Large SE-T-202-EDL3}\\[0.5 cm]				% Course Code
        \\textsc{\large Önn 3}\\[0.5 cm]				% Course Name
        \\rule{\linewidth}{0.2 mm} \\[0.4 cm]
        { \huge \bfseries \thetitle}\\
        \rule{\linewidth}{0.2 mm} \\[1.5 cm]
        
        \begin{minipage}{0.4\textwidth}
            \begin{flushleft} \large
                \emph{Höfundur:}\\
                \theauthor
                \end{flushleft}
                \end{minipage}~
                \begin{minipage}{0.4\textwidth}
                \begin{flushright} \large
                                        % Your Student Number
            \end{flushright}
        \end{minipage}\\[2 cm]
        
        {\large \thedate}\\[2 cm]
    
        \vfill
        
    \end{titlepage}


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \end{document}
    '''