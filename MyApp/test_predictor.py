from predictor import Predictor

if __name__ == "__main__" :
    predictor = Predictor("serialized_model.pkl")

    prediction = predictor.predict(
        age=30, 
        sex="male", 
        bmi=20,
        children=2,
        smoker="no", 
        region="southwest")
    
    print(prediction)