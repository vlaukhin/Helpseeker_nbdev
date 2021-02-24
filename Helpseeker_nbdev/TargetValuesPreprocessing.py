# AUTOGENERATED! DO NOT EDIT! File to edit: .ipynb_checkpoints/TargetValuesPreprocessing-checkpoint.ipynb (unless otherwise specified).

__all__ = ['get_target_df', 'get_target_df']

# Comes from StatsCanadaCore-checkpoint.ipynb, cell

import pandas as pd
import numpy as np
import os
import re
import geopandas as gp
import warnings
from pathlib import Path
warnings.filterwarnings("ignore")

# Comes from StatsCanadaCore-checkpoint.ipynb, cell

def _map_target_polygons(target,target_file,poly_file,target_df_regions):

    '''
    given the target as str as input this function reads in the appropriate final targets csv from target_values_paths
    and appropriate polygons from target_polygon_paths and merges them into a single geo dataframe

    parameters:
    ---------
    target-> str\n
    target_values_paths -> dict[str,str] paths to the target csvs\n
    target_polygon_paths -> dict[str,str] paths to the polygon .gpkg files\n
    target_df_regions -> list[str]\n

    ouput:
    --------
    mapped_df -> gp.GeoDataFrame

    target csv must have Community and Province columns.
    '''

    df = pd.read_csv(target_file)
    gdf = gp.read_file(poly_file)

    mapped_df = df.merge(gdf,how = 'left',left_on=target_df_regions,right_on =[target,'PRNAME'])
    mapped_df.dropna(subset = ['geometry'],inplace = True)
    mapped_df.drop(columns = [target,'PRNAME'],inplace = True)
    mapped_df = gp.GeoDataFrame(mapped_df,geometry = 'geometry')
    return mapped_df

# Comes from StatsCanadaCore-checkpoint.ipynb, cell

def get_target_df(target_features,target_path,polygon_path,target_df_regions,logger):
    '''
    main function for this script to return a dictionary of dataframes mapped to each target,

    parameters:
    ------------
    target_features -> gp.GeoDataFrame\n
    target_values_paths -> dict[str,str] paths to the target csvs\n
    target_polygon_paths -> dict[str,str] paths to the polygon .gpkg files\n
    target_df_regions -> list[str]

    returns:
    ---------
    mapped_target -> dict[str,gp.GeoDataFrame]
    '''
    logger.info(f"Preprocessing target features")
    mapped_targets = {}

    for target in ["homeless","suicide","violence"]:
        logger.info(f"mapping {target} polygon")

        poly_file = Path(polygon_path)/f"{target}_target_polygons.gpkg"
        target_file = Path(target_path)/f"{target}_targets_final.csv"

        df = _map_target_polygons(target,target_file,poly_file,target_df_regions)

        mapped_targets[target] = df
        logger.info(f"{target} polygon mapping completed")
    return mapped_targets

# Comes from StatsCanadaCore.ipynb, cell

import pandas as pd
import numpy as np
import os
import re
import geopandas as gp
import warnings
from pathlib import Path
warnings.filterwarnings("ignore")

# Comes from StatsCanadaCore.ipynb, cell

def _map_target_polygons(target,target_file,poly_file,target_df_regions):

    '''
    given the target as str as input this function reads in the appropriate final targets csv from target_values_paths
    and appropriate polygons from target_polygon_paths and merges them into a single geo dataframe

    parameters:
    ---------
    target-> str\n
    target_values_paths -> dict[str,str] paths to the target csvs\n
    target_polygon_paths -> dict[str,str] paths to the polygon .gpkg files\n
    target_df_regions -> list[str]\n

    ouput:
    --------
    mapped_df -> gp.GeoDataFrame

    target csv must have Community and Province columns.
    '''

    df = pd.read_csv(target_file)
    gdf = gp.read_file(poly_file)

    mapped_df = df.merge(gdf,how = 'left',left_on=target_df_regions,right_on =[target,'PRNAME'])
    mapped_df.dropna(subset = ['geometry'],inplace = True)
    mapped_df.drop(columns = [target,'PRNAME'],inplace = True)
    mapped_df = gp.GeoDataFrame(mapped_df,geometry = 'geometry')
    return mapped_df

# Comes from StatsCanadaCore.ipynb, cell

def get_target_df(target_features,target_path,polygon_path,target_df_regions,logger):
    '''
    main function for this script to return a dictionary of dataframes mapped to each target,

    parameters:
    ------------
    target_features -> gp.GeoDataFrame\n
    target_values_paths -> dict[str,str] paths to the target csvs\n
    target_polygon_paths -> dict[str,str] paths to the polygon .gpkg files\n
    target_df_regions -> list[str]

    returns:
    ---------
    mapped_target -> dict[str,gp.GeoDataFrame]
    '''
    logger.info(f"Preprocessing target features")
    mapped_targets = {}

    for target in ["homeless","suicide","violence"]:
        logger.info(f"mapping {target} polygon")

        poly_file = Path(polygon_path)/f"{target}_target_polygons.gpkg"
        target_file = Path(target_path)/f"{target}_targets_final.csv"

        df = _map_target_polygons(target,target_file,poly_file,target_df_regions)

        mapped_targets[target] = df
        logger.info(f"{target} polygon mapping completed")
    return mapped_targets