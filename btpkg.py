#!/usr/bin/env python3

'''
    Small leighweight wrapper around libtorrent for
    blob distribution
'''

#import asyncio
import click
import logging
import sys
import time

import build

# SystemError: Parent module '' not loaded, cannot perform relative import
#from . import (
#    build
#)
#from pathlib import Path

CLICK_CONTEXT_SETTINGS = {'help_option_names': ('-h', '--help')}
SHORT_HELP = 'Copy /fboss from fml tier to darkstorm isilons'

class CliOptions():
    ''' Object for holding CLI state information '''
    def __init__(self, debug):
        self.debug = debug

    def __repr__(self):
        ''' String Representation for debugging '''
        return 'Debug is {}'.format(self.debug)


class BtpkgCmd():
    ''' Base class for all sub commands to inherit from '''

    def __init__(self, cli_opts):
        ''' Store Global main arguments etc. '''
        self.options = cli_opts


def _handle_debug(ctx, param, debug):
    '''Turn on debugging if asked otherwise INFO default'''
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        format=(
            '[%(asctime)s] %(levelname)s: %(message)s (%(filename)s:%(lineno)d)'
        ),
        level=log_level
    )
    return debug


@click.group(short_help=SHORT_HELP, context_settings=CLICK_CONTEXT_SETTINGS)
@click.option(
    '-d',
    '--debug',
    is_flag=True,
    help='Turn on verbose logging',
    callback=_handle_debug,
)
@click.pass_context
def main(ctx, debug):
    ''' Lets build and fetch blobs over bitorrent '''
    # Class to hold all global options
    ctx.obj = CliOptions(debug)
    start_time = time.time()
    logging.debug("{} started @ {}".format(
        sys.argv[0],
        time.strftime('%Y%m%d%H%M%S', time.gmtime(start_time)))
    )
    logging.info("{} ran for {} seconds".format(
        sys.argv[0],
        time.time() - start_time,
    ))


def add_internal_modules():
    ''' Add internal modules to main parser '''
    main.add_command(build.BuildCli().build)


if __name__ == '__main__':
    # Hacks until I make a real package
#    top = Path(__file__).resolve().parents[3]
#    sys.path.append(str(top))

    # Add subcommands
    add_internal_modules()
    sys.exit(main())
