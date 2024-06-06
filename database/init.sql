CREATE DATABASE microservice;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(80) NOT NULL
);
INSERT INTO items (name) VALUES ('Item 1'), ('Item 2');
