is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male or tall or both.")
elif is_male and not(is_tall):
    print("You are a short male.")

elif not(is_male) and (is_tall):
    print("You are a tall or short male.")
else:
    print("You are a female and short.")