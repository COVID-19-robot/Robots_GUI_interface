import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


LARGE_FONT= ("Bookman Old Style", 15, 'bold')


class ServiceRobot(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        logo = Image.open("hsrlogo.png")
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo, bg="white")
        logo_label.Image = logo
        logo_label.pack()

        tk.Frame.__init__(self,parent, bg="white")
        label = tk.Label(self, text="HOME PAGE", font=LARGE_FONT, bg="white")
        label.pack(pady=10,padx=10)

        instructions = tk.Label(self, text="Welcome to the medicine dispensing hospital service robot interface. This is an \n interactive platform that allows isolation ward patients to receive their \n prescriptions from the robot. Nurses can also perform their administrative \n tasks such as loading prescriptions through the robot. Kindly select whether you \n are a patient or a nurse below.\n", font=LARGE_FONT, bg="white")
        instructions.pack()

        button = tk.Button(self, text="PATIENT", font=LARGE_FONT, padx='50', pady='8',
                            command=lambda: controller.show_frame(PageOne))
        button.pack(side='left')

        button2 = tk.Button(self, text="NURSE", font=LARGE_FONT, padx='50', pady='8',
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side='right')


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        label = tk.Label(self, text="MEDICATION DISPENSING", font=LARGE_FONT, bg="white")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        label = tk.Label(self, text="PATIENT PRESCRIPTION", font=LARGE_FONT, bg="white")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = ServiceRobot()
app.mainloop()
