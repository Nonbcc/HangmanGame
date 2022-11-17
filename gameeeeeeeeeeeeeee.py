# กนกวรรณ ดีหลี 63090500418
# จุฬาลักษณ์ ป้องศรี 63090500421
# โชตินรินทร์ พิสิฐพัฒิกุล 63090500423
# ปาลิตา สิมะบวรสุทธิ์ 63090500427
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from random import *

# set variables

global count_category
global count_character

# make first window

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Hangman")
win.setGeometry(480, 200, 1000, 700)

# make second window

win2 = QMdiSubWindow()
win2.setWindowTitle("Select Category and Characters")
win2.setGeometry(480, 200, 1000, 700)

# make third window

win3 = QMdiSubWindow()
win3.setWindowTitle("Play Hangman Now!!")
win3.setGeometry(480, 200, 1000, 700)

# make four window (show you lose or win with picture)

win4 = QMdiSubWindow()
win4.setWindowTitle("Your result in Game")
win4.setGeometry(480, 200, 1000, 700)

# Playing window

def third_window():
    global count_category
    global count_character

    # set background3 for win3

    background3 = QPixmap('background3.jpg').scaled(1000, 700)

    lb_image5 = QLabel(win3)
    lb_image5.setPixmap(background3)
    lb_image5.setGeometry(0, 0, 0, 400)
    lb_image5.move(0, 0)
    lb_image5.adjustSize()

    # set first character

    if count_character == 1:
        result_image1 = QPixmap('im1.1.png')
        result_image2 = QPixmap('im1.2.png')
        result_image3 = QPixmap('im1.3.png')
        result_image4 = QPixmap('im1.4.png')
        result_image5 = QPixmap('im1.5.png')
        result_image6 = QPixmap('im1.6.png')
        result_image7 = QPixmap('im1.7.png')
        win_image = QPixmap('winner.png')

        rs_image1 = QLabel(win3)
        rs_image1.setPixmap(result_image1)
        rs_image1.setGeometry(0, 0, 0, 200)
        rs_image1.move(18, 100)
        rs_image1.adjustSize()

        rs_image2 = QLabel(win3)
        rs_image2.setPixmap(result_image2)
        rs_image2.setGeometry(0, 0, 0, 200)
        rs_image2.move(140, 310)
        rs_image2.adjustSize()

        rs_image3 = QLabel(win3)
        rs_image3.setPixmap(result_image3)
        rs_image3.setGeometry(0, 0, 0, 200)
        rs_image3.move(42, 309)
        rs_image3.adjustSize()

        rs_image4 = QLabel(win3)
        rs_image4.setPixmap(result_image4)
        rs_image4.setGeometry(0, 0, 0, 200)
        rs_image4.move(220, 308)
        rs_image4.adjustSize()

        rs_image5 = QLabel(win3)
        rs_image5.setPixmap(result_image5)
        rs_image5.setGeometry(0, 0, 0, 200)
        rs_image5.move(68, 405)
        rs_image5.adjustSize()

        rs_image6 = QLabel(win3)
        rs_image6.setPixmap(result_image6)
        rs_image6.setGeometry(0, 0, 0, 200)
        rs_image6.move(169, 403)
        rs_image6.adjustSize()

        rs_image7 = QLabel(win3)
        rs_image7.setPixmap(result_image7)
        rs_image7.setGeometry(0, 0, 0, 200)
        rs_image7.move(-40, 30)
        rs_image7.adjustSize()

        # hide all first character picture

        rs_image1.setVisible(0)
        rs_image2.setVisible(0)
        rs_image3.setVisible(0)
        rs_image4.setVisible(0)
        rs_image5.setVisible(0)
        rs_image6.setVisible(0)
        rs_image7.setVisible(0)

    # set second character

    elif count_character == 2:
        result_image1 = QPixmap('im2.1.png')
        result_image2 = QPixmap('im2.2.png')
        result_image3 = QPixmap('im2.3.png')
        result_image4 = QPixmap('im2.4.png')
        result_image5 = QPixmap('im2.5.png')
        result_image6 = QPixmap('im2.6.png')
        result_image7 = QPixmap('im2.7.png')
        win_image = QPixmap('winner.png')

        rs_image1 = QLabel(win3)
        rs_image1.setPixmap(result_image1)
        rs_image1.setGeometry(0, 0, 0, 200)
        rs_image1.move(26, 100)
        rs_image1.adjustSize()

        rs_image2 = QLabel(win3)
        rs_image2.setPixmap(result_image2)
        rs_image2.setGeometry(0, 0, 0, 200)
        rs_image2.move(140, 329)
        rs_image2.adjustSize()

        rs_image3 = QLabel(win3)
        rs_image3.setPixmap(result_image3)
        rs_image3.setGeometry(0, 0, 0, 200)
        rs_image3.move(61, 329)
        rs_image3.adjustSize()

        rs_image4 = QLabel(win3)
        rs_image4.setPixmap(result_image4)
        rs_image4.setGeometry(0, 0, 0, 200)
        rs_image4.move(219, 328)
        rs_image4.adjustSize()

        rs_image5 = QLabel(win3)
        rs_image5.setPixmap(result_image5)
        rs_image5.setGeometry(0, 0, 0, 200)
        rs_image5.move(83, 410)
        rs_image5.adjustSize()

        rs_image6 = QLabel(win3)
        rs_image6.setPixmap(result_image6)
        rs_image6.setGeometry(0, 0, 0, 200)
        rs_image6.move(165, 410)
        rs_image6.adjustSize()

        rs_image7 = QLabel(win3)
        rs_image7.setPixmap(result_image7)
        rs_image7.setGeometry(0, 0, 0, 200)
        rs_image7.move(10, 80)
        rs_image7.adjustSize()

        # hide all second character picture

        rs_image1.setVisible(0)
        rs_image2.setVisible(0)
        rs_image3.setVisible(0)
        rs_image4.setVisible(0)
        rs_image5.setVisible(0)
        rs_image6.setVisible(0)
        rs_image7.setVisible(0)

    # set third character

    elif count_character == 3:
        result_image1 = QPixmap('im3.1.png')
        result_image2 = QPixmap('im3.2.png')
        result_image3 = QPixmap('im3.3.png')
        result_image4 = QPixmap('im3.4.png')
        result_image5 = QPixmap('im3.5.png')
        result_image6 = QPixmap('im3.6.png')
        result_image7 = QPixmap('im3.7.png')
        win_image = QPixmap('winner.png')

        rs_image1 = QLabel(win3)
        rs_image1.setPixmap(result_image1)
        rs_image1.setGeometry(0, 0, 0, 200)
        rs_image1.move(60, 100)
        rs_image1.adjustSize()

        rs_image2 = QLabel(win3)
        rs_image2.setPixmap(result_image2)
        rs_image2.setGeometry(0, 0, 0, 200)
        rs_image2.move(128, 310)
        rs_image2.adjustSize()

        rs_image3 = QLabel(win3)
        rs_image3.setPixmap(result_image3)
        rs_image3.setGeometry(0, 0, 0, 200)
        rs_image3.move(50, 308)
        rs_image3.adjustSize()

        rs_image4 = QLabel(win3)
        rs_image4.setPixmap(result_image4)
        rs_image4.setGeometry(0, 0, 0, 200)
        rs_image4.move(227, 308)
        rs_image4.adjustSize()

        rs_image5 = QLabel(win3)
        rs_image5.setPixmap(result_image5)
        rs_image5.setGeometry(0, 0, 0, 200)
        rs_image5.move(70, 410)
        rs_image5.adjustSize()

        rs_image6 = QLabel(win3)
        rs_image6.setPixmap(result_image6)
        rs_image6.setGeometry(0, 0, 0, 200)
        rs_image6.move(178, 418)
        rs_image6.adjustSize()

        rs_image7 = QLabel(win3)
        rs_image7.setPixmap(result_image7)
        rs_image7.setGeometry(0, 0, 0, 200)
        rs_image7.move(10, 80)
        rs_image7.adjustSize()

        # hide all third character picture

        rs_image1.setVisible(0)
        rs_image2.setVisible(0)
        rs_image3.setVisible(0)
        rs_image4.setVisible(0)
        rs_image5.setVisible(0)
        rs_image6.setVisible(0)
        rs_image7.setVisible(0)

    #  when click wrong answer show one image at a time and the last picture will show on window4

    def rs1():
        rs_image1.setVisible(1)

    def rs2():
        rs_image2.setVisible(1)

    def rs3():
        rs_image3.setVisible(1)

    def rs4():
        rs_image4.setVisible(1)

    def rs5():
        rs_image5.setVisible(1)

    def rs6():
        rs_image6.setVisible(1)

    # set You lose label

    def rs7():
        result_text = QLabel(win4)
        result_text.setText("You lose")
        result_text.setFont(QtGui.QFont("Arials", 35))
        result_text.adjustSize()

        rs_image7 = QLabel(win4)
        rs_image7.setPixmap(result_image7)
        rs_image7.setGeometry(0, 0, 0, 200)
        rs_image7.move(0, 40)
        result_text.move(610, 310)
        rs_image7.adjustSize()

        win3.close()
        win4.show()

    check_ans = ''
    global counttt
    counttt = 0

    # process to check ture or false answer

    def print_text():
        global counttt
        list_check = []
        checkkub2 = 0

        # print(list_ans)

        for i in check:
            checkkub = 0
            b = 0
            for j in list_ans:
                if i == ' ':
                    b = 1
                    break
                if i == j:
                    checkkub = 1
                    list_check.append(i)
            if b == 1:
                list_check.append(' ')
            elif checkkub == 0:
                list_check.append('_')
                checkkub2 = 1

        # set background4 for win4(win)

        background5 = QPixmap('background4(win).jpg').scaled(1000, 700)

        lb_image7 = QLabel(win4)
        lb_image7.setPixmap(background5)
        lb_image7.setGeometry(0, 0, 0, 400)
        lb_image7.move(0, 0)
        lb_image7.adjustSize()

        # set winner show

        if checkkub2 == 0:
            winner = QLabel(win4)
            winner.setPixmap(win_image)
            winner.setGeometry(0, 0, 0, 200)
            winner.move(50, 0)
            winner.adjustSize()

            result_text = QLabel(win4)
            result_text.setText("You win")
            result_text.setFont(QtGui.QFont("Arials", 35))
            result_text.adjustSize()
            result_text.move(620, 320)

            win3.close()
            win4.show()
        if counttt == 1:
            rs1()
        elif counttt == 2:
            rs2()
        elif counttt == 3:
            rs3()
        elif counttt == 4:
            rs4()
        elif counttt == 5:
            rs5()
        elif counttt == 6:
            rs6()
        elif counttt == 7:
            rs7()
        word.setText(check_ans.join(list_check))
        word.adjustSize()

    # set all button and process

    a_button = QPushButton(win3)
    a_button.setText('A')
    a_button.setFont(QtGui.QFont("Arials", 16))
    a_button.setGeometry(0, 0, 50, 50)
    a_button.move(440, 200)

    def append_a():
        global counttt
        list_ans.append('a')
        a_button.setVisible(0)
        if 'a' not in check:
            counttt += 1

    a_button.clicked.connect(append_a)
    a_button.clicked.connect(print_text)

    b_button = QPushButton(win3)
    b_button.setText('B')
    b_button.setFont(QtGui.QFont("Arials", 16))
    b_button.setGeometry(0, 0, 50, 50)
    b_button.move(540, 200)

    def append_b():
        global counttt
        list_ans.append('b')
        b_button.setVisible(0)
        if 'b' not in check:
            counttt += 1

    b_button.clicked.connect(append_b)
    b_button.clicked.connect(print_text)

    c_button = QPushButton(win3)
    c_button.setText('C')
    c_button.setFont(QtGui.QFont("Arials", 16))
    c_button.setGeometry(0, 0, 50, 50)
    c_button.move(640, 200)

    def append_c():
        global counttt
        list_ans.append('c')
        c_button.setVisible(0)
        if 'c' not in check:
            counttt += 1

    c_button.clicked.connect(append_c)
    c_button.clicked.connect(print_text)

    d_button = QPushButton(win3)
    d_button.setText('D')
    d_button.setFont(QtGui.QFont("Arials", 16))
    d_button.setGeometry(0, 0, 50, 50)
    d_button.move(740, 200)

    def append_d():
        global counttt
        list_ans.append('d')
        d_button.setVisible(0)
        if 'd' not in check:
            counttt += 1

    d_button.clicked.connect(append_d)
    d_button.clicked.connect(print_text)

    e_button = QPushButton(win3)
    e_button.setText('E')
    e_button.setFont(QtGui.QFont("Arials", 16))
    e_button.setGeometry(0, 0, 50, 50)
    e_button.move(840, 200)

    def append_e():
        global counttt
        list_ans.append('e')
        e_button.setVisible(0)
        if 'e' not in check:
            counttt += 1

    e_button.clicked.connect(append_e)
    e_button.clicked.connect(print_text)

    f_button = QPushButton(win3)
    f_button.setText('F')
    f_button.setFont(QtGui.QFont("Arials", 16))
    f_button.setGeometry(0, 0, 50, 50)
    f_button.move(440, 275)

    def append_f():
        global counttt
        list_ans.append('f')
        f_button.setVisible(0)
        if 'f' not in check:
            counttt += 1

    f_button.clicked.connect(append_f)
    f_button.clicked.connect(print_text)

    g_button = QPushButton(win3)
    g_button.setText('G')
    g_button.setFont(QtGui.QFont("Arials", 16))
    g_button.setGeometry(0, 0, 50, 50)
    g_button.move(540, 275)

    def append_g():
        global counttt
        list_ans.append('g')
        g_button.setVisible(0)
        if 'g' not in check:
            counttt += 1

    g_button.clicked.connect(append_g)
    g_button.clicked.connect(print_text)

    h_button = QPushButton(win3)
    h_button.setText('H')
    h_button.setFont(QtGui.QFont("Arials", 16))
    h_button.setGeometry(0, 0, 50, 50)
    h_button.move(640, 275)

    def append_h():
        global counttt
        list_ans.append('h')
        h_button.setVisible(0)
        if 'h' not in check:
            counttt += 1

    h_button.clicked.connect(append_h)
    h_button.clicked.connect(print_text)

    i_button = QPushButton(win3)
    i_button.setText('I')
    i_button.setFont(QtGui.QFont("Arials", 16))
    i_button.setGeometry(0, 0, 50, 50)
    i_button.move(740, 275)

    def append_i():
        global counttt
        list_ans.append('i')
        i_button.setVisible(0)
        if 'i' not in check:
            counttt += 1

    i_button.clicked.connect(append_i)
    i_button.clicked.connect(print_text)

    j_button = QPushButton(win3)
    j_button.setText('J')
    j_button.setFont(QtGui.QFont("Arials", 16))
    j_button.setGeometry(0, 0, 50, 50)
    j_button.move(840, 275)

    def append_j():
        global counttt
        list_ans.append('j')
        j_button.setVisible(0)
        if 'j' not in check:
            counttt += 1

    j_button.clicked.connect(append_j)
    j_button.clicked.connect(print_text)

    k_button = QPushButton(win3)
    k_button.setText('K')
    k_button.setFont(QtGui.QFont("Arials", 16))
    k_button.setGeometry(0, 0, 50, 50)
    k_button.move(440, 350)

    def append_k():
        global counttt
        list_ans.append('k')
        k_button.setVisible(0)
        if 'k' not in check:
            counttt += 1

    k_button.clicked.connect(append_k)
    k_button.clicked.connect(print_text)

    l_button = QPushButton(win3)
    l_button.setText('L')
    l_button.setFont(QtGui.QFont("Arials", 16))
    l_button.setGeometry(0, 0, 50, 50)
    l_button.move(540, 350)

    def append_l():
        global counttt
        list_ans.append('l')
        l_button.setVisible(0)
        if 'l' not in check:
            counttt += 1

    l_button.clicked.connect(append_l)
    l_button.clicked.connect(print_text)

    m_button = QPushButton(win3)
    m_button.setText('M')
    m_button.setFont(QtGui.QFont("Arials", 16))
    m_button.setGeometry(0, 0, 50, 50)
    m_button.move(640, 350)

    def append_m():
        global counttt
        list_ans.append('m')
        m_button.setVisible(0)
        if 'm' not in check:
            counttt += 1

    m_button.clicked.connect(append_m)
    m_button.clicked.connect(print_text)

    n_button = QPushButton(win3)
    n_button.setText('N')
    n_button.setFont(QtGui.QFont("Arials", 16))
    n_button.setGeometry(0, 0, 50, 50)
    n_button.move(740, 350)

    def append_n():
        global counttt
        list_ans.append('n')
        n_button.setVisible(0)
        if 'n' not in check:
            counttt += 1

    n_button.clicked.connect(append_n)
    n_button.clicked.connect(print_text)

    o_button = QPushButton(win3)
    o_button.setText('O')
    o_button.setFont(QtGui.QFont("Arials", 16))
    o_button.setGeometry(0, 0, 50, 50)
    o_button.move(840, 350)

    def append_o():
        global counttt
        list_ans.append('o')
        o_button.setVisible(0)
        if 'o' not in check:
            counttt += 1

    o_button.clicked.connect(append_o)
    o_button.clicked.connect(print_text)

    p_button = QPushButton(win3)
    p_button.setText('P')
    p_button.setFont(QtGui.QFont("Arials", 16))
    p_button.setGeometry(0, 0, 50, 50)
    p_button.move(440, 425)

    def append_p():
        global counttt
        list_ans.append('p')
        p_button.setVisible(0)
        if 'p' not in check:
            counttt += 1

    p_button.clicked.connect(append_p)
    p_button.clicked.connect(print_text)

    q_button = QPushButton(win3)
    q_button.setText('Q')
    q_button.setFont(QtGui.QFont("Arials", 16))
    q_button.setGeometry(0, 0, 50, 50)
    q_button.move(540, 425)

    def append_q():
        global counttt
        list_ans.append('q')
        q_button.setVisible(0)
        if 'q' not in check:
            counttt += 1

    q_button.clicked.connect(append_q)
    q_button.clicked.connect(print_text)

    r_button = QPushButton(win3)
    r_button.setText('R')
    r_button.setFont(QtGui.QFont("Arials", 16))
    r_button.setGeometry(0, 0, 50, 50)
    r_button.move(640, 425)

    def append_r():
        global counttt
        list_ans.append('r')
        r_button.setVisible(0)
        if 'r' not in check:
            counttt += 1

    r_button.clicked.connect(append_r)
    r_button.clicked.connect(print_text)

    s_button = QPushButton(win3)
    s_button.setText('S')
    s_button.setFont(QtGui.QFont("Arials", 16))
    s_button.setGeometry(0, 0, 50, 50)
    s_button.move(740, 425)

    def append_s():
        global counttt
        list_ans.append('s')
        s_button.setVisible(0)
        if 's' not in check:
            counttt += 1

    s_button.clicked.connect(append_s)
    s_button.clicked.connect(print_text)

    t_button = QPushButton(win3)
    t_button.setText('T')
    t_button.setFont(QtGui.QFont("Arials", 16))
    t_button.setGeometry(0, 0, 50, 50)
    t_button.move(840, 425)

    def append_t():
        global counttt
        list_ans.append('t')
        t_button.setVisible(0)
        if 't' not in check:
            counttt += 1

    t_button.clicked.connect(append_t)
    t_button.clicked.connect(print_text)

    u_button = QPushButton(win3)
    u_button.setText('U')
    u_button.setFont(QtGui.QFont("Arials", 16))
    u_button.setGeometry(0, 0, 50, 50)
    u_button.move(440, 500)

    def append_u():
        global counttt
        list_ans.append('u')
        u_button.setVisible(0)
        if 'u' not in check:
            counttt += 1

    u_button.clicked.connect(append_u)
    u_button.clicked.connect(print_text)

    v_button = QPushButton(win3)
    v_button.setText('V')
    v_button.setFont(QtGui.QFont("Arials", 16))
    v_button.setGeometry(0, 0, 50, 50)
    v_button.move(540, 500)

    def append_v():
        global counttt
        list_ans.append('v')
        v_button.setVisible(0)
        if 'v' not in check:
            counttt += 1

    v_button.clicked.connect(append_v)
    v_button.clicked.connect(print_text)

    w_button = QPushButton(win3)
    w_button.setText('W')
    w_button.setFont(QtGui.QFont("Arials", 16))
    w_button.setGeometry(0, 0, 50, 50)
    w_button.move(640, 500)

    def append_w():
        global counttt
        list_ans.append('w')
        w_button.setVisible(0)
        if 'w' not in check:
            counttt += 1

    w_button.clicked.connect(append_w)
    w_button.clicked.connect(print_text)

    x_button = QPushButton(win3)
    x_button.setText('X')
    x_button.setFont(QtGui.QFont("Arials", 16))
    x_button.setGeometry(0, 0, 50, 50)
    x_button.move(740, 500)

    def append_x():
        global counttt
        list_ans.append('x')
        x_button.setVisible(0)
        if 'x' not in check:
            counttt += 1

    x_button.clicked.connect(append_x)
    x_button.clicked.connect(print_text)

    y_button = QPushButton(win3)
    y_button.setText('Y')
    y_button.setFont(QtGui.QFont("Arials", 16))
    y_button.setGeometry(0, 0, 50, 50)
    y_button.move(840, 500)

    def append_y():
        global counttt
        list_ans.append('y')
        y_button.setVisible(0)
        if 'y' not in check:
            counttt += 1

    y_button.clicked.connect(append_y)
    y_button.clicked.connect(print_text)

    z_button = QPushButton(win3)
    z_button.setText('Z')
    z_button.setFont(QtGui.QFont("Arials", 16))
    z_button.setGeometry(0, 0, 50, 50)
    z_button.move(440, 575)

    def append_z():
        global counttt
        list_ans.append('z')
        z_button.setVisible(0)
        if 'z' not in check:
            counttt += 1

    z_button.clicked.connect(append_z)
    z_button.clicked.connect(print_text)

    # hide the bottom when you click

    a_button.setVisible(1)
    b_button.setVisible(1)
    c_button.setVisible(1)
    d_button.setVisible(1)
    e_button.setVisible(1)
    f_button.setVisible(1)
    g_button.setVisible(1)
    h_button.setVisible(1)
    i_button.setVisible(1)
    j_button.setVisible(1)
    k_button.setVisible(1)
    l_button.setVisible(1)
    m_button.setVisible(1)
    n_button.setVisible(1)
    o_button.setVisible(1)
    p_button.setVisible(1)
    q_button.setVisible(1)
    r_button.setVisible(1)
    s_button.setVisible(1)
    t_button.setVisible(1)
    u_button.setVisible(1)
    v_button.setVisible(1)
    w_button.setVisible(1)
    x_button.setVisible(1)
    y_button.setVisible(1)
    z_button.setVisible(1)

    # process when you select your category 1

    if count_category == 1:

        title_game = QLabel(win3)
        title_game.setText('Animals')
        title_game.setFont(QtGui.QFont("Arials", 30))
        title_game.adjustSize()
        title_game.move(600, 20)

        roll = randint(1, 10)
        if roll == 1:
            word = QLabel(win3)
            word.setText('c r _ c _ _ _ l _')
            list_ans = ['c', 'r', 'l']
            check = 'c r o c o d i l e'
            c_button.setVisible(0)
            r_button.setVisible(0)
            l_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(440, 100)
        elif roll == 2:
            word = QLabel(win3)
            word.setText('b _ _ r')
            list_ans = ['b', 'r']
            check = 'b e a r'
            b_button.setVisible(0)
            r_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(570, 100)
        elif roll == 3:
            word = QLabel(win3)
            word.setText('c _ _ e _')
            list_ans = ['c', 'e']
            check = 'c a m e l'
            c_button.setVisible(0)
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(535, 100)
        elif roll == 4:
            word = QLabel(win3)
            word.setText('e _ e p _ _ n _')
            list_ans = ['e', 'p', 'n']
            check = 'e l e p h a n t'
            e_button.setVisible(0)
            p_button.setVisible(0)
            n_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(450, 100)
        elif roll == 5:
            word = QLabel(win3)
            word.setText('k a _ _ a _ o o')
            list_ans = ['k', 'a', 'o']
            check = 'k a n g a r o o'
            k_button.setVisible(0)
            a_button.setVisible(0)
            o_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(450, 100)
        elif roll == 6:
            word = QLabel(win3)
            word.setText('_ _ a _ a')
            list_ans = ['a']
            check = 'k o a l a'
            a_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(545, 100)
        elif roll == 7:
            word = QLabel(win3)
            word.setText('l _ _ _')
            list_ans = ['l']
            check = 'l i o n'
            l_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(580, 100)
        elif roll == 8:
            word = QLabel(win3)
            word.setText('_ a _ _ a')
            list_ans = ['a']
            check = 'p a n d a'
            a_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(540, 100)
        elif roll == 9:
            word = QLabel(win3)
            word.setText('p _ _ g _ i _')
            list_ans = ['p', 'g', 'i']
            check = 'p e n g u i n'
            p_button.setVisible(0)
            g_button.setVisible(0)
            i_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(490, 100)
        elif roll == 10:
            word = QLabel(win3)
            word.setText('s _ a _ _')
            list_ans = ['s', 'a']
            check = 's h a r k'
            s_button.setVisible(0)
            a_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(540, 100)

    # process when you select your category 2

    elif count_category == 2:
        title_game = QLabel(win3)
        title_game.setText('Foods')
        title_game.setFont(QtGui.QFont("Arials", 30))
        title_game.adjustSize()
        title_game.move(620, 20)

        roll = randint(1, 10)
        if roll == 1:
            word = QLabel(win3)
            word.setText('b _ c _ _')
            list_ans = ['b', 'c']
            check = 'b a c o n'
            b_button.setVisible(0)
            c_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(530, 100)
        elif roll == 2:
            word = QLabel(win3)
            word.setText('_ a u _ a _ _')
            list_ans = ['a', 'u']
            check = 's a u s a g e'
            a_button.setVisible(0)
            u_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(480, 100)
        elif roll == 3:
            word = QLabel(win3)
            word.setText('_ m e _ e _ _ e')
            list_ans = ['m', 'e']
            check = 'o m e l e t t e'
            m_button.setVisible(0)
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(445, 100)
        elif roll == 4:
            word = QLabel(win3)
            word.setText('m _ _ t _ r _')
            list_ans = ['m', 't', 'r']
            check = 'm u s t a r d'
            m_button.setVisible(0)
            r_button.setVisible(0)
            t_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(480, 100)
        elif roll == 5:
            word = QLabel(win3)
            word.setText('n _ _ _ l _')
            list_ans = ['n', 'l']
            check = 'n o o d l e'
            n_button.setVisible(0)
            l_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(520, 100)
        elif roll == 6:
            word = QLabel(win3)
            word.setText('s _ _ _ m p')
            list_ans = ['s', 'm', 'p']
            check = 's h r i m p'
            s_button.setVisible(0)
            m_button.setVisible(0)
            p_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(500, 100)
        elif roll == 7:
            word = QLabel(win3)
            word.setText('h _ _ b u _ g _ _')
            list_ans = ['h', 'b', 'u', 'g']
            check = 'h a m b u r g e r'
            h_button.setVisible(0)
            b_button.setVisible(0)
            u_button.setVisible(0)
            g_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(420, 100)
        elif roll == 8:
            word = QLabel(win3)
            word.setText('_ _ z z _')
            list_ans = ['z']
            check = 'p i z z a'
            z_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(540, 100)
        elif roll == 9:
            word = QLabel(win3)
            word.setText('s t _ a _')
            list_ans = ['s', 't', 'a']
            check = 's t e a k'
            s_button.setVisible(0)
            t_button.setVisible(0)
            a_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(540, 100)
        elif roll == 10:
            word = QLabel(win3)
            word.setText('s _ a _ _ e _ _ i')
            list_ans = ['s', 'a', 'e', 'i']
            check = 's p a g h e t t i'
            s_button.setVisible(0)
            a_button.setVisible(0)
            e_button.setVisible(0)
            i_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(430, 100)

    # process when you select your category 3

    elif count_category == 3:
        title_game = QLabel(win3)
        title_game.setText('Colours')
        title_game.setFont(QtGui.QFont("Arials", 30))
        title_game.adjustSize()
        title_game.move(610, 20)

        roll = randint(1, 10)
        if roll == 1:
            word = QLabel(win3)
            word.setText('o _ _ n _ e')
            list_ans = ['o', 'n', 'e']
            check = 'o r a n g e'
            o_button.setVisible(0)
            n_button.setVisible(0)
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(500, 100)
        elif roll == 2:
            word = QLabel(win3)
            word.setText(' _ _ e e _')
            list_ans = ['e']
            check = 'g r e e n'
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(520, 100)
        elif roll == 3:
            word = QLabel(win3)
            word.setText('p _ _ _')
            list_ans = ['p']
            check = 'p i n k'
            p_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(550, 100)
        elif roll == 4:
            word = QLabel(win3)
            word.setText('p _ _ p _ _')
            list_ans = ['p']
            check = 'p u r p l e'
            p_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(500, 100)
        elif roll == 5:
            word = QLabel(win3)
            word.setText('_ e _')
            list_ans = ['e']
            check = 'r e d'
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(590, 100)
        elif roll == 6:
            word = QLabel(win3)
            word.setText('y _ _ _ o _')
            list_ans = ['y', 'o']
            check = 'y e l l o w'
            y_button.setVisible(0)
            o_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(510, 100)
        elif roll == 7:
            word = QLabel(win3)
            word.setText('_ l _ e')
            list_ans = ['l', 'e']
            check = 'b l u e'
            l_button.setVisible(0)
            e_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(580, 100)
        elif roll == 8:
            word = QLabel(win3)
            word.setText('b _ o _ _')
            list_ans = ['b', 'o']
            check = 'b r o w n'
            b_button.setVisible(0)
            o_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(530, 100)
        elif roll == 9:
            word = QLabel(win3)
            word.setText('_ _ a _')
            list_ans = ['a']
            check = 'g r a y'
            a_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(570, 100)
        elif roll == 10:
            word = QLabel(win3)
            word.setText('b _ _ c _')
            list_ans = ['b', 'c']
            check = 'b l a c k'
            b_button.setVisible(0)
            c_button.setVisible(0)
            word.setFont(QtGui.QFont("Arials", 50))
            word.adjustSize()
            word.move(540, 100)

    win3.show()
    win2.close()

# win show select categories and characters

def second_window():
    global tick
    tick = 0
    global count_category
    global count_character

    # set background2 for win2

    background2 = QPixmap('background2.jpg').scaled(1000, 700)

    lb_image5 = QLabel(win2)
    lb_image5.setPixmap(background2)
    lb_image5.setGeometry(0, 0, 0, 400)
    lb_image5.move(0, 0)
    lb_image5.adjustSize()

    text = QLabel(win2)
    text.setText("Please select one categories")
    text.adjustSize()
    text.setFont(QtGui.QFont("Arials", 24))
    text.setGeometry(280, -20, 500, 150)

    second_select = QLabel(win2)
    second_select.setText("Please select one characters")
    second_select.setStyleSheet("color: white")
    second_select.setFont(QtGui.QFont("Arials", 24))
    second_select.setGeometry(360, 200, 700, 300)

    # process button to select categories

    def first_buttoncheck():
        global tick
        global count_category
        count_category = 0
        if bt1.isChecked():
            label.setText("Animals")
            count_category += 1
            tick += 1
            bt2.setVisible(0)
            bt3.setVisible(0)
        elif bt2.isChecked():
            label.setText("Foods")
            count_category += 2
            tick += 1
            bt1.setVisible(0)
            bt3.setVisible(0)
        elif bt3.isChecked():
            label.setText("Colours")
            count_category += 3
            tick += 1
            bt1.setVisible(0)
            bt2.setVisible(0)
        else:
            bt1.setVisible(1)
            bt2.setVisible(1)
            bt3.setVisible(1)
            tick -= 1
        if tick == 2:
            click_bt.setVisible(1)
        else:
            click_bt.setVisible(0)

    # set bottom select your category

    bt1 = QCheckBox(win2)
    bt1.setText("Animals")
    bt1.setFont(QtGui.QFont("Arials", 24))
    bt1.toggled.connect(first_buttoncheck)
    bt1.setGeometry(440, 90, 200, 50)

    bt2 = QCheckBox(win2)
    bt2.setText("Foods")
    bt2.setFont(QtGui.QFont("Arials", 24))
    bt2.toggled.connect(first_buttoncheck)
    bt2.setGeometry(440, 140, 250, 70)

    bt3 = QCheckBox(win2)
    bt3.setText("Colours")
    bt3.setFont(QtGui.QFont("Arials", 24))
    bt3.toggled.connect(first_buttoncheck)
    bt3.setGeometry(440, 190, 200, 90)

    # process button to select characters

    def second_buttoncheck():
        global tick
        global count_character
        count_character = 0
        if bt4.isChecked():
            label.setText("1")
            count_character += 1
            tick += 1
            bt5.setVisible(0)
            bt6.setVisible(0)
        elif bt5.isChecked():
            label.setText("2")
            count_character += 2
            tick += 1
            bt4.setVisible(0)
            bt6.setVisible(0)
        elif bt6.isChecked():
            label.setText("3")
            count_character += 3
            tick += 1
            bt4.setVisible(0)
            bt5.setVisible(0)
        else:
            tick -= 1
            bt4.setVisible(1)
            bt5.setVisible(1)
            bt6.setVisible(1)
        if tick == 2:
            click_bt.setVisible(1)
        else:
            click_bt.setVisible(0)

    # set botton select your characters

    bt4 = QCheckBox(win2)
    bt4.setText("1")
    bt4.setFont(QtGui.QFont("Arials", 24))
    bt4.toggled.connect(second_buttoncheck)
    bt4.setGeometry(350, 490, 100, 300)

    bt5 = QCheckBox(win2)
    bt5.setText("2")
    bt5.setFont(QtGui.QFont("Arials", 24))
    bt5.toggled.connect(second_buttoncheck)
    bt5.setGeometry(600, 490, 100, 300)

    bt6 = QCheckBox(win2)
    bt6.setText("3")
    bt6.setFont(QtGui.QFont("Arials", 24))
    bt6.toggled.connect(second_buttoncheck)
    bt6.setGeometry(850, 490, 100, 300)

    # set picture characters

    character1 = QPixmap('Character1.png')
    character2 = QPixmap('Character2.png')
    character3 = QPixmap('Character3.png')

    lb_image1 = QLabel(win2)
    lb_image1.setPixmap(character1)
    lb_image1.setGeometry(0, 0, 0, 600)
    lb_image1.move(300, 400)
    lb_image1.adjustSize()

    lb_image2 = QLabel(win2)
    lb_image2.setPixmap(character2)
    lb_image2.setGeometry(0, 0, 0, 600)
    lb_image2.move(550, 400)
    lb_image2.adjustSize()

    lb_image3 = QLabel(win2)
    lb_image3.setPixmap(character3)
    lb_image3.setGeometry(0, 0, 0, 600)
    lb_image3.move(800, 400)
    lb_image3.adjustSize()

    # Ok button go to third window

    click_bt = QPushButton(win2)
    click_bt.setGeometry(0, 0, 80, 40)
    click_bt.setText('OK')
    click_bt.setVisible(0)
    click_bt.setFont(QtGui.QFont("Arials", 18))
    click_bt.move(900, 620)
    click_bt.clicked.connect(third_window)

    win2.show()
    win.close()

# Select exit button


def exit_choice():
    sys.exit(app.exec_())

# set main background

background1 = QPixmap('background1.jpg').scaled(1000,700)

lb_image4 = QLabel(win)
lb_image4.setPixmap(background1)
lb_image4.setGeometry(0, 0, 0, 400)
lb_image4.move(0, 0)
lb_image4.adjustSize()

# Head

label = QLabel(win)
label.setText("Hangman")
label.setFont(QtGui.QFont("Arials", 20))
label.setStyleSheet("color: white")
label.setGeometry(150, 250, 300, 150)
label.move(450, 137)

# play and exit

play_game = QPushButton(win)
play_game.clicked.connect(second_window)
play_game.setText("Play game")
play_game.setFont(QtGui.QFont("Arials", 20))
play_game.setGeometry(415, 250, 200, 70)
play_game.move(420, 240)

exit_game = QPushButton(win)
exit_game.clicked.connect(exit_choice)
exit_game.setText("exit")
exit_game.setFont(QtGui.QFont("Arials", 20))
exit_game.setGeometry(415, 250, 200, 70)
exit_game.move(420, 320)

win.show()
sys.exit(app.exec_())