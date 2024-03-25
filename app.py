from flask import Flask, render_template, request
from iris_predict import predict_iris

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict_iris(features)

    # # Map the prediction to class names
    # if prediction == 0:
    #     predicted_class = "Setosa"
    # elif prediction == 1:
    #     predicted_class = "Versicolor"
    # else:
    #     predicted_class = "Virginica"

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)