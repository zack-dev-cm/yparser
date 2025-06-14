"""Google Colab example for yparser.
This script shows how to parse a few image URLs on Colab.

`YParser` automatically installs ChromeDriver when running in Colab, so no
manual setup is required.
"""

from yparser.parser import YParser

image_urls = [
    "https://i.ytimg.com/vi/bj4QiFmFy2M/maxresdefault.jpg",
    "https://www.ejin.ru/wp-content/uploads/2019/07/3d064e1dc7ce5b4.jpg",
]

SAVE_PATH = "imgs"

parser = YParser(
    name="imgs",
    save_folder=SAVE_PATH,
    download_workers=2,
    parser_workers=1,
    limits=[10, 20],
    wandb_log=False,
)

parser.parse(links=image_urls)
