.PHONY: test

all: a.out

a.out: a.c
	gcc -g $< -o $@

clean:
	rm -rf a.out

test: a.out
	./gdb-tracer.py a.out

