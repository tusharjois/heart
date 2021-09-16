all: vuln 

vuln: vuln.c
	gcc -g -std=c99 -m32 -fno-stack-protector vuln.c -o vuln 

clean:
	rm -f vuln
