# Copyright (c) 2025 Thomas Duggan and Devin Reardon
# This work is licensed under CC BY-SA 4.0



###########################################
# Please run alongside "! Discord Bot.py" #
###########################################



# Note: run "sudo chmod a+rw /dev/ttyUSB0" in terminal to fix permission denial (Linux only probably)


from engi1020.arduino.api import *
from discord import *
from time import sleep

oled_clear() #Clears OLED screen to minimize light from Arduino

config = open("mode.py","w")
config.write("LD OF")
config.close()

D_vars = ["Temp","Temperature Response","Unsurpassed","temp_val_3"]	# Sets a list with several items, KEEP EVEN, STRINGS ONLY
    
velocity = [0,0]
password = ["1","2","3","4"]
pw_atmpt = []
    
Tempmon = open("Tmon.py","w")
Tempmon.write("Monitor Off")
Tempmon.close()

Petmode = open("Pet Mode.py","w")
Petmode.write("Monitor Off")
Tempmon.close()
    
pause = False
    
# Main program
    
while True:

    if D_vars[2] == "Unsurpassed":
        D_vars = ["Temp","Temperature Response","Unsurpassed","temp_val_3"]
    
    if D_vars[2] == "Surpassed":
        D_vars = ["Temp","Temperature Response","Surpassed","temp_val_3"]



    # Lockdown mode checks / execution (MUST BE FIRST STEP)
    
    
    config = open("mode.py","r")
    toggle = config.read()
    #print(toggle)		# For testing purposes only
    config.close()
    
    if toggle == "LD OF":
        D_vars[2] = "Unsurpassed"
        oled_clear()
        pause = False
    
    if toggle == "LD ON":
        #print(analog_read(6))		# For testing purposes only
        
        sound = analog_read(2)
        dist = int(ultra_get_centimeters(7))
        if pause == False:
            sleep(1)
            pause = True
        
        print("Sound:",sound, "\n", "Dist:",dist)		# For testing purposes only
        
        # dist > 70 or dist < 20 or
        if  sound > 320:
            D_vars[2] = "Surpassed"
            
        if D_vars[2] == "Surpassed":
            
            ############ DISCORD STUFF FOR SENDING MESSAGE ############
            intents = Intents.default()			# Sets Default Intents For Bot (discord  bot thing)
            intents.message_content = True		# Allows Bot To Read Messages
            client = Client(intents=intents)	# Sets default intents for bot
            @client.event						# Unknown, required
            async def on_ready():				# Send upon connecting
                channel = client.get_channel(1349166293781315727)	# Get Channel ID
                await channel.send(  '# CHECK VEHICLE'  )			# Send message to channel
                sleep(	5	)				# Wait 5 seconds
                await client.close()		# Disconnect from bot to continue script
            client.run(" BOT TOKEN GOES HERE ")
            #############################################################
            
            
            
            # Password System (Deemed uncessary)
            
            
#             if analog_read(0) in range(0,100):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + "9")
#                 if digital_read(6) == True:
#                     pw_atmpt.append("9")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(100,200):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + "8")
#                 if digital_read(6) == True:
#                     pw_atmpt.append("8")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(200,300):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '7')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("7")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(300,400):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '6')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("6")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(400,500):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '5')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("5")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(500,600):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '4')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("4")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(600,700):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '3')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("3")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(700,800):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '2')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("2")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(800,900):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '1')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("1")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             if analog_read(0) in range(900,2000):
#                 oled_clear()
#                 oled_print("Surpassed!")
#                 oled_print("Password:")
#                 oled_print("".join(pw_atmpt) + '0')
#                 if digital_read(6) == True:
#                     pw_atmpt.append("0")
#                     oled_print("Accepted!")
#                 sleep(1)
#                 
#             
#             if len(pw_atmpt) >= 4:
#                 if pw_atmpt[0:4] == password:
#                     D_vars[2] = "Unsurpassed"
#                     oled_clear()
#                     oled_print("Correct!")
#                     sleep(2)
#                     oled_clear()
#                 else:
#                     oled_clear()
#                     oled_print("Try Again!")
#                     sleep(2)
#                     oled_clear()
#                     pw_atmpt = []
    
                
                
    # Temperature Monitor Relay / Pet Mode
    
    
    Tempmon = open("Tmon.py","r")
    relay = Tempmon.read()
    Tempmon.close()
    # print(relay) #For testing purposes only
    if relay == "Monitor On":
        # print(pressure_get_temp()) #For testing purposes only
        if pressure_get_temp()-4 >= 20:
        
            ############ DISCORD STUFF FOR SENDING MESSAGE ############
            intents = Intents.default()			# Sets Default Intents For Bot (discord  bot thing)
            intents.message_content = True		# Allows Bot To Read Messages
            client = Client(intents=intents)	# Sets default intents for bot
            @client.event						# Unknown, required
            async def on_ready():				# Send upon connecting
                channel = client.get_channel(1349166293781315727)	# Get Channel ID
                await channel.send(  '## Comfortable Temperature Achieved'  )			# Send message to channel
                sleep(	5	)				# Wait 5 seconds
                await client.close()		# Disconnect from bot to continue script
            client.run(" BOT TOKEN GOES HERE ")
            ############################################################ 
            
            Tempmon = open("Tmon.py","w")
            Tempmon.write("Monitor Off")
            
            
    Petmode = open("Pet Mode.py","r")
    pet = Petmode.read()
    Petmode.close()
    #print(pet) #For testing purposes only
    if pet == "Monitor On":
        #print(pressure_get_temp()) #For testing purposes only
        if pressure_get_temp()-4 >= 30:
        
            ############ DISCORD STUFF FOR SENDING MESSAGE ############
            intents = Intents.default()			# Sets Default Intents For Bot (discord  bot thing)
            intents.message_content = True		# Allows Bot To Read Messages
            client = Client(intents=intents)	# Sets default intents for bot
            @client.event						# Unknown, required
            async def on_ready():				# Send upon connecting
                channel = client.get_channel(1349166293781315727)	# Get Channel ID
                await channel.send(  '# Temperature too high! Check on Pet!'  )			# Send message to channel
                sleep(	5	)				# Wait 5 seconds
                await client.close()		# Disconnect from bot to continue script
            client.run(" BOT TOKEN GOES HERE ")
            ############################################################ 
        
        
    
    # Temperature Monitor
    
    
    D_vars[1] = ["Temperature is",["NaN","°C"]]		# [1] is the string that the bot will print 
    
    D_vars[1][1][0]	= str(pressure_get_temp()-4)
    D_vars[1][1]	= "".join(D_vars[1][1])
    D_vars[1]		= " ".join(D_vars[1])
     
     
     
    # Sending D_var's to Discord bot (MUST BE LAST STEP)

    RAM = open("RAM.py","w")		# Opens the file "RAM.py" in write mode
    RAM.write(str(D_vars)[1:-1])	# Writes the list of items to the "RAM.py" file without brackets
    RAM.close()						# Closes the file "RAM.py"
        # Note: .py extention is soley for easy access inside Thonny
        
    #RAM = open("RAM.py","r")			# For Testing only
    #print("RAM Values: ",RAM.read())	# ^^^^^^^^^^^^^^^^
    #RAM.close()						# ^^^^^^^^^^^^^^^^
        
        