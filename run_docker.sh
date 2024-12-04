#!/bin/bash

# Function to display usage
usage() {
  echo "Usage: $0 -auto | -name <name>"
  exit 1
}

# Function for auto mode
auto_mode() {
  echo "=> Auto mode selected."

  # echo 'Stopping containers ...'
  # docker stop $(docker ps -a -q)
  
  local containers=(\
    "warehouse" \
    "kafka" \
    "producer-owm" \
    "producer-faker" \
    "producer-custom" \
    "consumer-logging" \
    "data-visualize" \
  )

  echo '=> Rerunning containers ...'
  for container in "${containers[@]}"; do
    echo "Running container: $container"
    name_mode "$container"
    sleep 10
  done
}

# Function for name mode
name_mode() {
  local service=$1
  local opts=$2
  if [ -z "$service" ]; then
      echo "Error: Missing name argument."
      usage
  fi

  echo "=> Running service: $service || Opts: $opts"

  docker compose \
    -f ./docker-compose.yml \
    up \
    $service \
    --build \
    --detach
}

# Check if no arguments are passed
if [ $# -eq 0 ]; then
  usage
fi

# Parse arguments
case "$1" in
  -auto)
    auto_mode
    ;;
  -name)
    name_mode "$2" "$3"
    ;;
  *)
    echo "Error: Invalid option."
    usage
    ;;
esac
