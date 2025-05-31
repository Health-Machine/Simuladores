from sensorConfig import *
import random

def calcular_corrente():
    variacao = random.uniform(-0.01, 0.02)
    tensao_saida = tensao_teorica + variacao
    return round((tensao_saida - tensao_padrao) / sensibilidade, 3)

def calcular_tensao():
    variacao = random.uniform(variacao_minima, vmax_in)
    return (variacao / vmax_in) * vmax_out

def calcular_temperatura():
    variacao = random.uniform(-variacao_maxima_temp, variacao_maxima_temp)
    return round(temperatura_nominal + variacao, 2)

def calcular_vibracao():
    variacao = random.uniform(-variacao_permitida, variacao_permitida)
    return round(velocidade_nominal + variacao, 3)

def calcular_pressao():
    variacao = random.uniform(-variacao_maxima_pressao, variacao_maxima_pressao)
    return round(pressao_nominal + variacao, 2)

def calcular_frequencia():
    variacao = random.uniform(-variacao_maxima_freq, variacao_maxima_freq)
    return round(frequencia_nominal + variacao, 2)