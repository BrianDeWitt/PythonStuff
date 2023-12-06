'''
# =================================================================
# 88888888          .d888
#    88            d8P"
#    88            88 
#    88    8888b.  888888  .d8b.
#    88    88  "8b 88     d8" "8b
#    88    88   88 88     Y8. .8P
# 88888888 88   88 88      "Y8P"
#
 File Name: DigiCore_Credentials.py
 Program Purpose: This program allows DigiCore employees to 
    add credentials to a file, view credentials added to the 
    file, and provides a way to exit the program. The entered 
    credentials are saved to a text file that remains between 
    executions of the script.
    This program achieves this via a windowed interface. To do
    this, the PySimpleGUI package (https://www.pysimplegui.org)
    is used. 
 Program Author: Brian DeWitt s8091778
 Date Started: 23 November 2023
 Date Completed: December 2023
 Last Updated: 6 December 2023 16:19
# =================================================================
'''

import PySimpleGUI as sg
import os  # used to access the filesystem on the operating system the script runs on
import csv # since we write a list to a file, need csv to read the list

'''
 === VARIABLES ===
 Create a variable that stores the path for the Text File that will store the credentials. 
 PLEASE NOTICE THAT THIS IS NOT A SECURE OR ENCRYPTED FILE! IT IS IN PLAIN TEXT! 
'''
CREDENTIALS_FILE_PATH = "NotDigiCoreCredentials.txt"
CREDENTIALS_GLOBAL = ()
CREDENTIALS_GLOBAL_STRIPPED = ()

# Check if a file to store the credentials already exists. 
# If it does not, then we create it.  
if not os.path.exists(CREDENTIALS_FILE_PATH):
    try:
        open(CREDENTIALS_FILE_PATH, 'a').close()
    except:
        print("File not found, so creating " + CREDENTIALS_FILE_PATH + "... \n")
        credentialsFile = open("NotDigiCoreCredentials.txt")
else:
    print("File was found. Continuing...")

'''
==========================================================================
88888888888
88                                   88     00
88                                   88     
88888888   88   88 88888b.   .d888b. 888888 88     .d8b.  88888b.  .d888b
88         88   88 88  "88b d8K      88     88    d8" "8b 88  "88b 88
88         88   88 88    88 88       88     88    88   88 88    88 "Y888b.
88         Y8b  88 88    88 d8K      Y8b.   Y8b   Y8. .8P 88    88     X88
88          "Y888k 88    88  "Y888K'  "Y88b  Y8b.  .d8b.  88    88  8888P"
=
======= These perform the actions to write credentials to and read =======
=======     credentials from the hard-coded file.                  =======
'''

# Function to handle adding credentials to the file. 
def add_a_credential():
    try: 
        with open(CREDENTIALS_FILE_PATH, 'a', encoding="UTF-8") as creds_file: 
            creds_writer = csv.writer(creds_file)
            creds_file.write(new_credential_information + "\n")
            sg.Popup('Success!', 'The credential information was saved to the file.', grab_anywhere=True, auto_close_duration=7, font="Any 16")
            print("this displays after attempting to add the information to the text file. \n")
    except IOError:
        print("Oh noes! File error. Go listen to Paramore. \n")
        return
    finally:
        creds_file.close()
# end of add_a_credential() 
        
# Function to read the credentials from the file an₫ display them to the window. 
def view_all_credentials():
    print("The function view_all_credentials was successfully called! \n")
    try:
        with open(CREDENTIALS_FILE_PATH, 'r', encoding="utf-8") as view_creds:
            # reader = view_creds.readlines()
            reader = csv.reader(view_creds)
            CREDENTIALS_GLOBAL = list(reader)
            print(type(CREDENTIALS_GLOBAL))
            print(str(CREDENTIALS_GLOBAL))
            window['-SHOWCREDS-'].update(values=CREDENTIALS_GLOBAL)
    except IOError: 
        print("Oh noes. IO errors.")
        return
    except csv.Error as csvE:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, csvE))
    finally:
        view_creds.close()
# end of def view_all_credentials()

'''
# ===============================================================
# 
# 88
# 88                                             88
# 88                                             88
# 88          8888b.     88   88   .d8b.  88  88 88888 .d888b
# 88          8   *8b    88   88  d8" "8b 88  88 88    88K 
# 88          8    88    88   88  88   88 88  88 88    "Y888b.
# 88          8    88b   Y8b  88  Y8. .8P Y8b 88 Y8b.      X88
# 8888888888   "Y88888b.  "Y8888   .d8b.   "Y888  "Y88  8888P" 
#                             88
#                         8b d8P  
#                          "Y8P"
# 
# =========== These display the window and its areas. ===========
'''
# PySimpleGUI layout that displays the Menu area
menu_options_area = [
    [sg.Text('Select an option: ', font='Any 16')],
    [sg.Button('Add a Credential', font='Any 14')],
    [sg.Button('View Credentials', font='Any 14')],
    [sg.Button('Exit', font="Any 14")],
]

# PysimpleGUI layout that displays the View Credentials area
view_credentials_area = [
    [sg.Table(values=CREDENTIALS_GLOBAL, headings=['Resource','Username','Password'], key='-SHOWCREDS-', font="Courier 10", auto_size_columns=True, vertical_scroll_only=False, expand_x=True, expand_y=True, num_rows=7)],
]

# PySimpleGUI layout that displays the Add Credentials area
add_credentials_area = [
    [sg.Text('Enter the credentials you wish to add.', font="Any 14")],
    [sg.Text('URL or Resource: ', font="Any 12"), sg.Input(key='-RESOURCEIN-', do_not_clear=False, tooltip="Type the URL or the name of the resource here")],
    [sg.Text('Username: ', font="Any 12"), sg.Input(key='-USERNAMEIN-', do_not_clear=False, tooltip="Type the username or registration name here")],
    [sg.Text('Password: ', font="Any 12"), sg.Input(key='-PASSWORDIN-', do_not_clear=False, tooltip="Type the password here. Make sure no one is looking")],
    [sg.Button('Save', font="Any 14"), sg.Cancel(button_color=('white', 'VioletRed3'), font="Any 14")],  
]

# PySimpleGUI layout that displays the menu as buttons. Clicking the relevant button allows the user
#    to add credentials, view already entered credentials, or exit the script. 
layout = [
    [sg.Text("Welcome to the DigiCore Credential Storer and Viewer(TM).", font="Courier 18")],
    [sg.Frame('Menu', menu_options_area, visible=True, key='-MENUAREA-', font='Any 16'), sg.VSeperator(), sg.Frame('Credentials Viewer', view_credentials_area, visible=False, size=(800,200), key='-VIEWCREDS-', font='Any 16')],
    [sg.Frame('Add Credential', add_credentials_area, visible=False, key='-ADDCREDS-', font="Any 16", element_justification='left')],
]

# Display the window and add a title to it 
window = sg.Window('DigiCore Credential Manager', layout, margins=(40,40), location=(70,50))

# ===========================================================
# 888888888888
# 88
# 88                                          88
# 88                                          88
# 88888888    'Y8       8Y'  .d88b.  88888b.  888886 .d888b
# 88           'Y8     8Y'  d8P  Y8b 88  "88b 88     88K
# 88            'Y8   8Y'   88888888 88    88 88     "Y888b.
# 88             'Y8 8Y'    Y8b.     88    88 Y8b.       X88
# 888888888888    'Y88       "Y8888  88    88  "Y88"  8888P'
#
# ----- The event loop to capture actions in the window  -------
# This allows the code to run until the user clicks either of the 
#      Exit or window close buttons.

while True:
    event, values = window.read() 
    print(event, values)  # for debugging
    # If the window is closed or the EXIT button is clicked, close the window
    if event == sg.WIN_CLOSED or event == 'Exit' or event is None:
        print("Now closing...") 
        break
    # If the view credentials button is clicked, call the view credentials function 
    elif event == 'View Credentials':
        print("View creds button was clicked.")
        window['-ADDCREDS-'].update(visible=False)
        window['-VIEWCREDS-'].update(visible=True)
        view_all_credentials()
        window['-SHOWCREDS-'].update(visible=True)
    # If the add credential button is clicked, call the add credentials function 
    elif event == "Add a Credential":
        window['-VIEWCREDS-'].update(visible=False)
        window['-ADDCREDS-'].update(visible=True)
    elif event == 'Save':  # If the Save button is clicked, do this
        print(event, values) # check if this section of code is called / run
        print("Save button clicked. \n")
        new_credential_information = str(f"{values['-RESOURCEIN-']}" + ", " + f"{values['-USERNAMEIN-']}" + ", " + f"{values['-PASSWORDIN-']}")
        add_a_credential()
    elif event == 'Cancel':
         print("Cancel button clicked. \n")
         window['-ADDCREDS-'].update(visible=False)
    else:
        print("Nothing was selected? ¯\\_(ツ)_/¯ \n")
window.close()
print("             ...and exiting. ¯\\_(ツ)_/¯")

# This exits the entire program, frees up resources, and prevents crashes and hangs.
exit()
