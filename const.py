# max number of components in a RPM
MAX_COMPONENTS = 2

# canvas parameters
IMAGE_SIZE = 160
CENTER = (IMAGE_SIZE / 2, IMAGE_SIZE / 2)
DEFAULT_RADIUS = IMAGE_SIZE / 4
DEFAULT_WIDTH = 2

# Attribute parameters
# Number
NUM_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
NUM_MIN = 0
NUM_MAX = len(NUM_VALUES) - 1

# Uniformity
UNI_VALUES = [False, False, False, True]
UNI_MIN = 0
UNI_MAX = len(UNI_VALUES) - 1

# Type
TYPE_VALUES = ["none", "triangle", "square", "pentagon", "hexagon", "circle"]
TYPE_MIN = 0
TYPE_MAX = len(TYPE_VALUES) - 1

# Size
SIZE_VALUES = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
SIZE_MIN = 0
SIZE_MAX = len(SIZE_VALUES) - 1

# Color
COLOR_VALUES = [255, 224, 196, 168, 140, 112, 84, 56, 28, 0]
COLOR_MIN = 0
COLOR_MAX = len(COLOR_VALUES) - 1

# Angle: self-rotation
ANGLE_VALUES = [-135, -90, -45, 0, 45, 90, 135, 180]
ANGLE_MIN = 0
ANGLE_MAX = len(ANGLE_VALUES) - 1
