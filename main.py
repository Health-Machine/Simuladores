import threading
import sensores

thread_sensor_corrente = threading.Thread(target=sensores.sim_corrente)
thread_sensor_corrente.start()

thread_sensor_tensao = threading.Thread(target=sensores.sim_tensao)
thread_sensor_tensao.start()

thread_sensor_corrente.join()
thread_sensor_tensao.join()
print("Execução do sensores concluída.")