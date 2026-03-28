# 💧 Smart Water Quality Analyzer & Safety Predictor

## 📌 Problem
Access to clean drinking water is a major issue. Many people cannot easily determine whether water is safe to drink.

## 🚀 Solution
This project uses Machine Learning to predict water quality based on parameters like pH, hardness, and turbidity.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📊 Features
- Predicts whether water is Safe or Unsafe
- Simple and interactive UI
- Uses real-world dataset

## ⚙️ How It Works
1. User enters water parameters  
2. Model processes input data  
3. Decision Tree predicts Safe/Unsafe  
4. Output is displayed on UI

2. Train model:
python train.py

3. Run application:
streamlit run app.py

## 📁 Project Structure
- app.py → User interface
- train.py → Model training
- water_quality.csv → Dataset
- requirements.txt → Libraries

## 🧠 Model Used
Decision Tree Classifier is used for classification of water as safe or unsafe.

## 🔬 Impurities Analyzed in This Project

This project analyzes different water quality parameters that indicate the presence of impurities:

### 1. pH (Acidity/Alkalinity)
Indicates whether water is acidic or basic. Extreme pH levels can be harmful and indicate chemical contamination.

### 2. Hardness
Represents the amount of dissolved calcium and magnesium salts. High hardness affects water usability.

### 3. Total Dissolved Solids (TDS)
Measures dissolved substances such as salts, minerals, and metals. High TDS indicates poor water quality.

### 4. Chloramines
Chemicals used for water disinfection. Excess levels may be harmful.

### 5. Sulfate
A naturally occurring substance that can affect taste and may cause health issues at high levels.

### 6. Conductivity
Shows the ability of water to conduct electricity, which increases with the presence of dissolved ions (impurities).

### 7. Organic Carbon
Indicates the presence of organic matter, which may lead to bacterial growth.

### 8. Trihalomethanes
Chemical compounds formed during water treatment that can be harmful in high amounts.

### 9. Turbidity
Measures water clarity. High turbidity indicates suspended particles and possible contamination.

## 📈 Result
The model predicts water safety with reasonable accuracy based on input parameters.
Model Accuracy: ~65–70%

## 👨‍💻 Author
Sameer yadav