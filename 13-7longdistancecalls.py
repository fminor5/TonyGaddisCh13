import tkinter
import tkinter.messagebox


class longDistanceCalls:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.radio_var = tkinter.DoubleVar() # For an Entry text field the value
                                             # must be an object of IntVar, DoubleVar
                                             # or StringVar which represents an
                                             # integer, float, or a string.
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame,
            text='Daytime (6:00 am through 5:59 pm): $0.07 per minute.',
            variable=self.radio_var, value=0.07)
        self.rb2 = tkinter.Radiobutton(
            self.top_frame,
            text='Evening (6:00 pm through 11:59 pm): $0.12 per minute.',
            variable=self.radio_var, value=0.12)
        self.rb3 = tkinter.Radiobutton(
            self.top_frame,
            text='Off-Peak (midnight through 5:59 am): $0.05 per minute.',
            variable=self.radio_var, value=0.05)

        self.number_minutes = tkinter.Label(
            self.top_frame, text='Enter the number of minutes:')
        self.minutes_entry = tkinter.Entry(self.top_frame, width=10)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.number_minutes.pack(side='left')
        self.minutes_entry.pack(side='left')

        self.calc_charge = tkinter.Button(
            self.bottom_frame, text='Calculate', command=self.total_charge)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_charge.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def total_charge(self):
        total_of_minutes = self.minutes_entry.get()
        #print(total_of_minutes)
        rate_category = self.radio_var.get()
        print(rate_category)
        charge_for_call = float(total_of_minutes) * float(rate_category)
        self.total = format(charge_for_call, '.2f')
        tkinter.messagebox.showinfo('Calculation', 'Your total charge is: $' +
                                    self.total)


longDistanceCalls()
