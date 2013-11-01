import winbrew

class Bullet(winbrew.Formula):
    url = 'https://bullet.googlecode.com/files/bullet-2.82-r2704.zip'
    homepage = ''
    sha1 = ''
    build_deps = ('cmake',)
    deps = ()

    def install(self):
        self.cd('bullet-2.82-r2704')
        self.cmake(('-G', 'Visual Studio 10'))
        self.msbuild(winbrew.msbuild_args+('BULLET_PHYSICS.sln',))
        self.libs('libs\\Release')
        self.includes('src')

    def test(self):
        pass
