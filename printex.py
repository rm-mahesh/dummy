import os
DUMMY = os.getenv("DUMMY_SECRET")


print("Hello am new to github")
if DUMMY:
    print("Goog to go")
else:
    print("Issue exists broo")
print(f'secret : {DUMMY}')