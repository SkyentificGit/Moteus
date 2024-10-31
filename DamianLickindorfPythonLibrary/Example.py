from moteus_fdcan_adapter import Controller
from moteus_fdcan_adapter import MoteusReg
import time
import math


def main():
    controller_1 = Controller(controller_ID = 1, device='/dev/ttyACM0')
    
    # read two encoders (if you have two, properly configured)
    response_data_enc = controller_1.get_data_enc()
    print(response_data_enc[MoteusReg.MOTEUS_REG_POSITION])
    print(response_data_enc[MoteusReg.MOTEUS_REG_ENC_2_POS])
    
    # read driver temperature and motor temperature
    response_data = controller_1.get_data()
    print(response_data[MoteusReg.MOTEUS_REG_TEMP])
    response_data_temp = controller_1.get_data_temp()
    print(response_data_temp[MoteusReg.MOTEUS_REG_MOTOR_TEMP])
    
    
    
    #controller_1.serial.write(b"can off\n")
    #response = controller_1.serial.readline()
    #print("Reply from CAN is off: ", response.decode('latin1'))
    # write compensation value to driver:
    #controller_1.serial.write(f"conf set motor_position.sources.2.compensation_table.4 0.1234\n".encode('utf8'))
    controller_1.serial.write(b"conf load\n")
    response = controller_1.serial.readline()
    print("Reply from CAN conf load command: ", response.decode('latin1'))
    #response = controller_1.serial.readline()
    #print("Reply from CAN conf id.id 2 command: ", response.decode('latin1'))
    controller_1.serial.write(b"can status\n")
    response = controller_1.serial.readline()
    print("Reply from CAN status command: ", response.decode('latin1'))

    #response = controller_1.serial.readline()
    #print("Reply from CAN command: ", response.decode('latin1'))
    #time.sleep(1.0)
    #response = controller_1.serial.readline()
    #print("Reply from CAN command: ", response.decode('latin1'))
    #time.sleep(1.0)
    #controller_1.serial.write(b"can on\n")
    #response = controller_1.serial.readline()
    #print("Reply from CAN command: ", response.decode('latin1'))
    
    
    
 
    
    



if __name__ == '__main__':
    main()
