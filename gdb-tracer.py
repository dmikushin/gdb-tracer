#!/usr/bin/python

ingdb = False

try:
    class TraceBreakpoint(gdb.Breakpoint):
        def stop (self):
            gdb.write('foo\n')
            # Continue automatically.
            return False
            # Actually stop.
            return True

    ingdb = True
    TraceBreakpoint('foo')
    gdb.execute('run')
    gdb.execute('quit')

except:
    pass

if (__name__ == '__main__') and not ingdb:
    import os, sys
    import subprocess
    thisScript = os.path.realpath(__file__)
    if len(sys.argv) != 2:
        print("Usage: {} <target_executable>".format(thisScript))
        exit(-1)
    targetExecutable = sys.argv[1]
    print(thisScript)
    print(targetExecutable)
    subprocess.call(['gdb', '--command', thisScript, targetExecutable])

