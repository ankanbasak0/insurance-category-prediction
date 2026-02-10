# Libraries and references
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import numpy
import pandas as pd
from user_input import rule_post
from test.predict import predict_premium_category, MODEL_VERSION



# FastAPI object
app = FastAPI()


     
# home (human readable)
@app.get('/')
def home():
    return {'mesasge' : 'Insurance Premium Category Prediction API'}


# production mandatory for clouds
# like AWS/ kubernetes (machine readable)
@app.get("/health")
@app.get("/healthz")
@app.get("/ping")
@app.get("/status")
def health_check():
    return {'status' : 'OK',
            'version' : MODEL_VERSION
            }



# 'post' route
@app.post('/predict')
def predict(input : rule_post):

    
    # model is trained in pandas dataframe so we need to transform 
    # our pydantic object to dict dataframe (combine all in one row)
    

    input_df = pd.DataFrame([{

        'bmi' : input.bmi,
        'age_group' : input.age_group,
        'lifestyle_risk' : input.lifestyle_risk,
        'city_tier' : input.city_tier,
        'income_lpa' : input.income_lpa,
        'occupation' : input.occupation

    }])

    try:
        prediction = predict_premium_category(input_df)

        # send to user
        return JSONResponse(status_code=200, content={'insurance_premium_category' : prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
    






















