# PyPackage

Clean, extract and visualise data.

## Instructions

Step 1: CMD

```
Create Environment Using CMD (refer to: https://stackoverflow.com/questions/35950740/virtualenv-is-not-recognized-as-an-internal-or-external-command-operable-prog)
```
python -m virtualenv .
.\scripts\activate
```

Step 2: CMD

```
pip install git+https://github.com/adilhadizul/tmux_buffer
```


Step 3: VSC Clean, Extract and Visualise

```
pip install pandas
pip install matplotlib
pip install tqdm
pip install tmux_buffer
```
import pandas as pd
import matplotlib.pyplot as plt
```
from tqdm import tqdm_notebook
```

```python
from tmux_buffer import tmux_buffer_cev_test

# clean the dataset
tmux_buffer_cev_test.cleandata(pd.read_csv('tmux-buffer.txt', sep='\t', header=None))
# extract data from dataset
tmux_buffer_cev_test.extractdata(pd.read_csv('cleanedfinal.txt', header=None))
# visualise graph using fold (other folds can be visualised by changing fold number, ie. Fold0,Fold1 etc...)
tmux_buffer_cev_test.Fold0(pd.read_csv('extractedfinal.csv', index_col=False))
```

3. Done
