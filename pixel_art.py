import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((100, 100, 3), dtype=np.uint8)

K = 10

for row in range(100):
    for column in range(100):

        horizontal = column - 50
        vertical = row - 50

        H = np.sqrt(horizontal**2 + vertical**2)

        if H == 0:
            brightness = 255
        else:
            brightness = (255 * K) / H

        if brightness > 255:
            brightness = 255

        brightness = int(brightness)

        image[row, column] = [brightness, brightness, brightness]

plt.imshow(image)
plt.axis("off")
plt.imsave("generative_glow.png", image)
plt.show()

























