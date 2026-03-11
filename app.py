from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)
model = load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict_page():
    return render_template("predict.html")

@app.route("/result", methods=["POST"])
def result():

    features = [
        float(request.form["Machine"]),
        float(request.form["DebugSize"]),
        float(request.form["DebugRVA"]),
        float(request.form["MajorImageVersion"]),
        float(request.form["MajorOSVersion"]),
        float(request.form["ExportRVA"]),
        float(request.form["ExportSize"]),
        float(request.form["IatVRA"]),
        float(request.form["MajorLinkerVersion"]),
        float(request.form["MinorLinkerVersion"]),
        float(request.form["NumberOfSections"]),
        float(request.form["SizeOfStackReserve"]),
        float(request.form["DllCharacteristics"]),
        float(request.form["ResourceSize"]),
        float(request.form["BitcoinAddresses"])
    ]

    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]

    # After training:
    # 1 = Benign
    # 0 = Ransomware
    if prediction == 1:
        output = "✅ BENIGN FILE (SAFE)"
    else:
        output = "⚠ RANSOMWARE DETECTED!"

    return render_template("result.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)