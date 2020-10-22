import os, shutil

def object_checker(toplevel, filepath):
    for i in os.listdir(filepath):
        if os.path.isdir(os.path.join(filepath,i)):
            try:
                object_checker(toplevel, os.path.join(filepath,i))
            except:
                pass
        elif i[-4:] == '.mp4' or i[-4:] == '.wmv' or i[-4:] == '.avi' or i[-4:] == '.mkv' or i[-4:] == '.mov' or i[-4:] == '.flv' or i[-5:] == '.m2ts' or i[-4:] == '.AVI' or i[-4:] == '.MKV' or i[-4:] == '.MP4':
            try:
                shutil.move(os.path.join(filepath,i), os.path.join(toplevel, i))
            except:
                pass
    
toplevel = os.getcwd()
object_checker(toplevel, toplevel)
