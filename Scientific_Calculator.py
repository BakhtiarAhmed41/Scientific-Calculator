-----------------------------------------------#  Scientific Calculator created with Tkinter Library of Python  #------------------------------------------------------


from tkinter import *
import math


root = Tk()
root.geometry("800x400")
root.title("Scientific Calculator")
root.configure(background = 'light grey')

Cal_F = Frame(root)
Cal_F.pack(side=TOP)

text_Input = StringVar()


def do_backspace():
    get = str(text_Input.get())
    get_a = get[:-1]
    text_Input.set(get_a)


def btnClick(numbers):
    operator = text_Input.get() + str(numbers)
    # global operator
    # operator = operator + str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def btnEquals():
    operator = str(text_Input.get())
    if "√" in operator:
        sumup = str(eval(operator.replace("√", "math.sqrt")))
        text_Input.set(sumup)
    if "π" in operator:
        sumup = str(eval(operator.replace("π", "math.pi")))
        text_Input.set(sumup)
    if "℮" in operator:
        sumup = str(eval(operator.replace("℮", "math.exp(1)")))
        text_Input.set(sumup)
    if "²" in operator:
        sumup = str(eval(operator.replace("²", "**2")))
        text_Input.set(sumup)
    if "³" in operator:
        sumup = str(eval(operator.replace("³", "**3")))
        text_Input.set(sumup)
    if "sin" in operator:
        sumup = str(eval(operator.replace("sin", "math.sin")))
        text_Input.set(sumup)
    if "cos" in operator:
        sumup = str(eval(operator.replace("cos", "math.cos")))
        text_Input.set(sumup)
    if "tan" in operator:
        sumup = str(eval(operator.replace("tan", "math.tan")))
        text_Input.set(sumup)
    if "mod" in operator:
        sumup = str(eval(operator.replace("mod", "%")))
        text_Input.set(sumup)
    else:
        sumup = str(eval(operator))
        text_Input.set(sumup)


txtDisplay = Entry(Cal_F, width=50, bg='white', bd=4, font=('arial', 18), justify=RIGHT,
                   textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=5, pady=1)


btnbrac1 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='(',
                  bg='gray51', command=lambda: btnClick("(")).grid(row=2, column=0)
btnbrac2 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text=')',
                  bg='gray51', command=lambda: btnClick(")")).grid(row=2, column=1)
btnmod = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='mod',
                bg='gray51', command=lambda: btnClick("mod")).grid(row=2, column=2)
btnClear = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='C',
                  bg='gray51', command=btnClear).grid(row=2, column=3)
btnbckspc = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='<<<',
                   bg='gray51', command=do_backspace).grid(row=2, column=4)



btnsqr = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='x²',
              bg='Light blue', command=lambda: btnClick("²")).grid(row=3, column=0)
btncube = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='x³',
              bg='Light blue', command=lambda: btnClick("³")).grid(row=3, column=1)
btnexp = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='℮',
              bg='Light blue', command=lambda: btnClick("℮")).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='n!',
                bg='Light blue', command=lambda: btnClick('fact(')).grid(row=3, column=3)
btndivide = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='/',
                bg='Light blue', command=lambda: btnClick('/')).grid(row=3, column=4)


btnsqrt = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='√',
                 bg='Light Blue', command=lambda: btnClick("√(")).grid(row=4, column=0)
btn7 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='7',
              bg='Light Blue', command=lambda: btnClick(7)).grid(row=4, column=1)
btn8 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='8',
              bg='Light Blue', command=lambda: btnClick(8)).grid(row=4, column=2)
btn9 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='9',
                  bg='Light Blue', command=lambda: btnClick(9)).grid(row=4, column=3)
btnmultiply = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='*',
                  bg='Light Blue', command=lambda: btnClick("*")).grid(row=4, column=4)



btnsin = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='sin',
              bg='Sky blue3', command=lambda: btnClick("sin(")).grid(row=5, column=0)
btn4 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='4',
              bg='Sky blue3', command=lambda: btnClick(4)).grid(row=5, column=1)
btn5 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='5',
              bg='Sky blue3', command=lambda: btnClick(5)).grid(row=5, column=2)
btn6 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='6',
                  bg='Sky blue3', command=lambda: btnClick(6)).grid(row=5, column=3)
btnsub = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='-',
                  bg='Sky blue3', command=lambda: btnClick("-")).grid(row=5, column=4)


btncos = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='cos',
              bg='Sky Blue2', command=lambda: btnClick("cos(")).grid(row=6, column=0)
btn1 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='1',
              bg='Sky Blue2', command=lambda: btnClick(1)).grid(row=6, column=1)
btn2 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='2',
              bg='Sky Blue2', command=lambda: btnClick(2)).grid(row=6, column=2)
btn3 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='3',
                  bg='Sky Blue2', command=lambda: btnClick(3)).grid(row=6, column=3)
btnadd = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='+',
                  bg='Sky Blue2', command=lambda: btnClick("+")).grid(row=6, column=4)


btntan = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='tan',
              bg='Sky blue', command=lambda: btnClick("tan(")).grid(row=7, column=0)
btndec = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='.',
              bg='Sky blue', command=lambda: btnClick(".")).grid(row=7, column=1)
btn0 = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='0',
              bg='Sky blue', command=lambda: btnClick(0)).grid(row=7, column=2)
btnpi = Button(Cal_F, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), width=7, text='π',
             bg='Sky blue', command=lambda: btnClick("π")).grid(row=7, column=3)
btnequal = Button(Cal_F, padx=16, pady=1, bd=4, fg='white', font=('arial', 16, 'bold'), width=7, text='=',
                  bg='black', command=btnEquals).grid(row=7, column=4)

root.mainloop()
