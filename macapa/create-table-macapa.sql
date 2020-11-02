CREATE USER 'admin'@'localhost' IDENTIFIED BY PASSWORD 'admin';
CREATE DATABASE IF NOT EXISTS admin;
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';

CREATE table contacts (
	id serial PRIMARY KEY,
	nome VARCHAR ( 200 ) NOT NULL,
	celular VARCHAR ( 20 ) NOT NULL
);
