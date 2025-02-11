import os

# Define project folder structure
project_name = "NOAA_Lightning_Analysis"
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "scripts",
    "outputs/figures",
    "docs"
]
files = {
    "data/raw/NOAA_lightning_strikes_2009_to_2018.csv": "",
    "notebooks/01_data_exploration.ipynb": "",
    "notebooks/02_data_cleaning.ipynb": "",
    "notebooks/03_visualization.ipynb": "",
    "notebooks/04_modeling.ipynb": "",
    "scripts/data_preprocessing.py": "# Script for cleaning data\n",
    "scripts/data_analysis.py": "# Script for analyzing data\n",
    "scripts/visualization.py": "# Script for visualizing data\n",
    "outputs/summary_statistics.csv": "Column1, Column2, Column3\n",
    "docs/README.md": "# NOAA Lightning Strikes Analysis\n\nProject description...",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\nscipy\nscikit-learn\njupyterlab",
    "environment.yml": """name: noaa_env
channels:
  - conda-forge
dependencies:
  - python=3.10
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scipy
  - scikit-learn
  - jupyterlab
"""
}

# Create project root directory
if not os.path.exists(project_name):
    os.makedirs(project_name)

# Create folders
for folder in folders:
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    full_path = os.path.join(project_name, file_path)
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(content)

print(f"✅ Project structure for '{project_name}' created successfully!")
