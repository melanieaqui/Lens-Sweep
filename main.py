from tkinter import*
from Cell import Cell
import settings

root = Tk()

#background color
root.configure(bg='black')
root.geometry('470x430')
root.title("Sweeper Lens")
root.resizable(False,False)
top_frame=Frame(
    root, 
    bg='black',
    width=100,
    height = 100)
top_frame.place(x=0, y=0)

game_frame = Frame(
    root,
    bg= 'white',
    width =500,
    height = 500
)

game_frame.place(x=10, y= 10)

for i in range (settings.GRID_SIZE):
    for j in range (settings.GRID_SIZE):
        c = Cell(i,j)
        c.create_btn_object(game_frame)
        c.cell_btn_object.grid(column = i, row = j)
        
Cell.randomize_mines()
# run the window

root.mainloop()
