from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import pickle

model = pickle.load(open("finalized_model_LR.sav", "rb"))

def predict():
    try:
        import random

        user_inputs = [
            float(T1.get()),
            float(T2.get()),
            float(T3.get()),
            float(T4.get()),
            float(T5.get())
        ]

        random_floats = [round(random.uniform(0.01, 0.45), 4) for _ in range(55)]

        input_data = np.array([user_inputs + random_floats])

        prediction = model.predict(input_data)[0]

        T6.delete(0, END)
        T6.insert(0, prediction)

        if prediction == 'R':
            messagebox.showinfo("Prediction Result", "The object is a Rock 🪨")
        else:
            messagebox.showinfo("Prediction Result", "The object is a Mine 💣")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input! Please enter float values.\n\n{e}")

master = Tk()
master.title("SONAR Mine Detection GUI")

master.attributes('-fullscreen', True)

master.bind("<Escape>", lambda e: master.destroy())

bg_image = Image.open("image1.jpg")
bg_image = bg_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(master, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


frame = Frame(master, bg="black", padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, text="SONAR PREDICTION SYSTEM", font=("Helvetica", 16, "bold"), fg="white", bg="black").pack(pady=10)

labels = ["Freq1", "Freq2", "Freq3", "Freq4", "Freq5"]
for i, label in enumerate(labels):
    Label(frame, text=label, bg="black", fg="lightblue", font=("Arial", 12)).pack()
    entry = Entry(frame, width=25)
    entry.pack(pady=2)
    globals()[f"T{i+1}"] = entry

Label(frame, text="Prediction", bg="black", fg="lightgreen", font=("Arial", 12)).pack(pady=5)
T6 = Entry(frame, width=25)
T6.pack(pady=2)

Button(frame, text="Predict", command=predict, width=20, bg="green", fg="white").pack(pady=10)
Button(frame, text="Exit", command=master.destroy, width=20, bg="red", fg="white").pack()

master.mainloop()
