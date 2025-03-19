from cell import Cell
import random
import time

class Maze():

    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = None

        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._draw_cells()


    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                x1 = self._x1 + (self._cell_size_x * i)
                x2 = self._x1 + (self._cell_size_x * (i+1))
                y1 = self._y1 + (self._cell_size_y * j)
                y2 = self._y1 + (self._cell_size_y * (j+1))
                cell = Cell(x1, x2, y1, y2, True, True, True, True, self._win)
                self._cells[i].append(cell)


    def _draw_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)


    def _break_entrance_and_exit(self):
        if self._num_rows and self._num_cols:
            self._cells[0][0].has_top_wall = False
            self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #check left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #check right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))

            #check up
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            #check down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))

            if not len(to_visit):
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False


            self._break_walls_r(next_index[0], next_index[1])
           
