export MYSQL_ROOT_PASSWORD
export SECRET_KEY
docker stack deploy --compose-file docker-compose.yaml animal-noise-project
docker service update --replicas 3 animal-noise-project_animal-noise-front