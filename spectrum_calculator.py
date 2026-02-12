import spekpy as sp # Import SpekPy
import matplotlib.pyplot as plt # Import library for plotting

s = sp.Spek(kvp=70, th=12, dk=0.5) # Create a spectrum with custom energy bin width (dk in keV)
s.filter('Al', 2.8) # Filter the spectrum
s.filter('Be', 3.0) # Filter the spectrum

hvl = s.get_hvl1() # Get the 1st half-value-layer
print(hvl,'mm') # Print value to screen
hv2 = s.get_hvl2() # Get the 1st half-value-layer
print(hv2,'mm') # Print value to screen

k, f = s.get_spectrum(edges=True) # Get the spectrum

# Write spectrum data to text file
with open('spectrum_data.txt', 'w') as file:
    file.write('Energy(keV)\tFluence(photons/cm2/mAs/keV)\n')
    for energy, fluence in zip(k, f):
        file.write(f'{energy}\t{fluence}\n')

print('Spectrum data saved to spectrum_data.txt')

plt.plot(k, f) # Plot the spectrum
plt.xlabel('Energy [keV]')
plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
plt.title('An example x-ray spectrum')
plt.show()
