import json

def fetch_mark (restrictions):
	marks=[]
	if "abstract" in restrictions:
		marks.append("abstract")
	if "blacklist" in restrictions:
		marks.append("blacklist")
	return marks

# formating input .json to a .json format readable for this tree visualization code: https://bl.ocks.org/mbostock/4339083

# 0. read AudioSet Ontology data
with open('ASO.json') as data_file:    
	raw_aso = json.load(data_file)

# format as dictionary:
## aso["/m/0dgw9r"] > {'restrictions': [u'abstract'], 'child_ids': [u'/m/09l8g', u'/m/01w250', u'/m/09hlz4', u'/m/0bpl036', u'/m/0160x5', u'/m/0k65p', u'/m/01jg02', u'/m/04xp5v', u'/t/dd00012'], 'name': u'Human sounds'}
aso={}
for category in raw_aso:
	tmp={}
	tmp["name"]=category["name"]	
	tmp["restrictions"]=category["restrictions"]
	tmp["child_ids"]=category["child_ids"]
	tmp["parents_ids"]=[]
	aso[category["id"]]=tmp

# 1. fetch higher_categories > ["/m/0dgw9r","/m/0jbk","/m/04rlf","/t/dd00098","/t/dd00041","/m/059j3w","/t/dd00123"]
for cat in aso: # find parents
	for c in aso[cat]["child_ids"]:
		aso[c]["parents_ids"].append(cat)

higher_categories=[] # higher_categories are the ones without parents
for cat in aso: 
	if aso[cat]["parents_ids"]==[]:
		higher_categories.append(cat)

# 2. format ASO properly!
out_json={}
out_json["name"]="Ontology"
out_json["children"]=[]
for category in higher_categories:
	dict1 = {}
	dict1["name"] = aso[category]["name"]
	dict1["mark"]=fetch_mark(aso[category]["restrictions"])
	childs2 = aso[category]["child_ids"]
	childs_names2=[]
	for child2 in childs2:
		child_name2 = {}
		child_name2["name"] = aso[child2]["name"]
		child_name2["mark"]=fetch_mark(aso[child2]["restrictions"])
		if "child_ids" in aso[child2]:
			childs3 = aso[child2]["child_ids"]
			childs_names3=[]
			for child3 in childs3:
				child_name3 = {}
				child_name3["name"] = aso[child3]["name"]
				child_name3["mark"]=fetch_mark(aso[child3]["restrictions"])
				if "child_ids" in aso[child3]:
					childs4 = aso[child3]["child_ids"]
					childs_names4=[]
					for child4 in childs4:
						child_name4 = {}
						child_name4["name"] = aso[child4]["name"]
						child_name4["mark"]=fetch_mark(aso[child4]["restrictions"])
						if "child_ids" in aso[child4]:
							childs5 = aso[child4]["child_ids"]
							childs_names5=[]
							for child5 in childs5:
								child_name5 = {}
								child_name5["name"] = aso[child5]["name"]
								child_name5["mark"]=fetch_mark(aso[child5]["restrictions"])
								childs_names5.append(child_name5)
							if childs_names5 : child_name4["children"]=childs_names5
						childs_names4.append(child_name4)
					if childs_names4 : child_name3["children"]=childs_names4
				childs_names3.append(child_name3)
			if childs_names3 : child_name2["children"]=childs_names3
		childs_names2.append(child_name2)
	if childs_names2 : dict1["children"]=childs_names2
	out_json["children"].append(dict1)

# 3. saving output .json
with open('./../ASO.html5.json', 'w') as f:
     json.dump(out_json, f, ensure_ascii=False)
