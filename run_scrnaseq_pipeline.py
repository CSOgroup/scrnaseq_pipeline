#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# single cell RNA seq analysis pipeline
# Written by: Divyanshu Srivastava
# Date: 2025 - 07 - 03
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
    description='Single Cell RNA-Seq Analysis Pipeline',
    epilog='''This pipeline is developed for Oricchiello Lab by Divyanshu Srivastava''',
    usage='%(prog)s [options] <samplesheet> <outdir> [<genome> or <fasta> and <gtf>]',
    add_help=True,
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Add long description
parser.add_argument_group('DESCRIPTION', '''This pipeline performs comprehensive single-cell RNA sequencing analysis using the nf-core/scrnaseq workflow.

The pipeline supports multiple alignment tools including CellRanger, STAR, and Alevin, and can process various single-cell protocols such as 10x Genomics, Smart-seq2, and others.

The pipeline requires either a genome reference or FASTA/GTF files for alignment. 
Output includes processed count matrices, quality metrics, clustering results, and interactive visualizations.''')

parser.add_argument_group('USAGE', '''Usage:
python run_scrnaseq_pipeline.py <samplesheet> <outdir> [<genome> or <fasta> and <gtf>]''')

parser.add_argument_group('OPTIONS', '''Options:
--show: Print the command without running. Useful for testing. (default: False)
--version: version of the nf-core pipeline to use (default: 4.0.0)
-a: aligner to use for alignment (default: cellranger)
-p: protocol used (default: auto)
--genome: genome to use for alignment (default: None)
--fasta: fasta file to use for alignment (default: None)
--gtf: gtf file to use for alignment (default: None)
--max_memory: maximum memory to use for the pipeline (default: 100.GB)
--max_cpus: maximum cpus to use for the pipeline (default: 12)
--save_reference: save the reference genome for later use (default: True)
--work_dir: path to the working directory (default: OUTDIR/work)
''')

parser.add_argument('samplesheet', help='path to the samplesheet CSV file')
parser.add_argument('outdir', help='path to the output directory where to store the results')

parser.add_argument('--show', action='store_true', help='Print the command without running. Useful for testing. (default: False)')
parser.add_argument('--version', default='4.0.0', help='version of the nf-core pipeline to use (default: 4.0.0)')
parser.add_argument('-a', '--aligner', default='cellranger', help='aligner to use for alignment (default: cellranger)')
parser.add_argument('-p', '--protocol', default='auto', help='protocol used (default: auto)')

# checking if the user provides genome or fasta and gtf files
parser.add_argument('--genome', default=None, help='genome to use for alignment (default: None)')
parser.add_argument('--fasta', default=None, help='fasta file to use for alignment (default: None)')
parser.add_argument('--gtf', default=None, help='gtf file to use for alignment (default: None)')
parser.add_argument('--save_reference', default=True, action='store_true', help='save the reference genome for later use (default: True)')
parser.add_argument('--work_dir', default=None, help='path to the working directory (default: OUTDIR/work)')

# memory ram and cpus
parser.add_argument('--max_memory', default='100.GB', help='maximum memory to use for the pipeline (default: 100.GB)')
parser.add_argument('--max_cpus', default=12, help='maximum cpus to use for the pipeline (default: 12)')

## extracting the arguments
args = parser.parse_args()

# show all the arguments nicely
print ('All the arguments:')
for arg in vars(args):
    print (f'\t{arg}: \t{getattr(args, arg)}')
print ('\n')

# if both provided, then the pipeline will use the genome and gtf files
if args.genome and args.fasta and args.gtf:
    print ('Both genome and fasta and gtf files provided. Using the genome and gtf files.')
    GENOME = None
    FASTA = args.fasta
    GTF = args.gtf
elif args.genome:
    print ('Genome provided. Using the genome file.')
    GENOME = args.genome
    FASTA = None
    GTF = None
elif args.fasta and args.gtf:
    print ('Fasta and gtf files provided. Using the fasta and gtf files.')
    GENOME = None
    FASTA = args.fasta
    GTF = args.gtf
else:
    raise ValueError('Either provide a genome or a fasta and gtf files')

## setting up the variables
# command line arguments
OUTDIR = args.outdir
SAMPLESHEET = args.samplesheet
GENOME = args.genome
ALIGNER = args.aligner
if args.work_dir:
    WORK_DIR = args.work_dir
else:
    WORK_DIR = os.path.join(OUTDIR, 'work')

# 10x specific parameters
PROTOCOL = args.protocol

# pipeline specific parameters
VERSION = args.version

# other parameters
LOGPATH = os.path.join(OUTDIR, 'pipeline_logs.txt')
MAX_MEMORY = args.max_memory
MAX_CPUS = args.max_cpus

## checking the arguments
# OUTDIR
assert os.path.exists(OUTDIR), f'OUTDIR does not exist: {OUTDIR}'
# SAMPLESHEET
assert os.path.exists(SAMPLESHEET), f'SAMPLESHEET does not exist: {SAMPLESHEET}'

print ()

## building the command
command = 'nextflow' 
command += f' -log {LOGPATH}'
command += ' run nf-core/scrnaseq'
command += f' -r {VERSION}'
command += f' --input {SAMPLESHEET}'
command += f' --aligner {ALIGNER}'
command += f' --outdir {OUTDIR}'
command += f' -work-dir {WORK_DIR}'
if GENOME:
    command += f' --genome {GENOME}'
else:
    command += f' --fasta {FASTA}'
    command += f' --gtf {GTF}'
    if args.save_reference:
        command += ' --save_reference'
command += f' --protocol {PROTOCOL}'
command += f' --max_memory {MAX_MEMORY}'
command += f' --max_cpus {MAX_CPUS}'
command += ' -profile docker'
command += ' -resume'
command += ' -with-report'
command += ' -bg'


print (f'Running the pipeline with the following command:')
print (command)
print ()

# Exit if the user wants to show the command
if args.show:
    warnings.warn('Only printing the command. To run the command, disable the -show flag')
    sys.exit()

#make sure the correct java is used
JAVA_HOME = '/usr/bin/java'
os.environ['JAVA_HOME'] = JAVA_HOME
os.environ['PATH'] = f'{JAVA_HOME}/bin:{os.environ["PATH"]}'

os.system(command)
