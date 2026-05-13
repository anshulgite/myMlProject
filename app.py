from flask import Flask, request,render_template
import numpy as np
import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException


application = Flask(__name__)

app = application

##route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Validate all required fields are present
            required_fields = ['gender', 'race_ethnicity', 'parental_level_of_education', 
                             'lunch', 'test_preparation_course', 'reading_score', 'writing_score']
            missing_fields = [field for field in required_fields if not request.form.get(field)]
            
            if missing_fields:
                return render_template('home.html', results=f"Error: Missing required fields - {', '.join(missing_fields)}")
            
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=int(request.form.get('reading_score')),
                writing_score=int(request.form.get('writing_score'))
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=result[0])
        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")
    
if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)