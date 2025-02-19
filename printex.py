import os
print(os.environ)

DUMMYY = os.getenv("DUMMY_SECRET")


print("Hello am new to github")
if DUMMYY is not None:
    print("Goog to go")
else:
    print("Issue exists broo")
print(f'secret : {DUMMYY}')