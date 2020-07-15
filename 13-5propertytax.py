import tkinter


class propertyTax:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame1 = tkinter.Frame()
        self.middle_frame2 = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.value_label = tkinter.Label(
            self.top_frame, text='Enter the actual value of your property')
        self.value_entry = tkinter.Entry(self.top_frame, width=10)

        self.value_label.pack(side='left')
        self.value_entry.pack(side='left')

        self.desc_label = tkinter.Label(
            self.middle_frame1, text='The assessment value is:')
        self.value = tkinter.StringVar()
        self.assessment_label = tkinter.Label(
            self.middle_frame1, textvariable=self.value)

        self.desc_label.pack(side='left')
        self.assessment_label.pack(side='left')

        self.desc_label2 = tkinter.Label(
            self.middle_frame2, text='The property tax is')
        self.value2 = tkinter.StringVar()
        self.tax_value = tkinter.Label(
            self.middle_frame2, textvariable=self.value2)

        self.desc_label2.pack(side='left')
        self.tax_value.pack(side='left')

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
        value = float(self.value_entry.get())

        assessment_value = value * 0.6

        prop_tax = (assessment_value / 100) * 0.75

        self.value.set(assessment_value)
        self.value2.set(prop_tax)


propertyTax()
