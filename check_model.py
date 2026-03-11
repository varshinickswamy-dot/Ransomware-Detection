from joblib import load
import pandas as pd

model = load("model.pkl")

data = pd.read_csv("ransomware_dataset.csv")

features = [
"Machine","DebugSize","DebugRVA",
"MajorImageVersion","MajorOSVersion",
"ExportRVA","ExportSize","IatVRA",
"MajorLinkerVersion","MinorLinkerVersion",
"NumberOfSections","SizeOfStackReserve",
"DllCharacteristics","ResourceSize",
"BitcoinAddresses"
]

benign = data[data["Benign"]==1][features].iloc[0]
malware = data[data["Benign"]==0][features].iloc[0]

print("Benign prediction:", model.predict([benign])[0])
print("Malware prediction:", model.predict([malware])[0])