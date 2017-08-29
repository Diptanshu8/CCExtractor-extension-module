from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print "inside install"
        print "*******"
        print "*******"
        print "*******"
        subprocess.check_call(['./package_build_scripts/build_library_package'])
        install.run(self)

setup(
           name='ccextractor',
           version = '0.2',
           author      = "Diptanshu Jamgade",
           description = "Python Extension module for CCExtractor",
           author_email  = 'diptanshuj@gmail.com',
           url='https://github.com/Diptanshu8/CCExtractor-extension-module',
           download_url='https://github.com/Diptanshu8/CCExtractor-extension-module/archive/0.2.tar.gz',
           keywords=['ccextractor'],
           packages = ['ccextractor'],
           package_dir = {'ccextractor':''},
           package_data = {'ccextractor':['_ccextractor.so','ccextractor.py']},
        include_package_data=True,
           cmdclass={
               'install':PostInstallCommand,
               },
           )
