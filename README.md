# Microservice Architecture
## Overview

This project demonstrates a simple microservice architecture with four components:
1. **API Service**: Handles API requests and interacts with the database.
2. **Frontend**: A simple static website that displays data retrieved from the API.
3. **Database**: Stores the data accessed by the API service.
4. **Centralized Auth Service**: Verifies JWT tokens and user authentication.

## Project Structure
microservice-architecture/
├── api-service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
├── frontend/
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── auth-service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
├── database/
│   └── init.sql
├── docker-compose.yml
└── .github/
    └── workflows/
        └── ci-cd.yml


## Getting Started

### Prerequisites

- Docker
- Docker Compose
- GitHub account (for CI/CD)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/microservice-architecture.git
    cd microservice-architecture
    ```

2. Build and run the services:
    ```bash
    docker-compose up --build
    ```

### API Service

The API service is built with Flask and provides a simple endpoint to retrieve a list of items.

- **Endpoint**: `/items`
- **Method**: `GET`
- **Response**: JSON array of items

### Auth Service

The Auth service is built with Flask and uses JWT for authentication.

- **Endpoint**: `/verify`
- **Method**: `POST`
- **Request Body**: `{"token": "your_jwt_token"}`
- **Response**: JSON message indicating token validity

### Frontend

The frontend is a simple static website that fetches data from the API service and displays it.

### Database

A PostgreSQL database initialized with a script to create the `items` table and insert sample data.

## CI/CD

This project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/ci-cd.yml`.

- **Build and Test**: Installs dependencies and runs unit tests for API and Auth services.
- **Docker Build and Push**: Builds Docker images and pushes them to Docker Hub.
- **Deployment**: Deploys the services using Docker Compose.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


