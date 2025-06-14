# yparser

Simple tool for collecting image URLs from Yandex. It relies on Selenium and works in Google Colab.

The repository contains usage examples in the `examples/` folder. The new `colab_example.py` demonstrates a minimal setup for running the parser on Colab.

## Installation

Install the required dependencies before using `YParser`:

```bash
pip install -r requirements.txt

# optional: install pandas if you want DataFrame output
pip install pandas
```

## Usage

```python
from yparser.parser import YParser

parser = YParser(
    name="imgs",
    save_folder="imgs",
    download_workers=2,
    parser_workers=1,
    limits=[10, 20],
    wandb_log=False,
)

parser.parse([
    "https://i.ytimg.com/vi/bj4QiFmFy2M/maxresdefault.jpg",
])
```
