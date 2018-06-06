import os,subprocess
cwd = os.getcwd()
included_extensions = ['jpg', 'bmp', 'png', 'gif']
subprocess.call(["mkdir","processed_imgs"])
while True:
    file_names = [fn for fn in os.listdir(cwd)
              if any(fn.endswith(ext) for ext in included_extensions)]
    for fn in file_names:
        subprocess.call(["./proc.sh",fn])
        subprocess.call(["mv",os.path.join(cwd,fn),os.path.join(cwd,"processed_imgs",fn)])

