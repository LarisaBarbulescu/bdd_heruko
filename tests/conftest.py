import pytest
import selenium
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture #face legatura intre teste
def browser():
    #initializam instanta de Chromedriver, se deschide tab-ul de chrome
    #driver = webdriver.Chrome(executable_path="C:\\Users\\Larisa\\Selenium\\chromedriver.exe")
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10) #asteapta maxim 10 sec, dar daca face actiunea mai repede, se inchide mai repede
    yield driver #executa liniile din fata inaintea testelor(inainte de deschidere tab)
    driver.quit()