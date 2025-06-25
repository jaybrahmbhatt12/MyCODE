function addTask()
{
    const input = document.getElementById("taskInput");
    const taskText = input.value.trim();
    if (taskText === "") return;

    const timestamp = new Date().toLocaleString();
    const li = createTaskElement(taskText, timestamp, false);
    document.getElementById("pendingList").appendChild(li);

    input.value = "";
}

function createTaskElement(text, time, isCompleted)
{
    const li = document.createElement("li");
    const content = document.createElement("span");
    content.innerHTML = `<strong>${text}</strong><br><small>${time}</small>`;

    const actions = document.createElement("div");
    actions.className = "task-actions";

    if (!isCompleted)
    {
    const completeBtn = document.createElement("button");
    completeBtn.textContent = "✔️ Done";
    completeBtn.onclick = () => completeTask(li, text);
    actions.appendChild(completeBtn);
    }

    const editBtn = document.createElement("button");
    editBtn.textContent = "✏️ Edit";
    editBtn.onclick = () => editTask(li, text);
    actions.appendChild(editBtn);

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "🗑️ Delete";
    deleteBtn.onclick = () => li.remove();
    actions.appendChild(deleteBtn);

    li.appendChild(content);
    li.appendChild(actions);
    return li;
}

function completeTask(taskElement, text)
{
    taskElement.remove();
    const time = new Date().toLocaleString();
    const completedTask = createTaskElement(text, `Completed: ${time}`, true);
    document.getElementById("completedList").appendChild(completedTask);
}

function editTask(taskElement, oldText)
{
    const newText = prompt("Edit your task:", oldText);
    if (newText)
    {
        const time = new Date().toLocaleString();
        const isCompleted = taskElement.parentNode.id === "completedList";
        const updatedTask = createTaskElement(newText, isCompleted ? `Completed: ${time}` : time, isCompleted);
        taskElement.replaceWith(updatedTask);
    }
}
