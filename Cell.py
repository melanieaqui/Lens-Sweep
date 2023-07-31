from tkinter import *
import settings
import random
import ctypes
import sys
from PIL import Image,ImageTk


class Cell:
     
    mines = [] #Class variable to store mine cells
    all = []
    
    #number of mines that aew not mines
    cell_count = (settings.GRID_SIZE**2)-settings.MINES_COUNT
    
    #number of mines
    unopened_mines = settings.MINES_COUNT

    def __init__ (self,x,y,is_mine = False):

        self.is_mine = is_mine
        self.is_flagged = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.exposed = False
    
        Cell.all.append(self)
        

    def create_btn_object (self, location, default, teemo, ward,root):
        btn = Button(
            location,
            bg='#042028',
            width = 40,
            height = 40,
            image=default
        )
        self.teemo_img=teemo
        self.ward_img=ward
        self.default=default
        self.root =root
        #left click
        btn.bind('<Button-1>',self.left_click)
        
        #right click
        btn.bind('<Button-3>',self.right_click)

        self.cell_btn_object = btn
    
    #right click functions, putting the flag     
    def right_click(self,e):
        
        #check if cell has already been exposed or open, i.e there is a number display
        if self.exposed == False:
            self.is_flagged = not self.is_flagged 

        if self.is_flagged and self.exposed == False:
            self.cell_btn_object.config(image=self.ward_img)

            if self.is_mine:
                Cell.unopened_mines-= 1
                print(Cell.unopened_mines)
                #check if all mine has been flagged
                
                if Cell.unopened_mines == 0:
                    self.root.update()
                    ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game over', 0)
                    sys.exit()
        #unflagged when it was already a mine
        elif not self.is_flagged and self.is_mine:
            Cell.unopened_mines+= 1
            self.cell_btn_object.configure(image=self.default)  # Remove flag display
        #unflag when not mine
        elif  self.exposed == False:
            self.cell_btn_object.configure(image=self.default)
    
    
    def left_click(self,e):
        #if cell is not flagged
        if not self.is_flagged:
            #not flagged but mine
            if self.is_mine:
                self.show_mine()   
                self.root.update()        
                ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine! You lose.', 'Game Over!', 0) 
                sys.exit()
            #not flagged but no more non mines
            else:
                self.show_cell()
                Cell.cell_count -= 1
                if Cell.cell_count == 0:
                    self.root.update()
                    ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game over', 0)
                    sys.exit()

        #flagged
        else:
            ctypes.windll.user32.MessageBoxW(0, 'That cell is warded!', 'Choose another cell', 0)
            return self

    def get_cell_by_axis(self, x, y):
        #return a cell object based on x, y
         for cell in Cell.all:
             if cell.x == x and cell.y == y:
                 return cell
                
    def show_cell(self):
        self.exposed=True
        self.cell_btn_object.config(image= "",
            text= self.count_mines_surrounded, 
            height=2,
            width=5,
            bg='#BE5A04',
            state = DISABLED,
            disabledforeground='black',
            relief=FLAT
            
        )  
    
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
        self.cell_btn_object.config(bg='#BE5A04',
            image=self.teemo_img, 
            relief=FLAT)
        Cell.unopened_mines -=1
        #Reveal all the mines
        if Cell.unopened_mines >=1:
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
    

