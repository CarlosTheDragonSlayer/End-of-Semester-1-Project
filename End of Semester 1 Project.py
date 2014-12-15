
from Tkinter import *
from tkMessageBox import *


class Calculator(Frame):

    
    def frame(this, side): 
        w = Frame(this)
        w.pack(side=side, expand=YES, fill=BOTH)
        return w

    def button(this, root, side, text, command=None): 
        w = Button(root, text=text, command=command) 
        w.pack(side=side, expand=YES, fill=BOTH)
        return w

    need_clr = False
    def digit(self, digit):
        if self.need_clr:
            self.display.set('')
            self.need_clr = False
        self.display.set(self.display.get() + digit)

    def sign(self):
        need_clr = False
        cont = self.display.get()
        if len(cont) > 0 and cont[0] == '-':
            self.display.set(cont[1:])
        else:
            self.display.set('-' + cont)

 
    def decimal(self):
        self.need_clr = False
        cont = self.display.get()
        lastsp = cont.rfind(' ')
        if lastsp == -1:
            lastsp = 0
        if cont.find('.',lastsp) == -1:
            self.display.set(cont + '.')

  
    def oper(self, op):
        self.display.set(self.display.get() + ' ' + op + ' ')
        self.need_clr = False

   
    def calc(self):
        try:
            self.display.set(`eval(self.display.get())`)
            self.need_clr = True
        except:
            showerror('Operation Error', 'Illegal Operation')
            self.display.set('')
            self.need_clr = False

    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Verdana 12 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')

 
        self.display = StringVar()
        e = Entry(self, relief=SUNKEN, textvariable=self.display)
        e.pack(side=TOP, expand=YES, fill=BOTH)

        
        for key in ("123", "456", "789"):
            keyF = self.frame(TOP)
            for char in key:
                self.button(keyF, LEFT, char,
                            lambda c=char: self.digit(c))

        keyF = self.frame(TOP)
        self.button(keyF, LEFT, '-', self.sign)
        self.button(keyF, LEFT, '0', lambda ch='0': self.digit(ch))
        self.button(keyF, LEFT, '.', self.decimal)


        opsF = self.frame(TOP)
        for char in "+-*/=":
            if char == '=':
                btn = self.button(opsF, LEFT, char, self.calc)
            else:
                btn = self.button(opsF, LEFT, char, 
                                  lambda w=self, s=char: w.oper(s))

        # Clear button.
        clearF = self.frame(BOTTOM)
        self.button(clearF, LEFT, 'Clr', lambda w=self.display: w.set(''))


if __name__ == '__main__':
    Calculator().mainloop()


