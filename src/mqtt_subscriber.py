import paho.mqtt.client as mqtt

job = "get:acs1"

# TODO: Setup the functions to handle the different data rceived from the different sensors


def on_publish(user, userdata, rc):
    print("Message published")
    pass

def on_connect(clients, userdata, flags, rc):
    print("Connected with code " + str(rc))
    client.subscribe("Sensor/acs1")
    client.publish("Sensor/acs1", "1")

    if job == "get:acs1":
        client.subscribe("Sensor/"+job.split(":")[1])
        client.publish("Sensor/"+job.split(":")[1], "send_data")
        job = "none"


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(payload)

    # if payload == "Got your message":
    #     print("They got your message")
    # else:
    #     print("They didn't get your message")
    # msg = payload.split(":")
    # TODO: Check for the sensor field of the msg and call suitable functions

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()