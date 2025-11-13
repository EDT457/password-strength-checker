import tkinter


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

def on_submit(rl):
    strength = ["Weaker", "Weak", "Strong", "Very Strong"]
    password = user_input.get()
    res = check_password(password)
    rl.config(text = strength[res])


def toggle():
    global password_visible
    if password_visible:
        password_visible = False
        showhide.config(text = "Show")
    else:
        password_visible = True
        showhide.config(text = "Hide")
    user_input.config(show="•" if not password_visible else "")

password_visible = False

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("400x300")

tkinter.Label(root, text = "password").pack()

user_input = tkinter.Entry(root, show="•")
user_input.pack()

showhide = tkinter.Button(root, text="Show", command= toggle)
showhide.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

tkinter.Button(root, text="Submit", command=lambda: on_submit(result_label)).pack()

root.mainloop()
