# Regression Model
Building and deploying a regression ML model.

![Test and Build](https://github.com/schmidtbri/regression-model/workflows/Test%20and%20Build/badge.svg)

This code is used in this [blog post]().

## Requirements
Python 3

## Installation 

The Makefile included with this project contains targets that help to automate several tasks.

To download the source code execute this command:

```bash
git clone https://github.com/schmidtbri/regression-model
```

Then create a virtual environment and activate it:

```bash
# go into the project directory
cd regression-model

make venv

source venv/bin/activate
```

Install the dependencies:

```bash
make dependencies
```

The requirements.txt file only includes the dependencies needed to make predictions with the model. To train the model you'll need to install the dependencies from the train_requirements.txt file:

```bash
make train-dependencies
```

## Running the Unit Tests
To run the unit test suite execute these commands:

```bash
# first install the test dependencies
make test-dependencies

# run the test suite
make test

# clean up the unit tests
make clean-test
```

## Running the Service

To start the service locally, execute these commands:

```bash

```

## Docker

To build a docker image for the service, run this command:

```bash
docker build -t insurance_charges_model:latest .
```

To run the image, execute this command:

```bash
docker run -d -p 80:80 insurance_charges_model
```

To watch the logs coming from the image, execute this command:

```bash
docker logs $(docker ps -lq)
```

To get the latest build of this image from Dockerhub, execute this command:

```bash
docker pull bschmidt135/insurance_charges_model
```