from datetime import datetime
import piexif

import os
import time

folder = './'

def get_datetime(filename):
    date_str = filename.split('-')[1]
    return datetime.strptime(date_str, '%Y%m%d')

def get_date(filename):
    date_str = filename.split('-')[1]
    return datetime.strptime(date_str, '%Y%m%d').strftime("%Y:%m:%d %H:%M:%S")


allowedFileEndings = ['mp4','jpg','3gp','jpeg']

filenames = [fn for fn in os.listdir(folder) if fn.split('.')[-1] in allowedFileEndings]

l = len(filenames)
print(l)

for i, filename in enumerate(filenames):

    if filename.endswith('mp4') or filename.endswith('3gp'):
        date = get_datetime(filename)
        modTime = time.mktime(date.timetuple())
        os.utime(folder + filename, (modTime, modTime))

    elif filename.endswith('jpg') or filename.endswith('jpeg'):
        exif_dict = {'Exif': {piexif.ExifIFD.DateTimeOriginal: get_date(filename)}}
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, folder + filename)

    print('{}: {}/{}'.format(filename, i + 1, l))
print('\nDone!')
