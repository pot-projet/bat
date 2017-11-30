#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright 2017 Pot project.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class Compile:
    def __init__(self, name: str, command: str, includes: [str], options: [str], extensions: [str]):
        self.__name = name
        self.__command = command

        self.__includes = []
        for inc in includes:
            if inc not in self.__includes:
                self.__includes.append(inc)

        self.__options = []
        for opt in options:
            if opt not in self.__options:
                self.__options.append(opt)

        self.__extensions = list(set(extensions))

        self.__include_cache = ""
        self.__options_cache = ""
        self.__update_include_cache()
        self.__update_options_cache()

    def command(self, input_file: str, output_file: str) -> str:
        return "{0} {1} {2} -o {3} {4}".format(
            self.__command, self.__options_cache, self.__include_cache, output_file, input_file
        )

    def __update_include_cache(self):
        self.__include_cache = ["-I{0}".format(inc) for inc in self.__includes]

    def __update_options_cache(self):
        self.__options_cache = " ".join(self.__options)

    @property
    def name(self):
        return self.__name


class Link:
    def __init__(self, command: str, library_paths: [str], libraries: [str], options: [str]):
        self.__name = "LINK"
        self.__command = command

        self.__library_paths = []
        for lib_path in library_paths:
            if lib_path in self.__library_paths:
                self.__library_paths.append(lib_path)

        self.__libraries = []
        for lib in libraries:
            if lib in self.__libraries:
                self.__libraries.append(lib)

        self.__options = options

        self.__options_cache = ""
        self.__libraries_cache = ""
        self.__library_paths_cache = ""
        self.__update_options_cache()
        self.__update_libraries_cache()
        self.__update_library_paths_cache()

    def command(self, input_files: [str], output_file: str) -> str:
        return "{0} {1} -o {2} {3} {4} {5}".format(
            self.__command, self.__options_cache, output_file,
            self.__library_paths_cache, self.__libraries_cache, " ".join(input_files)
        )

    def __update_libraries_cache(self):
        self.__libraries_cache = ["-l{0}".format(lib) for lib in self.__libraries]

    def __update_library_paths_cache(self):
        self.__library_paths_cache = ["-L{0}".format(path) for path in self.__library_paths]

    def __update_options_cache(self):
        self.__options_cache = " ".join(self.__options)
