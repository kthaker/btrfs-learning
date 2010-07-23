btree: main.c btree.c btree.h
	gcc main.c btree.c btree.h -o btree
clean:
	rm btree
