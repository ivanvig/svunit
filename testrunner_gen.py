#!/usr/bin/python3
from fusesoc.capi2.generator import Generator
import subprocess
import shutil
import os

class SVUnitGenerator(Generator):
    def run(self):
        cwd = self.files_root
        tb_files_arg = ('-t ' + ' -t '.join(self.config['test_files'])).split(' ')
        my_env = os.environ.copy()
        my_env["PATH"] = os.path.abspath(os.path.dirname(__file__)) + '/bin:' + my_env["PATH"]
        args = [
            'buildSVUnit',
            '-o',
            'generated'
        ] + tb_files_arg
        rc = subprocess.call(args, cwd=cwd, env=my_env)
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
