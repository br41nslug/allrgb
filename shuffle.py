from PIL import Image
import numpy as np

WIDTH = HEIGHT = 4096
# test = Image.new(mode='RGB',size=(WIDTH, HEIGHT))
# img = test.load()
orig = Image.open('bruteforce.png')
orig_px = orig.getdata()

orig_px = np.reshape(orig_px, (orig.height * orig.width, 3))
np.random.shuffle(orig_px)

orig_px = np.reshape(orig_px, (orig.height, orig.width, 3))

res = Image.fromarray(orig_px.astype('uint8'))
res.save('shuffle.png')