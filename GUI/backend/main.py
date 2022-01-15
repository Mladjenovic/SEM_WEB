import json
from flask_cors import CORS
from config import DevConfig
from flask_restx import Resource, Namespace, Api
from flask import Flask, request, jsonify, make_response, abort

from SPARQLWrapper import SPARQLWrapper, JSON, XML


app = Flask(__name__)
app.config.from_object(DevConfig)

CORS(app)

api = Api(app, doc='/docs')

query_ns = Namespace('query', description='Sparql query namespace')
api.add_namespace(query_ns)


@query_ns.route('/query1')
class Query1(Resource):
    def post(self):
        data = request.get_json()
        
        professor_name = data['professor_name']
        print(professor_name)
        queryString =   "prefix ns: <http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#> select distinct ?x ?contains_professors where { {?x ns:contains_professors  ?contains_professors filter regex(?contains_professors , "+ f"\"{professor_name}\"" + ") } .  }"
                        
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(queryString)
        sparql.setReturnFormat(JSON)

        try :
            results = sparql.query().convert()
            
            retval = []
            for result in results["results"]["bindings"]:
                print(result.get('x').get('value').split('#')[1])
                retval.append(result.get('x').get('value').split('#')[1])
                
            save_path_file = "query1_output.json"
            with open(save_path_file, "w") as f:
                f.write(json.dumps(results)) 

        except Exception as e:
            print(str(e))
            

        return jsonify({"Query1" : retval})

        
@query_ns.route('/query2')
class Query1(Resource):
    def get(self):
        queryString =   """     
                            prefix ns: <http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#>
                            select distinct ?subjectTitle ?subjectOutcomes ?contains_professors
                            where {
                                {?x  ns:subjectOutcomes ?subjectOutcomes filter regex(?subjectOutcomes, "Java")}. 
                                {?x ns:contains_professors ?contains_professors} .
                                {?x ns:subjectTitle  ?subjectTitle}
                            }
                        """
                                
        sparql = SPARQLWrapper("http://localhost:8890/sparql")
        sparql.setQuery(queryString)
        sparql.setReturnFormat(JSON)

        try :
            results = sparql.query().convert()
            
            for result in results["results"]["bindings"]:
                print(result.get('subjectOutcomes').get('value'))
                
            save_path_file = "query2_output.json"
            with open(save_path_file, "w") as f:
                f.write(json.dumps(results)) 

        except Exception as e:
            print(str(e))

        
        return jsonify({"Query2": f"{result.get('subjectTitle').get('value')}"})




@app.route("/", methods=['POST','GET'])
def default_example():
   if request.method == 'GET':
        return "hello world"
    
      

if __name__ == "__main__":
  app.run(debug=True, use_debugger=False, use_reloader=False)