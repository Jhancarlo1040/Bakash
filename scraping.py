from  search  import abrir_ventana
URL = abrir_ventana()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


Ruta  = r"c:\Program Files (x86)\chromedriver.exe"


service = Service(Ruta)
driver = webdriver.Chrome(service=service)
driver.get(f'{URL}') # tienda exito

Titulo_Producto = driver.find_element(By.CLASS_NAME,'product-title_product-title__heading___mpLA')
Especificacion = driver.find_element(By.CLASS_NAME,'product-title_product-title__specification__UTjNc')
precio_producto = driver.find_element(By.CLASS_NAME,'ProductPrice_container__price__XmMWA')
img_producto = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/button/img')
url_img = img_producto.get_attribute('src')









