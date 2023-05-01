import pika
import time
from os import listdir
from os.path import isfile, join


def publisher():
    # Set connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare name of queue
    channel.queue_declare(queue='my_q')

    # I look at what files are currently in the data folder
    only_files = str([f for f in listdir("data/") if isfile(join("data/", f))])

    channel.basic_publish(exchange='',
                          routing_key='my_q',
                          body=only_files)
    # print(f" [x] Sent {only_files}")
    connection.close()
