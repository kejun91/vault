import subprocess
    
def add_generic_password(name, password):
    result = subprocess.run(['security', 'add-generic-password', '-s', name, '-a', name, '-w', password])
    return result.returncode == 0

def find_generic_password(name):
    result = subprocess.run(['security', 'find-generic-password', '-w', '-s', name, '-a', name], capture_output = True, text = True)
    return result.stdout

def delete_generic_password(name):
    result = subprocess.run(['security', 'delete-generic-password', '-s', name, '-a', name], capture_output = True, text = True)
    return result.returncode == 0