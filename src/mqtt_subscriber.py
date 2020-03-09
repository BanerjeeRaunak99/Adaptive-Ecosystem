import paho.mqtt.client as mqtt

# TODO: Setup the functions to handle the different data rceived from the different sensors


def on_connect(clients, userdata, flags, rc):
    print("Connected with code " + str(rc))

    client.subscribe("Sensor/acs1")

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(payload)

    msg = payload.split(":")
    # TODO: Check for the sensor field of the msg and call suitable functions

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()