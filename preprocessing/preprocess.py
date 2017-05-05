import json

def get_all_children(category,aso):
	childs = aso[category]["child_ids"]
	childs_names = []
	for child in childs:
		child_name = {}
		child_name["name"] = aso[child]["name"]
		child_name["mark"] = aso[child]["restrictions"]
		if "child_ids" in aso[child]: child_name["children"] = get_all_children(child,aso)
		childs_names.append(child_name)
	if childs_names : return childs_names

# formating input .json to a .json format readable for this tree visualization code: https://bl.ocks.org/mbostock/4339083

# 0. read AudioSet Ontology data
with open('ontology.json') as data_file:    
	raw_aso = json.load(data_file)

# 1. format data as a dictionary
## aso["/m/0dgw9r"] > {'restrictions': [u'abstract'], 'child_ids': [u'/m/09l8g', u'/m/01w250', u'/m/09hlz4', u'/m/0bpl036', u'/m/0160x5', u'/m/0k65p', u'/m/01jg02', u'/m/04xp5v', u'/t/dd00012'], 'name': u'Human sounds'}
aso = {}
for category in raw_aso:
	tmp = {}
	tmp["name"] = category["name"]	
	tmp["restrictions"] = category["restrictions"]
	tmp["child_ids"] = category["child_ids"]
	tmp["parents_ids"] = []
	aso[category["id"]] = tmp

# 2. fetch higher_categories > ["/m/0dgw9r","/m/0jbk","/m/04rlf","/t/dd00098","/t/dd00041","/m/059j3w","/t/dd00123"]
for cat in aso: # find parents
	for c in aso[cat]["child_ids"]:
		aso[c]["parents_ids"].append(cat)

higher_categories=[] # higher_categories are the ones without parents
for cat in aso: 
	if aso[cat]["parents_ids"] == []:
		higher_categories.append(cat)

# 3. format ASO properly
out_json = {}
out_json["name"] = "Ontology"
out_json["children"] = []
for category in higher_categories:
	dict_level1 = {}
	dict_level1["name"] = aso[category]["name"]
	dict_level1["mark"] = aso[category]["restrictions"]
	dict_level1["children"] = get_all_children(category,aso)
	out_json["children"].append(dict_level1)

# 4. saving output .json
with open('./../ontology.html5.json', 'w') as f:
     json.dump(out_json, f, ensure_ascii=False)
