import sys
from PIL import Image
# from pprint import pprint

TOTAL_COLORS=16777216

img = Image.open(sys.argv[1])
colors = img.convert('RGB').getcolors(TOTAL_COLORS)
if len(colors) == TOTAL_COLORS:
    print("All RGB values are there!")
else:
    print("ERROR")
    sys.exit(1)
