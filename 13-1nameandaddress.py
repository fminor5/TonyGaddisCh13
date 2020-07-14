import tkinter


class NameandAddress():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.address = tkinter.StringVar()

        self.address_label = tkinter.Label(
            self.top_frame, textvariable=self.address)

        self.address_label.pack()

        self.show_info = tkinter.Button(
            self.bottom_frame, text='Show Info', command=self.show_info)
        self.quit = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.show_info.pack(side='left')
        self.quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        self.text = 'Javier Duarte \n 274 Baily Drive \n Waynesville, NC 27999'

        self.address.set(self.text)


NameandAddress()