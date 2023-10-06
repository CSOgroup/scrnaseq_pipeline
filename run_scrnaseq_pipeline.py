#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# single cell RNA seq analysis pipeline
# Written by: Divyanshu Srivastava
# Date: 2023 - 06 - 10
"""
# print python version and path
import sys
import os
import argparse
import warnings

print ("Python version and path:")
print (sys.version)
print (sys.executable)
print ()

parser = argparse.ArgumentParser(
    prog='run_scrnaseq_pipeline.py',
    description='Single Sell RNA-Seq pipeline',
    epilog='''This pipeline is developed for OricchioLab''',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument('samplesheet', help='path to the samplesheet CSV file')
parser.add_argument('outdir', help='path to the output directory where to store the results')

parser.add_argument('--show', action='store_true', help='Print the command without running. Useful for testing. (default: False)')
parser.add_argument('-a', '--aligner', default='cellranger', help='aligner to use for alignment (default: cellranger)')
parser.add_argument('-g', '--genome', default='hg38', help='genome to use for alignment (default: hg38)')
parser.add_argument('-p', '--protocol', default='10XV3', help='protocol used (default: 10XV3)')

## extracting the arguments
args = parser.parse_args()

## setting up the variables
# command line arguments
OUTDIR = args.outdir
SAMPLESHEET = args.samplesheet
GENOME = args.genome
ALIGNER = args.aligner

# 10x specific parameters
PROTOCOL = args.protocol

# pipeline specific parameters
VERSION = '2.4.1'

# other parameters
LOGPATH = os.path.join(OUTDIR, 'logs')
MAX_MEMORY="100.GB"
MAX_CPUS=12

## checking the arguments
# OUTDIR
assert os.path.exists(OUTDIR), f'OUTDIR does not exist: {OUTDIR}'
# SAMPLESHEET
assert os.path.exists(SAMPLESHEET), f'SAMPLESHEET does not exist: {SAMPLESHEET}'

print ()

## Displaying the parameters
print ('Running the pipeline with the following parameters:')
print ()
print (f'\tOUTDIR: \t{OUTDIR}')
print (f'\tSAMPLESHEET: \t{SAMPLESHEET}')
print (f'\tGENOME: \t{GENOME}')
print (f'\tALIGNER: \t{ALIGNER}')
print (f'\tVERSION: \t{VERSION}')
print (f'\tLOGPATH: \t{LOGPATH}')
print (f'\tMAX_MEMORY: \t{MAX_MEMORY}')
print (f'\tMAX_CPUS: \t{MAX_CPUS}')

## building the command
command = 'nextflow' 
command += f' -log {LOGPATH}'
command += ' run nf-core/scrnaseq'
command += f' -r {VERSION}'
command += f' --input {SAMPLESHEET}'
command += f' --aligner {ALIGNER}'
command += f' --outdir {OUTDIR}'
command += f' --genome {GENOME}'
command += f' --max_memory {MAX_MEMORY}'
command += f' --max_cpus {MAX_CPUS}'
command += ' -profile docker'
command += ' -resume'

print ()

if args.show:
    print (command)
    print ()
    warnings.warn('Only printing the command. To run the command, disable the -show flag')
    sys.exit()


print ('Running the command ...')
os.system(command)
print ('Pipeline finished. ')
print ()
