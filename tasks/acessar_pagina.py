import time
import logging
from resources import page_initial

from selenium.webdriver.common.by import By


def acessar_url(page, driver):
    logging.info('Acessando a url: ' + page)
    driver.get(page)
    driver.maximize_window()
    driver.set_page_load_timeout(20)


def validar_pagina(driver):
    logging.info('Validando se URL foi aberta com sucesso')
    if driver.find_element(By.XPATH, page_initial.painel['text']):
        logging.info('URL carregada')
    else:
        raise Exception('URL apresentou timeout')
    
def iniciar_contagem(driver):
    logging.info('Iniciando contagem')
    driver.find_element(By.XPATH, page_initial.button['start']).click() 