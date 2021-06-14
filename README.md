# GDB Side-Channel Tracer

A Python script to batch-trace a set of function calls of a given executable with GDB. The executable provides minimal debug info or no debug info at all. The debug information is adopted from a different binary defining the same set of functions with debug info.

A typical usecase of this instrument is to analyze a commercial application with no source or debug info available, which uses a well-known opensource third-party library.

