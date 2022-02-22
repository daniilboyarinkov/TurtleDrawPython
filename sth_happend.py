from turtle import *

bgcolor('grey5')
title('I love you')


def draw():
    texts = ['OUH', "Wtf is this?", "AFAIR", "here...", "HERE", "shuld b sth", "BUT...", "where is this?", "oh sorry...", "I found", "here we go"]
    color('violet')
    update()
    speed(1)
    rect()
    for i in range(len(texts)):
        if i > 7: color('violet'); speed(3)
        else: speed(6)
        write(texts[i], align='center', font=('Comic Sans MS', 55, 'bold'))
        rect()
    update()


def update():
    reset()
    color('violet')
    write('I LOVE YOU', align='center', font=('Comic Sans MS', 55, 'bold'))


def rect():
    color('red', 'black')
    begin_fill()
    forward(250)
    left(90)
    forward(100)
    left(90)
    forward(500)
    left(90)
    forward(100)
    left(90)
    forward(250)
    end_fill()


def main():
    draw()


if __name__ == "__main__":
    main()
    mainloop()
