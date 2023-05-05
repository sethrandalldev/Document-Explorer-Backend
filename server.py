from flask import Flask
from flask import request
from os import scandir
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.post("/question")
def get_question():
    print(request.form.get("document_id"))
    print(request.form.get("question"))
    return "Document"

@app.post("/documents")
def add_document():
    print(request.form)
    file = request.files.get("document")
    file.save(f"files/{request.form.get('title')}.pdf")
    return "Success", 204

@app.get("/documents")
def get_all_documents():
    entries = scandir("files")
    response = []
    i = 0
    for entry in entries:
        if entry.is_file():
            response.append({
                "id": i,
                "title": entry.name
            })
        i += 1
    return response

@app.get("/documents/<int:document_id>")
def get_document_by_id(document_id):
    for document in documents:
        if document["id"] == document_id:
            return document
    return "Not found", 404