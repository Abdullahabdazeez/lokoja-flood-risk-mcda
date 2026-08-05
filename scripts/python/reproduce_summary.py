from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "data" / "processed" / "tables"

headline = pd.read_csv(TABLES / "05_Lokoja_Headline_Project_Results.csv")
values = dict(zip(headline["Indicator"], headline["Result"]))

checks = {
    "Lokoja LGA area (km²)": 3406.818623770666,
    "High + Very High hazard area (km²)": 1305.1042635889326,
    "High + Very High hazard area (%)": 38.97370525940538,
    "Estimated population 2020": 253853.883294676,
    "Population in High + Very High final risk zones": 71195.49951250484,
    "High + Very High final risk area (km²)": 110.38524628421571,
    "Road length in High + Very High hazard zones (km)": 779.8877444612184,
    "Educational facilities in High + Very High hazard zones": 7.0,
    "Health facilities in High + Very High hazard zones": 21.0,
    "AHP Consistency Ratio": 0.009282691168439548,
}

for metric, expected in checks.items():
    actual = float(values[metric])
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=1e-8):
        raise ValueError(f"{metric}: expected {expected}, found {actual}")

print("RESULT REPRODUCTION: PASSED")
print(f"High + Very High hazard area: {values['High + Very High hazard area (km²)']:,.2f} km²")
print(f"High + Very High final-risk population: {values['Population in High + Very High final risk zones']:,.0f}")
print(f"Roads in High + Very High hazard: {values['Road length in High + Very High hazard zones (km)']:,.2f} km")
print(f"AHP consistency ratio: {values['AHP Consistency Ratio']:.4f}")
