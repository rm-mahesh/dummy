import os
secret = os.getenv("DUMMY_SECRET")


print("Hello am new to github")
if secret:
    print("Goog to go")
else:
    print("Issue exists broo")
print(f'secret : {secret}')