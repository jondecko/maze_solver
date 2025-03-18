from line import Line
from point import Point

class Cell():

    def __init__(self, win, x1, x2, y1, y2,
                 has_top_wall=True, has_right_wall=True,
                 has_bottom_wall=True, has_left_wall=True):
        self.has_left_wall = has_left_wall 
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win 


    def draw(self, fill_color="black"):
        print("drawing")
        p1 = Point(self._x1, self._y1) # Top left
        p2 = Point(self._x2, self._y1) # Top right
        p3 = Point(self._x2, self._y2) # Bottom left
        p4 = Point(self._x1, self._y2) # Bottom right
        if self.has_top_wall:
            l1 = Line(p1, p2)
            self._win.draw_line(l1)
        if self.has_right_wall:
            l2 = Line(p2, p3)
            self._win.draw_line(l2)
        if self.has_bottom_wall:
            l3 = Line(p3, p4)
            self._win.draw_line(l3)
        if self.has_left_wall:
            l4 = Line(p4, p1)
            self._win.draw_line(l4)
