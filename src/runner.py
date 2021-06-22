#!/usr/bin/env python3

import importlib
import threading
from core.mdpio import CoreIO


def main():   
    name:str="get_device_meta"
    keep_alive:bool=True
    main = importlib.import_module('main')

    print("Running 'get_device_meta' task")
    core:CoreIO = CoreIO(name, keep_alive)
    threading.Thread(target=main.run(core)).start()

main()
