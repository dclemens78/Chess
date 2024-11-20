# Danny Clemens

# chessboard.py

''' A GUI chessboard that the user can interact with '''

import tkinter as tk

SIZE = 8
SQUARESIZE = 80
INITIAL_BOARDSTATE = [["R", "N", "DB", "Q", "K", "LB", "N", "R"],
                      ["P", "P", "P", "P", "P", "P", "P", "P"],             
                      ["e", "e", "e", "e", "e", "e", "e", "e"],             
                      ["e", "e", "e", "e", "e", "e", "e", "e"],             
                      ["e", "e", "e", "e", "e", "e", "e", "e"],             
                      ["e", "e", "e", "e", "e", "e", "e", "e"],             
                      ["p", "p", "p", "p", "p", "p", "p", "p"],             
                      ["r", "n", "db", "q", "k", "lb", "n", "r"]] 
            
                


def main():
    
    root = tk.Tk()
    root.title("Chess Board")

    # Canvas for chessboard
    canvas = tk.Canvas(root, width=SIZE * SQUARESIZE, height=SIZE * SQUARESIZE)
    canvas.pack()
    
    draw_board(canvas)
    place_pieces(INITIAL_BOARDSTATE)
    
    root.mainloop()
    
        



def draw_board(canvas):
    
    for row in range(SIZE):
        
        for col in range(SIZE):
            
            x1, y1 = col * SQUARESIZE, row * SQUARESIZE
            x2, y2 = x1 + SQUARESIZE, y1 + SQUARESIZE
            
            color = "white" if (row + col) % 2 == 0 else "black"
            
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
            

def place_pieces(state): pass
    
            

if __name__ == "__main__":
    main()