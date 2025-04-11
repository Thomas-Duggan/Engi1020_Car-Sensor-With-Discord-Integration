# Copyright (c) 2025 Thomas Duggan and Devin Reardon
# This work is licensed under CC BY-SA 4.0



##########################################
# Please run alongside "! Car Sensor.py" #
##########################################



# Notes:
#   Downloading: Under "Tools", "Manage plug-ins", download "discord.py" (Thonny)
#   Alternate Download: python3 -m pip install -U discord.py (Linux)
#   Documentation: https://discordpy.readthedocs.io/


from discord import *
from time import sleep


intents = Intents.default()			# Sets Default Intents For Bot
intents.message_content = True		# Allows Bot To Read Messages

client = Client(intents=intents)	# Unknown, required
@client.event						# ^^^^^^^^^^^^^^^^^


async def on_message(message):		# Only responds to messages

    RAM = open("RAM.py","r")		# Opens the file "RAM.py"
    RAM_Value = RAM.read()			# Writes current message to variable
    RAM.close()						# Closes "RAM.py"
        # Note: .py extention is soley for easy access inside Thonny

    loc = []

    for i in range(len(RAM_Value)):
    
        skip = False				# Prevents below from running on first char
        if i == 0:					# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           skip = True				# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        if RAM_Value[i] == "," and skip == False:						# Finds locations of commas in document
            if (RAM_Value[i-1] == "'") and (RAM_Value[i+1] ==" "):		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                loc += [i]												# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    #print(RAM_Value)	# For testing purposes only
    #print(loc)			# ^^^^^^^^^^^^^^^^^^^^^^^^^
    
    
    
        ######### \/ DUPLICATE AS NEEDED: \/ #########
    
    user_message_1	=	RAM_Value[       1:loc[0]-1]		# Isolates string 1 using comma location
    bot_message_1	=	RAM_Value[loc[0]+3:loc[1]-1]		# Isolates string 2 using comma location
    lockdown_toggle	=	RAM_Value[loc[1]+3:loc[2]-1]		# And so on...
    unused			=	RAM_Value[loc[2]+3:      -1]
    

        ######### \/ DUPLICATE AS NEEDED: \/ #########

    if message.content.startswith(  "Help"  ):	# Help function (UPDATE REGULARLY)
        await message.channel.send( '''
# Commands:
** **
## Help
> Sends the message you're currently reading

## PN
> Sends Patch Notes

## Temp
> Sends the car's temperature
> ** **
> ***Note: Temperature may be off by up to ±3°C***

## Comft temp
> Sends a message when a comfortable temperature is acheived (20°C or higher)

## PM on
> Activates Pet Mode and sends a message when vehicle is too warm for pet (30°C or higher)

## PM off
> Deactivates Pet Mode

## Mode
> Sends Current Lockdown and Pet Mode statues

## LD on
> Activates Lockdown Mode

## LD off
> Deactivates Lockdown Mode
> ** **
> ***Note: May send several instances of "CHECK VEHICLE" after turning off lockdown mode. This is normal. Use "Mode" to test current status of Lockdown Mode.***

        '''  )
        return
    
    
    if message.content.startswith(  "PN"  ):	# Patch Notes (UPDATE REGULARLY)
        await message.channel.send( '''

### 14/3/25
> Added toggle for Lockdown Mode.
> Added "Lockdown on" command, "Lockdown off" command.

### 13/3/25
> Added "Tmp" command, "Help" command, "Pn" command.
> Updated Help command for "Tmp" and "Pn".
> Moved Discord variable initialization into main while statement

### 19/3/25
> Added "Mode" command.
> Added automated Discord messaging when levels are surpassed.
> Added surpassing levels for sound sensor.
> Added Help command for "Mode".
> Updated Help command for "Lockdown off".

### 21/3/25
> Started implementing Trip Logging system
> Started implementing Password system

### 28/3/35
> Changed "Tmp" command to "Temp"
> Changed "Lockdown on / off" command to "LD on / off"
> Added "Comft Temp" command, and added it to "Help"
> Added "PM on / off" command, and added it to "Help"

### 2/4/25
> Updated thresholds for LD's sound (200->320)
> Subtracted 4 from all instances of temperature to increase accuracy

        '''  )
        return
    

    if message.content.startswith(  "LD on"  ): # Reserved for activating lockdown mode
        
        config = open("mode.py","w")
        config.write("LD ON")
        config.close()
        
        await message.channel.send( "# LOCKDOWN MODE ACTIVATED"   )
        return
    
    
    if message.content.startswith(  "LD off"  ): # Reserved for deactivating lockdown mode
        
        config = open("mode.py","r")
        status = config.read()
        config.close()
        
        if status == "LD OF":
            await message.channel.send( "## Lockdown mode is already off"   )
            
        else:
            config = open("mode.py","w")
            config.write("LD OF")
            config.close()
            await message.channel.send( "## Lockdown mode deactivated"   )
        return
        

    if message.content.startswith(  user_message_1  ): # Reserved for "Tmp" command
        await message.channel.send( "## "+bot_message_1   )
        return
    
    
    if message.content.startswith(  "Mode"  ): # Reserved for showing temperature mode
        config = open("mode.py","r")
        current_mode_reading = config.read()
        config.close()
        petmode = open("Pet Mode.py","r")
        pet_mode_reading = petmode.read()
        petmode.close()
        
        if current_mode_reading == "LD OF":
            current_mode_sending = "## Lockdown Mode is OFF"
        if pet_mode_reading == "Monitor Off":
            pet_mode_sending = "## Pet Mode is OFF"
            
        if current_mode_reading == "LD ON":
            current_mode_sending = "# Lockdown Mode is **ON**"
        if pet_mode_reading == "Monitor On":
            pet_mode_sending = "## Pet Mode is ON"
            
        Message = "\n".join([current_mode_sending,pet_mode_sending])
            
        await message.channel.send( Message   )
        return
    
    
    if message.content.startswith(  "Comft temp"  ): # Reserved for Temperature Notification system
        
        Tempmon = open("Tmon.py","w")
        Tempmon.write("Monitor On")
        Tempmon.close()
        
        await message.channel.send( "## Message will be sent when temperature is comfortable"   )
        return
    
    if message.content.startswith(  "PM on"  ): # Reserved for Pet Mode Toggling
        
        pet = open("Pet Mode.py","w")
        pet.write("Monitor On")
        pet.close()
        
        await message.channel.send( "## Pet Mode On"   )
        return
    
    if message.content.startswith(  "PM off"  ): # Reserved for Pet Mode Toggling
        
        pet = open("Pet Mode.py","w")
        pet.write("Monitor Off")
        pet.close()
        
        await message.channel.send( "Pet Mode Off"   )
        return
                    

client.run(" BOT TOKEN GOES HERE ")
    

    
