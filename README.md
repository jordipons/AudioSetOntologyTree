# AudioSet Ontology Tree
Tree visualization of the AudioSet Ontology. See an online demo here: http://www.jordipons.me/apps/audioset/

Code adapted from: https://bl.ocks.org/mbostock/4339083 

Ontology from: https://github.com/audioset/ontology

Project done in collaboration with Xavier Favory, Eduardo Fonseca and Frederic Font. 

## Usage
Open `index.html` in your browser! It requires the following files next to it: `ontology.html5.json` (AudioSet Ontology properly formatted for our html) and `d3.v3.min.js` (D3 library for visualizations).

In case `ontology.html5.json` is not available:
1. Open `/AudioSetOntologyTree/preprocessing/` folder. It contains: `ontology.json` (AudioSet Ontology as in https://github.com/audioset/ontology) and `preprocessing.py` (python file for properly formatting the AudioSet Ontology).
2. Run: `python preprocessing.py` - to generate `/AudioSetOntologyTree/ontology.html5.json` file!

If AudioSet Ontology changes, one can re-compute `ontology.html5.json` by changing `ontology.json` with the updated AudioSet Ontology.
