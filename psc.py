
def check_password(password):
    score = 0
    if len(password) > 7:
        score += 1
    for char in password:
        if char.isupper():
            score += 1
            break
    for char in password:
        if char.isdigit():
            score += 1
            break
    return score


print("score: " + str(check_password(input("Input your password:"))))
