from tkinter import Tk, BOTH, Canvas


class Window():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def close(self):
        self.__running = False


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def draw_line(self, line, draw_color="black"):
        line.draw(self.__canvas, draw_color)

