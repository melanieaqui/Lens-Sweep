from tkinter import Button
import settings
import random
class Cell:
    all = []
    def __init__ (self,x,y, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
    
        Cell.all.append(self)
    def create_btn_object (self, location):
        btn = Button(
            location,
            width = 5,
            height =2

        )
        #left click
        btn.bind('<Button-1>',self.left_click)
        
        #right click
        btn.bind('<Button-3>',self.right_click)

        self.cell_btn_object = btn
    
    def left_click(self,e):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            
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
        
        #change into bomb icon later
        self.cell_btn_object.configure(bg='red')
    def right_click(self,e):
        print(e)
        print("righ")
        
    @staticmethod
    def randomize_mines():
        picked_cells= random.sample(
            Cell.all, settings.MINES_COUNT  
        )
        print(picked_cells) #for debug purposes remove later
        for c in picked_cells:
            c.is_mine = True
            
    def __repr__(self):
        return f"cell({self.x},{self.y})"