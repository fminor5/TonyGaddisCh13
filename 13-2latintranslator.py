import tkinter


class latinTranslator():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.label1 = tkinter.Label(
            self.top_frame, text='sinister').pack(side='left')

        self.value1 = tkinter.StringVar()

        self.translate1 = tkinter.Button(
            self.top_frame, text='Translate', command=self.translate1).pack(
            side='left')

        self.translate_label1 = tkinter.Label(
            self.top_frame, textvariable=self.value1).pack(side='left')

        self.label2 = tkinter.Label(
            self.middle_frame, text='dexter').pack(side='left')

        self.value2 = tkinter.StringVar()

        self.translate2 = tkinter.Button(
            self.middle_frame, text='Translate',
            command=self.translate2).pack(side='left')

        self.translate_label2 = tkinter.Label(
            self.middle_frame, textvariable=self.value2).pack(side='left')

        self.label3 = tkinter.Label(
            self.bottom_frame, text='medium').pack(side='left')

        self.value3 = tkinter.StringVar()

        self.translate3 = tkinter.Button(
            self.bottom_frame, text='Translate',
            command=self.translate3).pack(side='left')

        self.translate_label3 = tkinter.Label(
            self.bottom_frame, textvariable=self.value3).pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def translate1(self):
        self.text = 'left'

        self.value1.set(self.text)

    def translate2(self):
        self.text = 'right'

        self.value2.set(self.text)

    def translate3(self):
        self.text = 'center'

        self.value3.set(self.text)


latinTranslator()
