#!/usr/bin/env python3

import asyncio
import logging
import threading
from secrets import token_hex
from typing import List

from core.mdcliapi import MajorDomoClient
from core.mdwrkapi import MajorDomoWorker

# class ReqSocket():
#     def __init__(self, name:str, endpoint:str):
#         name:bytes = name.encode("utf-8")
#         self.worker = MajorDomoClient(endpoint, name)

#         #  1. Send 'name' request to Titanic
#         request = [name, b"Hello world"]
#         reply = self.service_call(self.worker, b"titanic.request", request)

class RepSocket():
    def __init__(self, name:str, endpoint:str):
        name:bytes = name.encode("utf-8")
        self.worker = MajorDomoWorker(endpoint, name)
        request = self.worker.recv(None)
        if request is None:
            raise # Worker was interrupted

    def recv(self, outputs:List, keep_alive:bool):
        request = self.worker.recv(outputs, keep_alive)
        if request is None:
            raise Exception


class CoreIO():
    # req_socket:ReqSocket
    rep_socket:RepSocket
    keep_alive:bool

    def __init__(self, name:str, keep_alive:bool) -> None:
        self.rep_socket = RepSocket(
            name="{}.outputs".format(name),
            endpoint="tcp://localhost:5555"
        )
        self.keep_alive = keep_alive
        
    def get_inputs(self) -> List:
        # Auth task
        task_input = {
            "address":"0x{}".format(token_hex(40)),
            "method": "ethr"
        }
        return task_input
    
    def set_outputs(self, outputs:List):
        while True:
            self.rep_socket.recv(outputs, self.keep_alive)
