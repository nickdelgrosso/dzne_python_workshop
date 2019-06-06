import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="This will make an image that highlights green areas.")
parser.add_argument("image")
parser.add_argument("image_out")

args = parser.parse_args()

filename = args.image
save_filename = args.image_out
threshold = 100

im = plt.imread(filename)
plt.imshow(im)

above_mean = im[:, :, 1] > threshold
plt.imshow(above_mean.astype(float), cmap="gray")

plt.imsave(save_filename, above_mean.astype(float), cmap="gray")
