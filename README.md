# Single Cell RNA-Seq processing pipeline

This pipeline is designed to process single cell RNA-Seq data from raw reads to a count matrix. It uses [nextflow pipeline](https://nf-co.re/scrnaseq/2.4.1). 

This pipeline is developed for [Oricchio Lab](https://www.epfl.ch/labs/oricchiolab/)

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

## Defaults

The pipeline uses the following default nextflow parameters. 

```
VERSION = '2.4.1'
MAX_MEMORY="100.GB"
MAX_CPUS=12
```

