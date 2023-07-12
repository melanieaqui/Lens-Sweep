from tkinter import*;
from Cell import Cell
root = Tk()

#background color
root.configure(bg='black')
root.geometry('1000x600')
root.title("Minesweeper")
root.resizable(False,False)
top_frame=Frame(
    root, 
    bg='black',
    width=1000,
    height = 100)
top_frame.place(x=0, y=0)

game_frame = Frame(
    root,
    bg= 'white',
    width =1000,
    height = 560
)

game_frame.place(x=0, y= 100)

c1 = Cell()
c1.create_btn_object(game_frame)

# run the window
root.mainloop()