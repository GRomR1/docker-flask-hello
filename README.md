# An example of the basic use of docker in web development

This is an example of [Docker](http://docker.com) usage with deployment a simple web app [flask-hello](https://github.com/GRomR1/flask-hello).

## Build image

To build image with all sources of application use this:
```shell script
docker build --tag flask-hello -f Dockerfile . 
```

The success result is:
```shell script
...
Successfully built 8662ac675d92
Successfully tagged flask-hello:latest
```

## Run container

Use `docker run` to run built application in container with name `flask`:
```shell script
docker run -p 80:5000 --name flask flask-hello 
```

The argument `-p 80:5000` will expose 80 port on the host and link it with 5000 container port to access the application.

## Open application

Just open next URL in browser: [http://localhost:80](http://localhost:80)