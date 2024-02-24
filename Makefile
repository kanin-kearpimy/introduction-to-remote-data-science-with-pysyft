.PHONY: start
start_server: 
	cd ./server && make start
start_clients:
	cd ./clients && make start