# Nginx-Flask-Mongo Template

A production-ready template for Python/Flask applications with Nginx reverse proxy and MongoDB database.

## Table of Contents
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Development](#development)
- [License](#license)

## Project Structure

```
.
├── compose.yaml
├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
└── nginx
    └── nginx.conf
```

## Technologies Used

- **Nginx**: High-performance web server and reverse proxy
- **Flask**: Lightweight Python web framework
- **MongoDB**: NoSQL document database
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container orchestration

## Deployment

### Prerequisites
- Docker installed
- Docker Compose installed
- Port 80 available on host machine

### Steps

1. Clone the repository
2. Navigate to project directory
3. Start the services:
```bash
$ docker compose up -d
```

### Expected Result

After deployment, you should see three running containers:
```bash
$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                  NAMES
a0f4ebe686ff   nginx                       "/bin/bash -c 'envsu…"   2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp     nginx-flask-mongo_web_1
dba87a080821   nginx-flask-mongo_backend   "./server.py"            2 minutes ago   Up 2 minutes                          nginx-flask-mongo_backend_1
d7eea5481c77   mongo                       "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   27017/tcp              nginx-flask-mongo_mongo_1
```

4. Verify the application is running:
```bash
$ curl localhost:80
Hello from the MongoDB client!
```

5. To stop and remove containers:
```bash
$ docker compose down
```

## Development

### Running in Development Mode

1. Start the services in development mode:
```bash
$ docker compose -f compose.dev.yaml up -d
```

2. Access the application at `http://localhost:80`

3. Flask server will automatically reload on code changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
