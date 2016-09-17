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
    @click.option(
        '-y',
        '--yes',
        help='Auto confirm ...',
        is_flag=True,
    )
    @click.pass_obj
    def build(cli_opts, yes):
        ''' Build a btpkg package and upload to seeders '''
        BuildBtpkg(cli_opts).run(yes)


class BuildBtpkg(btpkg.BtpkgCmd):
    ''' All build related methods '''

    def __init__(self, cli_opts):
        super().__init__(cli_opts)

    def run(self, yes):
        click.echo("Building the future of distrib systems - Debug = {}".format(
            self.options.debug
        ))
        click.echo("Yes = {}".format(yes))
