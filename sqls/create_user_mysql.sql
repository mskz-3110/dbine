DROP DATABASE IF EXISTS dbine;
CREATE DATABASE dbine;

DROP USER IF EXISTS reader;
CREATE USER reader IDENTIFIED BY 'READER';

GRANT ALL ON dbine.* TO reader;
