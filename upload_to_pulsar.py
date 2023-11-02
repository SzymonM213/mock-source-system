import pulsar
import json

from dinosaurs import generate_dinosaur

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

for i in range(1001):
    producer.send(json.dumps(generate_dinosaur()).encode('utf-8'))

client.close()