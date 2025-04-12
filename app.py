from flask import Flask, request, jsonify 
from models.task import Task

app = Flask(__name__)  # Cria uma instância da aplicação Flask

tasks = []
task_id_control = 1

# Criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
   global task_id_control # Variável global
   data = request.get_json()
   new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
   task_id_control += 1
   tasks.append(new_task)
   print(tasks)
   return jsonify({"message": "Nova tarefa criada com sucesso"})

# Listagem de Todas as Tarefas Cadastradas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
 
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)


# Listar única tarefa
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
   for t in tasks:
       if t.id == id:
           return jsonify(t.to_dict())
 
   return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


# Editar Tarefa
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
   task = None
   
   for t in tasks:
     if t.id == id:
       task = t
   
   if task == None:
     return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
 
   data = request.get_json()
   task.title = data['title']
   task.description = data['description']
   task.completed = data['completed']
   
   return jsonify({"message": "Tarefa atualizada com sucesso"})

# Deletar tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
   task = None
   for t in tasks:
     if t.id == id:
       task = t
       break
 
     if not task:
       return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
     
     tasks.remove(task)
     return jsonify({"message": "Tarefa deletada com sucesso"})


# Verifica se o script está sendo executado diretamente
# Inicia o servidor Flask com modo debug ativado
if __name__ == "__main__":  
    app.run(debug=True)  
