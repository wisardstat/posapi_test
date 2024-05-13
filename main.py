# from dotenv import load_dotenv
#from dotenv import dotenv_values
from os import getenv
import uvicorn

#load_dotenv()

PORT = int(getenv('PORT', 8080))
HOST = '127.0.0.1'

if __name__ == '__main__':
    uvicorn.run('app.api:app', host = HOST, port = PORT, reload = True)