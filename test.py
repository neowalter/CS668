# import os, string
# import shutil

## psutil
## fs.info
#  from fs.osfs import OSFS

# total, used, free = shutil.disk_usage("/")
#
# print("Total: %d GiB" % (total // (2**30)))
# print("Used: %d GiB" % (used // (2**30)))
# print("Free: %d GiB" % (free // (2**30)))

# get excution time
# import timeit
# print(timeit.timeit('def()', globals=globals()))



# get drives size
import wmi
c = wmi.WMI ()
obj = c.Win32_OperatingSystem()[0]
print(obj.MUILanguages)
for d in c.Win32_LogicalDisk():
    print(d.Caption, d.FreeSpace, d.Size, d.DriveType)
#
#
# w = wmi.WMI()
# disk = w.Win32_DiskDrive()[0]
#
# print("硬盘制造商Manufacturer",disk.Manufacturer)
# print("硬盘型号", disk.Model)
# print("硬盘sn", disk.SerialNumber)
# print("硬盘大小", int(disk.Size) / (1024 * 1024 * 1024))
# print(disk.Description)
# print(disk.DeviceID)
# print(disk.Name)
#
# for disk in c.Win32_LogicalDisk (DriveType=3):
#   print(disk.Caption, "%0.2f%% free" % (100.0 * int(disk.FreeSpace) / int(disk.Size)))

# method
# import os
# import string
# drive = string.ascii_uppercase
# valid_drives = []
# for each_drive in drive:
#     if os.path.exists(each_drive+":\\"):
#        print(each_drive)
#        valid_drives.append(each_drive+":\\")
# print(valid_drives)


# os.path.getsize(path）


# method
# import os
# drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
# print((drives))

# method
# import os, string
# available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
# print(available_drives)

# method
# import psutil
# drps = psutil.disk_partitions()
# drives = [dp.device for dp in drps if dp.fstype == 'NTFS']
# print(drives)
# print(drps)

# method
# from ctypes import windll, create_unicode_buffer, c_wchar_p, sizeof
# from string import ascii_uppercase
# def get_win_drive_names():
#
#     volumeNameBuffer = create_unicode_buffer(1024)
#     fileSystemNameBuffer = create_unicode_buffer(1024)
#     serial_number = None
#     max_component_length = None
#     file_system_flags = None
#     drive_names = []
#     #  Get the drive letters, then use the letters to get the drive names
#     bitmask = (bin(windll.kernel32.GetLogicalDrives())[2:])[::-1]  # strip off leading 0b and reverse
#     drive_letters = [ascii_uppercase[i] + ':/' for i, v in enumerate(bitmask) if v == '1']
#
#     for d in drive_letters:
#         rc = windll.kernel32.GetVolumeInformationW(c_wchar_p(d), volumeNameBuffer, sizeof(volumeNameBuffer),
#                                                    serial_number, max_component_length, file_system_flags,
#                                                    fileSystemNameBuffer, sizeof(fileSystemNameBuffer))
#         if rc:
#             drive_names.append(f'{volumeNameBuffer.value}({d[:2]})')  # disk_name(C:)
#     return drive_names
#
# get_win_drive_names()

#method
# import os
# print (os.popen("fsutil fsinfo drives").readlines())

#method
# import string
# from ctypes import windll
#
# def get_drives():
#     drives = []
#     bitmask = windll.kernel32.GetLogicalDrives()
#     for letter in string.ascii_uppercase:
#         if bitmask & 1:
#             drives.append(letter)
#         bitmask >>= 1
#
#     return drives
#
# if __name__ == '__main__':
#     print (get_drives())

# method to get the number of files and directories
# drive = string.ascii_uppercase
# valid_drives = []
# for each_drive in drive:
#     if os.path.exists(each_drive + ":\\"):
#         path = each_drive + ":\\"
#         print(path)
#
#         dirnum = 0
#         filenum = 0
#         # path = 'C:/Users/Dell/Desktop/test'
#
#         for lists in os.listdir(path):
#             sub_path = os.path.join(path, lists)
#             # print(sub_path)
#             if os.path.isfile(sub_path):
#                 filenum = filenum+1
#             elif os.path.isdir(sub_path):
#                 dirnum = dirnum+1
#
#         print('dirnum: ',dirnum)
#         print('filenum: ',filenum)