# Project Report: Flood Hazard, Vulnerability and Risk in Lokoja

## Background

Lokoja sits where the Niger and Benue rivers meet, and flooding is a recurring planning problem. I developed this project to map physical flood susceptibility and then compare that pattern with a population-informed risk layer.

The project was rebuilt after I noticed that an earlier five-class hazard map behaved too much like a quantile map, with classes occupying nearly equal areas. That made the visual result neat, but it weakened the physical interpretation.

## What I did

I combined eight flood-conditioning factors using an AHP weighted linear combination: distance to drainage, elevation, rainfall, slope, drainage density, land cover, clay content and NDVI.

Rather than define the final hazard classes first, I evaluated the continuous Flood Hazard Index against satellite-derived flood evidence from **2012, 2018 and 2022**. I then used fixed numerical thresholds for the final classes.

I also tested the model against reasonable changes in the AHP weights and simple DEM offset scenarios.

## What I found

High and Very High hazard together cover **1,136.71 km²**, including **22.22 km²** in the Very High class.

The High + Very High classes capture:

- **85.08%** of the 2012 historical flood evidence;
- **86.64%** of the 2018 evidence; and
- **86.36%** of the 2022 evidence.

Across the AHP sensitivity runs, mean class agreement is **91.21%** and the minimum sampled FHI rank correlation is **0.99666**.

The DEM offset stress tests retain about **85.4-85.5%** class agreement.

## Why I separate hazard from risk

The hazard map describes where the physical conditions are relatively more favourable for flooding. The risk layer adds population vulnerability and therefore answers a different question.

Within the common analysis domain, High + Very High physical hazard covers **1,125.64 km²**. Only **58.54 km²** of that area remains High or Very High in the final risk classification.

The final risk index is more strongly associated with population vulnerability than with the physical FHI. That is not a contradiction. It shows that human exposure changes the planning meaning of the physical hazard pattern.

## What the result means

The hazard map can support early development screening, drainage planning, emergency preparedness and the identification of places that deserve detailed hydraulic investigation.

The risk map is more useful when the question is where physical flood susceptibility overlaps with stronger human vulnerability.

Neither map is a hydraulic flood model.

## Important limitations

The analysis does not estimate flood depth, flow velocity, annual exceedance probability or return period. The DEM offset tests are sensitivity checks rather than measured error estimates for Lokoja.

A high-susceptibility location should therefore be treated as a place that deserves closer investigation, not as a prediction of an exact future flood depth.

## What I would add next

A logical next step would combine this screening model with hydraulic simulations, better exposure data and asset-level information. That would allow the analysis to move from relative susceptibility toward more detailed risk estimates.

## Main outputs

Final maps and charts are in [`assets`](../assets/), result tables in [`data`](../data/), validation records in [`validation`](../validation/) and the technical report in [`reports`](../reports/).

## Final note

The strongest lesson from the rebuild was that classification choices can change the story a map appears to tell. The final thresholds are therefore tied to historical flood evidence rather than chosen mainly for visual balance.
