import sys
import subprocess
import argparse
import logging

# verify if a program is self-producing
# a self-producing program will print its source code when executing

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cmd", required=True, type=str, help="command to run")
parser.add_argument("-s", "--source", required=True, type=str, help="file containing source code or expected output")
parser.add_argument("-v", "--verbose", action="store_true", help="verbose (print debug message)")

def main(args):
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    logging.info("using {}".format(args))
    sourcefile = args.source
    cmd = args.cmd.split()
    with open(sourcefile, "r") as f:
        source = f.read()
        logging.info("program source: \n{}".format(source))
    res = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = res.stdout.decode("utf-8")
    logging.info("program output: \n{}".format(output))
    result = source == output
    if result:
        print("program source matches output")
    else:
        print("program source does NOT match output")
    return 0 if result else 1

if __name__ == "__main__":
    args = parser.parse_args()
    # print(args)
    res_code = main(args)
    exit(res_code)
