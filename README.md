# Flask-MongoDB Docker Application

## Readme Like You Mean It 😂
*This isn't just a README. It's the README. The one your future self will thank you for. Or curse, depending on your commit messages*

## Overview

This is a containerized Flask web application with a MongoDB database using Docker Compose.

## Features

- Flask web framework   `# Python framework for building websites and web applications`
- MongoDB database integration
- Docker containerization
- Hot-reload for development

## Prerequisites

- Docker: Download and Install [DOCKER](https://docs.docker.com/engine/install/)
- Docker Compose: Install [DOCKER COMPOSE](https://docs.docker.com/compose/install/)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/William-Muko/Flask-MongoDB-App.git
cd Flask-MongoDB-App
```

2. Start the application:
```bash
docker-compose up
```

3. Open your browser and navigate to `http://localhost:5000`

## Development

To run in development mode with hot reload:
```bash
docker-compose up --build
```

The application will automatically reload when you make code changes.

## API Endpoints

- `GET /` - Returns a greeting message

## Database

MongoDB is available at:
- Connection string: `mongodb://localhost:27017`, which recommends you use `MongoDB Compass`
- Direct access: `mongodb://mongo:27017` (from within Docker network)

## Project Structure

```
├── app.py              # Flask application
├── Dockerfile          # Docker image definition
├── docker-compose.yml  # Multi-container setup
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to exclude from Git
├──  README.md          # Project documentation        
```

## Environment Variables

- `MONGO_URI`: MongoDB connection string (default: mongodb://mongo:27017/mydatabase)

## Useful Commands

- Start services: `docker-compose up`
- Start in background: `docker-compose up -d`
- Stop services: `docker-compose down`
- View logs: `docker-compose logs`
- Rebuild images: `docker-compose up --build`

## License

MIT License, see the [LICENSE](LICENSE) file for details.

*If you've made it this far, you deserve a coffee. Or a raise. Or both ☕🤑* *Happy Coding!🧑🏽‍💻*


