import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data,f)
        
def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
def delete_data(filepath, key):
    data = load_data(filepath)
    if key in data:
        del data[key]
        save_data(filepath, data)
        
        print(f"Data with key '{key}' deleted from clipboard.")
    else:
        print("key does not exist in clipboard.")
        

def clear_data(filepath):
    save_data(filepath, {})
    print("Clipboard cleared.")
    
def list_data(data):
    if data:
        for key,value in data.items():
            print(f"Key: {key}, Value: {value}")
    else:
        print("Clipboard is empty.")
        
def export_data(filepath,data):
    with open(filepath, "w") as f:
        json.dump(data, f)
    print("Clipboard data exported to file.")
def import_data(filepath):
    data = load_data(filepath)
    save_data(SAVED_DATA, data)
    print("Clipboard data imported from file.")
    


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data saved!")
        
    elif command == "load":
        key = input("Enter key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist.")
            
    elif command == "list":
        list_data(data)
        
    elif command == "delete":
        key = input("Enter the data  to delete: ")
        delete_data(SAVED_DATA, key)
    
    elif command == "clear":
        clear_data(SAVED_DATA)
    
    elif command == "export":
        export_data("clipboard_export.json",data)
        
    elif command == "import":
        import_data("clipboard_export.json")
    
    else:
        print("Invalid command. Please use 'save' , 'load', 'list', 'delete', 'clear', 'export' or 'import'.")
        
else:
    print ("Please provide exactly one command.")
    
