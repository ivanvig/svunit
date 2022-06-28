#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import subprocess
import shutil
import os

class SVUnitGenerator(Generator):
    def run(self):
        cwd = self.files_root
        args = ['buildSVUnit', '-o', 'generated']
        rc = subprocess.call(args, cwd=cwd)
        if rc:
            exit(1)

        shutil.rmtree(os.path.join(os.getcwd(), 'generated'), ignore_errors=True)
        shutil.move(os.path.join(cwd, 'generated'), os.getcwd())
        self.add_files([
            {'generated/.testrunner.sv' :{'file_type' : 'systemVerilogSource'}},
            {'generated/.__testsuite.sv' :{'file_type' : 'systemVerilogSource'}},
            ])

if __name__ == '__main__':
    g = SVUnitGenerator()
    g.run()
    g.write()
