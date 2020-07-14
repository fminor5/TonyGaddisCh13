import tkinter


class CelsiustoFahrenheit:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.celsius_label = tkinter.Label(
            self.top_frame, text='Enter a Celsius temperature: ')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)

        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        self.descr_label = tkinter.Label(
            self.middle_frame, text='Converted to Fahrenheit:')
        self.value = tkinter.StringVar()
        self.fahrenheit_label = tkinter.Label(
            self.middle_frame, textvariable=self.value)

        self.descr_label.pack(side='left')
        self.fahrenheit_label.pack(side='left')

        self.convert_button = tkinter.Button(
            self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        celsius = float(self.celsius_entry.get())

        fahrenheit = (9 / 5) * celsius + 32

        self.value.set(fahrenheit)


CelsiustoFahrenheit()
