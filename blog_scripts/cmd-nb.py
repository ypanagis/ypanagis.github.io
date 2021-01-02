# Adapted from https://medium.com/applied-data-science/full-stack-data-scientist-5-automating-report-generation-with-jupyter-notebooks-919e32e88d18
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.exporters import HTMLExporter

with open('command-args.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)
# Replace placeholders
# Jupyter notebooks are just a JSON file, so we can use the usual
# method to find and replace values
# Replace mean (LOC)
nb['cells'][1]['source'] = nb['cells'][1]['source'].replace("'Hello_world'","'Hello from script'")# Replace std (SCALE)
# nb['cells'][1]['source'] = nb['cells'][1]['source'].replace("'PUT_SCALE_HERE'",str(std))

# Execute Notebook
proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
proc.preprocess(nb)

# Access the 3rd notebook cell containing the printed message,
# get 'output' and the 'text attribute of it'
# This will be: 'Hello from script'
print(nb['cells'][2]['outputs'][0]['text'])

exporter = HTMLExporter()
with open(f'Report_world.html', 'w') as f:
    f.write(exporter.from_notebook_node(nb)[0])
