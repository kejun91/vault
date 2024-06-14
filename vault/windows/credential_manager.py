import subprocess

def add_generic_credential(name, credential):
    result = subprocess.run(['cmdkey', f'/generic:UpWebTools/{name}', f'/user:{name}', f'/pass:upwebtoolsstart-{credential}-upwebtoolsend'])
    return result.returncode == 0

def delete_generic_credential(name):
    result = subprocess.run(['cmdkey',f'/delete:UpWebTools/{name}'])
    return result.returncode == 0