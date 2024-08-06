def ageValidate(age):
    if not isinstance(age,int):
        raise RuntimeError ("Type is not valid...")
    if age<1 or age>120:
        raise RuntimeError ("Out of range...")
    return age

try:
    age=ageValidate(39)
    print(f"Age Is : {age}")
except RuntimeError as error:
    print (error)

print(100*'-')