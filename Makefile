NAME := tdd_workshop
TAG  := latest
IMG  := ${NAME}:${TAG}

build:
	docker build -t ${IMG}  .

tests:
	docker run ${IMG} python -m unittest
	