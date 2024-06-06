#!/bin/sh

# call wait-for-it with args and then start node if it succeeds
exec ./wait-for-it.sh -h "${DB_HOST}" -p "${DB_PORT}" -t 300 -s -- node start