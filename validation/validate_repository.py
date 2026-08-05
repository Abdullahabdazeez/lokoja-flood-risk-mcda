from pathlib import Path
import json
import sys
import pandas as pd
import rasterio

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "project.json",
    "LICENSE",
    "CITATION.cff",
    "requirements.txt",
    "assets/project-cover.png",
    "assets/repository-social-preview.png",
    "outputs/maps/01_final_flood_hazard_map.png",
    "outputs/maps/02_final_flood_risk_map.png",
    "data/processed/tables/05_Lokoja_Headline_Project_Results.csv",
    "data/processed/rasters/Lokoja_Final_Flood_Hazard_30m.tif",
    "data/processed/rasters/Lokoja_Final_Flood_Risk_Map_30m.tif",
]

failures = [f"Missing: {item}" for item in required if not (ROOT/item).exists()]

for path in ROOT.rglob("*"):
    if path.is_file() and path.stat().st_size > 24 * 1024 * 1024:
        failures.append(f"Browser-upload limit exceeded: {path.relative_to(ROOT)}")

try:
    meta = json.loads((ROOT/"project.json").read_text(encoding="utf-8"))
    if abs(meta["ahp_consistency_ratio"] - 0.009282691168439548) > 1e-12:
        failures.append("Unexpected AHP consistency ratio")
except Exception as exc:
    failures.append(f"Invalid metadata: {exc}")

for name in [
    "Lokoja_Final_Flood_Hazard_30m.tif",
    "Lokoja_Final_Flood_Risk_Map_30m.tif",
]:
    try:
        with rasterio.open(ROOT/"data/processed/rasters"/name) as ds:
            if abs(abs(ds.transform.a) - 30) > 0.1:
                failures.append(f"Unexpected raster resolution: {name}")
    except Exception as exc:
        failures.append(f"Raster validation failed for {name}: {exc}")

if failures:
    print("REPOSITORY VALIDATION: FAILED")
    for failure in failures:
        print("-", failure)
    sys.exit(1)

print("REPOSITORY VALIDATION: PASSED")
print("Required files, headline results, rasters and browser-upload limits are valid.")
