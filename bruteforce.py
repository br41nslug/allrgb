from PIL import Image

WIDTH = HEIGHT = 4096
test = Image.new(mode='RGB',size=(WIDTH, HEIGHT))
img = test.load()

t=0

for r in range(256):
  for g in range(256):
    for b in range(256):
      x = t % WIDTH
      y = int(t / WIDTH)
      img[x, y] = (r,g,b)
      # if t%100000==0:
      #   print(t)
      t += 1

test.save('bruteforce.png')