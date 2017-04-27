import json
def T_mean(data):
    x= sum(data)
    y=len(data)
    t= x*1.0/y
    return t
topo_NoIRLM=[[],[],[],[]]
topo_NoERLM=[[],[],[],[]]
#green
with open("exp2_5r1_lookup.json") as file_json:
    a=json.load(file_json)
topo_NoIRLM[0].append(T_mean(a['numsteps']))
topo_NoERLM[0].append(T_mean(a['numroutes']))
#red
with open("exp2_5r1_432_lookup.json") as file_json:
    b=json.load(file_json)
topo_NoIRLM[1].append(T_mean(b['numsteps']))
topo_NoERLM[1].append(T_mean(b['numroutes']))
#blue
with open("exp2_5r1_4321_lookup.json") as file_json:
    c=json.load(file_json)
topo_NoIRLM[2].append(T_mean(c['numsteps']))
topo_NoERLM[2].append(T_mean(c['numroutes']))
#yello
with open("exp2_5r1_43210_lookup.json") as file_json: 
    d=json.load(file_json)
topo_NoIRLM[3].append(T_mean(d['numsteps']))
topo_NoERLM[3].append(T_mean(d['numroutes']))


with open("exp2_5r5_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[0].append(T_mean(s['numsteps']))
topo_NoERLM[0].append(T_mean(s['numroutes']))
with open("exp2_5r5_432_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[1].append(T_mean(s['numsteps']))
topo_NoERLM[1].append(T_mean(s['numroutes']))
with open("exp2_5r5_4321_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[2].append(T_mean(s['numsteps']))
topo_NoERLM[2].append(T_mean(s['numroutes']))
with open("exp2_5r5_43210_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[3].append(T_mean(s['numsteps']))
topo_NoERLM[3].append(T_mean(s['numroutes']))

with open("exp2_5r10_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[0].append(T_mean(s['numsteps']))
topo_NoERLM[0].append(T_mean(s['numroutes']))
with open("exp2_5r10_432_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[1].append(T_mean(s['numsteps']))
topo_NoERLM[1].append(T_mean(s['numroutes']))
with open("exp2_5r10_4321_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[2].append(T_mean(s['numsteps']))
topo_NoERLM[2].append(T_mean(s['numroutes']))
with open("exp2_5r10_43210_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[3].append(T_mean(s['numsteps']))
topo_NoERLM[3].append(T_mean(s['numroutes']))

with open("exp2_5r15_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[0].append(T_mean(s['numsteps']))
topo_NoERLM[0].append(T_mean(s['numroutes']))
with open("exp2_5r15_432_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[1].append(T_mean(s['numsteps']))
topo_NoERLM[1].append(T_mean(s['numroutes']))
with open("exp2_5r15_4321_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[2].append(T_mean(s['numsteps']))
topo_NoERLM[2].append(T_mean(s['numroutes']))
with open("exp2_5r15_43210_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[3].append(T_mean(s['numsteps']))
topo_NoERLM[3].append(T_mean(s['numroutes']))

with open("exp2_5r20_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[0].append(T_mean(s['numsteps']))
topo_NoERLM[0].append(T_mean(s['numroutes']))
with open("exp2_5r20_432_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[1].append(T_mean(s['numsteps']))
topo_NoERLM[1].append(T_mean(s['numroutes']))
with open("exp2_5r20_4321_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[2].append(T_mean(s['numsteps']))
topo_NoERLM[2].append(T_mean(s['numroutes']))
with open("exp2_5r20_43210_lookup.json") as file_json:
    s=json.load(file_json)
topo_NoIRLM[3].append(T_mean(s['numsteps']))
topo_NoERLM[3].append(T_mean(s['numroutes']))

# j=0
# while j<4 :
#     print(topo_NoIRLM[j])
#     print(topo_NoERLM[j])
#     j+=1