import os



# Captura nome de usuario Windows #
local_user = os.environ['UserName']


PARAMETERS_INPUT = {
 'name_log': 'log',
 'dev_name': 'Fabio Neves',
 'process_name': 'RPA Challenge', 
 'path_driver': fr'C:\webdrivers\Edge\msedgedriver.exe',
 'url': 'https://rpachallenge.com/',
 'href': 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx' 
}

PARAMETERS_OUTPUT = {
    'path_output': fr'C:\Users\{local_user}\Project\RPA-Challenge\output',
    'download_path': fr'C:\Project\RPA-Challenge',
    'log_path': fr'C:\Users\{local_user}\Project\RPA-Challenge\output\log',
    'error_path': fr'C:\Users\{local_user}\Project\RPA-Challenge\output\screenshot'
}