from pyresearchutils.python_package_check import is_package_installed

FOUND_PYTORCH = is_package_installed("torch")
FOUND_TF = is_package_installed("tensorflow")
FOUND_WANDB = is_package_installed("wandb")
CONFIG = "config_file"
BASELOGFOLDER = 'base_log_folder'
SEED = 'seed'
DEVICE = None
