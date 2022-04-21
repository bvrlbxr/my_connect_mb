from connector import My_connector

# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)



if __name__ == "__main__":

    # (0, 1) по факту 40000, 1 - считывается 40001 регистр
    temp_sens = My_connector(("127.0.0.1", 5440), (0,1),"temp_sens_1")
    temp_sens.run()
