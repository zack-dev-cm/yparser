import os
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from yparser.src.parser.js_code import JS_DROP_FILE
from yparser.src.consts import IN_COLAB
from yparser.src.utils.colab_downloader import download_incolab_chromedriver

logger = logging.getLogger(__name__)


def init_wd(headless=True):
    """
    Initializing Chrome Webdriver from selenium library
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-user-media-security=true")
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    if IN_COLAB:
        download_incolab_chromedriver()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chromedriver_path = "/usr/bin/chromedriver"
        if not os.path.exists(chromedriver_path):
            alt_path = "/usr/lib/chromium-browser/chromedriver"
            chromedriver_path = alt_path if os.path.exists(alt_path) else None
        if chromedriver_path and os.path.exists(chromedriver_path):
            logger.info("Using system chromedriver at %s", chromedriver_path)
            service = Service(chromedriver_path)
        else:
            logger.warning("Chromedriver not found, falling back to webdriver_manager")
            service = Service(ChromeDriverManager().install())
    else:
        service = Service(ChromeDriverManager().install())
    try:
        wd = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        logger.exception("Error initializing webdriver: %s", e)
        raise
    return wd


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)
