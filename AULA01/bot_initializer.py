BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 30.0
IS_PRODUCTION = False

print('-------------------Inicializando-----------------')
print(f'Nome do Bot: {BOT_NAME} - Tipo: {type(BOT_NAME)}')
print(f'Nº Máx. Tentativas: {MAX_RETRIES} - Tipo: {type(MAX_RETRIES)}')
print(f'Tempo limite: {EXECUTION_TIMEOUT} - Tipo: {type(EXECUTION_TIMEOUT)}')
print(f'Ambiente de produção: {IS_PRODUCTION} - Tipo: {type(IS_PRODUCTION)}')
print('-------------------------------------------------')
