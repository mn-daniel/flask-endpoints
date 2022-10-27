from flask import Flask, render_template, send_file, request
app = Flask('app')

in_memory_datastore = {
   "COBOL" : {
     "name": "COBOL", 
     "publication_year": 1960, 
     "contribution": "record data"
   },
   "ALGOL" : {
     "name": "ALGOL", 
     "publication_year": 1958,
     "contribution": "scoping and nested functions"
   },
   "APL" : {
     "name": "APL", 
     "publication_year": 1962, 
     "contribution": "array processing"
   },
  "BASIC": {
    "name": "BASIC", 
    "publication_year": 1964, 
    "contribution": "runtime interpretation, office tooling"
  },
   "PL": {
     "name": "PL", 
     "publication_year": 1966, 
     "contribution": "constants, function overloading, pointers"
   },
   "SIMULA67": {
     "name": "SIMULA67", 
     "publication_year": 1967, 
     "contribution": "class/object split, subclassing, protected attributes"
   },
   "Pascal": {
     "name": "Pascal", 
     "publication_year": 1970,
     "contribution": "modern unary, binary, and assignment operator syntax expectations"
   },
   "CLU": {
     "name": "CLU", 
     "publication_year": 1975,
     "contribution": "iterators, abstract data types, generics, checked exceptions"
   }
}

@app.route('/')
def index():
  #return render_template("index.html")
  return {"programming_languages":list(in_memory_datastore.values())}

def update_programming_language(lang_name, new_lang_attributes):
   lang_getting_update = in_memory_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update
def delete_programming_language(lang_name):
   deleting_lang = in_memory_datastore[lang_name]
   del in_memory_datastore[lang_name]
   return deleting_lang 
@app.route('/programming_languages/<language>', methods=['GET', 'PUT','DELETE'])
def programming_languages_route(language):
  if request.method == 'GET':
    return in_memory_datastore[language]
  elif request.method == "PUT":
     return update_programming_language(language, request.get_json(force=True))
  elif request.method == "DELETE":
    return delete_programming_language(language)
    
    
def create_programming_language(new_lang):
   language_name = new_lang['name']
   in_memory_datastore[language_name] = new_lang
   return new_lang  
@app.route('/programming_languages', methods=['GET', 'POST'])
def programming_languages_routeII():
   if request.method == 'GET':
       return {"programming_languages":list(in_memory_datastore.values())}
   elif request.method == "POST":
       return create_programming_language(request.get_json(force=True))
    

@app.route('/style.css')
def style():
  return send_file('templates/style.css')

@app.route('/script.js')
def script():
  return send_file('templates/script.js')

@app.route('/favicon.png')
def favicon():
  return send_file('templates/favicon.png')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def server_overloaded(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

app.run(host='0.0.0.0', port=8080)