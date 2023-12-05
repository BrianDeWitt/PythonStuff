# =================================================================
# 88888888          .d888
#    88            d8P"
#    88            88 
#    88    8888b.  888888  .d8b.
#    88    88  "8b 88     d8" "8b
#    88    88   88 88     Y8. .8P
# 88888888 88   88 88      "Y8P"
#
'''
 File Name: DigiCore_Credentials.py
 Program Purpose: This program is for DigiCore to let their
    employees store credentials, allows users to enter new
    credentials, allows users to view saved credentials, and allow
    users to exit the program.
    The entered credentials must be saved between executions of
    the script.
 Program Author: Brian DeWitt s8091778
 Date Started: 23 November 2023
 Date Completed: 2023
 ----- NOTE: Uses the PySimpleGUI at https://www.pysimplegui.org 
 ----- However, this has been packaged as acWindows executable. MacOS upon request.
## TODO ITEMS: 
##   * output the contents of the credentials file in a Table. Might need a multiline instead.
##   * Return to the menu after a credential is added  
# =================================================================
'''

import PySimpleGUI as sg
import os
import csv # since we write a list to a file, need csv to read the list

# Create a variable that stores the path for the Text File that will store the credentials. 
# PLEASE NOTICE THAT THIS IS NOT A SECURE OR ENCRYPTED FILE! IT IS IN PLAIN TEXT! 

CREDENTIALS_FILE_PATH = "NotDigiCoreCredentials.txt"
CREDENTIALS_GLOBAL = ()

# If the file does not already exist, then create it
if not os.path.exists(CREDENTIALS_FILE_PATH):
    try:
        open(CREDENTIALS_FILE_PATH, 'a').close()
    except:
        print("File not found, so creating " + CREDENTIALS_FILE_PATH + "... \n")
        credentialsFile = open("NotDigiCoreCredentials.txt")
    '''
    finally:
        print("some other file problem.")
        pass
    '''
else:
    print("Some sort of file access error. Now exiting...")

# Function to handle adding credentials to the file. 
# The function name is add_a_credential()
def add_a_credential():
    try: 
        with open(CREDENTIALS_FILE_PATH, 'a') as creds_file: 
            creds_file.write(f"{new_credential_information}\n")
            sg.Popup('Success!', 'The credential information was saved to the file.', grab_anywhere=True, auto_close_duration='10', font="Any 16")
            print("this displays after attempting to add the information to the text file. \n")
    except IOError:
        print("Oh noes! File error. Try listening to Paramore. \n")
        return
# end of add_a_credential() 
        
# Function to display the credentials from the file. 
# At first (on 30 Nov 2023) I only had it list the contents without any formatting. 
def view_all_credentials():
    print("The function view_all_credentials was successfully called! \n")
    try:
        with open(CREDENTIALS_FILE_PATH, 'r') as view_creds:
            # reader = view_creds.readlines()
            print("Code to display the contents of the file. ")
            reader = csv.reader(view_creds)
            CREDENTIALS_GLOBAL = list(reader)
            print(type(CREDENTIALS_GLOBAL))
            # CREDENTIALS_GLOBAL_STRIPPED[:] = map(str.strip, CREDENTIALS_GLOBAL)
            # CREDENTIALS_GLOBAL_STRIPPED = (s.strip("(,',)") for s in CREDENTIALS_GLOBAL)
            window['-SHOWCREDS-'].update(values=CREDENTIALS_GLOBAL)
            # for credential in credentials['-RESOURCEIN-', '-USERNAMEIN-', '-PASSWORDIN-']:
            #    CREDENTIALS.append()
            #    return CREDENTIALS
    except IOError: 
        print("Oh noes. IO errors.")
        return
    '''
    finally:
        print("serious problems, Coach Z. ")
        return
    ''' 
# end of def view_all_credentials()

    
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
# --------- These display the areas of the window -----------

menu_options_area = [
    [sg.Text('Select an option: ', font='Courier 14')],
    [sg.Button('Add a Credential', font='Any 14')],
    [sg.Button('View Credentials', font='Any 14')],
    [sg.Button('Exit', font="Any 14")],
]

view_credentials_area = [
    [sg.Text('The saved credentials: ', font='Courier 16')],
    [sg.Table(values=CREDENTIALS_GLOBAL, headings=['Resources','Username','Password'], key='-SHOWCREDS-', font="Any 14", auto_size_columns=True)], 
#    [sg.Multiline(expand_y=True, expand_x=True, key='-CREDENTIALSDISPLAY-', disabled=True)],
]

add_credentials_area = [
    [sg.Text('Enter the credentials you wish to add.', font="Any 14")],
    [sg.Text('URL or Resource: ', font="Any 12"), sg.Input(key='-RESOURCEIN-', do_not_clear=False, tooltip="Type the URL or the name of the resource here")],
    [sg.Text('Username: ', font="Any 12"), sg.Input(key='-USERNAMEIN-', do_not_clear=False, tooltip="Type the username or registration name here")],
    [sg.Text('Password: ', font="Any 12"), sg.Input(key='-PASSWORDIN-', do_not_clear=False, tooltip="Type the password here. Make sure no one is looking")],
    [sg.Button('Save', font="Any 14"), sg.Button('Cancel', font="Any 14")], 
]

# Create the menu to let the operator choose to add credentials, view already entered credentials, 
#    or exit the script. 
layout = [
    [sg.Text("Welcome to the DigiCore Credential Storer and Viewer(TM).", font="Courier 18")],
    [sg.Frame('Menu', menu_options_area, visible=True, key='-MENUAREA-', font='Any 16'),sg.VSeperator(), sg.Frame('Credentials Viewer', view_credentials_area, visible=False, key='-VIEWCREDS-', font='Any 16')],
    [sg.Frame('Add Credential', add_credentials_area, visible=False, key='-ADDCREDS-', font="Any 16", element_justification='left')],
]

# Display the window and add a title to it 
window = sg.Window('DigiCore Credential Viewer Menu', layout, margins=(50,40), element_justification='l')

#
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
# This allows the code to run until the user clicks the Exit button or the window close button.

while True:
    event, values = window.read() 
    # TODO put code to check for file here? 
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
        print(event, values) # check if this is called / run
        print("Save button clicked. \n")
        new_credential_information = (values['-RESOURCEIN-'], values['-USERNAMEIN-'], values['-PASSWORDIN-']) 
        # add_a_credential(new_credential_information)
        add_a_credential()
    elif event == 'Cancel':
         print("Cancelled adding cred. \n")
         window['-ADDCREDS-'].update(visible=False)
    else:
        print("Nothing was selected? ¯\\_(ツ)_/¯ \n")
window.close()
print("...and exiting...")

# This exits the entire program, frees up resources and prevents crashes and hangs
exit()
