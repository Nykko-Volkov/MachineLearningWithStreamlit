import streamlit as st


with st.form("todo_form"):
    st.title("Todo List App")
    task = st.text_input("Enter a task")
    submit = st.form_submit_button("Add Task")
    if submit:
        st.success(f"Task '{task}' added to the list!")
        with open("todo_list.txt", "a") as f:
            f.write(task + "\n")
            


with open("todo_list.txt", "r") as f:
    tasks = f.readlines()
st.write("## Your Todo List")

cols = st.columns([0.1, 0.7, 0.2])
for i, task in enumerate(tasks):
    cols[0].write(f"{i+1}")
    cols[1].write(task.strip()  )
    if cols[2].button("X", key=f"delete_{i}"):
        tasks.pop(i)
        with open("todo_list.txt", "w") as f:
            f.writelines(tasks)
    # # delete button for each task
