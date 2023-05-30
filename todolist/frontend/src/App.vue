<template>
  <div>
    <button @click="fetchTasks"> Fetch task list</button>
    <div>
      <ul>
        <li v-for="task in tasks">
          {{ task.priority }} 
          {{task.task_name}}
          {{task.time}}
          <span v-if="task.complete"></span>
          <span v-else></span>
          <label for="completed">completed:</label>
          <input type="checkbox" name="completed" id="completed"><br>
          <span><button class = "btn btn-danger p-2" v-on:click="deleteTask(task.id)">delete</button></span>
        </li>
      </ul>
      
      <br>
      <form id="addTaskForm">
        <label for="priority_no">Priority level:</label>
        <input type="number" name="priority_no" id="priority_no"><br>

        <label for="the_task">Task:</label>
        <input type="text" name="the_task" id="the_task"><br>

        <label for="task_time">Time:</label>
        <input type="time" name="task_time" id="task_time"><br>

      </form>
    
      <button type="button" form="addTaskForm" value="Submit" v-on:click="addTask">add task</button><br>  
    </div>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
export default{
   data(){
    return{
      tasks: [],
    }
   },
   methods:{
    async fetchTasks(){
      let response = await fetch("http://localhost:8000/api/tasks",{
        method: "GET",
      })
      let data = await response.json()
      this.tasks = data.tasks
    },
    async addTask() {
      const data = new FormData(document.getElementById("addTaskForm"));
      let response = await fetch("http://localhost:8000/api/tasks", {
        method: "POST",
        body: data,
      });
      this.fetchTasks();
    },
    async deleteTask(id) {
      let response = await fetch("http://localhost:8000/api/tasks", {
        method: "DELETE",
      });
      let data = await response.json();
      console.log(data);
      this.fetchTasks();
    },
    async editTask() {
      const data = new FormData(document.getElementById("edit"));
      let response = await fetch("http://localhost:8000/api/tasks/<int:task_id>", {
        method: "PUT",
        body: JSON.stringify(data),
      });
      this.fetchTasks();
    },
   },
   
   mounted(){
      this.fetchTasks();
   },
};
</script> 












