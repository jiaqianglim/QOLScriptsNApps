import os, shutil

def object_checker(toplevel, filepath):
    vidlist4 = ['.mp4', '.wmv', '.avi','.mkv', '.mov', '.flv']
    for i in os.listdir(filepath):
        if os.path.isdir(os.path.join(filepath,i)):
            try:
                object_checker(toplevel, os.path.join(filepath,i))
            except:
                pass
        elif i[-4:] in vidlist4:
            try:
                shutil.move(os.path.join(filepath,i), os.path.join(toplevel, i))
            except:
                pass
    
toplevel = os.getcwd()
object_checker(toplevel, toplevel)
