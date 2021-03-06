#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, argparse, random, string
from kafka import KafkaProducer

parser = argparse.ArgumentParser(description='Import images for disconnected OCP installs')
parser.add_argument('kafka', action="store", default="kafka-hc-kafka-bootstrap.kafka.svc.cluster.local:9092", help='kafka bootstrap endpoint, Ex: kafka-hc-kafka-bootstrap.kafka.svc.cluster.local:9092')
parser.add_argument('-t', action="store", default=False, required=True, help='kafka topic')
args = parser.parse_args()

producer = KafkaProducer(security_protocol='SSL',
                         ssl_check_hostname=False,
                         bootstrap_servers=args.kafka)

letters = string.ascii_letters
send_message = (''.join(random.choice(letters) for i in range(20)))
print("sending '%s' to '%s'"%(send_message, args.topic))
future = producer.send(args.topic, b"%s"%send_message)
result = future.get(timeout=60)

