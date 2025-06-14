"""Google Colab example for text queries using yparser.
This script shows how to parse image URLs for several phrases on Colab.
"""

from yparser.parser import YParser

queries = [
    "Christine Todd Whitman",
    "Steve Lavin",
    "Doris Roberts",
    "Bridget Fonda",
    "Richard Virenque",
]

SAVE_PATH = "imgs"

parser = YParser(
    name="people",
    save_folder=SAVE_PATH,
    download_workers=2,
    parser_workers=1,
    limits=[10],
    parse_type="text",
)

parser.parse(queries)
