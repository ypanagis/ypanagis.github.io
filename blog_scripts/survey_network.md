```python
import pandas as pd
```

Imagine we have the following responses in a survey


```python
df = pd.DataFrame(data=
        [['slightly influenced', 'slightly influenced',
        'slightly influenced'],
       ['highly influenced', 'highly influenced', 'not at all'],
       ['influenced', 'highly influenced', 'not at all'],
       ['influenced', 'influenced', 'moderately influenced'],
       ['slightly influenced', 'slightly influenced',
        'slightly influenced'],
       ['moderately influenced', 'slightly influenced',
        'slightly influenced'],
       ['moderately influenced', 'influenced', 'moderately influenced'],
       ['influenced', 'highly influenced', 'slightly influenced'],
       ['influenced', 'influenced', 'slightly influenced'],
       ['highly influenced', 'slightly influenced',
        'slightly influenced']], columns=['factor_one', 'factor_two', 'factor_three'], )
```


```python
df.index = ['person_%d'%i for i in range(10)]
```

### Connections between individuals
We will connect people if they are *both* `influenced` or `highly influenced` by at least one of the 3 factors. We first better convert `influenced` or `highly influenced` to `1` and the other values to `0`.


```python
df_converted = df.applymap(lambda x: 
                             1 if x in ('influenced', 'high influenced') else 0)
```

Now make an _adjacency_ DataFrame by computing the inner product of `df_converted` with its transpopse `df_converted.T`. An effect of the inner product, is that tthe value element `(i,j)` of the matrix, will count the number of similar influences of respondent `i` with respondent `j`.


```python
df_adj = df_converted @ df_converted.T
```


```python
df_adj
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_0</th>
      <th>person_1</th>
      <th>person_2</th>
      <th>person_3</th>
      <th>person_4</th>
      <th>person_5</th>
      <th>person_6</th>
      <th>person_7</th>
      <th>person_8</th>
      <th>person_9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>person_0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_3</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_7</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_8</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>person_9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Note:** element `(person_3,person_8)=2` because reponses of `person_3` and `person_8` are *influenced by both `factor_one` and `factor_two`*.
Now let's convert the above adjacency matrix to an edge, for it to be easily exported in CSV and imported eg. in `Gephi` or `networkx`


```python
df_adj[df_adj >=1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_0</th>
      <th>person_1</th>
      <th>person_2</th>
      <th>person_3</th>
      <th>person_4</th>
      <th>person_5</th>
      <th>person_6</th>
      <th>person_7</th>
      <th>person_8</th>
      <th>person_9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>person_0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>person_9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



get row and column indexes, with non zero values


```python
import numpy as np
rows, cols = np.where(df_adj >= 1)
```

now get edge `weights` in a list, too 


```python
weights = [df_adj.iloc[rows[i], cols[i]] for i in range(len(rows.tolist()))]
```

from this point and on we can create a list of edges as tuples


```python
edge_list = zip(rows.tolist(), cols.tolist(), weights)
```

and create a `DataFrame` from it


```python
edge_df = pd.DataFrame(edge_list, columns=['Src', 'Dest', 'Weight'])
```

We can of course export to CSV if we want


```python
edge_df.to_csv('edges.csv', sep=',', index=None) # We leave index as None in order not to export a, rather useless, first field, to CSV 
```


```python

```
