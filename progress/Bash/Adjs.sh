

adj () {
    # spliting the file 
    SRA-toolkit/sratoolkit.3.0.0-mac64/bin/fasterq-dump -O fastqer_$1 --split-files $1

    # compressing the file 
    gzip fastqer_$1/$1_1.fastq && gzip fastqer_$1/$1_2.fastq 

    # deleting the non compressed files
    rm fastqer_$1/$1_1.fastq && rm fastqer_$1/$1_2.fastq 
}


adj $1 
