import tkinter as tk
from tkinter import ttk
from widgets import Element, Key, Demo
from load    import main_layout, sec_layout, elements, types

root = tk.Tk()
root.title('Periodic Table')

# Frame for entire table
table = tk.Frame(root)
table.pack()

# Frame for main elements of table
main_tab = tk.Frame(table)
main_tab.pack()

# Frame for the key of the table
key_tab = ttk.LabelFrame(main_tab,text='Legend')
key_tab.grid(row=0,column=0,columnspan=10,rowspan=3)

# Frame for the demo widget
repr_tab = ttk.Frame(main_tab)
repr_tab.grid(row=0,column=5,columnspan=10,rowspan=3)

# Frame for secondary elements
sec_tab = tk.Frame(table)
sec_tab.pack()

# Heading
tk.Label(main_tab,text='Periodic Table',font=(0,21,'bold')).grid(row=0,column=3,columnspan=10)

# Loop through layout and place elements in the reserved locations
count = 0
for p,i in enumerate(main_layout):
    for q,j in enumerate(i):
        text = elements[count]
        if j:
            # For lanthides in between main table
            if 56 <= count <= 70:
                if count == 56:
                    text = '*'
                else:
                    count = 71
                    text = elements[count]
            
            # For actinoids in between main table
            elif 88 <= count <= 103:
                if count == 88:
                    text = '**'
                else:
                    count = 103
                    text = elements[count]
            
            Element(main_tab,element=text).grid(row=p,column=q,padx=2,pady=2)
            count += 1

# Loop through secondary layout and place elements in the reserved locations
count = 56 # Start position of lantinides
for p,i in enumerate(sec_layout):
    for q,j in enumerate(i):
        text = elements[count]
        # For Actinoids
        if count >= 71:
            text = elements[count+17]
        Element(sec_tab,element=text).grid(row=p,column=q,padx=2,pady=2)
        count += 1

# Placing the legend in 3x4 grid
for i in range(3):
    for j in range(4):
        if 4*i+j < len(types):
            Key(key_tab,e_type=types[4*i+j]).grid(row=i+1,column=j,sticky='w',padx=5,pady=5)

# Placing the representation in the frame
Demo(repr_tab, elements[0]).grid(row=i,column=j+1,rowspan=5)

root.mainloop()