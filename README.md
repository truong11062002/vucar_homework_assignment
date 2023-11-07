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
- R2 được sử dụng cho quá trình đánh giá kết quả đầu ra, R2 cao hơn cho thấy kết quả tốt hơn.
- Num_folds là số lần dữ liệu được chia thành train, test. Num_folds càng lớn cho thấy mô hình càng mạnh mẽ hơn.
- Dựa vào kết quả trên, Linear Regression đạt được kết quả cao nhất với R2 Score (0.6959), kế đến là Ridge Regression (0.6873) và Lasso Regression (0.6958). Điều này cho thấy rằng, những mô hình này khá phù hợp cho việc dự đoán giá xe hơi.
- Mô hình Random Forest Regression và Decision Tree (max_depth=2) có kết quả thấp nhất với R2 Score lần lượt là 0.1948, 0.1249. Điều này cho thấy những mô hình này không thích hợp với dữ liệu này. Ngoài ra Decision Tree (max_depth=5) đạt được 0.4119 cao hơn Random Forest nhưng lại thấp hơn Linear Regression.

⇒ Nhìn chung, Linear Regression là lựa chọn tốt nhất cho bộ dữ liệu về dự đoán giá xe này. Tuy nhiên, Random Forest Regression có thể là lựa chọn tốt nếu mô hình less sensitive hơn với các outliers.

# Improvements
- Loại bỏ các outliers trong dữ liệu
- Tìm ra mối tương đồng giữa các đặc trưng cần thiết trong dữ liệu.
- Sử dụng kỹ thuật Gradient Boosting, cụ thể là XGBoost, CatBoost, LightGBM.
- Khai thác thêm một số đặc trưng cho quá trình training mô hình (Hiện tại là 6/15).

