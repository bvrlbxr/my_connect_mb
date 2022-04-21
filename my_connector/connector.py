from thingsboard_gateway.connectors.connector import Connector
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
import time
import datetime

# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

class My_connector(Connector):

    """
    reg_address = (address,count)
    ip_address = (address,port)
    """

    def __init__(self, ip_address, reg_address, name):
        self.ip_address = ip_address[0]
        self.My_connector = ModbusTcpClient(ip_address[0], ip_address[1], timeout=3)
        self.stopped = False
        self.reg_address = reg_address
        self.name = name

        try:
            self.My_connector.connect()
        except ConnectionException:
            print("Connection Failed!")

    def run(self):

        with open(f"./{self.name}.txt", "a") as f:

            while True:

                if not self.stopped:
                    data = self.My_connector.read_holding_registers(self.reg_address[0]
                                                                    , self.reg_address[1]
                                                                    , unit=1)

                    f.write(f"{data.registers[0]},{str(datetime.datetime.now())[:-7]}\n")
                    time.sleep(0.5)

                if self.stopped:
                    break

    def close(self):
        self.stopped = True

    def open(self):
        pass

    def get_name(self):
        pass

    def is_connected(self):
        pass

    def on_attributes_update(self, content):
        pass

    def server_side_rpc_handler(self, content):
        pass

