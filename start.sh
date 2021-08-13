#!/bin/sh
docker-compose up -d --build
docker-compose exec web python manage.py migrate account zero
docker-compose exec web python manage.py migrate