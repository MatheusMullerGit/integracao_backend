CREATE USER admin WITH PASSWORD 'admin' CREATEDB;
CREATE DATABASE admin
    WITH 
    OWNER = admin
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE table contacts (
	id serial PRIMARY KEY,
	nome VARCHAR ( 100 ) NOT NULL,
	celular VARCHAR ( 13 ) NOT NULL
);
