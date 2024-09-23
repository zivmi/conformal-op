# Conformal Option Pricing <!-- omit in toc -->

Reproduction of "Conformal prediction of option prices" by Joao A. Bastos, with some extensions.

## TL;DR: <!-- omit in toc -->

- [Introduction](#introduction)
- [Project Setup](#project-setup)
- [Project Organization](#project-organization)

## Introduction

## Project Setup

### Conda <!-- omit in toc -->

Using conda, create a new environment with the necessary packages:

```bash
conda env create -f environment.yml
```

Or visit the [conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) for more information.

### Simulate data <!-- omit in toc -->

To simulate data, run the following command from the root directory of the project:

```bash
python src/simulations/simulate_data.py
```

This will create a csv file of ~35mb in the `data/simulated` directory. The code for simulation and
a peak into the output is given in the notebook `notebooks/1.0-mz-simulate-data.ipynb`. Parameters
of simulation are stored in `src/simulations/config.py`.


## Project Organization

```
├── LICENSE            
├── README.md          
├── data
│   ├── simulated      
│   ├── interim        <- Intermediate data, usually used in notebooks to document the analysis.
│   ├── processed      <- The data sets used for fitting final models. 
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Papers, notes, and other documentation
│   └── references     <- Data dictionaries, manuals, and all other explanatory materials.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is:
│                         - a number in the format of `X.Y`, where `X` relates to the topic and `Y`
│                           to a subtopic (different data, different model, additional tweaks, etc.),
│                         - the creator's initials ('mz' for Miroslav, 'nm' for Naoaki, etc.),
│                         - and a short delimited description at the end, e.g.
│                           `1.0-mz-initial-data-exploration-yfinance`
│                           `1.1-nm-initial-data-exploration-optionmetrics`
│                           `1.1-mz-initial-data-exploration-optionmetrics`
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. 
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── environment.yml   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `conda env export > .env_temp.yml` and then manually copy
│                         the main packages to `environment.yml`, like lightgbm, crepes, etc. 
│                         Let `conda` handle other dependencies.
│
└── src                <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes conformal-op a Python module
    │        
    ├── features                <- Code to create features for modeling, from the raw data
    │
    ├── models                  <- Code to train models and run model inference with trained models
    │
    ├── simulations             <- Code to simulate data 
    │
    ├── utils                   <- Utility functions used throughout the project
    │
    └── visualization           <- Code to create visualizations
```

--------

