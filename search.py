import os
import fnmatch

def find_all(pattern,path):
  print "Searching"
  for root,dirs,files in os.walk(path):
    for name in files:
      if fnmatch.fnmatch(name,pattern): 
        print (os.path.join(root,name))

if __name__ == '__main__':
  if os.name =='posix':
    file_path = raw_input("Enter a path to search for:  (Defaults to /home/)")
    if file_path == "":
      file_path = '/home/'
  elif os.name == 'nt':
    file_path = raw_input("Enter a path to search for:  (Defaults to C:\)")

    if file_path == "":
      file_path = 'C:'
  else:
    print "Your Operating system is not supported. Please use a NT or posix machnie"
    exit()

  file_name = raw_input("Enter the filename to search for")
  print file_name, file_path
  find_all(file_name,file_path)
