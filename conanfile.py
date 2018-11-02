from conans import ConanFile, CMake, tools

Сlass HelloConan(ConanFile):
    name = "hello"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/sdukshis/ci-corehard"
    description = "Demo CI/CD workshop project"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "gtest/1.8.1@bincrafters/stable"
    exports_sources = [
        "include/*",
        "src/*",
        "tests/*",
        "CMakeLists.txt",
    ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

