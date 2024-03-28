import time
import logging
import pandas as pd

from time import strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from resources import page_initial


# Atribuindo váriaveis relacionadas ao nome e diretório do Excel #
def session_excel(download_path):
    path_excel = download_path+'\challenge.xlsx'
    df = pd.read_excel(path_excel, sheet_name="Sheet1")
    logging.info("Criando o dataframe excel")
    return df


def inserir_campos(df, driver):
    logging.info('Percorrendo a planilha')

    for index_df in range(len(df)):
        var_firstname = df.loc[index_df, "First Name"]
        var_lastname = df.loc[index_df, "Last Name "]
        var_companyname = df.loc[index_df, "Company Name"]
        var_rolecompany = df.loc[index_df, "Role in Company"]
        var_address = df.loc[index_df, "Address"]
        var_phone= df.loc[index_df, "Phone Number"]
        var_phone = str(var_phone)
        var_email= df.loc[index_df, "Email"]

        driver.find_element(By.XPATH, page_initial.form['firstname']).send_keys(var_firstname)
        driver.find_element(By.XPATH, page_initial.form['lastname']).send_keys(var_lastname)
        driver.find_element(By.XPATH, page_initial.form['company']).send_keys(var_companyname)
        driver.find_element(By.XPATH, page_initial.form['role']).send_keys(var_rolecompany)
        driver.find_element(By.XPATH, page_initial.form['address']).send_keys(var_address)
        driver.find_element(By.XPATH, page_initial.form['phone']).send_keys(var_phone)
        driver.find_element(By.XPATH, page_initial.form['email']).send_keys(var_email)

        driver.find_element(By.CSS_SELECTOR, page_initial.button['submit']).click()
       


