from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

def sparql_query(where_clause, object):
    query = f"""
    PREFIX kgc: <http://kgc.knowledge-graph.jp/ontology/kgc.owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX cc: <http://creativecommons.org/ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    SELECT DISTINCT ?{object}
    FROM <http://kgc.knowledge-graph.jp/data/SpeckledBand>
    WHERE {{
        {where_clause}
        FILTER(LANG(?{object}) = 'en')
    }}
    """

    sparql = SPARQLWrapper("http://kg.hozo.jp/fuseki/ikgrc/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    list = []

    for result in results["results"]["bindings"]:
        label = result[object]["value"]
        list.append(label)

    list = pd.DataFrame(list, columns=[object])

    return list

def count_freq(df1, df2, obj, trg):
    df1['count'] = 0

    for target in df2[trg]:
        for object in df1[obj]:
            if object in target:
                df1.loc[df1[obj] == object, "count"] += 1

    df1.sort_values("count", ascending=False, inplace=True)

    return df1

def query_person_situation(person):

    sparql = SPARQLWrapper("http://kg.hozo.jp/fuseki/ikgrc/sparql")
    query = f"""
    PREFIX kgc: <http://kgc.knowledge-graph.jp/ontology/kgc.owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?s ?o ?o2 ?o3 ?o4 ?o5 ?o6
    FROM <http://kgc.knowledge-graph.jp/data/SpeckledBand>
    WHERE {{
        ?s rdf:type kgc:Situation;
            kgc:subject <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> ;
            kgc:hasPredicate ?o5 ;
            kgc:source ?o ;
            kgc:what ?o2 .
        ?o2 rdfs:label ?o3 .
        ?o5 rdfs:label ?o6 .
        <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> rdfs:label ?o4 .
        
        FILTER(LANG(?o) = 'en')
        FILTER(LANG(?o3) = 'en')
        FILTER(LANG(?o4) = 'en')
        FILTER(LANG(?o6) = 'en')
    }}
    """
    #TODO: kgc:subject가 두 개 이상 정의되어 있는 것들이 있는데 어떻게 해야 할지 모르겠음.
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)


    subjects = []
    objects = []
    whats = []
    person = []
    haspredicate = []
    type = []

    for result in results["results"]["bindings"]:
        subject = result["s"]["value"]
        object = result["o"]["value"]
        what = result["o3"]["value"]
        who = result["o4"]["value"]
        predicate = result["o6"]["value"]

        subjects.append(subject)
        objects.append(object)
        whats.append(what)
        person.append(who)
        haspredicate.append(predicate)
        type.append("Situation")

    csv = pd.DataFrame({"ID": subjects, "People": person, "Event": objects, "What": whats, "hasPredicate": haspredicate, "Type": type})
    # csv.to_csv(f"{person}.csv", index=False)

    return csv


def query_person_statement(person):
    sparql = SPARQLWrapper("http://kg.hozo.jp/fuseki/ikgrc/sparql")
    query = f"""
    PREFIX kgc: <http://kgc.knowledge-graph.jp/ontology/kgc.owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?s ?o ?o2 ?o3 ?o4 ?o5 ?o6
    FROM <http://kgc.knowledge-graph.jp/data/SpeckledBand>
    WHERE {{
        ?s rdf:type kgc:Statement;
            kgc:subject <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> ;
            kgc:hasPredicate ?o5 ;
            kgc:source ?o ;
            kgc:what ?o2 .
        ?o2 rdfs:label ?o3 .
        ?o5 rdfs:label ?o6 .
        <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> rdfs:label ?o4 .

        FILTER(LANG(?o) = 'en')
        FILTER(LANG(?o3) = 'en')
        FILTER(LANG(?o4) = 'en')
        FILTER(LANG(?o6) = 'en')
    }}
    """
    # TODO: kgc:subject가 두 개 이상 정의되어 있는 것들이 있는데 어떻게 해야 할지 모르겠음.
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)

    subjects = []
    objects = []
    whats = []
    person = []
    haspredicate = []
    type = []

    for result in results["results"]["bindings"]:
        subject = result["s"]["value"]
        object = result["o"]["value"]
        what = result["o3"]["value"]
        who = result["o4"]["value"]
        predicate = result["o6"]["value"]

        subjects.append(subject)
        objects.append(object)
        whats.append(what)
        person.append(who)
        haspredicate.append(predicate)
        type.append("Statement")

    csv = pd.DataFrame(
        {"ID": subjects, "People": person, "Event": objects, "What": whats, "hasPredicate": haspredicate, "Type": type})
    # csv.to_csv(f"{person}.csv", index=False)

    return csv

def query_person_thought(person):
    sparql = SPARQLWrapper("http://kg.hozo.jp/fuseki/ikgrc/sparql")
    query = f"""
    PREFIX kgc: <http://kgc.knowledge-graph.jp/ontology/kgc.owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?s ?o ?o2 ?o3 ?o4 ?o5 ?o6
    FROM <http://kgc.knowledge-graph.jp/data/SpeckledBand>
    WHERE {{
        ?s rdf:type kgc:Thought ;
            kgc:subject <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> ;
            kgc:hasPredicate ?o5 ;
            kgc:source ?o ;
            kgc:what ?o2 .
        ?o2 rdfs:label ?o3 .
        ?o5 rdfs:label ?o6 .
        <http://kgc.knowledge-graph.jp/data/SpeckledBand/{person}> rdfs:label ?o4 .

        FILTER(LANG(?o) = 'en')
        FILTER(LANG(?o3) = 'en')
        FILTER(LANG(?o4) = 'en')
        FILTER(LANG(?o6) = 'en')
    }}
    """
    # TODO: kgc:subject가 두 개 이상 정의되어 있는 것들이 있는데 어떻게 해야 할지 모르겠음.
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)

    subjects = []
    objects = []
    whats = []
    person = []
    haspredicate = []
    type= []

    for result in results["results"]["bindings"]:
        subject = result["s"]["value"]
        object = result["o"]["value"]
        what = result["o3"]["value"]
        who = result["o4"]["value"]
        predicate = result["o6"]["value"]

        subjects.append(subject)
        objects.append(object)
        whats.append(what)
        person.append(who)
        haspredicate.append(predicate)
        type.append("Thought")

    csv = pd.DataFrame(
        {"ID": subjects, "People": person, "Event": objects, "What": whats, "hasPredicate": haspredicate, "Type": type})
    # csv.to_csv(f"{person}.csv", index=False)

    return csv