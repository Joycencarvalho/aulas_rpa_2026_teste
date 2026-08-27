BOT_NAME = "RPA_LAB_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 50.5
IS_PRODUCTION = True

print('-------------------Inicializando-----------------')
print(f'Nome do Bot: {BOT_NAME} - Tipo: {type(BOT_NAME)}')
print(f'Nº Máx. Tentativas: {MAX_RETRIES} - Tipo: {type(MAX_RETRIES)}')
print(f'Tempo limite: {EXECUTION_TIMEOUT} - Tipo: {type(EXECUTION_TIMEOUT)}')
print(f'Ambiente de produção: {IS_PRODUCTION} - Tipo: {type(IS_PRODUCTION)}')
print('-------------------------------------------------')
