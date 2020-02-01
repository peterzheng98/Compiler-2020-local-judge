import yaml
import os
import json
import subprocess

configuration = {}
color_none = "\033[0m"
color_green = "\033[0;32m"
color_yellow = "\033[1;33m"
color_red = "\033[0;31m"
color_blue = "\033[0;34m"
color_purple = "\033[0;35m"

def buildCompiler():
    print(' == 1 ==[ ]== Build Your Compiler')
    buildScriptPath = os.path.join(configuration['path']['compiler'], 'build.sh')
    process = None
    try:
        process = subprocess.Popen(["sh", buildScriptPath], cwd=configuration['path']['compiler'], stdout=subprocess.PIPE, shell=False)
        process.wait(configuration['buildlimit'])
        if process.returncode == 0:
            print('{} == 1 ==[√]== Build successfully.{}'.format(color_green, color_none))
        else:
            print('{} == 1 ==[x]== Build failed with exitcode {}.{}'.format(color_red, process.returncode, color_none))
            exit(0)
        pass
    except subprocess.TimeoutExpired as identifier:
        print('{} == 1 ==[T]== Build Timeout.{}'.format(color_yellow, color_none))
        try:
            process.kill()
        except Exception as identifier:
            pass
        pass
    except Exception as identifier:
        print('{} == 1 ==[x]== Build failed with runtime error {}.{}'.format(color_red, identifier, color_none))
        exit(0)
    

def runSemantic():
    print(' == 2 ==[ ]== Semantic Judge Start')
    pass

def runCodegen():
    pass

def runOptimize():
    pass


if __name__ == '__main__':
    content = open('config.yaml', 'r', encoding='utf-8').read()
    configuration = yaml.safe_load(content)
    assert 'stage' in configuration.keys()
    assert 'path' in configuration.keys()
    assert 'compiler' in configuration['path'].keys()
    assert 'dataset' in configuration['path'].keys()
    assert 'timelimit' in configuration.keys()
    assert 'memlimit' in configuration.keys()
    assert 'instlimit' in configuration.keys()
    assert 'buildlimit' in configuration.keys()
    buildCompiler()
    if configuration['stage'] == 'semantic':
        runSemantic()
    elif configuration['stage'] == 'codegen':
        runCodegen()
    elif configuration['stage'] == 'optimize':
        runOptimize()
    else:
        print(' [!] Error: stage can only be [semantic, codegen, optimize]')
    print(' == Judge Finished')
    
    


