from tkinter import *


def meter_to_feet():
    meter = float(meter_input.get())
    feet = meter * 3.28084
    feet_output_label.config(text=f"{feet:.2f}")


window = Tk()
window.attributes('-topmost', True)
window.title("Meter to Feet Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


meter_input = Entry(width=7)
meter_input.insert(END, string="0")
meter_input.grid(column=1, row=0)

meter_label = Label(text="Meter")
meter_label.grid(column=2, row=0)
meter_label.config(pady=10)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(pady=10)

feet_output_label = Label(text="0")
feet_output_label.grid(column=1, row=1)

feet_label = Label(text="Feet")
feet_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=meter_to_feet)
calculate_button.grid(column=1, row=2)


window.mainloop()
