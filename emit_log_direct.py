#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

key = ''
if len(sys.argv) > 1:
    key = sys.argv[1]
else:
    'info'

message = ' '.join(sys.argv[2:]) or 'No message sent'
channel.basic_publish(
    exchange='direct_logs', routing_key=key, body=message)
print(" → Sent %r: %r" % (key, message))

connection.close()
