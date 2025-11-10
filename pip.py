# Using an installed package

# Using numpy and pandas
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
data = pd.DataFrame(arr, columns=['Numbers'])
print("\nDataFrame:\n", data)