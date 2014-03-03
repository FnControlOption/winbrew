import winbrew
import os
import glob

class Sdl(winbrew.Formula):
    url = 'https://www.libsdl.org/release/SDL-1.2.15.zip'
    homepage = 'http://libsdl.org'
    sha1 = ''
    deps = ()

    def directx(self):
        """
        Find the DirectX SDK and set the INCLUDE/LIBPATH env vars to include
        the path to the header/library files.
        """
        sdks = glob.glob("C:\\Program Files*\\Microsoft DirectX SDK*")
        try:
            sdk = sdks[0]
        except IndexError, e:
            self.error("no DirectX SDK found")
        os.environ['LIBPATH'] = ';'.join((
            os.environ.get('LIBPATH', ''),
            os.path.join(sdk, 'Lib', 'x86'),
        ))
        os.environ['INCLUDE'] = ';'.join((
            os.environ.get('INCLUDE', ''),
            os.path.join(sdk, 'Include')
        ))

    def install(self):
        self.directx()
        self.cd('VisualC')
        self.msbuild(winbrew.msbuild_args+('/p:VCBuildAdditionalOptions=/useenv', 'SDL.sln'))
        self.libs('SDL\\Release')
        self.cd('..')
        self.includes('include', 'SDL')

