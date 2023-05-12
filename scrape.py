from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from database import updateFirebase
from formatters import formatPriceEuro, formatPriceExito

def scrapeExito(url, productId):
    # Crea una instancia del controlador de navegador
    driver = webdriver.Chrome()

    # Carga la página que deseas obtener datos
    driver.get(url)

    # Espera a que se carguen los elementos necesarios
    wait = WebDriverWait(driver, 10)
    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body > div.render-container.render-route-store-product > div > div.vtex-store__template.bg-base > div > div > div > div:nth-child(4) > div > div:nth-child(11) > div > section > div > div.pr0.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > div > div > div > div > div > div > div > div.vtex-flex-layout-0-x-flexCol.vtex-flex-layout-0-x-flexCol--product-price-PDP.ml0.mr0.pl0.pr0.flex.flex-column.h-100.w-100 > div:nth-child(1) > div > div > div.exito-vtex-components-4-x-selling-price.flex.items-center > div > span")))

    # Extrae los títulos de los artículos
    for article in articles:
        formattedPrice = formatPriceExito(article.text.strip())
        print(formattedPrice)

    updateFirebase(productId, 'exito', formattedPrice)

    # Cierra el navegador
    driver.quit()

def scrapeEuro(url, productId):
        # Crea una instancia del controlador de navegador
    driver = webdriver.Chrome()

    # Carga la página que deseas obtener datos
    driver.get(url)

    # Espera a que se carguen los elementos necesarios
    wait = WebDriverWait(driver, 10)
    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#product-price-234 > span")))

    # Extrae los títulos de los artículos
    for article in articles:
        formattedPrice = formatPriceEuro(article.text.strip())
        print(formattedPrice)

    updateFirebase(productId, 'euro', formattedPrice)

    # Cierra el navegador
    driver.quit()

def scrapeCarulla(url, productId):
        # Crea una instancia del controlador de navegador
    driver = webdriver.Chrome()

    # Carga la página que deseas obtener datos
    driver.get(url)

    # Espera a que se carguen los elementos necesarios
    wait = WebDriverWait(driver, 10)
    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body > div.render-container.render-route-store-product > div > div.vtex-store__template.bg-base > div > div > div > div:nth-child(3) > div > div:nth-child(6) > div > section > div > div.pr0.vtex-flex-layout-0-x-stretchChildrenWidth.flex > div > div > div > div > div > div > div > div > div.vtex-flex-layout-0-x-flexCol.ml0.mr0.pl0.pr0.flex.flex-column.h-100.w-100 > div:nth-child(1) > div > div > div.exito-vtex-components-4-x-selling-price.flex.items-center > div > span")))

    # Extrae los títulos de los artículos
    for article in articles:
        formattedPrice = formatPriceExito(article.text.strip())
        print(formattedPrice)

    updateFirebase(productId, 'carulla', formattedPrice)

    # Cierra el navegador
    driver.quit()

def scrapeJumbo(url, productId):
        # Crea una instancia del controlador de navegador
    driver = webdriver.Chrome()

    # Carga la página que deseas obtener datos
    driver.get(url)

    # Espera a que se carguen los elementos necesarios
    wait = WebDriverWait(driver, 10)
    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#items-price > div > div")))

    # Extrae los títulos de los artículos
    for article in articles:
        formattedPrice = formatPriceExito(article.text.strip())
        print(formattedPrice)

    updateFirebase(productId, 'jumbo', formattedPrice)

    # Cierra el navegador
    driver.quit()
