# Introduction
The objective of this project is to forecast the price of a pre-owned automobile by considering factors such as the manufacturer's name, model name, and various other parameters.

- **Modeling:**
    - How well does your model perform?
        - Mô hình hồi quy XGBoost hoạt động tốt nhất trong số các mô hình được cung cấp. Nó có điểm R2 cao nhất, nghĩa là nó phù hợp nhất với dữ liệu trong thế giới thực. Ngoài ra, nó có giá trị MAE và RMSE thấp nhất, cho thấy dự đoán của nó nhìn chung chính xác hơn.
    - How effective is the selected metric in evaluating model performance?
        - R2 Score, MAE và RMSE đều chỉ ra rằng Hồi quy XGBoost là mô hình hoạt động tốt nhất. Điều này cho thấy các số liệu đã chọn có hiệu quả trong việc đánh giá hiệu suất của mô hình cho bài toán dự đoán giá xe.


    | Metric | Strengths | Weaknesses |
    | --- | --- | --- |
    | R2 score | Cho biết mức độ phù hợp của mô hình với dữ liệu | Không nhạy cảm với outlier, nếu thêm các đặc trưng không liên quan vẫn được đánh giá tốt  |
    | MAE | Độ đo hiệu suất của mô hình tốt hơn R2 Score, ít nhạy cảm hơn với các outliers | Không cung cấp thông tin về hướng của lỗi |
    | RMSE | Độ đo tốt hơn MAE, Vì nó phạt các giá trị error nặng hơn. | Nhạy cảm hơn với các giá trị outliers |
    - How could your model be improved?
        - **Feature engineering**: Tạo đặc trưng mới từ các đặc trưng hiện có hoặc chuyển đổi các đặc trưng hiện có để làm cho chúng có nhiều thông tin hơn cho mô hình.
        - **Data Cleaning**: Loại bỏ hoặc fill các giá trị bị thiếu, xử lý các giá trị ngoại lệ và chuẩn hóa các đặc trưng để đảm bảo chúng ở scale tương tự.
        - Tìm thêm nhiều mô hình khác nhau để thử nghiệm.
        - **Hyperparameter tuning**: Tinh chỉnh tham số của mô hình để tối ưu hoá hiệu suất của chúng.
        - **Ensample Methods**: Kết hợp nhiều mô hình thành một mô hình tổng hợp để cải thiện hiệu suất tổng thể (bagging và boosting).
        - Cải thiện khả năng của mô hình trong việc nắm bắt các mối quan hệ và mẫu phức tạp trong dữ liệu.
        - **Cross-validation**: Đánh giá hiệu suất của mô hình trên các tập hợp con dữ liệu khác nhau và tránh bị overfitting.
        - Phân tích tầm quan trọng của các đặc trưng.
  
- **Backend:**
  - Present my idea for db car price prediction:
      - Bảng Cars chứa các FK của những bảng liên quan giúp dễ quản lý và truy vấn thông tin.
      - Các bảng origin, type, gearbox type, fuel type, color, condition để dễ dàng chuẩn hóa dữ liệu và giảm sự dư thừa.
      - Mỗi table được ref đều chứa ID riêng biệt và mô tả cho nó, giúp dễ dàng quản lý và truy vấn dữ liệu liên quan.
      - Các FK được liên kết với bảng Car do đó sẽ đảm bảo được tính toàn vẹn dữ liệu. Dễ dàng ngăn chặn các thông tin sai lệch từ người dùng.
      - Điều này có lợi cho các truy vấn và phân tích liên quan đến giá xe và các thuộc tính của chúng.
  - How robust and efficient is the backend system you develop?
      - **Chất lượng của dữ liệu** được sử dụng để huấn luyện và thử nghiệm mô hình dự đoán là rất quan trọng. Dữ liệu chất lượng cao, sạch sẽ và cập nhật mới nhất sẽ dẫn đến những dự đoán chính xác hơn.
      - Việc lựa chọn và thiết kế đặc trưng (feature) được sử dụng trong mô hình dự đoán có thể tác động đáng kể đến hiệu suất của nó. Các đặc trưng liên quan, chẳng hạn như thông số kỹ thuật của xe, xu hướng thị trường và dữ liệu lịch sử về giá, cần được lựa chọn cẩn thận.
      - Việc lựa chọn thuật toán machine learning có thể ảnh hưởng đến hiệu quả và độ chính xác của hệ thống.
      - Mô hình phải được đánh giá bằng các số liệu thích hợp, chẳng hạn như sai số bình phương trung bình (MSE) hoặc sai số tuyệt đối trung bình (MAE), để đánh giá độ chính xác và độ tin cậy của nó.
      - Xử lý lượng dữ liệu và lưu lượng truy cập ngày càng tăng một cách hiệu quả (Cloud).
      - Bảo trì và giám sát: Các mô hình có thể cần được đào tạo lại định kỳ khi dữ liệu phát triển.
      - Khả năng diễn giải của mô hình, đặc biệt là các trường hợp dự đoán có thể gây ra hậu quả đáng kể.
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
- Ridge Regression: The Ridge Regression model has the highest R2 Score, reaching 0.6777. This indicates that the model best fits the real data among the evaluated models. However, the Ridge Regression model has higher MAE and RMSE compared to some other models.

- Linear Regression: The Linear Regression model has the second-highest R2 Score, reaching 0.6421. This model has lower MAE and RMSE compared to the Ridge Regression model but higher than some other models.

- Random Forest Regression: The Random Forest Regression model has the lowest R2 Score, reaching 0.3043. This suggests that the model is not a good fit for the real data compared to other models. However, the Random Forest Regression model has lower MAE and RMSE compared to some other models.

- Decision Tree (max_depth=2): The Decision Tree model with max_depth=2 has a lower R2 Score compared to the Linear Regression and Ridge Regression models but higher than the Random Forest Regression model. This model has lower MAE and RMSE compared to the Random Forest Regression model but higher than some other models.

- Decision Tree (max_depth=5): The Decision Tree model with max_depth=5 has an R2 Score equivalent to the Decision Tree with max_depth=2. This model has lower MAE and RMSE compared to the Random Forest Regression model.

- XGBoost Regression: The XGBoost Regression model has the third-highest R2 Score, reaching 0.7118. This model has the lowest MAE and RMSE among the evaluated models.

- Lasso Regression: The Lasso Regression model has an undefined R2 Score because it has some predicted values equal to 0.

⇒ Based on the analysis above, it can be seen that the XGBoost Regression model is the most suitable regression model for the real data among the evaluated models. This model has the highest R2 Score and the lowest MAE and RMSE.

# Error Analysis (Vietnamese version)
- Ridge Regression: Mô hình Ridge Regression có R2 Score cao nhất, đạt 0.6777. Điều này cho thấy mô hình phù hợp với dữ liệu thực tế tốt nhất trong số các mô hình được đánh giá. Tuy nhiên, mô hình Ridge Regression có MAE và RMSE cao hơn so với một số mô hình khác.
- Linear Regression: Mô hình Linear Regression có R2 Score thứ hai, đạt 0.6421. Mô hình này có MAE và RMSE thấp hơn so với mô hình Ridge Regression nhưng cao hơn so với một số mô hình khác.
- Random Forest Regression: Mô hình Random Forest Regression có R2 Score thấp nhất, đạt 0.3043. Điều này cho thấy mô hình không phù hợp với dữ liệu thực tế tốt như các mô hình khác. Tuy nhiên, mô hình - Random Forest Regression có MAE và RMSE thấp hơn so với một số mô hình khác.
- Decision Tree (max_depth=2): Mô hình Decision Tree với max_depth=2 có R2 Score thấp hơn so với mô hình Linear Regression và Ridge Regression nhưng cao hơn so với mô hình Random Forest Regression. Mô hình này có MAE và RMSE thấp hơn so với mô hình Random Forest Regression nhưng cao hơn so với một số mô hình khác.
- Decision Tree (max_depth=5): Mô hình Decision Tree với max_depth=5 có R2 Score tương đương với mô hình Decision Tree với max_depth=2. Mô hình này có MAE và RMSE thấp hơn so với mô hình Random Forest Regression.
- XGBoost Regression: Mô hình XGBoost Regression có R2 Score cao thứ ba, đạt 0.7118. Mô hình này có MAE và RMSE thấp nhất trong số các mô hình được đánh giá.
- Lasso Regression: Mô hình Lasso Regression có R2 Score không xác định do có một số giá trị dự đoán bằng 0.

=> Dựa vào phân tích trên, có thể thấy rằng mô hình XGBoost Regression là mô hình hồi quy phù hợp nhất với dữ liệu thực tế trong số các mô hình được đánh giá. Mô hình này có R2 Score cao nhất và MAE và RMSE thấp nhất.
# Improvements
- Remove outliers from the data.
- Identify the similarity between the relevant features in the data.
- Utilize the Gradient Boosting technique, specifically XGBoost, CatBoost, and LightGBM.
- Explore additional features for the model training process (Currently 8/15).

