# TFM Paper #14: Large-Scale Structure Codebase

Reproduce cosmic structure formation results from:
> "Filaments, Voids, and Clusters Without Dark Matter: Spacetime Wave Dynamics in Cosmic Structure Formation"

## Quick Start
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
Run HPC simulation (300 Mpc/h box)
python simulations/tfm_lss_solver.py --box_size 300 --resolution 1024
Generate figures from paper:
python analysis/power_spectrum.py
python analysis/void_statistics.py
