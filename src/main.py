import logging
from typing import List
from core.mdpio import CoreIO

def run(core:CoreIO):
    try:
        # get task inputs
        inputs:List = core.get_inputs()

        # Get the ABNF definition for the EnergyWeb DID
        DID:str = "did:{}:{}".format(inputs["method"], inputs["address"])

        # set task outputs
        core.set_outputs([DID.encode("utf-8")])
    except Exception as error:
        logging.error(error)