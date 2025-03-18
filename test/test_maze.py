import unittest

from maze import Maze

class Tests(unittest.TestCase):


    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_no_cols(self):
        num_cols = 0 
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)

    def test_different_dimensions(self):
        m1 = Maze(0, 0, 5, 8, 10, 10)
        self.assertEqual(len(m1._cells), 8)
        self.assertEqual(len(m1._cells[0]), 5)
        m2 = Maze(0, 0, 20, 15, 10, 10)
        self.assertEqual(len(m2._cells), 15)
        self.assertEqual(len(m2._cells[0]), 20)

    def test_cell_creation(self):
        cell_size = 10
        m = Maze(0, 0, 3, 3, cell_size, cell_size)
        
        # Check first cell coordinates
        first_cell = m._cells[0][0]
        self.assertEqual(first_cell._x1, 0)
        self.assertEqual(first_cell._y1, 0)
        self.assertEqual(first_cell._x2, cell_size)
        self.assertEqual(first_cell._y2, cell_size)
        
        # Check middle cell coordinates
        middle_cell = m._cells[1][1]
        self.assertEqual(middle_cell._x1, cell_size)
        self.assertEqual(middle_cell._y1, cell_size)
        self.assertEqual(middle_cell._x2, cell_size * 2)
        self.assertEqual(middle_cell._y2, cell_size * 2)

    def test_maze_create_busting_out_ent_and_exit(self):
        num_cols = 5 
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        c1 = m1._cells[0][0]
        self.assertEqual(c1.has_top_wall, False)
        self.assertEqual(c1.has_right_wall, True)
        self.assertEqual(c1.has_bottom_wall, True)
        self.assertEqual(c1.has_left_wall, True)

        c2 = m1._cells[4][9]
        self.assertEqual(c2.has_top_wall, True)
        self.assertEqual(c2.has_right_wall, True)
        self.assertEqual(c2.has_bottom_wall, False)
        self.assertEqual(c2.has_left_wall, True)


if __name__ == "__main__":
    unittest.main()
