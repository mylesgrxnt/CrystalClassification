# CrystalClassification

## Proposal

We will work with crystal structure data from The Materials Project, specifically focusing on the “Crystal Structures (SCAN/R2SCAN)” and “Crystal Structures (GGA/GGA+U)” entries in their database. The main aim of this project is going to be to create a predictive model that can predict the lattice parameters and atomic basis of a crystal structure given its material properties, specifically its band structure, density of states, heat capacity, and hardness. We will explore the use of polynomial regression models, using Mean Squared Error to assess error. In such a large and complex dataset, we will be sure to implement some L1 or L2 Regularization as well, depending on what is needed. Additionally, we will compare our findings with the Density Functional Theory (DFT) model, which produces material properties given an atomic structure, to see how our model compares to adjacently related simulations. We will compare our findings to see how consistent they are with leading research in material science [Burke, 2012, Jain et al, 2013, Sholl, D. S., & Steckel, J. A., 2009, Perdew, J. P., Burke, K., & Ernzerhof, M., 1996].

## Getting Started
1. Start (or activate) your virtual environment. Make sure to name it 'venv' so it's in the gitignore.
2. Run 'pip install mp_api' or 'pip install -r requirements.txt'
3. Create a file named secretInfo.py and put APIKEY = ".........." (your API key)
4. Make sure to have fun :D