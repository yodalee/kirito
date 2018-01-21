.PHONY: clean

EXECUTABLE = load
CPPFLAGS = -g --std=c++11 -I./cnpy
LDFLAGS = -L./cnpy/build/ -lcnpy -lz -Xlinker -rpath=./cnpy/build
CC = g++

SOURCES = load.cpp
OBJS = $(patsubst %.cpp, %.o, $(SOURCES))


ALL: $(EXECUTABLE)

$(EXECUTABLE): $(OBJS)
	$(CC) $(LDFLAGS) $^ -o $@

%.o: %.c
	$(CC) $(CPPFLAGS) $< -o $@

clean:
	rm $(EXECUTABLE)
	rm $(OBJS)
