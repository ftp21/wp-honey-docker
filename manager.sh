#!/bin/bash
#stop docker-compose down -v
#start docker-compose up --build --force-recreate --no-deps -d
case "$1" in 
start)
   docker-compose up --build --force-recreate --no-deps -d
   ;;
stop)
   docker-compose down -v
   ;;
status)
   docker-compose ps
   ;;
*)
   echo "Usage: $0 {start|stop|status}"
esac

exit 0 
