import tkinter as tk
import webbrowser
from load import read, color_dict

class Element(tk.Frame):
    def __init__(self,master,element,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        
        if not element.startswith('*'):
            data   = read(element).values.tolist()
            symbol = data[0]
            at_no  = data[1]
            at_ms  = data[2]
            e_type = data[3]
            wiki   = data[4]
            color  = self.find_color(e_type)
            
            tk.Label(self,text=at_no,font=(0,10),bg=color,takefocus=0).pack(anchor='w')
            tk.Label(self,text=symbol,font=(0,18,'bold'),bg=color,fg='white',takefocus=0).pack()
            tk.Label(self,text=element,font=(0,9),bg=color,takefocus=0).pack()
            tk.Label(self,text=at_ms,font=(0,7),bg=color,takefocus=0).pack()

            self.bind('<Double-1>',lambda e: webbrowser.open(wiki))
            for wid in self.children:
                self.children.get(wid).bind('<Double-1>',lambda e: webbrowser.open(wiki))
            
        else:
            if element == '*':
                text  = 'Lanthanide'
                color = self.find_color(text)   
                
            else:
                text  = 'Actinide'
                color = self.find_color(text)   
            
            tk.Label(self,text=text,bg=color,font=(0,9)).pack(fill="both",expand=1)
            tk.Label(self,text='89-103',font=(0,18,'bold'),bg=color,fg='white').pack(fill="both",expand=1)
            tk.Label(self,text='(Check below)',bg=color,font=(0,8)).pack(fill="both",expand=1)
                
        self['bg'] = color
        self.config(width=100)
        self.config(height=105)
        self.pack_propagate(0)

    def find_color(self,e_type):
        return color_dict[e_type]

class Key(Element):
    def __init__(self,master,e_type,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)

        color = self.find_color(e_type)
        psuedo_img = tk.PhotoImage(height=1,width=1)
        
        tk.Label(self,image=psuedo_img,bg=color,height=15,width=15).pack(side='left')
        tk.Label(self,text=e_type).pack()

class Demo(tk.Frame):
    def __init__(self,master,e_type,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        self['width'] = 500
        self['height'] = 150
        
        cnv = tk.Canvas(self)
        cnv.pack()

        wid = Element(self,element=e_type)
        cnv.create_window(250,100,window=wid,tags='win')

        x,y,x1,y1 = 150,60,200,60
        cnv.create_line(x    ,y   ,x1    ,y1   ,arrow='last',tags='arrow')
        cnv.create_line(x+150,y+40,x+200 ,y1+40,arrow='first',tags='arrow')
        cnv.create_line(x    ,y+65,x1    ,y1+65,arrow='last',tags='arrow')
        cnv.create_line(x+150,y+85,x+200 ,y1+85,arrow='first',tags='arrow')

        cnv.create_text(40,47,text='Atomic Number',anchor='nw')
        cnv.create_text(355,90,text='Symbol',anchor='nw')
        cnv.create_text(93,115,text='Element',anchor='nw')
        cnv.create_text(355,132,text='Atomic Mass',anchor='nw')

        self.pack_propagate(0)

if __name__ == '__main__':
    root = tk.Tk()

    Element(root,'Hydrogen').pack(padx=5,pady=20)
    Key(root,e_type='Halogen').pack()
    Demo(root,'Hydrogen').pack()
    
    root.mainloop()