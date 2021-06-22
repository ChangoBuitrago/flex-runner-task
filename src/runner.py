#!/usr/bin/env python3

import importlib.util
import threading

import yaml

from core.mdpio import CoreIO


def main():   
    stream = open("./src/task.yaml", 'r')
    task_yaml = yaml.load(stream, Loader=yaml.FullLoader)

    name:str=task_yaml["name"]
    main_path:bool=task_yaml["runs"]["main"]["path"]
    keep_alive:bool=task_yaml["runs"]["main"]["keep_alive"]

    spec = importlib.util.spec_from_file_location("main", main_path)
    main = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main)

    print("Running '{}' task".format(name))
    core:CoreIO = CoreIO(name, keep_alive)
    threading.Thread(target=main.run(core)).start()

main()
