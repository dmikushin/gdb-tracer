#!/usr/bin/python

ingdb = False

try:
    import gdb
    ingdb = True

    READELF_BINARY = 'readelf'

    class AddSymbolFileAuto (gdb.Command):
        def __init__(self):
            super(AddSymbolFileAuto, self).__init__("add-symbol-file-auto", gdb.COMMAND_FILES)

        def invoke(self, solibpath, from_tty):
            import os
            self.dont_repeat()
            if os.path.exists(solibpath) == False:
                gdb.write("No such file or directory: {}".format(solibpath))
                return
            offset = self.get_text_offset(solibpath)
            if offset == "":
                gdb.write('Failed to add symbols from file: {}'.format(solibpath))
                return
            gdb_cmd = "add-symbol-file %s %s" % (solibpath, offset)
            gdb.execute(gdb_cmd, from_tty)

        def get_text_offset(self, solibpath):
            import subprocess
            elfres = subprocess.check_output([READELF_BINARY, "-WS", solibpath])
            for line in elfres.splitlines():
                if b"] .text " in line:
                    gdb.write('test\n')
                    return "0x" + str(line.split()[4])
            return "" 

        def complete(self, text, word):
            return gdb.COMPLETE_FILENAME

    AddSymbolFileAuto()

    def stopHandler(stopEvent):
        for b in stopEvent.breakpoints:
            gdb.write('breakpoint\n')
            gdb.execute('continue')

    gdb.events.stop.connect (stopHandler)
    #gdb.execute('add-symbol-file-auto lib.so')
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

