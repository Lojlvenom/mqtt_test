import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
    print(msg.payload.decode())

    
client = mqtt.Client()
client.connect("192.168.15.177",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()