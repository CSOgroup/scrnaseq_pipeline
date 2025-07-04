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

## UPDATES (Date: 03 July 2025)

- Updated nf-core pipeline version to 4.0.0 (https://nf-co.re/scrnaseq/4.0.0/)
- The pipeline version can be over-written using the `--version` parameter.
- Added support to run pipeline with custom reference genomes (by providing a genome.fasta and annotations.gtf file)
- With the fasta + gtf option, the pipeline also by default saves the generates reference genome for later uses. 
- CellBender call removed from pipeline, as it was taking too long to run. This can always be run separately if needed.


## Sample sheet
Remember to have the first line "exactly" as 
sample,fastq_1,fastq_2

## Problems ?
- java issues? Make sure to run pipeline can see the correct java installations. This could be happening if you are inside a virtual environment where a separate installation of java exists.

## TODOs
- max cpu and max memory arguments unused 

<hr>
Maintained by - [divyanshu srivastava] (https://github.com/divyanshusrivastava)