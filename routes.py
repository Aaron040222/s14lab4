from flask import Flask, render_template
import joblib as joblib

app = Flask(__name__)
model = joblib.load('./regr.pkl')
model2 = joblib.load('./SplitRegr.pkl')
model3 = joblib.load('./DecisionTree.pkl')

@app.route('/')
def index():
	features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
	prediction = model.predict([[4, 2.5, 3005, 15, 17903.0, 1]])[0][0].round(1)
	prediction = str(prediction)
	prediction2 = model2.predict([[4, 2.5, 3005, 15, 17903.0, 1]])[0][0].round(1)
	prediction2 = str(prediction2)
	prediction3 = model3.predict([[4, 2.5, 3005, 15, 17903.0, 1]]).round(1)
	prediction3 = str(prediction3)[1:-1]
	return render_template("index.html", prediction=prediction, prediction2=prediction2, prediction3=prediction3)


