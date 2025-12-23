const taskList = document.getElementById("taskList");
const taskInput = document.getElementById("taskInput");

window.onload = loadTasks;

function loadTasks() {
    fetch("http://127.0.0.1:8000/api/tasks/")
        .then(res => res.json())
        .then(tasks => {
            taskList.innerHTML = "";
            tasks.forEach(task => {
                const li = document.createElement("li");

                const span = document.createElement("span");
                span.textContent = task.text;
                if (task.completed) span.classList.add("completed");

                span.onclick = () => toggleTask(task.id);

                const btn = document.createElement("button");
                btn.textContent = "X";
                btn.onclick = () => deleteTask(task.id);

                li.appendChild(span);
                li.appendChild(btn);
                taskList.appendChild(li);
            });
        });
}

function addTask() {
    if (taskInput.value.trim() === "") return;

    fetch("http://127.0.0.1:8000/api/tasks/add/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: taskInput.value })
    }).then(() => {
        taskInput.value = "";
        loadTasks();
    });
}

function toggleTask(id) {
    fetch(`http://127.0.0.1:8000/api/tasks/${id}/toggle/`, {
        method: "PUT"
    }).then(loadTasks);
}

function deleteTask(id) {
    fetch(`http://127.0.0.1:8000/api/tasks/${id}/delete/`, {
        method: "DELETE"
    }).then(loadTasks);
}
