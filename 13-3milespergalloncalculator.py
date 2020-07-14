import tkinter


class MilesPerGallonCalc:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame1 = tkinter.Frame()
        self.middle_frame2 = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallons = tkinter.Label(
            self.top_frame, text='Enter the number of gallons of gas:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        self.gallons.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles = tkinter.Label(
            self.middle_frame1,
            text='Enter the number of miles you will be driving:')
        self.miles_entry = tkinter.Entry(self.middle_frame1, width=10)
        self.miles.pack(side='left')
        self.miles_entry.pack(side='left')

        self.desc_label = tkinter.Label(self.middle_frame2,
                                        text='MPG calculated:')
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.middle_frame2,
                                       textvariable=self.value)
        self.desc_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.calc_button = tkinter.Button(
            self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame1.pack()
        self.middle_frame2.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        gallons = float(self.gallons_entry.get())

        miles = float(self.miles_entry.get())

        mpg = miles / gallons

        self.value.set(mpg)


MilesPerGallonCalc()
