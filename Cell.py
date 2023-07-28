from tkinter import *
import settings
import random
import ctypes
import sys
from functools import partial


class Cell:
   # TEEMO_IMG = PhotoImage(file="Teemo_Mushroom_Trap_Render.png")

    mines = [] #Class variable to store mine cells
    all = []
    cell_count = 75
    cell_mines = settings.MINES_COUNT
    icon = None
    def __init__ (self,x,y,is_mine = False):

        self.is_mine = is_mine
        self.is_flagged = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
    
        Cell.all.append(self)
        

    def create_btn_object (self, location):
        btn = Button(
            location,
            width = 5,
            height =2,
           # image = icon

        )
        #left click
        btn.bind('<Button-1>',self.left_click)
        
        #right click
        btn.bind('<Button-3>',self.right_click)

        self.cell_btn_object = btn
        
    def right_click(self,e):
        
        self.is_flagged = not self.is_flagged  # Toggle the is_flagged attribute

        if self.is_flagged:
            self.cell_btn_object.configure(image=PhotoImage(file="Teemo_Mushroom_Trap_Render.png")) 
            self.cell_btn_object.image(file="Teemo_Mushroom_Trap_Render.png") # Display "F" for flagged cell
            if self.is_mine:
                #self.show_cell()
                Cell.cell_mines-= 1
                print(Cell.cell_mines)
                if Cell.cell_mines == 0:
                    ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game over', 0)
        else:
            self.cell_btn_object.configure(text="")  # Remove flag display
        print(e)
        
    def left_click(self,e):
        #if cell is not flagged
        if not self.is_flagged:
            if self.is_mine:
                self.show_mine()
               # ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine! You lose.', 'Game Over!', 0)
               # sys.exit()
            else:
                self.show_cell()
                Cell.cell_count -= 1
                if Cell.cell_count == 0:
                    ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game over', 0)
        
        else:
            ctypes.windll.user32.MessageBoxW(0, 'That cell is warded!', 'Choose another cell', 0)
            return self

    def get_cell_by_axis(self, x, y):
        #return a cell object based on x, y
         for cell in Cell.all:
             if cell.x == x and cell.y == y:
                 return cell
                
    def show_cell(self):
         self.cell_btn_object.configure(text= self.count_mines_surrounded)  
    
    @property       
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def count_mines_surrounded(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count +=1
        return count
    def show_mine(self):
        icon = PhotoImage(file="Teemo_Mushroom_Trap_Render.png")
        #change into bomb icon later
        self.cell_btn_object.configure(text=icon)
        self.cell_btn_object.configure
        Cell.cell_mines -=1
        #Reveal all the mines
        if Cell.cell_mines >=1:
            for mine in Cell.mines:
            #if mine is not flagged
                if not mine.is_flagged: #Only reveal unflagged mines
                    mine.show_mine()

    
        
    @staticmethod
    def randomize_mines():
        picked_cells= random.sample(
            Cell.all, settings.MINES_COUNT  
        )
        Cell.mines.extend(picked_cells) #Add mine cells to the 'mines' list
        print(picked_cells) #for debug purposes remove later
        for c in picked_cells:
            c.is_mine = True
            
    def __repr__(self):
        return f"cell({self.x},{self.y})"
    
    

