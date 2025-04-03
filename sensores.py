import sys
import random
import pandas as pd
import datetime as dt
import time
import database

inicio = 1000
fim = 6000
passo = 100

ID_SENSOR_CORRENTE = database.get_sensor('ACS712 30A')
ID_SENSOR_TENSAO = database.get_sensor('ZMPT101B')

engine = database.get_engine()

# Corrente
tensao_padrao = 2.5      
sensibilidade = 0.066        
corrente_nominal = 10.0
tensao_teorica = tensao_padrao + corrente_nominal * sensibilidade

# Tensão
vmax_out = 3.53
vmax_in = 400
variacao_minima = 220


def measure_memory():
    return sys.getsizeof([]) / (1024 * 1024)
def simular_dados(sensor_id, calcular_valor):
    valores = []
    start_time = time.time()
    start_memory = measure_memory()

    for repeticoes in range(inicio, fim + 1, passo):
        for _ in range(repeticoes):
            valor_calculado = calcular_valor()
            insert = {
                'fk_sensor': sensor_id,
                'valor': valor_calculado,
                'data_captura': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            valores.append(insert)

    end_time = time.time()
    end_memory = measure_memory()

    df = pd.DataFrame(valores)
    df.to_sql('captura', con=engine, if_exists='append', index=False)

    print("""
    Tempo de execução: {:.2f} segundos
    Memória usada: {:.2f} MB
    """.format(end_time - start_time, end_memory - start_memory))


def calcular_corrente():
    variacao = random.uniform(-0.01, 0.02)
    tensao_saida = tensao_teorica + variacao
    return round((tensao_saida - tensao_padrao) / sensibilidade, 3)


def calcular_tensao():
    variacao = random.uniform(variacao_minima, vmax_in)
    return (variacao / vmax_in) * vmax_out


def sim_corrente():
    simular_dados(ID_SENSOR_CORRENTE, calcular_corrente)


def sim_tensao():
    simular_dados(ID_SENSOR_TENSAO, calcular_tensao)
