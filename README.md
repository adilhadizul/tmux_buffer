# PyPackage

Clean, extract and visualise data.

## Instructions

1. Install:

```
pip install python_package
```

2. Clean, Extract and Visualise:

```python
from python_package import tmux_buffer_cev_test

# clean the dataset
cleandata(pd.read_csv('tmux_buffer.txt', sep='\t', header=None))
# extract data from dataset
extractdata(pd.read_csv('cleanedfinal.txt', header=None))
# visualise graph using fold (other folds can be visualised by changing fold number, ie. Fold0,Fold1 etc...)
Fold0(pd.read_csv('extractedfinal.csv', index_col=False))
```

3. Done
