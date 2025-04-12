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


# Verifica se o script está sendo executado diretamente
# Inicia o servidor Flask com modo debug ativado
if __name__ == "__main__":  
    app.run(debug=True)  
