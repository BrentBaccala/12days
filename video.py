#!/usr/bin/python3

import datetime
from dateutil import parser

first_ts = None
last_ts = None
last_frames = 0
last_image = 'blank.png'

offset = 0

translator={'<Enter>' : 'blank.png', 'a' : 'frame10.png', 'b' : 'frame11.png', 'c' : 'frame12', 'm': 'merry.png'}

def output_frames(frames):
            global first_ts, last_ts, last_frames, last_image
            if last_image == 'frame12':
                for i in range(last_frames, frames):
                    off = i - last_frames
                    if off < 15 or off%6 < 3:
                        print(f"cp image12a.png workdir/{i:04}.png")
                    else:
                        print(f"cp image12b.png workdir/{i:04}.png")
            else:
                for i in range(last_frames, frames):
                    print(f"cp {last_image} workdir/{i:04}.png")
            last_frames = frames

with open('data') as f:
    for line in f.read().split('\n'):
        fields = line.split()
        if fields:
            (ts1,ts2,ts3,us) = fields[1].split(':')
            ts=':'.join([ts1,ts2,ts3])
            pts = parser.parse(ts)
            pts = pts.replace(microsecond=int(us))
            if not first_ts:
                first_ts = pts
                last_ts = pts
            diff = pts-first_ts
            us = diff.total_seconds() + (diff.microseconds /1000000)
            diff2 = pts-last_ts
            us2 = diff2.total_seconds() + (diff2.microseconds /1000000)
            frames = int(us2*30) - offset
            output_frames(frames)
            if len(fields) > 2:
                #print(frames, fields[2])
                last_image = translator.get(fields[2], f'frame{fields[2]}.png')
            else:
                #print(frames, 'space')
                last_image = 'blank.png'

# Last batch of frames:
#
# echo $(soxi -D try2.wav) \* 30 | bc
# 30 fps; 7638 video frames

output_frames(7638)
