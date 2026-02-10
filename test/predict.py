import pickle

# import ml model
with open('model_pkl/model.pkl','rb') as file:
    model = pickle.load(file)


# normally extracted from MLFlow
MODEL_VERSION = '1.0.1'


# prediction function
def predict_premium_category(input_df):
    # predict
    prediction = model.predict(input_df)[0]

    return prediction


