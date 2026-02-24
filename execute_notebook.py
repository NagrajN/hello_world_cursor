#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Execute the data analysis notebook
"""

import subprocess
import sys
import time
from pathlib import Path
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'

def wait_for_packages():
    """Wait until all required packages are available"""
    required = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy', 'jupyter']
    
    for attempt in range(60):  # Try for 60 seconds
        try:
            for pkg in required:
                __import__(pkg)
            print("[OK] All packages available!")
            return True
        except ImportError as e:
            if attempt % 5 == 0:
                print(f"Waiting for packages... ({attempt}s)")
            time.sleep(1)
    
    print("[ERROR] Packages not available after 60 seconds")
    return False

def download_dataset():
    """Download dataset from Kaggle if needed"""
    csv_file = Path('cs_students.csv')
    
    if csv_file.exists():
        print(f"[OK] Dataset already exists: {csv_file.name}")
        return True
    
    print("Downloading dataset from Kaggle...")
    try:
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-q', 'kaggle'
        ], check=True)
        
        subprocess.run([
            'kaggle', 'datasets', 'download', '-d',
            'zahranusratt/cs-students-performance-dataset',
            '-p', '.', '--unzip'
        ], check=True)
        
        print("[OK] Dataset downloaded successfully!")
        return True
    except Exception as e:
        print(f"[WARNING] Could not download dataset: {e}")
        print("You can manually download from:")
        print("https://www.kaggle.com/datasets/zahranusratt/cs-students-performance-dataset")
        return False

def execute_notebook():
    """Execute the notebook using nbconvert"""
    notebook = Path('data_analysis.ipynb')
    output = Path('data_analysis_output.ipynb')
    
    if not notebook.exists():
        print(f"[ERROR] Notebook not found: {notebook}")
        return False
    
    print(f"\nExecuting notebook: {notebook.name}")
    print("=" * 60)
    
    try:
        subprocess.run([
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--to', 'notebook',
            '--execute',
            '--ExecutePreprocessor.timeout=600',
            '--output', str(output),
            str(notebook)
        ], check=True)
        
        print("\n" + "=" * 60)
        print("[OK] Notebook executed successfully!")
        print(f"Output saved to: {output.name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error executing notebook: {e}")
        return False

if __name__ == '__main__':
    print("CS Students Performance Data Analysis")
    print("=" * 60)
    
    if not wait_for_packages():
        print("\nInstalling packages manually...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q',
                       'pandas', 'numpy', 'matplotlib', 'seaborn', 'scipy', 'jupyter'],
                      check=False)
        time.sleep(5)
    
    if not download_dataset():
        print("\n[WARNING] Continuing without dataset file...")
        print("   Add the CSV file manually and re-run the notebook")
    
    if execute_notebook():
        print("\n[OK] Analysis complete!")
    else:
        print("\n[ERROR] Failed to execute notebook")
        sys.exit(1)
