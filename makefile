.PHONY: test

all: a.out

a.out: a.c lib.h
	gcc -O0 $< -o $@

lib.so: lib.c lib.h a.out
	gcc -g -shared $< -o $@
	objcopy --only-keep-debug lib.so debug_info
	objcopy --add-gnu-debuglink=debug_info a.out

clean:
	rm -rf a.out lib.so debug_info

test: a.out lib.so
	./gdb-tracer.py a.out

