from moteus_fdcan_adapter import Controller
from moteus_fdcan_adapter import MoteusReg
import time
import math
import matplotlib.pyplot as plt

def main():
    controller_1 = Controller(controller_ID = 1, device='/dev/ttyACM0')
    
    #to work properly, timeout should be set to nan (default_timeout_s in tview, 0x027 registre)
    
    #response_data = controller_1.get_data()
    #print(response_data[MoteusReg.MOTEUS_REG_POSITION])
    
    ##read two encoders (if you have two, properly configured)
    #response_data_enc = controller_1.get_data_enc()
    #print(response_data_enc[MoteusReg.MOTEUS_REG_POSITION])
    #print(response_data_enc[MoteusReg.MOTEUS_REG_ENC_2_POS])
    
    ##read driver temperature and motor temperature
    #response_data = controller_1.get_data()
    #print(response_data[MoteusReg.MOTEUS_REG_TEMP])
    #response_data_temp = controller_1.get_data_temp()
    #print(response_data_temp[MoteusReg.MOTEUS_REG_MOTOR_TEMP])
    
    
    
    #send raw CAN bus message (similar to one in reference.md of moteus)
    #this will try to move the motor with the maximum allowable speed/acceleration!!!
    controller_1.serial.write(b"can send 8001 01000a0720600000000000140400130d\n")
    response = controller_1.serial.readline()
    print("Reply from CAN command: ", response.decode('latin1'))
    time.sleep(10.0)
    response = controller_1.serial.readline()
    print("Reply from CAN command: ", response.decode('latin1'))
    
    #controller_1.serial.write(b"can send 8001 01000a0720600000000000140400130d\n")
    #response = controller_1.serial.readline()
    #print("Reply from CAN command: ", response.decode('latin1'))
    #time.sleep(1.0)
    #response = controller_1.serial.readline()
    #print("Reply from CAN command: ", response.decode('latin1'))
    
    #stop the motor if it moved (disable motor) it also clears all the error
    controller_1.command_stop()
    
    #move the motor with the max velocity and max acceelration
    response_pos = controller_1.set_position_lim(position=2.0, max_torque=0.2, kd_scale=1.0, vel_lim=10., acc_lim=40., get_data=True, print_data=True)
    print(response_pos[MoteusReg.MOTEUS_REG_POSITION]) #position before the motion
    time.sleep(10.0) #allow the time for motion
    response_data = controller_1.get_data()
    print(response_data[MoteusReg.MOTEUS_REG_POSITION]) #position after the movement
    
    controller_1.command_stop()
    
    
    #response_pos = controller_1.set_position(position=.5, max_torque=0.2, kd_scale=1.0, get_data=True, print_data=True)
    #print(response_pos[MoteusReg.MOTEUS_REG_POSITION])
    #print(response_pos[MoteusReg.MOTEUS_REG_MODE])
    #print(response_pos[MoteusReg.MOTEUS_REG_FAULT])
    
    #check the status of the FDCANUSB adapter
    controller_1.serial.write(b"can status\n")
    response = controller_1.serial.readline()
    print("Reply from CAN status command: ", response.decode('latin1'))


if __name__ == '__main__':
    main()
