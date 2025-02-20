import os
from dotenv import load_dotenv

load_dotenv("secrets.env")

secret1=os.getenv("SECRET1")
secret2=os.getenv("SECRET2")


print(secret1,secret2)
