import tkinter as tk

import PIL
import pyttsx3
from PIL import ImageTk, Image
import random


class App_Sber(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = None
        self.geometry("1500x900")
        self.configure(background="White")

        image_1 = PIL.Image.open("images/img_1.png")
        photo = PIL.ImageTk.PhotoImage(image_1)

        label_image_1 = tk.Label(self, image=photo)
        label_image_1.image = photo
        label_image_1.pack()

        self.engine = pyttsx3.init()

        self.queue_label = tk.Label(self, text="Очередь:", font=10)
        self.queue_listbox = tk.Listbox(self, font=10)
        self.call_button = tk.Button(self, text="Следующий", command=self.call_next, font=10)
        self.ticket_label = tk.Label(self, text="Ваш билет:", font=10)
        self.ticket_number_label = tk.Label(self, text="", font=10)
        self.your_ticket = tk.Label(self, text="В связи с недостатком бумаги, сфотографируйте билет и QR", font=10)
        self.get_ticket_button = tk.Button(self, text="Получить билет", command=self.get_ticket, font=10)

        self.curr_client_label_exp = tk.Label(self, text="Обслуживается", font=40)
        self.curr_client_label = tk.Label(self, text="", font=40)
        self.curr_client_label_exp.place(x=200, y=350)
        self.curr_client_label.place(x=200, y=400)

        self.queue_label.pack()
        self.queue_listbox.pack()
        self.call_button.pack()
        self.ticket_label.pack()
        self.ticket_number_label.pack()
        self.your_ticket.pack()
        self.get_ticket_button.pack()

        self.is_started = False
        self.is_init = False
        self.click = ""
        self.newWindow = None

    def call_next(self):
        if self.queue_listbox.size() != 0:
            a = random.randint(0, self.queue_listbox.size() - 1)
            self.engine.say(f"{self.queue_listbox.get(a)}, приготовьтесь")
            self.curr_client_label.configure(text=f"{self.queue_listbox.get(a)}")
            self.queue_listbox.delete(a)
            if a % 2 == 0 and self.queue_listbox.size() >= 2:
                self.queue_listbox.delete(a + 1)
            self.engine.runAndWait()

    def click1(self):
        self.click = "A"

    def click2(self):
        self.click = "B"

    def click3(self):
        self.click = "C"

    def click4(self):
        self.click = "D"

    def click5(self):
        self.click = "E"

    def click6(self):
        self.click = "F"

    def click7(self):
        self.click = "G"

    def get_ticket(self):
        self.grab_set()

        self.newWindow = tk.Toplevel(self)
        self.newWindow.geometry("1000x1000")
        label = tk.Label(self.newWindow, text="Выберите цель посещения", font=30)
        button1 = tk.Button(self.newWindow, text="Мне только спросить", font=30, command=self.click1)
        button2 = tk.Button(self.newWindow, text="Я не из этой группы", font=30, command=self.click2)
        button3 = tk.Button(self.newWindow, text="У меня эпик", font=30, command=self.click3)
        button4 = tk.Button(self.newWindow, text="У меня локальная задача", font=30, command=self.click4)
        button5 = tk.Button(self.newWindow, text="Мне только сдать аттестацию", font=30, command=self.click5)
        button6 = tk.Button(self.newWindow, text="Хочу сдать зачет", font=30, command=self.click6)

        image_2 = PIL.Image.open("images/volk.jpg")
        photo = PIL.ImageTk.PhotoImage(image_2)

        label_image_2 = tk.Label(self.newWindow, image=photo)
        label_image_2.image = photo
        label_image_2.pack()

        label.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()

        self.newWindow.wait_window()

        self.grab_release()

        ticket_number = random.randint(1, 100)
        if self.queue_listbox.size() != 0:
            a = random.randint(0, self.queue_listbox.size())
        else:
            a = 0
        self.queue_listbox.insert(a, f"Клиент {self.click + str(ticket_number)}")

        self.ticket_number_label.configure(text=f"{self.click + str(ticket_number)}")

        if not self.is_started:
            self.img = ImageTk.PhotoImage(Image.open("images/qr_photo.png"))
            tk.Label(self, image=self.img).pack()
            self.is_started = True

        if self.queue_listbox.size() == 1 and not self.is_init:
            self.is_init = True
            self.start_timer()

    def start_timer(self):

        if len(self.queue_listbox.get(0, tk.END)) == 1:
            self.call_next()
        else:
            self.after(1, self.call_next)
        self.after(30000, self.start_timer)


if __name__ == '__main__':
    app = App_Sber()
    app.mainloop()
