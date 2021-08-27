import cv2
import sklearn
from sklearn.cluster import KMeans
from PIL import ImageColor


def get_theme_color(img):
  cv2_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  cv2_img = cv2_img.reshape(
    (cv2_img.shape[0] * cv2_img.shape[1], 3))

  cluster = KMeans(
    n_clusters=5)

  cluster.fit(
    X=cv2_img)

  cluster_centers_arr = cluster.cluster_centers_.astype(
    int,
    copy=False)

  dst = []

  for i, rgb_arr in enumerate(cluster_centers_arr):
    color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
    dst.append(ImageColor.getcolor(color_hex_str, "RGB"))

  return dst