import os
import random
import string
import time

try: # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook # Try to import discord_webhook
except ImportError: # If it chould not be installed
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() # Exit the program
try: # Setup try statement to catch the error
    import requests # Try to import requests
except ImportError: # If it has not been installed
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # Exit the program


class NitroGen: # Initialise the class
    def __init__(self): # The initaliseaiton function
        self.fileName = "Nitro Codes.txt" # Set the file name the codes are stored in

    def main(self): # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
        if os.name == "nt": # If the system is windows
            os.system("title Nitro Generator and Checker - Made by lil adhd") # Change the title
        else: # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - this shit fast lol\a', end='', flush=True) # Update title of command prompt

        print("""    ,ad8888888888888888ba,
                     ad88888888888888888888888a,
                   a88888\"8888888888888888888888,
                ,8888"\ \ \"P88888888888888888888b,
                d88 \ \       `""P88888888888888888,
              ,8888b               ""88888888888888,
              d8P'''  ,aa,              ""888888888b
              888bbdd888888ba,  ,I         "88888888,
              8888888888888888ba8"         ,88888888b
             ,888888888888888888b,        ,8888888888
             (88888888888888888888,      ,88888888888,
             d888888888888888888888,    ,8   "8888888b
             88888888888888888888888  .;8'"""  (888888
             8888888888888I"8888888P ,8" ,aaa,  888888
             888888888888I:8888888" ,8"  'b8d'  (88888
             (8888888888I'888888P' ,8) \         88888
              88888888I"  8888P'  ,8")  \        88888
              8888888I'   888"   ,8" (   )       88888
              (8888I"     "88,  ,8"             ,8888P
               888I'       "P8 ,8"   ____      ,88888)
              (88I'          ",8"  M""""""M   ,888888'
             ,8I"            ,8(    "aaaa"   ,8888888
         ,8I'             ,888a           ,8888888)
       ,8I'            ,888888,       ,888888888
    ,8I'             ,8888888'`-===-'888888888'
 ,8I'            ,8888888"        88888888"
 8I'            ,8"    88         "888888P
8I            ,8'     88          `P888"
8I           ,8I      88            "8ba,.
(8,         ,8P'      88              88""8bma,.
 8I        ,8P'       88,              "8b   ""P8ma,
 (8,      ,8d"        `88,               "8b     `"8a
  8I     ,8dP         ,8X8,                "8b.    :8b
  (8    ,8dP'  ,I    ,8XXX8,                `88,    8)
   8,   8dP'  ,I    ,8XxxxX8,     I,         8X8,  ,8
   8I   8P'  ,I    ,8XxxxxxX8,     I,        `8X88,I8
   I8,  "   ,I    ,8XxxxxxxxX8b,    I,        8XXX88I,
   `8I      I'  ,8XxxxxxxxxxxxXX8    I        8XXxxXX8,
    8I     (8  ,8XxxxxxxxxxxxxxxX8   I        8XxxxxxXX8,
   ,8I     I[ ,8XxxxxxxxxxxxxxxxxX8  8        8XxxxxxxxX8,
   d8I,    I[ 8XxxxxxxxxxxxxxxxxxX8b 8       (8XxxxxxxxxX8,
   888I    `8,8XxxxxxxxxxxxxxxxxxxX8 8,     ,8XxxxxxxxxxxX8
   8888,    "88XxxxxxxxxxxxxxxxxxxX8)8I    .8XxxxxxxxxxxxX8
  ,8888I     88XxxxxxxxxxxxxxxxxxxX8 `8,  ,8XxxxxxxxxxxxX8"
  d88888     `8XXxxxxxxxxxxxxxxxxX8'  `8,,8XxxxxxxxxxxxX8"
  888888I     `8XXxxxxxxxxxxxxxxX8'    "88XxxxxxxxxxxxX8"
  88888888bbaaaa88XXxxxxxxxxxxXX8)      )8XXxxxxxxxxXX8"
  8888888I, ``""""""8888888888888888aaaaa8888XxxxxXX8"
  (8888888I,                      .  ```"""""88888P"
   88888888I,                   ,8I   8,       I8"
    """88888I,                ,8I'    "I8,    ;8"
           `8I,             ,8I'       `I8,   8)
            `8I,           ,8I'          I8  :8'
             `8I,         ,8I'           I8  :8
              `8I       ,8I'             `8  (8
               8I     ,8I'                8  (8;
               8I    ,8"                  I   88,
              .8I   ,8'                       8"8,
              (PI   '8                       ,8,`8,
             .88'            ,@           .a8X8,`8,
             (88             @@         ,a8XX888,`8,
            (888             @'       ,d8XX8"  "b `8,
           .8888,                     a8XXX8"    "a `8,
          .888X88                   ,d8XX8I"      9, `8,
         .88:8XX8,                 a8XxX8I'       `8  `8,
        .88' 8XxX8a             ,ad8XxX8I'        ,8   `8,
        d8'  8XxxxX8ba,      ,ad8XxxX8I"          8  ,  `8,
       (8I   8XxxxxxX888888888XxxxX8I"            8  II  `8
       8I'   "8XxxxxxxxxxxxxxxxxxX8I'            (8  8)   8;
      (8I     8XxxxxxxxxxxxxxxxxX8"              (8  8)   8I
      8P'     (8XxxxxxxxxxxxxxX8I'                8, (8   :8
     (8'       8XxxxxxxxxxxxxxX8'                 `8, 8    8
     8I        `8XxxxxxxxxxxxX8'                   `8,8   ;8
     8'         `8XxxxxxxxxxX8'                     `8I  ,8'
     8           `8XxxxxxxxX8'                       8' ,8'
     8            `8XxxxxxX8'                        8 ,8'
     8             `8XxxxX8'                        d' 8'
     8              `8XxxX8                         8 8'
     8                "8X8'                         "8"
     8,                `88                           8
     8I                ,8'                          d)
     `8,               d8                          ,8
      (b               8'                         ,8'
       8,             dP                         ,8'
       (b             8'                        ,8'
        8,           d8                        ,8'
        (b           8'                       ,8'
         8,         a8                       ,8'
         (b         8'                      ,8'
          8,       ,8                      ,8'
          (b       8'                     ,8'
           8,     ,8                     ,8'
           (b     8'                    ,8'
            8,   d8                    ,8'
            (b  ,8'                   ,8'
             8,,I8                   ,8'
             I8I8'                  ,8'
             `I8I                  ,8'
              I8'                 ,8'
              "8                 ,8'
              (8                ,8'
              8I               ,8'
              (b,   8,        ,8)
              `8I   "88      ,8i8,
               (b,          ,8"8")
               `8I  ,8      8) 8 8
                8I  8I      "  8 8
                (b  8I         8 8
                `8  (8,        b 8,
                 8   8)        "b"8,
                 8   8(         "b"8
                 8   "I          "b8,
                 8                `8)
                 8                 I8
                 8                 (8
                 8,                 8,
                 Ib                 8)
                 (8                 I8
                  8                 I8
                  8                 I8
                  8,                I8
                  Ib                8I
                  (8               (8'
                   8               I8
                   8,              8I
                   Ib             (8'
                   (8             I8
                   `8             8I
                    8            (8'
                    8,           I8
                    Ib           8I
                    (8           8'
                     8,         (8
                     Ib         I8
                     (8         8I
                     (8         8I
                      8,        8'
                      (b       (8
                       8,      I8
                       I8      I8
                       (8      I8
                        8      I8,
                        8      8 8,
                        8,     8 8'
                       ,I8     "8"
                      ,8"8,     "b
                     ,8' `8      8
                    ,8'   8      8,
                   ,8'    (a     "b
                  ,8'     `8      (b
                  I8/      8       8,
                  I8-/     8       `8,
                  (8/-/    8        `8,
                   8I/-/  ,8         `8
                   `8I/--,I8        \-8)
                    `8I,,d8I       \-\8)
                      "bdI"8,     \-\I8
                           `8,   \-\I8'
                            `8,,--\I8'
                             `Ib,,I8'
                              `I8I'



                                                        """) # Print the title card
        time.sleep(2) # Wait a few seconds
        self.slowType("ayo this checker bussin?", .02) # Print who developed the code
        time.sleep(1) # Wait a little more
        self.slowType("\nInput How Many Codes to Generate and Check: ", .02, newLine = False) # Print the first question

        num = int(input('')) # Ask the user for the amount of codes

        # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
        self.slowType("\nDo you wish to use a discord webhook? \nIf so type it here or press enter to ignore: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None # If the url is empty make it be None insted

        # print() # Print a newline for looks

        valid = [] # Keep track of valid codes
        invalid = 0 # Keep track of how many invalid codes was detected

        for i in range(num): # Loop over the amount of codes to check
            code = "".join(random.choices( # Generate the id for the gift
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            url = f"https://discord.gift/{code}" # Generate the url

            result = self.quickChecker(url, webhook) # Check the codes

            if result: # If the code was valid
                valid.append(url) # Add that code to the list of found codes
            else: # If the code was not valid
                invalid += 1 # Increase the invalid counter by one

            if os.name == "nt": # If the system is windows
                os.system(f"title Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by lil adhd") # Change the title
            else: # If it is a unix system
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by lil adhd \a', end='', flush=True) # Change the title

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") # Give a report of the results of the check

        input("\nThe end! Press Enter 5 times to close the program.") # Tell the user the program finished
        [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


    def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
        for i in text: # Loop over the message
            print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
            time.sleep(speed) # Sleep a little before the next one
        if newLine: # Check if the newLine argument is set to True
            print() # Print a final newline to make it act more like a normal print statement

    def generator(self, amount): # Function used to generate and store nitro codes in a seperate file
        with open(self.fileName, "w", encoding="utf-8") as file: # Load up the file in write mode
            print("Wait, Generating for you") # Let the user know the code is generating the codes

            start = time.time() # Note the initaliseation time

            for i in range(amount): # Loop the amount of codes to generate
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Generate the code id

                file.write(f"https://discord.gift/{code}\n") # Write the code

            # Tell the user its done generating and how long tome it took
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Function used to check nitro codes from a file
        valid = [] # A list of the valid codes
        invalid = 0 # The amount of invalid codes detected
        with open(self.fileName, "r", encoding="utf-8") as file: # Open the file containing the nitro codes
            for line in file.readlines(): # Loop over each line in the file
                nitro = line.strip("\n") # Remove the newline at the end of the nitro code

                # Create the requests url for later use
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # Get the responce from the url

                if response.status_code == 200: # If the responce went through
                    print(f" Valid | {nitro} ") # Notify the user the code was valid
                    valid.append(nitro) # Append the nitro code the the list of valid codes

                    if notify is not None: # If a webhook has been added
                        DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else: # If there has not been a discord webhook setup just stop the code
                        break # Stop the loop since a valid code was found

                else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                    print(f" Invalid | {nitro} ") # Tell the user it tested a code and it was invalid
                    invalid += 1 # Increase the invalid counter by one

        return {"valid" : valid, "invalid" : invalid} # Return a report of the results

    def quickChecker(self, nitro, notify = None): # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Get the response from discord

        if response.status_code == 200: # If the responce went through
            print(f" Valid | {nitro} ", end="") # Notify the user the code was valid
            with open("Nitro Codes.txt", "w") as file: # Open file to write
                file.write(nitro) # Write the nitro code to the file it will automatically add a newline

            if notify is not None: # If a webhook has been added
                DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                    url = notify,
                    content = f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True # Tell the main function the code was found

        else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
            print(f" Invalid | {nitro} ", end="") # Tell the user it tested a code and it was invalid
            return False # Tell the main function there was not a code found

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() # Run the main code
