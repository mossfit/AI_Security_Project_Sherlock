import pandas as pd
from query import query_person_situation, query_person_statement, query_person_thought

julia_situation = query_person_situation("Julia")
holmes_situation = query_person_situation("Holmes")
roylott_situation = query_person_situation("Roylott")
helen_situation = query_person_situation("Helen")
watson_situation = query_person_situation("Watson")
man_situation = query_person_situation("man")
sister_situation = query_person_situation("sister")
roma_situation = query_person_situation("Roma")
coroner_situation = query_person_situation("coroner")
housekeeper_situation = query_person_situation("housekeeper")
culprit_situation = query_person_situation("culprit")
all_people_situation = pd.concat([julia_situation, holmes_situation, roylott_situation, helen_situation, watson_situation, man_situation, sister_situation,
                        roma_situation, coroner_situation, housekeeper_situation, culprit_situation], axis=0)

all_people_situation.to_csv("all_people_situation.csv", index=False)

julia_statement = query_person_statement("Julia")
holmes_statement = query_person_statement("Holmes")
roylott_statement = query_person_statement("Roylott")
helen_statement = query_person_statement("Helen")
watson_statement = query_person_statement("Watson")
man_statement = query_person_statement("man")
sister_statement = query_person_statement("sister")
roma_statement = query_person_statement("Roma")
coroner_statement = query_person_statement("coroner")
housekeeper_statement = query_person_statement("housekeeper")
culprit_statement = query_person_statement("culprit")
all_people_statement = pd.concat([julia_statement, holmes_statement, roylott_statement, helen_statement, watson_statement, man_statement, sister_statement,
                        roma_statement, coroner_statement, housekeeper_statement, culprit_statement], axis=0)

all_people_statement.to_csv("all_people_statement.csv", index=False)

julia_thought = query_person_thought("Julia")
holmes_thought = query_person_thought("Holmes")
roylott_thought = query_person_thought("Roylott")
helen_thought = query_person_thought("Helen")
watson_thought = query_person_thought("Watson")
man_thought = query_person_thought("man")
sister_thought = query_person_thought("sister")
roma_thought = query_person_thought("Roma")
coroner_thought = query_person_thought("coroner")
housekeeper_thought = query_person_thought("housekeeper")
culprit_thought = query_person_thought("culprit")
all_people_thought = pd.concat([julia_thought, holmes_thought, roylott_thought, helen_thought, watson_thought, man_thought, sister_thought,
                                roma_thought, coroner_thought, housekeeper_thought, culprit_thought], axis=0)
all_people_thought.to_csv("all_people_thought.csv", index=False)


all_people = pd.concat([all_people_situation, all_people_statement, all_people_thought], axis=0)
all_people["ID"].replace("http://kgc.knowledge-graph.jp/data/SpeckledBand/", "", regex=True, inplace=True)
all_people.to_csv("all_people.csv", index=False)




