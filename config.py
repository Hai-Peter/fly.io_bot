import os
MODE = os.environ.get('MODE', 'prod')
WEB_HOOK = os.environ["WEB_HOOK"]
BOT_TOKEN = os.environ["5828213778:AAEcT5NlixzsK-8yWzG4XcNxu05A55ysB6k"]
PORT = int(os.environ.get('PORT', '8080'))
NICK = os.environ.get('NICK', None)
config = {
    "email": os.environ["duckhai23@proton.me"],
    "password": os.environ["haind2355"]
}
# deploy.sh config.py main.yml README.md docker-compose.yml github-action-secrets
