# Single Cell RNA-Seq processing pipeline

This pipeline is designed to process single cell RNA-Seq data from raw reads to a count matrix. It uses [nextflow pipeline](https://nf-co.re/scrnaseq/).  

This pipeline is developed for [Oricchio Lab](https://www.epfl.ch/labs/oricchiolab/)

<b> Make sure to be added to docker group to run this pipeline. Contact the maintainers !!<b>

## Usage
```
Single Sell RNA-Seq pipeline

positional arguments:
  samplesheet           path to the samplesheet CSV file
  outdir                path to the output directory where to store the results

options:
  -h, --help            show this help message and exit
  --show                Print the command without running. Useful for testing. (default: False)
  -a ALIGNER, --aligner ALIGNER
                        aligner to use for alignment (default: cellranger)
  -g GENOME, --genome GENOME
                        genome to use for alignment (default: hg38)
  -p PROTOCOL, --protocol PROTOCOL
                        protocol used (default: 10XV3)
```

## Genomes available

1. Human - 
    - GRCh37
    - GRCh38
    - hg19
    - hg38
2. Mouse - 
    - GRCm38
    - mm10

## Defaults

The pipeline uses the following default nextflow parameters. 

```
VERSION = '2.4.1'
MAX_MEMORY="100.GB"
MAX_CPUS=12
```

## Sample sheet
Remember to have the first line "exactly" as 
sample,fastq_1,fastq_2

## NOTE
This pipeline runs cellranger: 8.0.0.

<hr>
Maintained by - [divyanshu srivastava] (https://github.com/divyanshusrivastava)