from amodem import wave
import subprocess as sp
import signal


def test_launch():
    p = wave.launch(tool='true', fname='fname')
    assert p.wait() == 0

def test_exit():
    p = wave.launch(tool='python', fname='-', stdin=sp.PIPE)
    s = b'import sys; sys.exit(42)'
    p.stdin.write(s)
    p.stdin.close()
    assert p.wait() == 42

def test_io():
    p = wave.launch(tool='python', fname='-', stdin=sp.PIPE, stdout=sp.PIPE)
    s = b'Hello World!'
    p.stdin.write(b'print("' + s + b'")\n')
    p.stdin.close()
    assert p.stdout.read(len(s)) == s

def test_kill():
    p = wave.launch(tool='python', fname='-', stdin=sp.PIPE, stdout=sp.PIPE)
    p.kill()
    assert p.wait() == -signal.SIGKILL