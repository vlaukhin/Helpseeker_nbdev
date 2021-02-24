# Helpseeker_nbdev
> A demo of nbdev in the context of a deep dive project.


This file will become your README and also the index of your documentation.

## Install

`pip install Helpseeker_nbdev`

## How to use

Running the TargetValuesPreprocessing script

```
logger = logging.logging_setup(log_level='INFO')

mapped_targets = TargetValuesPreprocessing.get_target_df(
       config.target_features,
       config.target_path,
       config.polygon_path,
       config.target_df_regions,
       logger)
```

    {
     "event": "Preprocessing target features",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 12856)"
    }
    {
     "event": "mapping homeless polygon",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 13848)"
    }
    Failed to auto identify EPSG: 7
    {
     "event": "homeless polygon mapping completed",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 110617)"
    }
    {
     "event": "mapping suicide polygon",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 111614)"
    }
    Failed to auto identify EPSG: 7
    {
     "event": "suicide polygon mapping completed",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 205335)"
    }
    {
     "event": "mapping violence polygon",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 206361)"
    }
    Failed to auto identify EPSG: 7
    {
     "event": "violence polygon mapping completed",
     "timestamp": "datetime.datetime(2021, 2, 23, 23, 38, 59, 283128)"
    }
    

```
mapped_targets['homeless'].head()
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
      <th>Year</th>
      <th>Province</th>
      <th>Community</th>
      <th>PIT Total</th>
      <th>PIT-Sheltered</th>
      <th>PIT-Unsheltered</th>
      <th>DV_target</th>
      <th>CSDNAME</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2002</td>
      <td>British Columbia</td>
      <td>Burnaby</td>
      <td>18</td>
      <td>14</td>
      <td>44</td>
      <td>Burnaby</td>
      <td>Burnaby</td>
      <td>POLYGON ((4026984.377 2004001.803, 4027065.283...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>British Columbia</td>
      <td>Delta/White Rock</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>Delta</td>
      <td>MULTIPOLYGON (((4027416.129 1971099.869, 40275...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>British Columbia</td>
      <td>Langley</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>Langley</td>
      <td>POLYGON ((4044035.820 1983268.574, 4044044.823...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2002</td>
      <td>British Columbia</td>
      <td>Maple Ridge/Pitt Meadows</td>
      <td>66</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>Maple Ridge</td>
      <td>POLYGON ((4060993.469 1993881.186, 4061981.717...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>British Columbia</td>
      <td>New Westminster</td>
      <td>74</td>
      <td>0</td>
      <td>0</td>
      <td>New Westminster</td>
      <td>New Westminster</td>
      <td>POLYGON ((4031000.411 1995145.954, 4031031.369...</td>
    </tr>
  </tbody>
</table>
</div>


