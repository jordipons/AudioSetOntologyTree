# AudioSet Ontology Tree
Tree visualization of the AudioSet Ontology. 

Code adapted from: https://bl.ocks.org/mbostock/4339083 

Ontology from: https://github.com/audioset/ontology

Thanks to Xavier Favory, Eduardo Fonseca and Frederic Font. 

## Usage
Open index.html in your browser! It requires the following files next to it: ASO.html5.json (the AudioSet Ontology formatted properly) and d3.v3.min.js (D3 library for visualizations).

In case ASO.html5.json is not available:
1. Open /AudioSetOntologyTree/preprocessing/ folder. It contains: ASO.json (AudioSet Ontology as in https://github.com/audioset/ontology) and preprocessing.py (python file for properly formatting the AudioSet Ontology).
2. Run: python preprocessing.py - to generate /AudioSetOntologyTree/ASO.html5.json file!

If AudioSet Ontology changes, one can re-compute ASO.html5.json by changing ASO.json with the updated AudioSet Ontology.
