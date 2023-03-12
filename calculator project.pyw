import threading
from tkinter import *


window=Tk()
window.title('CALCULATOR')
window.geometry('300x410')
window.config(bg='#005c99')



expression=""
input_text=StringVar() 

def press(num):
  
  global expression 
  expression=expression+str(num)
  input_text.set(expression)

def clear_btn():
  global expression
  expression=""
  input_text.set("0")


def equal_press():
  try:
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
  except:
    '''lbl=Label(window,text='syntax error',fg='#323232',font=('bold',13))   #323232   #D93527
    lbl.place(x=105,y=55)
    lbl.after(1300,lbl.destroy)
    btn_clear()'''
    
    result='Syntax Error...'
    input_text.set(result)
    start_time=threading.Timer(2,clear_btn)
    start_time.start()


def percentage():
  try:
    global expression
    result=str(eval(expression)/100)
    input_text.set(result)
    expression=""
  except:
    result='syntax error...'
    input_text.set(result)
    start_time=threading.Timer(2,clear_btn)
    start_time.start()
      

def back_space():
    
    global expression
    expression=expression[:-1]
    #input_text.set(input_text.get()[0:-1])
    # a=str(input_text.set(input_text.get()[0:-1]))
    input_text.set(expression)
    #print(expression)
    if (len(expression)==0):
      input_text.set('0')

  
   #006666   #14C4D8  #523272 #000050 #8B008B  #473471 #009999 #993366   #b30086   #66004d   #000080   #005c99


entry=Entry(window,textvariable=input_text, bd=10,fg='black',font='bold',state=DISABLED,justify= RIGHT,bg='silver',disabledbackground='silver',disabledforeground='black')
entry.place(x=25,y=40,height=60,width=250)


btn_AC=Button(window,text='AC',padx=15,pady=5,bg='#deeded',bd='4',activebackground='#B2B2B3',activeforeground='WHITE',command=lambda:clear_btn())
btn_AC.place(x=25,y=140)

btn_divide=Button(window,text='÷',padx=20,pady=5,bg='#deeded',bd='4',command=lambda:press('/'),activebackground='#B2B2B3',activeforeground='white')
btn_divide.place(x=90,y=140)


btn_multiplication=Button(window,text='X',padx=20,pady=5,bg='#deeded',bd='4',command=lambda:press('*'),activebackground='#B2B2B3',activeforeground='white')
btn_multiplication.place(x=155,y=140)

btn_back=Button(window,text='⌫',padx=15,pady=5,bd='4',bg='#deeded',activebackground='#B2B2B3',command=lambda:back_space(),activeforeground='white')
btn_back.place(x=220,y=140)

btn9=Button(window,text='9',padx=20,pady=5,bd='4',command=lambda: press(9),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn9.place(x=155,y=190)

btn8=Button(window,text='8',padx=20,pady=5,bd='4',command=lambda: press(8),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn8.place(x=90,y=190)

btn7=Button(window,text='7',padx=20,pady=5,bd='4',command=lambda:press(7),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn7.place(x=25,y=190)

btn6=Button(window,text='6',padx=20,pady=5,bd='4',command=lambda:press(6),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn6.place(x=155,y=240)

btn5=Button(window,text='5',padx=20,pady=5,bd='4',command=lambda:press(5),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn5.place(x=90,y=240)

btn4=Button(window,text='4',padx=20,pady=5,bd='4',command=lambda:press(4),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn4.place(x=25,y=240)

btn3=Button(window,text='3',padx=20,pady=5,bd='4',command=lambda:press(3),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn3.place(x=155,y=290)


btn_2=Button(window,text='2',padx=20,pady=5,bd='4',command=lambda:press(2),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_2.place(x=90,y=290)

btn_1=Button(window,text='1',padx=20,pady=5,bd='4',command=lambda:press(1),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_1.place(x=25,y=290)

btn_zero=Button(window,text='0',padx=20,pady=5,bd='4',command=lambda:press(0),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_zero.place(x=90,y=340)


btn_percentage=Button(window,text='%',padx=18,pady=5,bd='4',bg='#deeded',command=lambda:percentage(),activebackground='#B2B2B3',activeforeground='white')
btn_percentage.place(x=25,y=340)



btn_point=Button(window,text='.',padx=22,pady=5,bd='4',command=lambda:press('.'),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_point.place(x=155,y=340)

btn_minus=Button(window,text='-',padx=20,pady=5,bd='4',command=lambda:press('-'),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_minus.place(x=220,y=190)


btn_plus=Button(window,text='+',padx=18,pady=5,bd='4',command=lambda:press('+'),bg='#deeded',activebackground='#B2B2B3',activeforeground='white')
btn_plus.place(x=220,y=240)

btn_equal=Button(window,text='=',bg='#CD0000',fg='white',padx=17,pady=30,bd='4',command=lambda:equal_press(),activebackground='#991521',activeforeground='black')
btn_equal.place(x=220,y=290)

window.resizable(0,0)
window.mainloop() 







