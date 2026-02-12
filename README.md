# Energy Spectrum Calculator

This project demonstrates how to generate and analyze X-ray spectra using the SpekPy library.

## What the Code Does

### Spectrum Generation
- Creates an X-ray spectrum with:
  - **70 kVp** (kilovolt peak) - the maximum tube voltage
  - **12° anode angle** - the angle of the tungsten target

### Filtration
- Applies **2.8 mm of Aluminum (Al)** filtration
- Applies **3.0 mm of Beryllium (Be)** filtration

These filters modify the spectrum by removing lower energy photons (beam hardening).

### Analysis
- Calculates and prints the **first half-value layer (HVL1)** - the thickness of material needed to reduce the beam intensity by 50%
- Calculates and prints the **second half-value layer (HVL2)** - the additional thickness needed to reduce the beam by another 50%

### Visualization
- Retrieves the energy spectrum data (energy values and fluence)
- Plots the spectrum showing:
  - **X-axis**: Photon energy in keV
  - **Y-axis**: Fluence per mAs per unit energy (photons/cm²/mAs/keV)
  - **Title**: "An example x-ray spectrum"

## Use Cases
This is typical code for X-ray physics simulations, commonly used in:
- Medical physics
- Radiology
- Radiation protection

The code helps understand beam characteristics and quality for various applications.
