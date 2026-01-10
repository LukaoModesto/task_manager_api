from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy #orm para o banco

print ("servidor iniciado")
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #otimização

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) #chave primaria
    title = db.Column(db.String(100), nullable=False) #obrigatorio :v
    done = db.Column(db.Boolean, default=False) #status da tarefa

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}
    
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "API rodando com sucesso"}

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all() #busca as tarefas no banco
    return jsonify([task.to_dict() for task in tasks])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Campo 'title' é obrigatorio"}), 400

    task = Task(title=data["title"])
    db.session.add(task) #adiciona ao banco
    db.session.commit() #salva
    return jsonify(task.to_dict()), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON obrigatorio"}), 400
    
    #Busca a tarefa pelo id
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarefa nao encontrada"}), 404
    
    # Atualiza os campos se vierem no JSON

    if "title" in data:
        task.title = data["title"]
    if "done" in data:
        task.done = data["done"]

    db.session.commit() #salva alterações
    return jsonify(task.to_dict()), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    
    db.session.delete(task) #remove do banco
    db.session.commit()
    return jsonify({"message": "Tarefa deletada"}), 200

if __name__ == "__main__":
    app.run(debug=True)