#!/usr/bin/env python3

'''
    Class to take care of building btpkgs
'''

#import asyncio
import click
import logging

# TODO(cooper): Make relative imports work
#from . import btpkg
import btpkg


class BuildCli():

    @click.command()
    @click.pass_obj
    def build(cli_opts):
        ''' Build a btpkg package and upload to seeders '''
        BuildBtpkg(cli_opts).run()


class BuildBtpkg(btpkg.BtpkgCmd):
    ''' All build related methods '''

    def __init__(self, cli_opts):
        super().__init__(cli_opts)

    def run(self):
        click.echo("Building the future of distrib systems - Debug = {}".format(
            self.options.debug
        ))
