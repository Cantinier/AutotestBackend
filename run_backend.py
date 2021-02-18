import config
from app import app

if __name__ == '__main__':
    app.run(host=config.SERVER_URL, port=config.SERVER_PORT)