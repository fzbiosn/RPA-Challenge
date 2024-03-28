import os
import requests
import logging
from resources import page_initial

from selenium.webdriver.common.by import By


def download_arquivo(href_file, download_path, driver):
    logging.info('Extraindo o arquivo: ' + href_file)
    if os.path.exists(download_path+'\challenge.xlsx'):
        os.remove(download_path+'\challenge.xlsx')
    response = requests.get(href_file)
    if "content-disposition" in response.headers:
         content_disposition = response.headers["content-disposition"]
         filename = content_disposition.split("filename=")[1]
    else:
        filename = href_file.split("/")[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")


def validar_download(download_path,):
    logging.info('Validando se a extracao foi reaizada sucesso')
    if os.path.exists(download_path+'\challenge.xlsx'):
        logging.info('Extracao carregada')
    else:
        raise Exception('Extracao apresentou erros')
