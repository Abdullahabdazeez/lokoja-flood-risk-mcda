# Lokoja Flood Hazard, Vulnerability and Risk Assessment

Lokoja sits at the Niger–Benue confluence, where low-lying terrain and major river systems create persistent flood-planning challenges. This project rebuilt an earlier GIS multi-criteria flood assessment to make its hazard classification empirically testable rather than dependent on near-equal class breaks.

Eight flood-conditioning factors were combined using AHP, with a consistency ratio of 0.0093. The continuous Flood Hazard Index was validated against satellite-derived flood evidence from 2012, 2018 and 2022 before fixed numerical thresholds were adopted. High and Very High hazard cover about 1,136.71 km² of the valid FHI domain and capture roughly 85–87% of the mapped historical flood evidence across the three events.

Sensitivity tests showed very strong preservation of the continuous hazard ranking under AHP weight perturbation, while DEM offset tests confirmed that elevation uncertainty can still alter categorical classes in Lokoja's low-relief confluence setting. The final analysis also separates physical hazard from population-informed risk: most High/Very High hazard land is reduced to Low or Moderate final risk where population vulnerability is lower.

Tools: Google Earth Engine, Python, GeoPandas/Rasterio, remote sensing, AHP/MCDA and historical flood validation.
