import os
import sys

from dotenv import load_dotenv
load_dotenv()

import cv2
import PIL
from PIL import Image

import utils.color
import utils.spotify
import utils.cv2

OUTER_WIDTH = 1280
OUTER_HEIGHT = 670
INNER_WIDTH = 670
INNER_HEIGHT = 670
PADDING = int((OUTER_WIDTH - INNER_WIDTH) / 2)

DST_DIR = "./dst/"


def main():

  # .envから認証情報を取得
  SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
  SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

  # コマンドライン引数を取得
  args = sys.argv

  # 書き出す画像名
  name = args[1]

  # spotifyから取得するアルバムのid
  spotify_url = args[2]
  album_id = spotify_url
  album_id = album_id.replace("https://open.spotify.com/album/", "")
  album_id = album_id.split("?")[0]

  # spotifyからカバー画像取得
  cover_url = utils.spotify.get_album_cover_url(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, album_id)

  # web画像をcv2画像に変換
  cover_img = utils.cv2.imread_web(cover_url)

  # 色抽出
  color_list = utils.color.get_theme_color(cover_img)

  # 画像生成（pil）
  cv2_img = cover_img
  cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
  cv2_img = cv2.resize(cv2_img, (INNER_WIDTH, INNER_HEIGHT))

  pil_img = Image.fromarray(cv2_img)

  for i, new_color in enumerate(color_list):

    print(new_color)

    new_pil_img = Image.new(
      mode='RGB',
      size=(OUTER_WIDTH, OUTER_HEIGHT),
      color=new_color)

    new_pil_img.paste(
      im=pil_img,
      box=(PADDING, 0))

    path = DST_DIR + name + "_" + str(i + 1) + ".jpg"

    # new_pil_img.show()
    new_pil_img.save(path, quality=1280)


if __name__ == "__main__":
  main()