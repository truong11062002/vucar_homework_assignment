from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
main_model = pickle.load(open('./models/xgb_r.pkl','rb'))
car=pd.read_csv('./data/cleaned_car_v3.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies = sorted(car['brand'].unique())
    car_models = sorted(car['model'].unique())
    years = sorted(car['manufacture_date'].unique(), reverse=True)
    fuel_type = sorted(car['fuel'].unique())
    condition = sorted(car['condition'].unique())
    type_car = sorted(car['type_car'].unique())
    mileage_v2 = sorted(car['mileage_v2'].unique())
    
    companies.insert(0,'Select Company')
    return render_template('index.html',
                           companies=companies, 
                           car_models=car_models,
                           years=years,
                           fuel_types=fuel_type, 
                           condition=condition, 
                           type_car=type_car, 
                           mileage_v2=mileage_v2)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    brand = request.form.get('companies')
    model = request.form.get('car_models')
    
    manufacture_date = request.form.get('year')
    fuel = request.form.get('fuel_type')
    mileage_v2 = request.form.get('kilo_driven')
    condition = request.form.get('condition')
    type_car = request.form.get('type_car')
    # curr_year = pd.Timestamp.now().year
    # years_since_manufacture = curr_year - int(manufacture_date)
    
    
    prediction = main_model.predict(pd.DataFrame(columns=['brand', 'model', 'manufacture_date', 'fuel', 'mileage_v2', 'condition', 'type_car'],
       data=np.array([brand, model, manufacture_date, fuel, mileage_v2, condition, type_car]).reshape(1,7)))
    # Return VND
    return str('{:,.0f}'.format(prediction[0]))



if __name__=='__main__':
    app.run()