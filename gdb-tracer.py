#!/usr/bin/python

ingdb = False

try:
    import gdb
    ingdb = True

    def stopHandler(stopEvent):
        for b in stopEvent.breakpoints:
            gdb.write('breakpoint\n')
            gdb.execute('continue')

    gdb.events.stop.connect (stopHandler)
    gdb.rbreak('foo')
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

