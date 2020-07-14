import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create two label widgets
        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window,
                                    text='This is my GUI program.')

        # Call both labels widgets pack method.
        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()


MyGUI()


