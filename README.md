# Kino Request Helper

## Purpose
Script was developed to query the Loteria Electrónica de Puerto Rico results API, and obtain the latest results for the game "Kino". Results are then stored in a sqlite database.

## Configuration
On the provided [config.yaml](./config.yaml) file, the amount of records to be queried for the results API can be adjusted. This file also contains specific information regards the local SQLite database configuration.

## Dependecies
This script was developed using python version 3.10, and makes use of the following dependecies:
- [requests](https://pypi.org/project/requests/)
- [PyYAML](https://pypi.org/project/PyYAML/)
