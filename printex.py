import os
from dotenv import load_dotenv

load_dotenv("secrets.env")
# print("*******SECRETS FROM ENV FILE********")
# secret1=os.getenv("SECRET1")
# secret2=os.getenv("SECRET2")


# print(secret1,secret2)
# print("*************************************")
# print("*******SECRETS FROM inline actions********")
# secret3=os.environ.get("DB_USER")
# secret4=os.environ.get("DB_PASS")


# print(secret3,secret4)
# print("*************************************")
print("******* SECRETS FROM GITHUB ACTIONS ********")

TEST_SECRET_1 = os.environ.get("TEST_SECRET_1")
TEST_SECRET_2 = os.environ.get("TEST_SECRET_2")

print(f"DB_USER: {TEST_SECRET_1}")  
print(f"DB_PASS: {TEST_SECRET_2}")
print("*************************************")
