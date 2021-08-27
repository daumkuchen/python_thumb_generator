import tempfile
import requests
import cv2


def imread_web(url):
  res = requests.get(url)

  img = None

  with tempfile.NamedTemporaryFile(dir='./') as fp:
    fp.write(res.content)
    fp.file.seek(0)
    img = cv2.imread(fp.name)

  return img