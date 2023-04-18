from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from infra.infra import getData
import os

current_path = os.path.dirname(os.path.abspath(__file__))

class Dominio:
    def __repr__(self):
        return self.__str__() 
 
    @staticmethod
    def scraping():  
        try:   
            DRIVER_PATH = f'/opt/chromedriver'  
            data = getData(f"https://google.com", DRIVER_PATH)
            return data 
        except:  
            raise 
         