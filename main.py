from window import Window
from cell import Cell
#from line import Line
#from point import Point

def main():
    print("Main starting")
    win = Window(800, 600)

    cells = [
        Cell(win, 100, 150, 100, 150, True, False, True, True),
        Cell(win, 150, 200, 100, 150, True, False, True, False),
        Cell(win, 200, 250, 100, 150, True, False, True, False),
        Cell(win, 250, 300, 100, 150, True, True, True, False),
    ]
    for cell in cells:
        cell.draw()

    cells[0].draw_move(cells[1])
    cells[1].draw_move(cells[2], True)

    win.wait_for_close()


main()
