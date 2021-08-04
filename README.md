# A Tiny Task Handler

A simple and elegant task handler using Flask and Celery. Useful for running time-intensive applications and scale up dynamically to add new tasks with utmost ease.

## Setup
1. Create a `.env` file similar to `.env.example`
2. Start the application by running `docker-compose up`
3. Flask should start at http://localhost:5000

## A working example
1. A sample task named `sleep` has been provided under `./app/configs/`
2. First create a JSON file `sleep.json` something like -
```json
{
  "args": {
    "welcometext": "Sleeping for 10 seconds...",
    "seconds": 10,
    "exittext": "Waking up. Bye!"
  }
}
```
3. Then run the command -
`$ curl -X POST http://localhost:5000/task/sleep -d @sleep.json -H "Content-Type: application/json"`

## Creating a new task
To create a new task, simply create a new configuration file under `./app/configs`. Then perform a `POST` request to `http://localhost:5000/task/<task-name>` to run the new task.
