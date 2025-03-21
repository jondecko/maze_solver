from maze import Maze
from window import Window
from cell import Cell
#from line import Line
#from point import Point

def main():
    print("Main starting")

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 1400
    screen_y = 1050
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


main()
