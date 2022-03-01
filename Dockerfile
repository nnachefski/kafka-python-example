FROM registry.access.redhat.com/ubi7/python-38@sha256:ac2315bc1f0267eaa7a9e48b946e3c2ba7bd5d7f091c760d271a2f0a30ee8846

RUN pip3 install kafka-python

ENV SCRIPT=producer.py

ENTRYPOINT ["./${SCRIPT}"]