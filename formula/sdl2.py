import winbrew
import os
import glob

class Sdl2(winbrew.Formula):
    url = 'http://libsdl.org/release/SDL2-2.0.3.zip'
    homepage = 'http://libsdl.org'
    sha1 = '6da4247162bb2477a36529f9db71f579fd3e5f6f'
    build_deps = ()
    deps = ()

    def directx(self):
        """
        Find the DirectX SDK and set the INCLUDE/LIBPATH env vars to include
        the path to the header/library files.
        """
        sdks = glob.glob("C:\\Program Files*\\Microsoft DirectX SDK*")
        try:
            sdk = sdks[0]
        except IndexError as e:
            self.error("no DirectX SDK found")
        os.environ['LIBPATH'] = ';'.join((
            os.environ.get('LIBPATH', ''),
            os.path.join(sdk, 'Lib', 'x86'),
        ))
        os.environ['INCLUDE'] = ';'.join((
            os.environ.get('INCLUDE', ''),
            os.path.join(sdk, 'Include')
        ))

    def build(self):
        self.directx()
        self.cd('VisualC')
        self.msbuild(winbrew.msbuild_args+('SDL_VS2013.sln',))

    def install(self):
        self.includes('include', 'SDL2')

    def test(self):
        pass
