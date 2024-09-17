# conformal-op

Reproduction of "Conformal prediction of option prices" by Joao A. Bastos, with some extensions.

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
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `conda list -e > requirements.txt`
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

