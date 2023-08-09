from behave import given, when, then
from todo_list import ToDoList


@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()


@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        task_desc = row["Task"]
        context.todo_list.add_task(task_desc)
        if "Status" in row and row["Status"] == "Completed":
            context.todo_list.mark_task_as_completed(task_desc)


@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)


@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = context.todo_list.list_tasks()


@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_list.mark_task_as_completed(task)


@when('the user removes the task "{task}"')
def step_impl(context, task):
    context.todo_list.remove_task(task)


@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear()


@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    found_task = context.todo_list.find_task(task)
    assert found_task is not None, f'Task "{task}" not found in the to-do list'


@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    found_task = context.todo_list.find_task(task)
    assert found_task is None, f'Task "{task}" was found in the to-do list'


@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    found_task = context.todo_list.find_task(task)
    assert found_task.status == "Completed", f'Task "{task}" is not marked as completed'


@then('the to-do list should be empty')
def step_impl(context):
    assert not context.todo_list.tasks, 'To-do list is not empty'


@then('the output should contain')
def step_impl(context):
    for row in context.table:
        task_desc = row["Task"]
        found_task = context.todo_list.find_task(task_desc)
        assert found_task is not None, f'Task "{task_desc}" not found in listed tasks'
