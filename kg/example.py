from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
sparql = SPARQLWrapper("https://dbpedia.org/sparql")


sparql.setQuery("""
                      # Prologue
    select ?s ?p ?o { # Projection (columns)
        ?s ?p ?o .    # Pattern (cells)
    }
    limit 10          # Modifier (rows)
""")

sparql.setReturnFormat(JSON)
result = sparql.query().convert()
pprint(result)