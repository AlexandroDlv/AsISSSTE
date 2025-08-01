import os
from dotenv import load_dotenv
from pymongo import MongoClient

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)
MONGODB_URI = os.environ['MONGODB_URI']
client = MongoClient(MONGODB_URI)

db=client['AsISSSTE']