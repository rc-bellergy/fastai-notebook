import fastbook
fastbook.setup_book()

from fastbook import *
from fastai.vision.widgets import *

import os
from dotenv import load_dotenv

# 加載 .env 檔案中的環境變數
load_dotenv()


import requests

def search_images_google(keyword):
    """
    Google Custom Search API for images
    """

    # 從環境變數取得 GOOGLE_SEARCH_API_KEY
    GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')

    # Extract image URLs
    image_urls = []

    search_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        'key': GOOGLE_SEARCH_API_KEY,
        'cx': "b75e7be86f39f415b", # Custom Search Engine ID
        'q': keyword,
        'searchType': 'image',
        'num': 10,  # Max 10 per request
        'safe': 'active'
    }

    for i in range(15):
      response = requests.get(search_url, params=params)
      response.raise_for_status()

      results = response.json()

      if 'items' in results:
          for item in results['items']:
              image_urls.append(item['link'])

    return image_urls

## Example usage
# urls = []
# urls = search_images_google('grizzly bear')
# print(len(urls))

## Download images (only run once)
bear_types = 'grizzly','black','teddy'
path = Path('images')

if not path.exists():
    path.mkdir()
    for o in bear_types:
        dest = (path/o)
        dest.mkdir(exist_ok=True)
        results = search_images_google(f'{o} bear')
        download_images(dest, urls=results)

# Get image files list
fns = get_image_files(path)
print(f"Total images:{ len(fns) }")

failed = verify_images(fns)
print(f"Failed images:{ len(failed) }")
print(f"Sample failed images:{failed[:5]}")

# 刪除不相容的圖片
failed.map(Path.unlink);
print(f"Total images:{ len(fns) }")
