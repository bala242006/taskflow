const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const stats = document.getElementById("stats");


async function loadTasks() {
    const response = await fetch("/api/tasks");
    const tasks = await response.json();

    renderTasks(tasks);
}


function renderTasks(tasks) {
    taskList.innerHTML = "";

    if (tasks.length === 0) {
        taskList.innerHTML = `
            <div class="empty-state">
                🎉 No tasks yet! Add one to get started.
            </div>
        `;

        stats.textContent = "";
        return;
    }

    tasks.forEach(task => {

        const li = document.createElement("li");

        li.innerHTML = `
            <span class="${task.completed ? "completed" : ""}">
                ${task.title}
            </span>

            <div class="actions">

                <button
                    class="done-btn"
                    onclick="toggleTask(${task.id}, ${!task.completed})">
                    ${task.completed ? "↩️" : "✓"}
                </button>

                <button
                    class="delete-btn"
                    onclick="deleteTask(${task.id})">
                    🗑️
                </button>

            </div>
        `;

        taskList.appendChild(li);
    });

    stats.textContent = `Total Tasks: ${tasks.length}`;
}


taskForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const title = taskInput.value.trim();

    if (!title) {
        return;
    }

    await fetch("/api/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title })
    });

    taskInput.value = "";

    loadTasks();
});


async function toggleTask(id, completed) {

    await fetch(`/api/tasks/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ completed })
    });

    loadTasks();
}


async function deleteTask(id) {

    if (!confirm("Delete this task?")) {
        return;
    }

    await fetch(`/api/tasks/${id}`, {
        method: "DELETE"
    });

    loadTasks();
}


loadTasks();
