# Solution

## TL;DR

I use polars to extract data from the csv, load in memory, transform and convert back to csv.  
I also use pytest to do unit and end-to-end test.  

## Replication steps

1. create a virtual environment: `python3 -m venv myvenv`.  
2. Run: `source myvenv/bin/activate`  
3. Run: `pip install -r requirements.txt`  
4. Run the transformer script: `python transformer.py`  
5. Run tests: `pytest`  