#import necessary librariesc:
import json
import csv
import os

#Create a variable with the user's profile file path
import os
user_path = os.getenv('USERPROFILE')
#print(user_path)

#get the VSCode extensions directory
extensions_dir = os.path.join(user_path,'.vscode\extensions')

#get the list of installed extensions
extension_list = os.listdir(extensions_dir)

#create the directory where the csv file will be stored
os.makedirs(os.path.dirname(r'C:\Scripts\extensions.csv'), exist_ok=True)

#open a csv file
csv_file = open(os.path.join(r'C:\Scripts\extensions.csv'), 'w+', newline='')

#create a csv writer object
csv_writer = csv.writer(csv_file)

#write the header row
csv_writer.writerow(['Extension Name', 'Description'])

#iterate through the list of extensions
for extension in extension_list:
    #get the path to the extension's package.json
    json_path = os.path.join(extensions_dir, extension, 'package.json')

    #open and read the contents of the json file with the specified encoding
    with open(json_path, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)

    #get the name and description of the extension
    extension_name = data['name']
    extension_description = data['description']

    #write the extension name and description to the csv file
    csv_writer.writerow([extension_name, extension_description])

#close the csv file
csv_file.close()

# Print if CSV was created or not
if os.path.isfile(os.path.join(r'C:\Scripts\extensions.csv')):
    print('CSV file was successfully created.')
else:
    print('CSV file was not created.')