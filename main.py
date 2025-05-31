import threading
import sensor
import json

threads = [
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_CORRENTE, sensor.calcular_corrente)),
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_TENSAO, sensor.calcular_tensao)),
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_TEMPERATURA, sensor.calcular_temperatura)),
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_VIBRACAO, sensor.calcular_vibracao)),
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_PRESSAO, sensor.calcular_pressao)),
    threading.Thread(target=sensor.simular_dados_unificado, args=(sensor.ID_SENSOR_FREQUENCIA, sensor.calcular_frequencia)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

with open('dados_todos_sensores.json', 'w', encoding='utf-8') as f:
    json.dump(sensor.rawData, f, ensure_ascii=False, indent=4)

print('Dados de todos os sensores salvos em dados_todos_sensores.json')