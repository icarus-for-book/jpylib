#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# LICENSE 
# 
# you *MUST* buy coffee for jinsub < jinny831@gmail.ccom > 
#


import os
import sys
import subprocess
import shlex

__all__ = ['shrun','env','argv','basename','abspath','dirname',
           'join','fexists','chdir','curdir', 'export','getThisModulePath',
           'getThisModuleDir','safe_makeDirs','cp','rm']

debug_mode = True

def log(msg):
    if debug_mode:
        print msg


def shrun(cmd):
    cmds = shlex.split(cmd)
    print '[cmd]', cmds
    pipe = subprocess.Popen(cmds, stdout = subprocess.PIPE)
    pipe.wait()
    ret = pipe.stdout.read()
    return ret.strip()

env = os.environ
argv = sys.argv
basename = os.path.basename
abspath = os.path.abspath
dirname = os.path.dirname
join = os.path.join
fexists = os.path.exists
chdir=os.chdir

def curdir():
    'get current dir'
    return os.path.abspath(os.curdir)

def getThisModulePath():
    return os.path.abspath(sys._getframe(1).f_code.co_filename)

def getThisModuleDir():
    return os.path.dirname(getThisModulePath())

def export(key,val = None):
    'export variable to shell'
    
    if val == None:
        val = globals().get(key)
    if val == None:
        val = sys._getframe(1).f_globals.get(key)

    if val == None:
        return

    env[key] = val


    
def safe_makeDirs(path):
    'make dirs'

    if isinstance(path, (list,tuple)):
        dirs = path
    else:
        dirs = [path]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

def cp( src, dst ):
    cmd = ['cp']
    cmd.append('-fr')

    # src

    if isinstance(src, str):
        cmd.append(src)

    elif isinstance(src, (tuple, list)):
        cmd.extend(src)


    # dst
    cmd.append(dst)

    log( cmd )

    # make sure dst directory
    if os.path.dirname(dst):
        safe_makeDirs(os.path.dirname(dst))

    subprocess.call(cmd)


def rm( path ):
    cmd = ['rm']
    cmd.append( '-rf' )
    cmd.append(path)
    
    subprocess.call(cmd)
