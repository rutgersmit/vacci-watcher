# vacci-watcher
Docker image/Python script that checks prullenbakvaccin.nl and sends a Telegram message when is a vaccination is available.

Easy way
Pull the docker-compose.yaml and create the containers with docker-compose.
Change the environment variables before or edit the values afterwards.

To recieve notifications via Telegram, generate a bot (just Google how to) and find your chat id. Add those values to the ENV variables.
