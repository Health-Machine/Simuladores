import os
import sys
import time
import json
import asyncio
import threading
import datetime as dt
import iotHubConnection
import pandas as pd

from dotenv import load_dotenv
from sensorConfig import *
from sensorSimulation import *

load_dotenv()
start = 1000
end = 1500
step = 100
raw_data = []
lock = threading.Lock()

def measure_memory():
    return sys.getsizeof([]) / (1024 * 1024)

def get_connection_string(device_id_env, key_env):
    hostname = os.getenv('HOSTNAME')
    device_id = os.getenv(device_id_env)
    shared_key = os.getenv(key_env)
    return f'HostName={hostname};DeviceId={device_id};SharedAccessKey={shared_key}'

def simulate_unified_data(sensor_id, calculate_value):
    start_time = time.time()
    capture_time = 5
    values = []
    while time.time() - start_time < capture_time:
        calculated_value = calculate_value()
        record = {
            'fk_sensor': sensor_id,
            'value': calculated_value,
            'capture_date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        values.append(record)
        time.sleep(1)
    with lock:
        raw_data.extend(values)

async def simulate_data(sensor_id, calculate_value, hub_connection=None):
    start_time = time.time()
    start_memory = measure_memory()
    await hub_connection.connect()
    for repetitions in range(start, end + 1, step):
        for _ in range(repetitions):
            calculated_value = calculate_value()
            record = {
                'fk_sensor': sensor_id,
                'value': calculated_value,
                'capture_date': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            # if hub_connection:
            #     await hub_connection.send_message(json.dumps(record))
    await hub_connection.disconnect()
    end_time = time.time()
    end_memory = measure_memory()
    print(f"\nExecution time: {end_time - start_time:.2f} seconds\nMemory used: {end_memory - start_memory:.2f} MB\n")

def sim_current():
    con = iotHubConnection.IoTHubConnection(get_connection_string('ELECTRIC_CURRENT_DEVICE_ID', 'ELECTRIC_CURRENT_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_CORRENTE, calculate_current, hub_connection=con))

def sim_voltage():
    con = iotHubConnection.IoTHubConnection(get_connection_string('VOLTAGE_DEVICE_ID', 'VOLTAGE_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_TENSAO, calculate_voltage, hub_connection=con))

def sim_temperature():
    con = iotHubConnection.IoTHubConnection(get_connection_string('TEMPERATURE_DEVICE_ID', 'TEMPERATURE_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_TEMPERATURA, calculate_temperature, hub_connection=con))

def sim_vibration():
    con = iotHubConnection.IoTHubConnection(get_connection_string('VIBRATION_DEVICE_ID', 'VIBRATION_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_VIBRACAO, calculate_vibration, hub_connection=con))

def sim_pressure():
    con = iotHubConnection.IoTHubConnection(get_connection_string('PRESSURE_DEVICE_ID', 'PRESSURE_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_PRESSAO, calculate_pressure, hub_connection=con))

def sim_frequency():
    con = iotHubConnection.IoTHubConnection(get_connection_string('FREQUENCY_DEVICE_ID', 'FREQUENCY_SHARED_ACCESS_KEY'))
    asyncio.run(simulate_data(ID_SENSOR_FREQUENCIA, calculate_frequency, hub_connection=con))