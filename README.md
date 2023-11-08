# Introduction
The objective of this project is to forecast the price of a pre-owned automobile by considering factors such as the manufacturer's name, model name, and various other parameters.
# Demo
https://github.com/truong11062002/vucar_homework_assignment/assets/74360292/ed9c3b78-9012-48ad-bbf8-88f546a5741a

# Setup env
```
git clone https://github.com/truong11062002/vucar_homework_assignment.git
conda create --name <your_env>
conda activate <your_env>
conda install pip
pip install -r requirements.txt
```

# Run app
```
flask --app application run
```

# Run with debugging
```
flask --app application run --debug
```
And then running on http://127.0.0.1:5000

# Experimental Results

| Model | R2 Score | num_folds |
|---|---|---|
| Ridge Regression | 0.6873 | 5 |
| **Linear Regression** | **0.6959** | 5 |
| Random Forest Regression | 0.1948 | 5 |
| Decision Tree (max_depth=2) | 0.1249 | 5 |
| Decision Tree (max_depth=5) | 0.4119 | 5 |
| XGBoost Regression | 0.6810 | 5 |
| Lasso Regression | 0.6958 | 5 |

# Error Analysis
- R2 is used for evaluating the output results, a higher R2 indicates better results."
- Num_folds is the number of times data is divided into train and test sets. A higher Num_folds indicates a stronger model.
- Based on the results, Linear Regression achieved the highest R2 Score (0.6959), followed by Ridge Regression (0.6873) and Lasso Regression (0.6958). This shows that these models are quite suitable for predicting car prices.
- The Random Forest Regression and Decision Tree (max_depth=2) models achieved the lowest results with R2 Scores of 0.1948 and 0.1249, respectively. This indicates that these models are not suitable for this dataset. Additionally, Decision Tree (max_depth=5) achieved 0.4119, higher than Random Forest but lower than Linear Regression.

⇒ In general, Linear Regression is the best choice for this car price prediction dataset. However, Random Forest Regression could be a good choice if the model is less sensitive to outliers.

# Improvements
- Remove outliers from the data.
- Identify the similarity between the relevant features in the data.
- Utilize the Gradient Boosting technique, specifically XGBoost, CatBoost, and LightGBM.
- Explore additional features for the model training process (Currently 6 out of 15).

