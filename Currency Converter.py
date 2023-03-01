from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

# input
money = IntVar()
Label(text="จำนวนเงิน(THB)", padx=10, font=30).grid(row=0, sticky=W)
et1 = Entry(font=30, width=30, textvariable=money)
et1.grid(row=0, column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน", padx=10, font=30).grid(row=1, sticky=W)
Combo = ttk.Combobox(width=30, font=30, textvariable=choice)
Combo["values"] = ("EUR", "JPY", "USD", "GBP")
Combo.grid(row=1, column=1)

# output
Label(text="ผลการคำนวน", padx=10, font=30).grid(row=2, sticky=W)
et2 = Entry(font=30, width=30)
et2.grid(row=2, column=1)


def calculate():
    amount = money.get()
    currency = choice.get()
    if currency == "EUR":
        et2.delete(0, END)
        result = "{:.2f} EUR(ยูโร)".format(amount * 0.026)
        et2.insert(0, result)
    elif currency == "JPY":
        et2.delete(0, END)
        result = "{:.2f} JPY(เยน)".format(amount * 3.91)
        et2.insert(0, result)
    elif currency == "USD":
        et2.delete(0, END)
        result = "{:.2f} USD(ดอลล่า)".format(amount * 0.030)
        et2.insert(0, result)
    elif currency == "GBP":
        et2.delete(0, END)
        result = "{:.2f} GBP(ปอนด์)".format(amount * 0.025)
        et2.insert(0, result)
    else:
        et2.delete(0, END)
        result = "ไม่พบข้อมูล"
        et2.insert(0, result)


Button(text="คำนวน", font=30, width=15, command=calculate).grid(row=3, column=1, sticky=W)
Button(text="ล้าง", font=30, width=15, command=lambda: (et1.delete(0, END), et2.delete(0, END))).grid(row=3, column=1, sticky=E)
root.mainloop()