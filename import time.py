import time
import random
import json
import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_BROKER = "mqtt.beia-telemetrie.ro"
MQTT_PORT = 1883
MQTT_TOPIC = "training/device/Elena-Gusatu"
PUBLISH_INTERVAL = 10  # seconds

# Function to simulate getting sensor data
def get_sensor_data():
    # Simulate temperature between -10 and 40 degrees Celsius
    temperature = round(random.uniform(5, 40), 2)
    
    # Simulate air pollution index between 0 and 500
    pollution_index = round(random.uniform(0, 500), 2)
    
    return {
        'temperature': temperature,
        'pollution_index': pollution_index,
        #'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }

# Callback for connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}\n")

# Initialize MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the MQTT client in a separate thread
client.loop_start()

try:
    while True:
        sensor_data = get_sensor_data()
        if sensor_data:
            sensor_data_json = json.dumps(sensor_data)
            result = client.publish(MQTT_TOPIC, sensor_data_json)

            status = result[0]
            if status == 0:
                print(f"Sent `{sensor_data_json}` to topic `{MQTT_TOPIC}`")
            else:
                print(f"Failed to send message to topic `{MQTT_TOPIC}`")
        
        time.sleep(PUBLISH_INTERVAL)
except KeyboardInterrupt:
    print("Simulation stopped")
finally:
    client.loop_stop()
    client.disconnect()
