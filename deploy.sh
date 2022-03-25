export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml card-deck-stack
docker service update --replicas 3 card-deck-stack_front-end