
12days.mp4: workdir/0000.png
	ffmpeg -framerate 30 -start_number 55 -i 'workdir/%04d.png' -i try2.wav -c:v libx264 -c:a aac -r 10 -pix_fmt yuv420p $@

frame1.png: mkframes.py
	./mkframes.py

workdir: frame1.png
	mkdir -p workdir
	./video.py | bash
