import os
from datetime import datetime
import piexif

folder = 'test_images/'

def get_date(filename):
    date_str = filename.split('-')[1]
    return datetime.strptime(date_str, '%Y%m%d').strftime("%Y:%m:%d %H:%M:%S")

filenames = [fn for fn in os.listdir(folder) if fn.split('.')[-1] == 'jpg']
l = len(filenames)
for i, filename in enumerate(filenames):
    exif_dict = {'0th': { piexif.ImageIFD.DateTime: get_date(filename) }}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, folder + filename)
    print('{}/{}'.format(i + 1, l))
print('\nDone!')
