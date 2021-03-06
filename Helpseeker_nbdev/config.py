# AUTOGENERATED! DO NOT EDIT! File to edit: config.ipynb (unless otherwise specified).

__all__ = ['config_file_path', 'f', 'config', 'stats_can_regions', 'stats_can_feature_by_ids_dir', 'target_path',
           'target_features', 'feature_encoding_map_dir', 'polygon_path', 'target_df_regions', 'config_file_path', 'f',
           'config', 'stats_can_regions', 'stats_can_feature_by_ids_dir', 'target_path', 'target_features',
           'feature_encoding_map_dir', 'polygon_path', 'target_df_regions']

# Comes from StatsCanadaCore-checkpoint.ipynb, cell
from pathlib import Path
import json

config_file_path = Path("config.json")
f = open(config_file_path,"r")
config = json.load(f)

# Comes from StatsCanadaCore-checkpoint.ipynb, cell
stats_can_regions = config['stats_canada']['stats_can_regions']
stats_can_feature_by_ids_dir =config['stats_canada']['stats_can_feature_by_ids_dir']
target_path = config["target_path"]
target_features = config['target_features']
feature_encoding_map_dir = config["feature_encoding_map_dir"]
polygon_path = config["polygon_path"]
target_df_regions = config["target_df_regions"]

# Comes from StatsCanadaCore.ipynb, cell
from pathlib import Path
import json

config_file_path = Path("config.json")
f = open(config_file_path,"r")
config = json.load(f)

# Comes from StatsCanadaCore.ipynb, cell
stats_can_regions = config['stats_canada']['stats_can_regions']
stats_can_feature_by_ids_dir =config['stats_canada']['stats_can_feature_by_ids_dir']
target_path = config["target_path"]
target_features = config['target_features']
feature_encoding_map_dir = config["feature_encoding_map_dir"]
polygon_path = config["polygon_path"]
target_df_regions = config["target_df_regions"]