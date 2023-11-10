# Introduction
The objective of this project is to forecast the price of a pre-owned automobile by considering factors such as the manufacturer's name, model name, and various other parameters.

- **Modeling:**
    - How well does your model perform?
        - As you can see, XGBoost Regression has a significant advantage over the other models in terms of R2 score, MAE, and RMSE. This indicates that it consistently produces more accurate predictions.
    - How effective is the selected metric in evaluating model performance?
        - R2 score measures the proportion of the variance in the dependent variable that is predicted by the model. It is a good indicator of how well the model fits the data. However, R2 score is not sensitive to outliers and can be artificially inflated by including irrelevant features in the model.
        - MAE measures the average absolute difference between the predicted and actual values. It is a more robust measure of model performance than R2 score, as it is less sensitive to outliers. However, MAE does not provide any information about the direction of the errors.
        - RMSE measures the average squared difference between the predicted and actual values. It is a more sensitive measure of model performance than MAE, as it penalizes large errors more heavily. However, RMSE is also more sensitive to outliers.
        - R2 score, MAE, and RMSE all indicate that XGBoost Regression is the best-performing model. This suggests that the selected metrics are effective in evaluating model performance for this particular task.
---------------




| Metric   | Strengths                                                                                  | Weaknesses                                                                               |
|:-------- | ------------------------------------------------------------------------------------------ |:---------------------------------------------------------------------------------------- |
| R2 score | Good indicator of how well the model fits the data                                         | Not sensitive to outliers, can be artificially inflated by including irrelevant features |
| MAE      | More robust measure of model performance than R2 score, less sensitive to outliers         | Does not provide any information about the direction of the errors                       |
| RMSE     | More sensitive measure of model performance than MAE, penalizes large errors more heavily. | More sensitive to outliers                                                               |

-----------
- **Modeling:**
    - How could your model be improved?
        - **Feature engineering**: Creating new features from existing ones or transforming existing features to make them contain more information for the model.
        - **Data Cleaning**: Removing or filling missing values, handling outliers, and standardizing features to ensure they are on a similar scale.
        - **Modeling**: Exploring various different models to experiment
        - **Hyperparameter tuning**: Adjusting the model's parameters to optimize their performance.
        - **Ensample Methods**: Combining multiple models into an aggregated model to improve overall performance (e.g., bagging and boosting).
        - **Cross-validation**: Evaluating the model's performance on different subsets of data and avoiding overfitting.
        - Analyzing the importance of features. Enhancing the model's ability to capture complex relationships and patterns in the data.
---------
- **Backend:**
  - How robust and efficient is the backend system you develop?
      - **Data quality** used for training and testing predictive models is very important. High-quality, clean, and up-to-date data leads to more accurate predictions.
      - The choice and design of features used in the prediction model can significantly impact its performance. Relevant features, such as car specifications, market trends, and historical price data, need to be carefully selected.
      - The choice of machine learning algorithms can influence the efficiency and accuracy of the system.
      - The model must be evaluated using appropriate metrics, such as mean squared error (MSE) or mean absolute error (MAE), to assess its accuracy and reliability.
      - Efficient handling of the growing volume of data and access (Cloud).
      - Maintenance and monitoring: Models may need periodic retraining as the data evolves.
      - The interpretability of the model, especially in cases where predictions can have significant consequences.
# Demo
https://github.com/truong11062002/vucar_homework_assignment/assets/74360292/ed9c3b78-9012-48ad-bbf8-88f546a5741a

# Setup env
```
git clone https://github.com/truong11062002/vucar_homework_assignment.git
cd vucar_homework_assignment
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

| Model                       | R2 Score | MAE    | MSE     | RMSE   |
| --------------------------- |:-------- | ------ |:------- |:------ |
| Ridge Regression            | 0.6777   | 0.0038 | 0.00013 | 0.0117 |
| **Linear Regression**       | 0.6421   | **0.0037** | 0.0002  | 0.0123 |
| Random Forest Regression    | 0.3043   | 0.0080 | 0.0003  | 0.0172 |
| Decision Tree (max_depth=2) | 0.2691   | 0.0081 | 0.0003  | 0.0176 |
| Decision Tree (max_depth=5) | 0.2827   | 0.0067 | 0.0003  | 0.0175 |
| XGBoost Regression          | **0.7118**   | 0.0042 | **0.00012** | **0.0111** |
| Lasso Regression            | Nan      | 0.0091 | 0.0004  | 0.0206 |

# Error Analysis (English version)
Based on the experimental results table, we can see that: 
- XGBoost Regression provides the best results with the highest R2 Score of 0.7118, the lowest MSE of 0.00012, and the lowest RMSE of 0.0111. This indicates that this model makes the most accurate predictions compared to other models.
- Linear Regression achieves the lowest MAE of 0.0037, demonstrating the smallest average absolute error.
- Ridge Regression and Linear Regression also perform reasonably well, with R2 Scores of 0.6777 and 0.6421, respectively.
- Random Forest Regression, Decision Tree (max_depth=2), and Decision Tree (max_depth=5) yield less favorable results with low R2 Scores (around 0.3) and higher MAE, MSE, and RMSE compared to other models.
- Lasso Regression cannot compute an R2 Score (resulting in "Nan"), and it provides the highest MAE, MSE, and RMSE values among all the models.
=> Based on the analysis above, it can be seen that the XGBoost Regression model is the most suitable regression model for real-world data among the evaluated models. This model has the highest R2 Score and the lowest MAE and RMSE.

# Error Analysis (Vietnamese version)
Dựa vào bảng thực nghiệm ta có thể thấy rằng:
- XGBoost Regression cho kết quả tốt nhất với chỉ số R2 Score cao nhất là 0.7118, MSE thấp nhất là 0.00012 và RMSE thấp nhất là 0.0111. Điều này cho thấy mô hình này dự đoán chính xác nhất so với các mô hình khác.
- Linear Regression cho kết quả MAE thấp nhất là 0.0037, điều này cho thấy mô hình này có độ lỗi trung bình tuyệt đối nhỏ nhất.
- Ridge Regression và Linear Regression cũng cho kết quả khá tốt với R2 Score lần lượt là 0.6777 và 0.6421.
- Random Forest Regression, Decision Tree (max_depth=2) và Decision Tree (max_depth=5) cho kết quả không tốt lắm với R2 Score thấp (khoảng 0.3) và MAE, MSE, RMSE cao hơn so với các mô hình khác.
- Lasso Regression không thể tính được R2 Score (kết quả là Nan), và cho kết quả MAE, MSE, RMSE cao nhất trong tất cả các mô hình.

=> Dựa vào phân tích trên, có thể thấy rằng mô hình XGBoost Regression là mô hình hồi quy phù hợp nhất với dữ liệu thực tế trong số các mô hình được đánh giá. Mô hình này có R2 Score cao nhất và MAE và RMSE thấp nhất.
# Future works
- Remove outliers from the data.
- Identify the similarity between the relevant features in the data.
- Utilize the Gradient Boosting technique, specifically XGBoost, CatBoost, and LightGBM.
- Explore additional features for the model training process (Currently 8/15).

