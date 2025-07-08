# 💣 Underwater Mine Detection using Machine Learning

This project predicts whether a sonar reading corresponds to a **mine** or a **rock**, based on the **UCI SONAR dataset**. It combines:
- 🧠 A Logistic Regression model trained on 60 sonar frequencies
- 🖥️ A fullscreen Tkinter GUI
- 🎯 Smart predictions using only **5 user inputs**, padded with realistic random values

---

## 📁 Project Structure

Underwater_Mine_Detection/

├── sonar.csv 

├── finalized_model_LR.sav 

├── main_training.py 

├── gui_predictor.py 

├── image1.jpg 

├── README.md 

---

## 🛠 Technologies Used

- Python 3.x
- Tkinter (GUI)
- Scikit-learn (ML)
- NumPy, Pandas
- Pillow (for image background)

---

## 🧠 Model Details

- **Algorithm:** Logistic Regression
- **Training Accuracy:** ~83%
- **Testing Accuracy:** ~76%
- **Feature Count:** 60 sonar readings (5 from user + 55 random)

---

## 🚀 How to Run the Project

### 🔧 Step 1: Install Dependencies

```bash
pip install numpy pandas scikit-learn pillow

### 🧪 Step 2: Train the Model

```bash
python main_training.py

### 🖥️ Step 3: Launch the GUI

```bash
python gui_predictor.py

### 🧾 Sample Inputs

✅ Predict Mine (💣)
Freq1: 0.40
Freq2: 0.38
Freq3: 0.36
Freq4: 0.42
Freq5: 0.44

❌ Predict Rock (🪨)
Freq1: 0.02
Freq2: 0.04
Freq3: 0.01
Freq4: 0.03
Freq5: 0.05

## 👨‍💻 Contributors
Sudeep T S

Chandana K

Sai Sreeya T

Shreyas N B

## 📚 Dataset Reference
UCI Machine Learning Repository:
🔗 Sonar, Mines vs. Rocks
