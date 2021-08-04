import json
from os import getenv


def create_task_commands(params):
    """
    Parse config file and create command to execute
    :param params: arguments received via API call
    :return: commands to be executed
    """
    with open(params["config_file"], "r") as fp:
        task = json.load(fp)

    commands = []

    if "code_url" in task and task["code_url"]:
        commands.append(f"cd {getenv('HOME')} && git clone {task['code_url']}")

    cmd = task["execution"]["command"]

    for i in range(len(task["execution"]["args"])):
        arg = task["execution"]["args"]["arg%s" % (i + 1)]
        cmd += f" --{arg} \"{params['args'][arg]}\""

    commands.append(cmd)
    return commands
