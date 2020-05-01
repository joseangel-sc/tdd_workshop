NAME := joseangelsc/tdd_workshop
TAG  := $(shell git log --pretty=format:'%h' -n 1)
IMG  := ${NAME}:${TAG}

# INSIDE DOCKER
build:
	docker build -t ${IMG} .

tests:
	docker run -v ${PWD}:/app ${IMG} python -m unittest

push:
	docker push ${IMG}
	