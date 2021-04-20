from datetime import datetime
import piexif

import re
import os
import time

folder = './'

def get_datetime(filename):
    date_str = filename.split('-')[1]
    return datetime.strptime(date_str, '%Y%m%d')

def get_date(filename):
    date_str = filename.split('-')[1]
    return datetime.strptime(date_str, '%Y%m%d').strftime("%Y:%m:%d %H:%M:%S")

fn_regex = re.compile(r'(IMG|VID)-(\d{8})-WA.*\.(jpe?g|mp4|3gp)')

filenames = [fn for fn in os.listdir(folder) if re.match(fn_regex, fn)]

num_files = len(filenames)
print("Number of files: {}".format(num_files))

for i, filename in enumerate(filenames):

    if filename.endswith('mp4') or filename.endswith('3gp'):
        date = get_datetime(filename)
        modTime = time.mktime(date.timetuple())
        os.utime(folder + filename, (modTime, modTime))

    elif filename.endswith('jpg') or filename.endswith('jpeg'):
        exif_dict = {'Exif': {piexif.ExifIFD.DateTimeOriginal: get_date(filename)}}
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, folder + filename)

    num_digits = len(str(num_files))
    print("{num:{width}}/{max} - {filename}"
            .format(num=i+1, width=num_digits, max=num_files, filename=folder+filename))
print('\nDone!')
