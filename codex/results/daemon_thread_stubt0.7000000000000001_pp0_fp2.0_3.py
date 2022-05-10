import sys, threading

def run():
    global g_Radiator, g_Balcony_Windows, g_A_C, g_Gas_Valve, g_Humidifier, g_Dehumidifier, g_Door, g_AI_Mode
    global g_AI_Mode, g_H_Flag, g_D_Flag, g_A_Flag, g_Mode_Flag
    global g_Humidifier, g_Dehumidifier, g_A_C, g_Gas_Valve, g_Balcony_Windows, g_Radiator
    global g_Input_Temperature, g_Input_Humidity, g_Input_Gas, g_Input_Balcony_Windows, g_Input_Door_Opened, g_AI_Mode, g_Mode_Flag
    global g_Past_Temperature, g_Past_Humidity, g_Past_Gas, g_Past_Balcony_Windows, g_Past_Door_Opened
    global g_Output_Temperature, g_Output_Humidity, g_Output_Gas, g_Output_Balcony_Windows, g_Output_D
