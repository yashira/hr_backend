from flask import Flask
from flask_cors import CORS
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer import ExplorerPlayground
from flask import request, jsonify
from queries.teacher.queries import listTeacher_resolver
from queries.subject.queries import listSubject_resolver
from mutations.subject.mutation import createSubject_resolver

app = Flask(__name__)
CORS(app)

PLAYGROUND_HTML = ExplorerPlayground(title="Cool API").html(None)

query = ObjectType("Query")
mutation = ObjectType("Mutation")

#Teachers
query.set_field("listTeachers", listTeacher_resolver)

#Subject
query.set_field("listSubjects", listSubject_resolver)
mutation.set_field("createSubject", createSubject_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code