from tkinter import *

root = Tk()
root.title("โปรแกรมคำนวนพื้นที่วงกลม")

# การหาพื้นที่วงกลม
Label(text="รัศมี", font=30).grid(row=0, sticky=W)  # สรา้งข้อความ

radius = IntVar()  # ประกาศตัวแปรเพื่อรับข้อมูลเป็นตัวเลข
et1 = Entry(width=30, textvariable=radius, font=30)  # สรา้งกล่องเพื่อมารับข้อมูล
et1.grid(row=0, column=1)  # จัดรูปแบบ
Label(text="พื้นที่วงกลม", font=30).grid(row=1, sticky=W)
et2 = Entry(width=30, font=30)
et2.grid(row=1, column=1)


def caculate():  # เมื่อกดปุ่มคำนวนเเล้วให้เรียกใช้ฟังก์ชั่น
    et2.delete(0, END)  # ให้ล้างค่าเมื่อมีการคำนวนเสร็จเเล้วไม่ให้กดซ้ำได้
    r = radius.get()
    area = 3.14 * r * r
    et2.insert(0, area)


def deletetext():  # การล้างค่าออกจากโปรแกรม
    et1.delete(0, END)
    et2.delete(0, END)


btn1 = Button(text="คำนวน", command=caculate).grid(row=2, column=1, sticky=W)
btn1 = Button(text="ล้าง", command=deletetext).grid(row=2, column=1, sticky=E)
mainloop()