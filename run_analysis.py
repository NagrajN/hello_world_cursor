#!/usr/bin/env python
"""
Script to download CS Students Performance dataset and run the analysis notebook
"""

import os
import sys
import subprocess
from pathlib import Path

def download_dataset():
    """Download the dataset from Kaggle"""
    csv_file = 'cs_students.csv'
    
    if Path(csv_file).exists():
        print(f"✓ {csv_file} already exists")
        return True
    
    print("Attempting to download from Kaggle...")
    try:
        subprocess.run([
            'kaggle', 'datasets', 'download', '-d', 
            'zahranusratt/cs-students-performance-dataset', 
            '-p', '.', '--unzip'
        ], check=True)
        print("✓ Dataset downloaded successfully!")
        return True
    except FileNotFoundError:
        print("✗ Kaggle CLI not found. Installing...")
        subprocess.run(['pip', 'install', 'kaggle'], check=True)
        return download_dataset()
    except subprocess.CalledProcessError as e:
        print(f"✗ Error downloading: {e}")
        print("\nPlease download manually from:")
        print("https://www.kaggle.com/datasets/zahranusratt/cs-students-performance-dataset")
        return False

def install_dependencies():
    """Install required Python packages"""
    required_packages = [
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scipy',
        'jupyter',
        'notebook'
    ]
    
    print("\nInstalling required packages...")
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.run(['pip', 'install', package], check=True)

def run_notebook():
    """Run the Jupyter notebook"""
    notebook_file = 'data_analysis.ipynb'
    
    if not Path(notebook_file).exists():
        print(f"✗ {notebook_file} not found")
        return False
    
    print(f"\n{'='*60}")
    print(f"Starting Jupyter Notebook: {notebook_file}")
    print(f"{'='*60}")
    
    try:
        subprocess.run(['jupyter', 'notebook', notebook_file], check=False)
        return True
    except Exception as e:
        print(f"✗ Error running notebook: {e}")
        return False

if __name__ == '__main__':
    print("CS Students Performance - Data Analysis Pipeline")
    print("=" * 60)
    
    # Install dependencies
    install_dependencies()
    
    # Download dataset
    if not download_dataset():
        print("\n⚠ Dataset not available. Exiting.")
        sys.exit(1)
    
    # Run notebook
    if run_notebook():
        print("\n✓ Notebook execution completed")
    else:
        print("\n✗ Failed to run notebook")
        sys.exit(1)
