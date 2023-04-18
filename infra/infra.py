 
from sqlalchemy import create_engine  
import pandas as pd   

from sqlalchemy import create_engine   
import pandas as pd  
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
  
def getData(url, path):
    print(url)
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/opt/chrome/chrome"
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-tools")
        chrome_options.add_argument("--no-zygote")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("window-size=2560x1440")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
        chrome_options.add_argument("--remote-debugging-port=9222") 
        driver = webdriver.Chrome(path, options=chrome_options) 
        driver.get(url)  
        tr = driver.find_elements_by_tag_name('tr')
        driver.quit()  
        return tr
    except:
        raise
