from shapes import Shapes
class Piece:
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0
        self.color = Shapes.shape_colors[Shapes.shapes.index(shape)]
