import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()



def send_mesage(message):        
    client.connect("192.168.15.177",1883,60)
    client.publish("topic/test", message);
    client.disconnect();


while True:
    
    message = input("foo: ")
    if len(message) > 0:
        send_mesage(message)

