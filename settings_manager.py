#defining our functions:

def add_setting(settings, data):

    #[1] checking if settings is a dictionary and data is a tuple
    if not isinstance(settings, dict) or not isinstance(data, tuple):
        return 'make sure to use dictionary and a tuple as parameters'

    #[2] converting our key and value to lowercase
    key = data[0].lower()
    value = data[1].lower()
    
    #[3] checking if setting exists or not
    if key in [k.lower() for k in settings.keys()]:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        settings[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'
    
def update_setting(settings, data):

    #[1] checking if settings is a dictionary and data is a tuple
    if not isinstance(settings, dict) or not isinstance(data, tuple):
        return 'make sure to use dictionary and a tuple as parameters'

    #[2] converting our key and value to lowercase
    key = data[0].lower()
    value = data[1].lower()

    #[3] checking if setting exists or not
    if key in [k.lower() for k in settings.keys()]:
        settings[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'
    

def delete_setting(settings, data):

    #[1] checking if settings is a dictionary and data is a string
    if not isinstance(settings, dict) or not isinstance(data, str):
        return 'make sure to use dictionary and a string as parameters'

    #[2] converting our key to lowercase
    key = data.lower()

    #[3] checking if setting exists or not
    if key in [k.lower() for k in settings.keys()]:
        settings.pop(key)
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'
    

def view_settings(settings):

    #checking if settings dictionary is empty or not
    if not settings:
        return 'No settings available.'
    else:
        viewer = 'Current User Settings:\n'
        for key, value in settings.items():
            key = key.capitalize()
            viewer += f'{key}: {value}\n'
        return viewer

#testing our functions

#[1] add_setting function
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))

#[2] update_setting function
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))

#[3] delete_setting function
print(delete_setting({'theme': 'light'}, 'theme'))
print(delete_setting({'theme': 'light'}, 'volume'))

#[4] view_setting function
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
print(view_settings({}))

#[5] project request:adding test_settings
test_settings = {
    'study_mode': 'on'
}