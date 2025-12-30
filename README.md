# 🚢 Titanic Survival Prediction (82.55% Accuracy)

This is my **first Machine Learning project** where I predict whether a passenger would survive the Titanic tragedy based on features like class, age, gender, fare, and embarked location.

check tour survival https://titanic-survival-ml-project.onrender.com




---API https://titanic-survival-ml-project.onrender.com/predict

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


3 -> Class<Br>
female -> sex<Br>
26-> age<Br>
0 -> number of siblings<Br>
0 - >numper of parent<Br>
7 -> ticked price you paid<Br>
'S' -> place where you live usualy (S : Southemphetom England , C : Cherburg France , Q : Queenstown Irland)


data = pd.DataFrame([{
    'Pclass': d.Pclass,
    'Sex': d.Sex,
    'Age': d.Age,
    'Siblings': d.Siblings,    
    'Parents': d.Parents,
    'Fare': d.ticket_price,
    'Embarked': d.place
    }])



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
