import pandas as pd
from query import sparql_query, query_person_situation, query_person_statement, query_person_thought, query_person_situation_when, \
    query_person_statement_when, query_person_thought_when, query_person_situation_where, query_person_statement_where, \
    query_person_thought_where, query_person_situation_whom, query_person_statement_whom, query_person_thought_whom

people = sparql_query('?s rdf:type kgc:Person ; rdfs:label')
people = [element.replace(' ', '_') for element in people]
print(people)

all_people_situation = query_person_situation(people)
all_people_situation.to_csv("all_people_situation.csv", index=False)
all_people_statement = query_person_statement(people)
all_people_statement.to_csv("all_people_statement.csv", index=False)
all_people_thought = query_person_thought(people)
all_people_thought.to_csv("all_people_thought.csv", index=False)
all_people = pd.concat([all_people_situation, all_people_statement, all_people_thought], axis=0, ignore_index=True)
all_people["ID"].replace("http://kgc.knowledge-graph.jp/data/SpeckledBand/", "", regex=True, inplace=True)

all_people_situation_when = query_person_situation_when(people)
all_people_situation_when.to_csv("all_people_situation_when.csv", index=False)
all_people_statement_when = query_person_statement_when(people)
all_people_statement_when.to_csv("all_people_statement_when.csv", index=False)
all_people_thought_when = query_person_thought_when(people)
all_people_thought_when.to_csv("all_people_thought_when.csv", index=False)
all_people_when = pd.concat([all_people_situation_when, all_people_statement_when, all_people_thought_when], axis=0,
                            ignore_index=True)
all_people_when.to_csv("all_people_when.csv", index=False)
all_people_when["ID"].replace("http://kgc.knowledge-graph.jp/data/SpeckledBand/", "", regex=True, inplace=True)

for idx, row in all_people.iterrows():
    for idx_2, row_2 in all_people_when.iterrows():
        if row["Event"] == row_2["Event"]:
            all_people.loc[idx, "When"] = all_people_when.loc[idx_2, "When"]
            all_people_when.drop(index=idx_2, inplace=True)
            break
all_people = pd.concat([all_people, all_people_when], axis=0, ignore_index=True)

all_people_situation_where = query_person_situation_where(people)
all_people_situation_where.to_csv("all_people_situation_where.csv", index=False)
all_people_statement_where = query_person_statement_where(people)
all_people_statement_where.to_csv("all_people_statement_where.csv", index=False)
all_people_thought_where = query_person_thought_where(people)
all_people_thought_where.to_csv("all_people_thought_where.csv", index=False)
all_people_where = pd.concat([all_people_situation_where, all_people_statement_where, all_people_thought_where], axis=0,
                                ignore_index=True)
all_people_where["ID"].replace("http://kgc.knowledge-graph.jp/data/SpeckledBand/", "", regex=True, inplace=True)

for idx, row in all_people.iterrows():
    for idx_2, row_2 in all_people_where.iterrows():
        if row["Event"] == row_2["Event"]:
            all_people.loc[idx, "Where"] = all_people_where.loc[idx_2, "Where"]
            all_people_where.drop(index=idx_2, inplace=True)
            break

all_people = pd.concat([all_people, all_people_where], axis=0, ignore_index=True)

all_people_situation_whom = query_person_situation_whom(people)
all_people_situation_whom.to_csv("all_people_situation_whom.csv", index=False)
all_people_statement_whom = query_person_statement_whom(people)
all_people_statement_whom.to_csv("all_people_statement_whom.csv", index=False)
all_people_thought_whom = query_person_thought_whom(people)
all_people_thought_whom.to_csv("all_people_thought_whom.csv", index=False)
all_people_whom = pd.concat([all_people_situation_whom, all_people_statement_whom, all_people_thought_whom], axis=0,
                                ignore_index=True)
all_people_whom["ID"].replace("http://kgc.knowledge-graph.jp/data/SpeckledBand/", "", regex=True, inplace=True)


for idx, row in all_people.iterrows():
    for idx_2, row_2 in all_people_whom.iterrows():
        if row["Event"] == row_2["Event"]:
            all_people.loc[idx, "Whom"] = all_people_whom.loc[idx_2, "Whom"]
            all_people_whom.drop(index=idx_2, inplace=True)
            break

all_people = pd.concat([all_people, all_people_whom], axis=0, ignore_index=True)


all_people.to_csv("all_people.csv", index=False)






