import logging
import utils.services
import tasks.extrair_excel
import tasks.acessar_pagina
import tasks.preencher_formulario

from tenacity import retry, stop_after_delay, stop_after_attempt

''' Start Pre Process:
:Import variables
:Init webdriver    
:Start logging
'''
from input.config import PARAMETERS_INPUT, PARAMETERS_OUTPUT
# utils.services.start_logging(PARAMETERS_INPUT['process_name'],
#                              PARAMETERS_INPUT['dev_name'],
#                              'Last Modification - 27/03/2024', 
#                              PARAMETERS_OUTPUT['log_path'])
edgedriver= utils.services.start_webdriver()




''' Start Process
:Run Tasks
'''
@retry(stop=(stop_after_delay(30) | stop_after_attempt(3)))
def run_tasks():


    step = '01_Acessar_Pagina_Inicial'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.acessar_pagina.acessar_url(PARAMETERS_INPUT['url'],edgedriver)
        tasks.acessar_pagina.validar_pagina(edgedriver)
        tasks.acessar_pagina.iniciar_contagem(edgedriver)
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step, edgedriver, PARAMETERS_OUTPUT['error_path'])
        utils.services.finish_drive(edgedriver)
    logging.info('-----------------------------')



    step = '02_Extrair_Excel'
    logging.info('Iniciando o step: ' + step)
    try:
        tasks.extrair_excel.download_arquivo(PARAMETERS_INPUT['href'],PARAMETERS_OUTPUT['download_path'],edgedriver)
        tasks.extrair_excel.validar_download(PARAMETERS_OUTPUT['download_path'])
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step, edgedriver, PARAMETERS_OUTPUT['error_path'])
        utils.services.finish_drive(edgedriver)
    logging.info('-----------------------------')



    step = '03_Preencher_Formulario'
    logging.info('Iniciando o step: ' + step)
    try:
        df = tasks.preencher_formulario.session_excel(PARAMETERS_OUTPUT['download_path'])
        tasks.preencher_formulario.inserir_campos(df, edgedriver)
    except Exception as x:
        logging.error("Erro no step: " + step + " - " + str(x))
        utils.services.screenshot(step, edgedriver, PARAMETERS_OUTPUT['error_path'])
        utils.services.finish_drive(edgedriver)
    logging.info('-----------------------------')

    'Finish Services Bot'
    utils.services.finish_drive(edgedriver)


run_tasks()
