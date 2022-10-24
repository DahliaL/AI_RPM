import math
from PIL import Image, ImageDraw


class SQUARE:

  def __init__(self, name):
    self.name = name

  def square_generator(self, edge_length, offset):
    ##Generator for coordinates in a hexagon
    x, y = offset
    for angle in range(0, 360, 90):
      x += math.cos(math.radians(angle)) * edge_length
      y += math.sin(math.radians(angle)) * edge_length
      yield x, y

  def makeSquare(self, xoff, yoff, fillCol, imgOut, EdLen):
    draw = ImageDraw.Draw(imgOut)
    hexagon = self.square_generator(
      EdLen,
      offset=(((imgOut.size[0] / 2) + xoff - (EdLen / 2)),
              ((imgOut.size[1] / 2) + yoff - (EdLen / 2))))
    draw.polygon(list(hexagon), outline='black', fill=fillCol)


class HEX:

  def __init__(self, name):
    self.name = name

  def hexagon_generator(self, edge_length, offset):
    ##Generator for coordinates in a hexagon
    x, y = offset
    for angle in range(0, 360, 60):
      x += math.cos(math.radians(angle)) * edge_length
      y += math.sin(math.radians(angle)) * edge_length
      yield x, y

  def makeHex(self, xoff, yoff, fillCol, imgOut, EdLen):
    draw = ImageDraw.Draw(imgOut)
    hexagon = self.hexagon_generator(
      EdLen,
      offset=(((imgOut.size[0] / 2) + xoff - (EdLen / 2)),
              ((imgOut.size[1] / 2) + yoff - ((EdLen / math.sin(120)) / 2))))
    draw.polygon(list(hexagon), outline='black', fill=fillCol)


class LINE:

  def __init__(self, name):
    self.name = name

  def makeLine(self, imgOut):
    draw = ImageDraw.Draw(imgOut)
    draw.line([(0, imgOut.size[1] / 2), (imgOut.size[0], imgOut.size[1] / 2)],fill="black",width=1)
