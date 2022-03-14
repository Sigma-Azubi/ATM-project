from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(80 * blank_space + "SIGMABANK ATM")
        self.root.geometry("640x650+220+0")
        self.root.configure(background = 'gainsboro')

# # =======================================FRAMES================================================

        MainFrame = Frame(self.root, bd = 20, width = 740, height = 700, relief = RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd = 7, width = 734, height = 300, relief = RIDGE)
        TopFrame1.grid(row = 1, column = 0, padx = 8)

        TopFrame2 = Frame(MainFrame, bd = 7, width = 730, height = 300, relief = RIDGE)
        TopFrame2.grid(row = 0, column = 0, padx = 8)

        TopFrame2Left = Frame(TopFrame2, bd = 5, width = 190, height = 300, relief = RIDGE)
        TopFrame2Left.grid(row = 0, column = 0, padx = 3)

        TopFrame2Mid = Frame(TopFrame2, bd = 5, width = 200, height = 300, relief = RIDGE)
        TopFrame2Mid.grid(row = 0, column = 1, padx = 3)

        TopFrame2Right = Frame(TopFrame2, bd = 5, width = 190, height = 300, relief = RIDGE)
        TopFrame2Right.grid(row = 0, column = 2, padx = 3)

#=============================================FUNCTIONS===================================================
        def enter_Pin():
                pinNo = self.txtReceipt.get("1.0", "end-1c")
                if ((pinNo == str("1234")) or (pinNo == str("5678")) or (pinNo == str("9012"))):
                        self.txtReceipt.delete("1.0", END)

                        self.txtReceipt.insert(END, '\t\tSIGMABANK ATM' + "\n\n\n")
                        self.txtReceipt.insert(END, 'WITHDRAW\t\t\t\t LOAN' + "\n\n\n")
                        self.txtReceipt.insert(END, 'CASH WITH RECEIPT\t\t\t\t DEPOSIT' + "\n\n\n\n")
                        self.txtReceipt.insert(END, 'BALANCE\t\t\t REQUEST NEW PIN' + "\n\n\n\n")
                        self.txtReceipt.insert(END, 'MINI STATEMENT\t\t\t PRINT STATEMENT' + "\n\n\n")

                        self.btnArrowR1 = Button(TopFrame2Right, width = 90, height = 45, state = NORMAL, command = loan,
                        image = self.img_arrow_Right).grid(row = 0, column = 0, padx = 2, pady = 2)

                        self.btnArrowR2 = Button(TopFrame2Right, width = 90, height = 45, state = NORMAL, command = deposit,
                        image = self.img_arrow_Right).grid(row = 1, column = 0, padx = 2, pady = 2)

                        self.btnArrowR3 = Button(TopFrame2Right, width = 90, height = 45, state = NORMAL, command = request_new_pin,
                        image = self.img_arrow_Right).grid(row = 2, column = 0, padx = 2, pady = 2)

                        self.btnArrowR4 = Button(TopFrame2Right, width = 90, height = 45, state = NORMAL, command = statement,
                        image = self.img_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)

                        #=========================================================================

                        self.btnArrowL1 = Button(TopFrame2Left, width = 90, height = 45, state = NORMAL, command = withdrawcash,
                        image = self.img_arrow_Left).grid(row = 0, column = 0, padx = 2, pady = 2)

                        self.btnArrowL2 = Button(TopFrame2Left, width = 90, height = 45, state = NORMAL,
                        image = self.img_arrow_Left).grid(row = 1, column = 0, padx = 2, pady = 2)

                        self.btnArrowL3 = Button(TopFrame2Left, width = 90, height = 45, state = NORMAL, command = balance,
                        image = self.img_arrow_Left).grid(row = 2, column = 0, padx = 2, pady = 2)

                        self.btnArrowL4 = Button(TopFrame2Left, width = 90, height = 45, state = NORMAL, command = statement, 
                        image = self.img_arrow_Left).grid(row = 3, column = 0, padx = 2, pady = 2)
                else:
                        self.txtReceipt.delete("1.0", END)
                        self.txtReceipt.insert(END, 'INVALID PIN!' + "\n\n")

        def clear():
                self.txtReceipt.delete("1.0", END)
                self.btnArrowL1 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Left).grid(row = 0, column = 0, padx = 2, pady = 2)

                self.btnArrowL2 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Left).grid(row = 1, column = 0, padx = 2, pady = 2)

                self.btnArrowL3 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Left).grid(row = 2, column = 0, padx = 2, pady = 2)

                self.btnArrowL4 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Left).grid(row = 3, column = 0, padx = 2, pady = 2)

                #======================================================================================

                self.btnArrowR1 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, command = loan,
                image = self.img_arrow_Right).grid(row = 0, column = 0, padx = 2, pady = 2)

                self.btnArrowR2 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 1, column = 0, padx = 2, pady = 2)

                self.btnArrowR3 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 2, column = 0, padx = 2, pady = 2)

                self.btnArrowR4 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)

        #==========================================KEYS FUNCTIONING=====================================
        def insert0():
                value0 = 0
                self.txtReceipt.insert(END, value0)

        def insert1():
                value1 = 1
                self.txtReceipt.insert(END, value1)

        def insert2():
                value2 = 2
                self.txtReceipt.insert(END, value2)

        def insert3():
                value3 = 3
                self.txtReceipt.insert(END, value3)

        def insert4():
                value4 = 4
                self.txtReceipt.insert(END, value4)

        def insert5():
                value5 = 5
                self.txtReceipt.insert(END, value5)

        def insert6():
                value6 = 6
                self.txtReceipt.insert(END, value6)

        def insert7():
                value7 = 7
                self.txtReceipt.insert(END, value7)

        def insert8():
                value8 = 8
                self.txtReceipt.insert(END, value8)

        def insert9():
                value9 = 9
                self.txtReceipt.insert(END, value9)

        def cancel():
                Cancel = tkinter.messagebox.askyesno("SIGMABANK ATM", "Are You Sure You Want To Cancel The Process? ")
                if Cancel > 0:
                        self.root.destroy()
                        return

        #============================ATM TRANSACTIONS===================================================

        def withdrawcash():
                enter_Pin()
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.focus_set()

        def loan():
                enter_Pin()
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, "Loan $ ")
                self.txtReceipt.focus_set()

        def deposit():
                enter_Pin()
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.focus_set()

        def request_new_pin():
                enter_Pin()
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, "\t\tWELCOME TO SIGMABANK\n")
                self.txtReceipt.insert(END, "Your New Pin Will Be Sent To Your Email Address!\n")   
                self.txtReceipt.insert(END, 'WITHDRAW\t\t\t\t LOAN' + "\n\n\n")
                self.txtReceipt.insert(END, 'CASH WITH RECEIPT\t\t\t\t DEPOSIT' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'BALANCE\t\t\t REQUEST NEW PIN' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'MINI STATEMENT\t\t\t PRINT STATEMENT' + "\n\n\n")
                self.txtReceipt.insert(END, "\t\tTHANK YOU FOR BANKING WITH US!\n")

        def balance():
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, "\t\tWELCOME TO SIGMABANK\n")
                self.txtReceipt.insert(END, "$1296" + "\n")   
                self.txtReceipt.insert(END, 'WITHDRAW\t\t\t\t LOAN' + "\n\n\n")
                self.txtReceipt.insert(END, 'CASH WITH RECEIPT\t\t\t\t DEPOSIT' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'BALANCE\t\t\t REQUEST NEW PIN' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'MINI STATEMENT\t\t\t PRINT STATEMENT' + "\n\n\n")
                self.txtReceipt.insert(END, "\t\tTHANK YOU FOR BANKING WITH US!\n")

        def statement():
                pinNo1 = str(self.txtReceipt.get("1.0", "end-1c"))
                pinNo2 = str(pinNo1)
                pinNo3 = float(pinNo2)
                pinNo4 = float(1296 - (pinNo3))
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, "\n\t" + str(pinNo4) + "\t\t")
                self.txtReceipt.insert(END, "\t\t\t\n\n Account balance $" + str(pinNo4) + "\t\t\n\n")
                self.txtReceipt.insert(END, "Rent \t\t\t\$1200" + "\n\n")
                self.txtReceipt.insert(END, "Water bill \t\t\t\$79.4" + "\n\n")
                self.txtReceipt.insert(END, "Elec Power" + "s\t\t\t\$79.4" + "\n\n")
                self.txtReceipt.insert(END, "Student Loan" + "\t\t\t\$300" + "\n\n")
                self.txtReceipt.insert(END, "Fuel" + "\t\t\t\$80" + "\n\n")




        # #=============================================================================================

                self.img_arrow_Right = PhotoImage(file = "arrowR.png")

                self.btnArrowR1 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 0, column = 0, padx = 2, pady = 2)

                self.btnArrowR2 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 1, column = 0, padx = 2, pady = 2)

                self.btnArrowR3 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED,
                image = self.img_arrow_Right).grid(row = 2, column = 0, padx = 2, pady = 2)

                self.btnArrowR4 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, command = statement,
                image = self.img_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)



# #============================================WIDGETS====================================================

        self.txtReceipt = Text(TopFrame2Mid, height = 17, width = 42, bd = 12, font = ('arial', 9, 'bold'))
        self.txtReceipt.grid(row = 0, column = 0)

        self.img_arrow_Left = PhotoImage(file = "arrowL.png")

        self.btnArrowL1 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED, command = withdrawcash,
        image = self.img_arrow_Left).grid(row = 0, column = 0, padx = 2, pady = 2)

        self.btnArrowL2 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED,
        image = self.img_arrow_Left).grid(row = 1, column = 0, padx = 2, pady = 2)

        self.btnArrowL3 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED, command = balance,
        image = self.img_arrow_Left).grid(row = 2, column = 0, padx = 2, pady = 2)

        self.btnArrowL4 = Button(TopFrame2Left, width = 90, height = 45, state = DISABLED, command = statement,
        image = self.img_arrow_Left).grid(row = 3, column = 0, padx = 2, pady = 2)

# #=============================================================================================

        self.img_arrow_Right = PhotoImage(file = "arrowR.png")

        self.btnArrowR1 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, command = loan,
        image = self.img_arrow_Right).grid(row = 0, column = 0, padx = 2, pady = 2)

        self.btnArrowR2 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, command = deposit,
        image = self.img_arrow_Right).grid(row = 1, column = 0, padx = 2, pady = 2)

        self.btnArrowR3 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, command = request_new_pin,
        image = self.img_arrow_Right).grid(row = 2, column = 0, padx = 2, pady = 2)

        self.btnArrowR4 = Button(TopFrame2Right, width = 90, height = 45, state = DISABLED, 
        image = self.img_arrow_Right).grid(row = 3, column = 0, padx = 2, pady = 2)

# #========================================PIN NUMBER BUTTONS=================================

        self.img1 = PhotoImage(file = "one.png")
        self.btn1 = Button(TopFrame1, width = 75, height = 38, command = insert1,
        image = self.img1).grid(row = 2, column = 0, padx = 6, pady = 4)

        self.img2 = PhotoImage(file = "two.png")
        self.btn2 = Button(TopFrame1, width = 75, height = 38, command = insert2,
        image = self.img2).grid(row = 2, column = 1, padx = 6, pady = 4)

        self.img3 = PhotoImage(file = "three.png")
        self.btn3 = Button(TopFrame1, width = 75, height = 38, command = insert3,
        image = self.img3).grid(row = 2, column = 2, padx = 6, pady = 4)

        self.imgCE = PhotoImage(file = "cancel.png")
        self.btnCancel = Button(TopFrame1, width = 75, height = 38, command = cancel,
        image = self.imgCE).grid(row = 2, column = 3, padx = 6, pady = 4)

# #================================================================================================

        self.img4 = PhotoImage(file = "four.png")
        self.btn4 = Button(TopFrame1, width = 75, height = 38, command = insert4,
        image = self.img4).grid(row = 3, column = 0, padx = 6, pady = 4)

        self.img5 = PhotoImage(file = "five.png")
        self.btn5 = Button(TopFrame1, width = 75, height = 38, command = insert5,
        image = self.img5).grid(row = 3, column = 1, padx = 6, pady = 4)

        self.img6 = PhotoImage(file = "six.png")
        self.btn6 = Button(TopFrame1, width = 75, height = 38, command = insert6,
        image = self.img6).grid(row = 3, column = 2, padx = 6, pady = 4)

        self.imgCl = PhotoImage(file = "clear.png")
        self.btnClear = Button(TopFrame1, width = 75, height = 38, command = clear,
        image = self.imgCl).grid(row = 3, column = 3, padx = 6, pady = 4)

# #==============================================================================================

        self.img7 = PhotoImage(file = "seven.png")
        self.btn7 = Button(TopFrame1, width = 75, height = 38, command = insert7,
        image = self.img7).grid(row = 4, column = 0, padx = 6, pady = 4)

        self.img8 = PhotoImage(file = "eight.png")
        self.btn8 = Button(TopFrame1, width = 75, height = 38, command = insert8,
        image = self.img8).grid(row = 4, column = 1, padx = 6, pady = 4)

        self.img9 = PhotoImage(file = "nine.png")
        self.btn9 = Button(TopFrame1, width = 75, height = 38, command = insert9,
        image = self.img9).grid(row = 4, column = 2, padx = 6, pady = 4)

        self.imgEnter = PhotoImage(file = "enter.png")
        self.btnEnter = Button(TopFrame1, width = 75, height = 38, command = enter_Pin,
        image = self.imgEnter).grid(row = 4, column = 3, padx = 6, pady = 4)

# #==============================================================================================

        self.imgSp1 = PhotoImage(file = "empty.png")
        self.btnSp1 = Button(TopFrame1, width = 75, height = 38, 
        image = self.imgSp1).grid(row = 5, column = 0, padx = 6, pady = 4)

        self.img0 = PhotoImage(file = "zero.png")
        self.btn0 = Button(TopFrame1, width = 75, height = 38, command = insert0,
        image = self.img0).grid(row = 5, column = 1, padx = 6, pady = 4)

        self.imgSp2 = PhotoImage(file = "empty.png")
        self.btnSp2 = Button(TopFrame1, width = 75, height = 38, 
        image = self.imgSp2).grid(row = 5, column = 2, padx = 6, pady = 4)

        self.imgSp3 = PhotoImage(file = "empty.png")
        self.btnSp3 = Button(TopFrame1, width = 75, height = 38, 
        image = self.imgSp3).grid(row = 5, column = 3, padx = 6, pady = 4)

if __name__== '__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()