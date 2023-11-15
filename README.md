[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/hZT7Ifs6)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12355035&assignment_repo_type=AssignmentRepo)
# Regression Model

Building and deploying a regression ML model.

This code is used in this [blog post](https://www.tekhnoal.com/regression-model.html).

## Requirements

Python 3
Pip-tools
To install pip-tools use this command:

```bash
pip install pip-tools
```
After that you can verify if it's installed correctly by writting this command:

```bash
pip-compile -h
```


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

Before running the command make dependencies, i use to run this command below first to make sure that i'll the latest version:
```bash
pip-compile requirements.in --upgrade
```
This will update the requirements.txt file;
After that now we can write this command:

```bash
make dependencies
```

## Running the Unit Tests
Before running the unit test suite we have to execute these commands first:
we'll do the same thing with the first pip-compile but this time with test_requirements.in so we make sure that we have the latest versions:
```bash
pip-compile test_requirements.in --upgrade
```

After that you can execute these command:

```bash
make test-dependencies
```

```bash
# run the test suite
make test

# clean up the unit tests
make clean-test
```

When i execute this command i had an error because the model was trained in a previous version of scikit-learn (0.24.2), so 3 tests were done but 2 failed. So i had to retrain the model in my current version of scikit-learn (1.3.2) and all tests succeed. T oretrain the model I've read the blog post to understand how the model was trained and i did the same with the latest version. The project now is working perfectly and is up to date.

## Running the Service

To start the service locally, execute these commands:

```bash
uvicorn rest_model_service.main:app --reload
```

## Generating an OpenAPI Specification

To generate the OpenAPI spec file for the REST service that hosts the model, execute these commands:

```bash
export PYTHONPATH=./
generate_openapi --output_file=service_contract.yaml
```

![Image 2023-11-13 à 22 58](https://github.com/uqam-lomagnin/logging-of-regression-model-socrate-01/assets/75217262/fa8e397b-a0dc-44be-ae74-abe7c3adf1d8)


The results are here:
![Image 2023-11-07 à 23 32](https://github.com/uqam-lomagnin/logging-of-regression-model-socrate-01/assets/75217262/7cdd1ef4-2bf2-42d6-adef-ceccee7f57c7)
![Image 2023-11-07 à 23 32](https://github.com/uqam-lomagnin/logging-of-regression-model-socrate-01/assets/75217262/42743c73-818d-4c13-b2a8-bff7cec843d5)



## Docker

To build a docker image for the service, run this command:

```bash
docker build -t insurance_charges_model:0.1.0 .
```

To run the image, execute this command:

```bash
docker run -d -p 80:80 insurance_charges_model:0.1.0
```

To watch the logs coming from the image, execute this command:

```bash
docker logs $(docker ps -lq)
```

To stop the docker image, execute this command:

```bash
docker kill $(docker ps -lq)
```
