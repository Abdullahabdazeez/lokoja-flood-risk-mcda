# Flood Hazard, Vulnerability and Risk Assessment — Lokoja LGA, Nigeria

## Overview

Lokoja lies at the Niger–Benue confluence and has experienced major flood events. This project develops and validates a GIS-based multi-criteria flood-susceptibility assessment and then separates **physical flood hazard** from **population-informed risk**.

The reconstruction specifically addresses a major classification weakness in an earlier version of the project: the previous five hazard classes had near-equal areas and therefore behaved like quantile classes. Those classes have been superseded by **fixed numerical Flood Hazard Index (FHI) thresholds calibrated against historical flood evidence**.

**Research question:** Can a multi-criteria flood-susceptibility model identify historically flood-affected land in Lokoja while remaining stable to reasonable weighting and terrain uncertainty?

## Study Area

Lokoja Local Government Area, Kogi State, Nigeria.

The valid reconstructed FHI domain covers approximately **3,353.08 km²**.

## Methodology

Eight flood-conditioning criteria were combined through an Analytic Hierarchy Process (AHP) weighted linear combination:

| Criterion | Weight |
|---|---:|
| Distance to Drainage | 24.58% |
| Elevation | 20.29% |
| Rainfall | 15.85% |
| Slope | 12.18% |
| Drainage Density | 9.79% |
| LULC | 7.37% |
| Clay | 6.23% |
| NDVI | 3.71% |

The documented **AHP consistency ratio is 0.0093**.

The continuous FHI was independently evaluated against satellite-derived flood evidence for **2012, 2018 and 2022** before final hazard classes were established.

## Validation-Supported Hazard Classes

| Hazard class | FHI rule |
|---|---|
| Very Low | FHI < 3.20 |
| Low | 3.20 ≤ FHI < 3.29 |
| Moderate | 3.29 ≤ FHI < 3.37 |
| High | 3.37 ≤ FHI < 3.83 |
| Very High | FHI ≥ 3.83 |

These are **fixed numerical thresholds**. No equal-area or quantile classification is used in the final hazard product.

## Key Findings

- **High + Very High hazard:** **1,136.71 km²**
- **Very High hazard:** **22.22 km²**
- Historical flood evidence captured by High + Very High hazard:
  - **2012: 85.08%**
  - **2018: 86.64%**
  - **2022: 86.36%**
- Mean class agreement across AHP perturbations: **91.21%**
- Minimum sampled FHI rank correlation across AHP perturbations: **0.99666**
- DEM ±10 m stress tests retain approximately **85.4–85.5%** class agreement.

## Hazard vs Risk

The final project deliberately distinguishes **physical susceptibility** from **population-informed risk**.

Within the common R7B analysis domain:

- High + Very High physical hazard: **1,125.64 km²**
- Of that land, only **58.54 km²** remains High or Very High in the existing final-risk classification.
- **58.05%** of High/Very High hazard land becomes Low final risk.
- **31.96%** becomes Moderate final risk.

The existing risk index is more strongly associated with population vulnerability (**Spearman ρ = 0.62144**) than with the FHI (**ρ = 0.35780**).

This does **not** mean the physical hazard model failed. It shows that exposure/vulnerability substantially modifies physical hazard when final risk is calculated.

## Robustness

AHP sensitivity was tested using 32 one-at-a-time weight perturbations at ±10% and ±20%, with every weight vector renormalized to sum to one.

DEM uncertainty was assessed using uniform elevation-offset stress tests at −10 m, −5 m, +5 m and +10 m. These offsets are **sensitivity scenarios**, not measured Lokoja-specific DEM errors.

## Planning Interpretation

The hazard map identifies land with comparatively high physical flood susceptibility and can support:

- development screening;
- land-use planning;
- drainage and infrastructure prioritization;
- emergency preparedness;
- identification of locations requiring detailed hydraulic investigation.

The final risk surface answers a different question: where physical hazard overlaps with stronger human vulnerability/exposure.

## Important Limitation

This is a **GIS/MCDA flood-susceptibility assessment**. It does not estimate:

- flood depth;
- annual exceedance probability;
- return period;
- hydraulic flow characteristics.

## Repository Structure

```text
assets/
  maps/
  charts/

data/
  final/
  tables/

docs/
reports/
validation/

README.md
CITATION.cff
project.json
RELEASE_NOTES.md
```

## Tools

Google Earth Engine · Python · Rasterio · GIS · Remote Sensing · AHP/MCDA · Historical Flood Validation

## Author

**Abdullah Abdazeez Ayomide**  
Geospatial Planner | GIS & Remote Sensing Analyst | Environmental & Urban Planning Researcher
