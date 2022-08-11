# Flask + Actions Example

![example](https://github.com/andrewakim/flask-actions-example/.github/workflows/test-and-scan.yml/badge.svg?branch=master)

This is an example of how to build a simple Flask application using GitHub Actions.

## Requirements
* Docker
* Basic knowledge of Python

## Getting started
From the root of this project, first build the Docker image of your app:

* `docker build -t flask-actions-example .` - this creates a Docker image of your application.
* `docker run -dp 8080:8080 --name my-flask-app flask-actions-example` - we are running the flask-actions-example app, naming the container 'my-flask-app', and binding port 8080 so we can see the app in the next step.  Option `-d` runs the container in detached mode.
* Open up the browser of your choice and go to localhost:8080.

To stop the docker container run:
* `docker stop my-flask-app`
* `docker rm my-flask-app` will remove the container and keep a clean house.