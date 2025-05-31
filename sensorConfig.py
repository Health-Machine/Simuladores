# config_sensores.py

# IDs dos sensores
ID_SENSOR_CORRENTE = 1
ID_SENSOR_TENSAO = 2
ID_SENSOR_TEMPERATURA = 3
ID_SENSOR_VIBRACAO = 4
ID_SENSOR_PRESSAO = 5
ID_SENSOR_FREQUENCIA = 6

# Corrente
tensao_padrao = 2.5
sensibilidade = 0.066
corrente_nominal = 10.0
tensao_teorica = tensao_padrao + corrente_nominal * sensibilidade

# Tensão
vmax_out = 3.53
vmax_in = 400
variacao_minima = 220

# Temperatura
temperatura_nominal = 25.0
variacao_maxima_temp = 0.8

# Vibração
velocidade_nominal = 10.0
variacao_permitida = 2.0

# Frequência
frequencia_nominal = 60.0
variacao_maxima_freq = 1.5

# Pressão
pressao_nominal = 35.0
variacao_maxima_pressao = 0.5