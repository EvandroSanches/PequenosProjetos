#buscar previsão do tempo utilizando a biblioteca selenium e gerando arquivo json com a informação
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get('www.google.com')


