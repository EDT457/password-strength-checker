import tkinter
min_length = 12

def check_password(password):
    score = 0
    if len(password) > min_length:
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

def update_counter(event):
    current_length = len(user_input.get())
    length.config(text = f"Characters: {current_length}/{min_length}", fg="green" if current_length >= min_length else "red")

password_visible = False

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("400x300")

tkinter.Label(root, text = "Input Password").pack()

user_input = tkinter.Entry(root, show="•")
user_input.bind("<KeyRelease>", update_counter)
user_input.pack()

showhide = tkinter.Button(root, text="Show", command= toggle)
showhide.pack()

length = tkinter.Label(root, text = f"Characters: 0/{min_length}", fg="red")
length.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

tkinter.Button(root, text="Submit", command=lambda: on_submit(result_label)).pack()

root.mainloop()
