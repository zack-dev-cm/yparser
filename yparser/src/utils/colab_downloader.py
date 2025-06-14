import subprocess
import os

from yparser.src.consts import IN_COLAB


def download_incolab_chromedriver():
    """Install ChromeDriver when running inside Google Colab."""
    if IN_COLAB:
        subprocess.run('apt-get update', shell=True, check=True)
        subprocess.run('apt-get install -y chromium-chromedriver', shell=True, check=True)
        if not os.path.exists('/usr/bin/chromedriver'):
            subprocess.run(
                'ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver',
                shell=True,
                check=True,
            )
