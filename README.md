# 🚢 Titanic Survival Prediction (82.55% Accuracy)

This is my **first Machine Learning project** where I predict whether a passenger would survive the Titanic tragedy based on features like class, age, gender, fare, and embarked location.

---API IN Progress

## 📌 Project Highlights
- 🎯 Accuracy: **82.55%**
- 🤖 Model: **KNN (k=27)**
- ⚙️ Techniques Used:  
  - PCA (0.95 variance preserved)  
  - Pipeline + ColumnTransformer  
  - StandardScaler & OneHotEncoder  
- 🎛 User input prediction system

---
Uses : 

model = joblib.load("titanic_model.pkl") <Br>
model.predict([[3, "female", 26, 0, 0, 7, "S"]])


3 -> Class
female -> sex
26-> age
0 -> number of siblings
0 - >numper of parent
7 -> ticked price you paid
'S' -> place where you live usualy (S : Southemphetom England , C : Cherburg France , Q : Queenstown Irland)




## 🧠 Workflow
```text
Data → Preprocessing → Encoding + Scaling → PCA → KNN Model → Prediction


🧠              
Feature	        Type	        Notes

Pclass	        Categorical	    OneHotEncoded
Sex	            Categorical	    OneHotEncoded
Age	            Numeric	        Scaled
Siblings	    Numeric	        Scaled
Parents	        Numeric	        Scaled
Fare	        Numeric	        Scaled
Embarked	    Categorical	    OneHotEncoded
