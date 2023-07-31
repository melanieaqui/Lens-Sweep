#Lens Sweep by Team Sweepers
    #Aquino, Melanie
    #Plopino, Cyrus
from tkinter import*
from Cell import Cell
import settings
from PIL import Image,ImageTk

root = Tk()

#background color
root.configure(bg='#1A1825')
root.geometry('479x479')
root.title("Lens Sweep")
root.resizable(False,False)
top_frame=Frame(
    root, 
    bg='black',
    width=100,
    height = 100)
top_frame.place(x=0, y=0)

game_frame = Frame(
    root,
    bg= '#BE5A04',
    width =500,
    height = 500,
)

game_frame.place(x=10, y= 10)

#icons
logo = ImageTk.PhotoImage(Image.open("LoL_icon.png").resize((30,30)))
teemo = ImageTk.PhotoImage(Image.open("Teemo_Mushroom_Trap_Render.png").resize((30,30)))
ward = ImageTk.PhotoImage(Image.open("warded.png").resize((30,30)))

#create button object that will represent the cells   
for i in range (settings.GRID_SIZE):
    for j in range (settings.GRID_SIZE):
        c = Cell(i,j)
        c.create_btn_object(game_frame,logo, teemo, ward,root)
        c.cell_btn_object.grid(column = i, row = j)
        
Cell.randomize_mines()

# run the window
root.mainloop()
