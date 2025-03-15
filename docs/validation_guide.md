# Validating TFM Against Observations

## SDSS Void Statistics
1. Download SDSS void catalog: `wget [SDSS_URL]`
2. Run comparison script:
   ```bash
   python analysis/void_statistics.py --sdss_data [PATH] --tfm_data data/void_catalog.h5

   from analysis.cmb_peaks import compare_planck
compare_planck('data/cmb_simulations.h5', planck_data='data/planck2018.fits')
