import tkinter
import tkinter.messagebox


class joesAutomotive:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.oil_change = tkinter.IntVar()
        self.lube_job = tkinter.IntVar()
        self.radiator_flush = tkinter.IntVar()
        self.transmission_flush = tkinter.IntVar()
        self.inspection = tkinter.IntVar()
        self.muffler_replacement = tkinter.IntVar()
        self.tire_rotation = tkinter.IntVar()

        self.oil_change.set(0)
        self.lube_job.set(0)
        self.radiator_flush.set(0)
        self.transmission_flush.set(0)
        self.inspection.set(0)
        self.muffler_replacement.set(0)
        self.tire_rotation.set(0)

        self.cb_var1 = tkinter.Checkbutton(
            self.top_frame, text='Oil change--$30.00', variable=self.oil_change,
            onvalue=30, offvalue=0)
        self.cb_var2 = tkinter.Checkbutton(
            self.top_frame, text='Lube job--$20.00', variable=self.lube_job,
            onvalue=20, offvalue=0)
        self.cb_var3 = tkinter.Checkbutton(
            self.top_frame, text='Radiator flush--$40.00',
            variable=self.radiator_flush, onvalue=40, offvalue=0)
        self.cb_var4 = tkinter.Checkbutton(
            self.top_frame, text='Transmission flush--$100.00',
            variable=self.transmission_flush, onvalue=100, offvalue=0)
        self.cb_var5 = tkinter.Checkbutton(
            self.top_frame, text='Inspection--$35.00', variable=self.inspection,
            onvalue=35, offvalue=0)
        self.cb_var6 = tkinter.Checkbutton(
            self.top_frame, text='Muffler replacement--$200.00',
            variable=self.muffler_replacement, onvalue=200, offvalue=0)
        self.cb_var7 = tkinter.Checkbutton(
            self.top_frame, text='Tire rotation--$20.00',
            variable=self.tire_rotation, onvalue=20, offvalue=0)

        self.cb_var1.pack()
        self.cb_var2.pack()
        self.cb_var3.pack()
        self.cb_var4.pack()
        self.cb_var5.pack()
        self.cb_var6.pack()
        self.cb_var7.pack()

        self.calc_button = tkinter.Button(
            self.bottom_frame, text='Calculate', command=self.calc_total)
        self.quit_button = tkinter.Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_total(self):
        self.message = 'Your total amount: '
        total = self.oil_change.get() + self.lube_job.get() + \
                self.radiator_flush.get() + self.transmission_flush.get() + \
                self.inspection.get() + self.muffler_replacement.get() + \
                self.tire_rotation.get()

        self.total_amount = format(float(total), ",.2f")

        tkinter.messagebox.showinfo('Total Amount: $', self.total_amount)


joesAutomotive()
